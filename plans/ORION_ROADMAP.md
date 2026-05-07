# ORION — Roadmap di Implementazione

Orchestratore AI multi-agente per Coop Alleanza 3.0.  
Stato: **pianificazione** — nessun codice scritto.  
Ultimo aggiornamento: 2026-05-05 (aggiunto admin panel)

---

## Indice

1. [Visione architetturale](#1-visione-architetturale)
2. [Fase 1 — Backend Orion](#2-fase-1--backend-orion)
3. [Fase 2 — Frontend Orion (chat)](#3-fase-2--frontend-orion-chat)
4. [Fase 3 — Admin Panel Orion](#4-fase-3--admin-panel-orion)
5. [Fase 4 — Infrastruttura Terraform](#5-fase-4--infrastruttura-terraform)
6. [Fase 5 — Sistema di Valutazione](#6-fase-5--sistema-di-valutazione)
7. [Fase 6 — Deploy e Go-Live](#7-fase-6--deploy-e-go-live)
8. [Dipendenze e vincoli](#8-dipendenze-e-vincoli)
9. [Decisioni architetturali aperte](#9-decisioni-architetturali-aperte)

---

## 1. Visione architetturale

Orion è un **agente orchestratore** che eredita tutte le capacità di Vera (RAG, upload documenti on-the-fly, internet search, guardrail) e aggiunge uno strato di routing intelligente verso agenti specializzati.

```
Utente → [Frontend Orion]
              ↓
         [Backend Orion]
              │
              ├─ routing step (LLM call strutturata, Gemini Flash)
              │   Output: { agent, complexity, confidence, clarification_needed }
              │
              ├─ agent == "self"          → pipeline Vera (RAG + search + generation)
              ├─ agent == "sysaid_gemini" → HTTP proxy → sysaid-backend
              ├─ agent == "sysaid_sonnet" → HTTP proxy → sysaid-sonnet-backend
              ├─ agent == "allycare"      → HTTP proxy → nps-backend
              └─ agent == "coopolicy"     → HTTP proxy → docs-backend
```

**Principi di design:**
- I backend degli agenti specializzati **non vengono modificati** — tutta la logica di adattamento sta nel proxy di Orion.
- Il token Entra ID dell'utente viene forwardato as-is ai sub-agenti.
- Orion gestisce la propria storia di conversazione (tutti i turni, tutti gli agenti).
- La stima di complessità viene passata ai sub-agenti come campo opzionale non-breaking.

---

## 2. Fase 1 — Backend Orion

**Base:** fork di `vera-backend`. Si eredita tutto; si aggiungono 2 moduli e si modifica il chat endpoint.

### Step 1.1 — Setup repository e struttura

- [ ] Creare directory `orion-backend/` nella repo mono
- [ ] Copiare `vera-backend/` come base
- [ ] Rinominare riferimenti interni da "vera" a "orion" (app name, API prefix `/api/orion`, log labels)
- [ ] Aggiornare `requirements.txt` con eventuali dipendenze aggiuntive (`httpx` per il proxy HTTP)

### Step 1.2 — Router Agent (`app/agents/router_agent.py`)

Nuovo modulo. Responsabilità: classificare il prompt con una LLM call leggera (Gemini Flash) e restituire un output strutturato.

**Output schema (tool use / structured output):**
```json
{
  "agent": "self | sysaid_gemini | sysaid_sonnet | allycare | coopolicy",
  "complexity": "low | medium | high",
  "confidence": 0.0,
  "reasoning": "Chain of Thought esplicita",
  "clarification_needed": null
}
```

**Logica confidence:**
- `confidence >= 0.80` → routing diretto
- `0.60 <= confidence < 0.80` → routing con warning nel log
- `confidence < 0.60` → non fare routing, restituire `clarification_needed` con la domanda da porre all'utente

**System prompt del router:** (da definire e iterare con il sistema di valutazione — vedi Fase 4)
- Descrive ogni agente disponibile con capacità, dominio, esempi di query tipiche
- Include mapping complexity → modello target (utile per SysAid che già fa model routing)
- Include regola per CooPolicy: verificare prima i gruppi Entra ID nel token

### Step 1.3 — Agent Proxy (`app/services/agent_proxy.py`)

Nuovo modulo. Responsabilità: chiamare il backend dell'agente selezionato via HTTP e normalizzare la risposta.

**Endpoint target:**

| Agent key | URL base (env var) | Endpoint |
|---|---|---|
| `sysaid_gemini` | `SYSAID_BACKEND_URL` | `/api/sysaid/prompt` |
| `sysaid_sonnet` | `SYSAID_SONNET_BACKEND_URL` | `/api/sysaid-sonnet/prompt` |
| `allycare` | `NPS_BACKEND_URL` | `/api/nps/prompt` |
| `coopolicy` | `DOCS_BACKEND_URL` | `/api/docs/prompt` |

**Payload inviato:**
```json
{
  "prompt": "<prompt utente>",
  "history": [...],
  "conversation_id": "<conv_id nel backend target, se noto>",
  "complexity": "low | medium | high"
}
```

**Normalizzazione response:** il proxy mappa le response shape eterogenee (SysAid ha `queries`, docs ha `sources`) verso un formato uniforme per il frontend Orion.

**Gestione errori:** se il sub-agente risponde 4xx/5xx o va in timeout, Orion gestisce la risposta in proprio (fallback su pipeline Vera) e logga l'evento.

### Step 1.4 — Integrazione nel chat endpoint

Modificare `app/api/chat.py` (e `chat_stream.py`) per inserire il routing step prima del normale flusso Vera:

```
receive request
    → [NUOVO] router_agent.classify(prompt, history, token_payload)
    → if clarification_needed → return clarification response
    → if agent != "self"      → agent_proxy.forward(...)
    → else                    → normal Vera pipeline (RAG + search + LLM)
```

### Step 1.5 — Gestione ACL CooPolicy

- Prima di fare routing su `coopolicy`, verificare che il `token_payload["groups"]` contenga almeno uno dei gruppi in `DOCS_ALLOWED_GROUPS`
- Se l'utente non è autorizzato: escludere `coopolicy` dall'insieme dei target possibili nel routing (non esporre l'esistenza dell'agente all'utente non autorizzato)

### Step 1.6 — Variabili d'ambiente aggiuntive

Nuove env var da aggiungere rispetto a Vera:

| Variabile | Descrizione |
|---|---|
| `SYSAID_BACKEND_URL` | URL interno Cloud Run sysaid-backend |
| `SYSAID_SONNET_BACKEND_URL` | URL interno Cloud Run sysaid-sonnet-backend |
| `NPS_BACKEND_URL` | URL interno Cloud Run nps-backend |
| `DOCS_BACKEND_URL` | URL interno Cloud Run docs-backend |
| `ROUTER_CONFIDENCE_THRESHOLD` | Soglia sotto cui chiedere chiarimenti (default: 0.60) |
| `ROUTER_MODEL` | Modello per il routing step (default: gemini-2.5-flash) |

### Step 1.7 — Identità visiva / naming

- Aggiornare il system prompt: da "VERA" a "ORION"
- Aggiornare il profilo persona (mantenere valori Coop, cambiare nome e metafora visiva)
- Aggiornare `/health` e metadata FastAPI

---

## 3. Fase 2 — Frontend Orion (chat)

**Base:** fork di `vera-frontend`.

### Step 2.1 — Setup

- [ ] Creare directory `orion-frontend/`
- [ ] Copiare `vera-frontend/` come base
- [ ] Aggiornare `package.json`, titolo app, API base URL (`/api/orion`)

### Step 2.2 — Branding

- [ ] Cambiare nome e logo (da VERA a ORION — tema astronomico/costellazione)
- [ ] Aggiornare palette colori se richiesto
- [ ] Aggiornare copy dell'interfaccia (placeholder input, messaggi di benvenuto, ecc.)

### Step 2.3 — UI per routing trasparente (opzionale ma consigliato per la tesi)

- [ ] Badge visivo che mostra quale agente ha gestito la risposta (es. "Risposta generata da: SysAid Sonnet — Complessità: Alta")
- [ ] Indicatore di confidence del routing (utile nella demo di tesi)
- [ ] Messaggio di chiarimento: quando Orion chiede all'utente di specificare, renderizzarlo in modo distinto visivamente

### Step 2.4 — Gestione response shape

- [ ] Adattare il renderer per gestire il formato normalizzato di Orion
- [ ] Gestire `sources[]` (CooPolicy) e `queries[]` / `charts[]` (SysAid) in modo unificato

---

## 4. Fase 3 — Admin Panel Orion

Il pannello admin di Orion segue lo stesso pattern già consolidato nel progetto:

```
admin-portal-frontend  (hub)
      ├── /admin/        →  admin-frontend         →  vera-backend   (/api/admin/*)
      ├── /rag-admin/    →  rag-agent-admin-frontend  →  rag-agent-admin-backend
      └── /orion-admin/  →  orion-admin-frontend   →  orion-backend  (/api/orion-admin/*)
```

### Step 3.1 — Admin Portal Hub (modifica minima)

Aggiungere una card Orion in `admin-portal-frontend/src/pages/Home.tsx` nell'array `ADMIN_APPS`:

```typescript
{
  id: 'orion',
  name: 'Orion Admin',
  description: 'Gestisci utenti, configurazioni e monitora il routing intelligente dell\'orchestratore Orion.',
  path: '/orion-admin/',
  color: '#1a1a2e',   // tema astronomico — adattare al branding definitivo
  tags: ['Utenti', 'Routing', 'System Prompt', 'Metriche'],
}
```

### Step 3.2 — Backend admin (`orion-backend/app/api/admin_orion.py`)

Aggiungere al backend Orion (già fork di Vera) il router admin specifico.  
Il prefisso API sarà `/api/orion-admin` anziché `/api/admin`.

**Endpoint ereditati da Vera admin** — stessa logica, prefisso diverso:

| Endpoint | Descrizione |
|---|---|
| `GET /api/orion-admin/users` | Lista utenti Orion (badge, quota) |
| `POST /api/orion-admin/users` | Crea utente |
| `PUT /api/orion-admin/users/{id}` | Aggiorna badge/quota |
| `DELETE /api/orion-admin/users/{id}` | Elimina utente |
| `GET /api/orion-admin/logs` | Log conversazioni |
| `GET /api/orion-admin/stats` | Statistiche uso |
| `GET/PUT /api/orion-admin/settings/{key}` | Settings (temperature, guardrails, PII) |
| `GET/POST/PUT /api/orion-admin/plans` | Piani quota |
| `GET/POST /api/orion-admin/starters` | Conversation starters |
| `GET/POST /api/orion-admin/ai-models` | Modelli AI disponibili |
| `GET /api/orion-admin/feedback` | Feedback utenti |
| `GET/POST /api/orion-admin/pii-groups` | Gruppi PII / guardrail exemptions |

**Endpoint nuovi, specifici di Orion:**

| Endpoint | Descrizione |
|---|---|
| `GET /api/orion-admin/routing-logs` | Log del routing: agente scelto, complexity, confidence, reasoning per ogni turno — paginato, filtrabile per agente/data |
| `GET /api/orion-admin/routing-stats` | Aggregati: accuracy agente e complexity nel tempo, distribuzione confidence, clarification rate |
| `GET /api/orion-admin/router-prompt` | Legge il system prompt del router corrente (da `app_settings` key `router_system_prompt`) |
| `PUT /api/orion-admin/router-prompt` | Salva nuova versione del system prompt del router + timestamp versione |
| `GET /api/orion-admin/router-prompt/history` | Storico versioni del system prompt (se si implementa versioning in DB) |

### Step 3.3 — Frontend admin (`orion-admin-frontend/`)

**Base:** fork di `admin-frontend`.  
`VITE_API_URL` → `/api/orion-admin`

**Struttura pagine:**

```
orion-admin-frontend/src/pages/
├── Login.tsx              ← invariata (stessa logica Entra ID)
├── Dashboard.tsx          ← adattata (aggiunge widget routing metrics)
├── Users.tsx              ← invariata (solo cambio API base URL)
├── Models.tsx             ← invariata
├── Plans.tsx              ← invariata
├── Settings.tsx           ← invariata
├── Starters.tsx           ← invariata
├── Logs.tsx               ← invariata
├── Feedback.tsx           ← invariata
├── PiiGroups.tsx          ← invariata
├── RoutingLogs.tsx        ← NUOVA (vedi dettaglio sotto)
├── RouterPrompt.tsx       ← NUOVA (vedi dettaglio sotto)
└── RouterMetrics.tsx      ← NUOVA (vedi dettaglio sotto)
```

**Pagina `RoutingLogs.tsx` — dettaglio:**
- Tabella paginata dei turni: timestamp, username, prompt excerpt, agente selezionato, complexity, confidence (con colore: verde ≥0.80, giallo 0.60-0.80, rosso <0.60), clarification yes/no
- Filtri: per agente, per data, per range confidence
- Click su una riga → espande il `reasoning` completo (Chain of Thought del router)

**Pagina `RouterPrompt.tsx` — dettaglio:**
- Textarea con il system prompt corrente del router (caricato da `GET /api/orion-admin/router-prompt`)
- Campo "Versione" (es. v1.2) e "Note di release"
- Pulsante "Salva e Attiva" → `PUT /api/orion-admin/router-prompt`
- Avviso: "Modificare il system prompt influenza il comportamento del routing. Eseguire una valutazione dopo ogni modifica."
- Storico versioni (opzionale v1)

**Pagina `RouterMetrics.tsx` — dettaglio:**
- Card KPI: Agent Accuracy %, Complexity Accuracy %, Clarification Rate %, Mean Confidence
- Grafico a barre: accuracy per agente (self, sysaid_gemini, sysaid_sonnet, allycare, coopolicy)
- Grafico timeline: accuracy nel tempo (per data)
- Distribuzione confidence: istogramma dei valori di confidence (attesi vs errati)
- Filtro per periodo

---

## 5. Fase 4 — Infrastruttura Terraform

**Base:** `ai-agents-iac-infrastructure/` — stesso pattern degli altri servizi.

### Step 4.1 — Cloud Run services

Aggiungere a `var.cloud_run_services` in `variables.tf` **tre** nuovi servizi:
```hcl
"orion-backend"        = { ... }
"orion-frontend"       = { ... }
"orion-admin-frontend" = { ... }
```

Env var specifiche per `orion-backend` (blocchi `dynamic "env"`):
- `SYSAID_BACKEND_URL`, `SYSAID_SONNET_BACKEND_URL`, `NPS_BACKEND_URL`, `DOCS_BACKEND_URL`
- `ROUTER_CONFIDENCE_THRESHOLD`, `ROUTER_MODEL`
- Tutti gli env var già presenti in Vera (DB, Vertex AI, CORS, ecc.)

Env var specifiche per `orion-admin-frontend`:
- `VITE_API_URL=/api/orion-admin` (o configurata via nginx come gli altri admin frontend)

### Step 4.2 — Secret Manager

- [ ] Nessun secret nuovo se i backend target sono raggiungibili via URL interno Cloud Run (no autenticazione aggiuntiva se stesso progetto GCP)
- [ ] Verificare che il Service Account di Orion abbia `roles/run.invoker` sui backend target se usano autenticazione Cloud Run-to-Cloud Run

### Step 4.3 — Cloud Build triggers

- [ ] Aggiungere `google_cloudbuildv2_repository` per `orion-backend`, `orion-frontend`, `orion-admin-frontend`
- [ ] Aggiungere `google_cloudbuild_trigger` per branch `test` e `main` per tutti e tre
- [ ] Creare `cloudbuild.yaml` in ciascuna directory (stesso pattern degli altri)

### Step 4.4 — Load Balancer / URL mapping

Tre nuovi path nel URL map:

| Path | Cloud Run target |
|---|---|
| `/orion/*` | `orion-frontend` |
| `/orion-admin/*` | `orion-admin-frontend` |
| `/api/orion/*` | `orion-backend` |
| `/api/orion-admin/*` | `orion-backend` (stesso servizio, prefisso diverso) |

- [ ] Aggiornare certificato SSL se necessario

### Step 4.5 — Admin Portal Hub

- [ ] Modificare `admin-portal-frontend/src/pages/Home.tsx` — aggiungere card Orion in `ADMIN_APPS[]`
- [ ] Rebuild e redeploy di `admin-portal-frontend` (modifica minima)

### Step 4.6 — Database

- [ ] Orion ha il proprio Cloud SQL PostgreSQL (stesso istanza, database separato — seguire il pattern degli altri agenti)
- [ ] Migration per tabella `orion_routing_logs`:
  ```sql
  CREATE TABLE orion_routing_logs (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      username VARCHAR(255) NOT NULL,
      conversation_id UUID,
      prompt_excerpt VARCHAR(500),
      agent_selected VARCHAR(50),
      complexity VARCHAR(20),
      confidence FLOAT,
      clarification_asked BOOLEAN DEFAULT false,
      reasoning TEXT,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
  );
  ```
- [ ] Migration per `app_settings` key `router_system_prompt` (seed del prompt iniziale)

---

## 6. Fase 5 — Sistema di Valutazione

Applicazione separata per il testing iterativo del system prompt del router.  
**Non è un Cloud Run service** — è uno script Python eseguibile manualmente (o schedulabile).

### Step 5.1 — Struttura tabella Coda "Test Suite Orion"

Creare una tabella Coda con le seguenti colonne:

| Colonna | Tipo | Descrizione |
|---|---|---|
| `ID` | Text | Identificativo test case (es. TC-001) |
| `Prompt` | Text | Prompt utente da testare |
| `Agente Atteso` | Select | `self / sysaid_gemini / sysaid_sonnet / allycare / coopolicy` |
| `Complessità Attesa` | Select | `low / medium / high` |
| `Categoria` | Select | Categoria tematica del prompt (SysAid, NPS, Policy, General, Ambiguous) |
| `Note` | Text | Motivazione della classificazione corretta |
| `Attivo` | Checkbox | Se includere nel test run corrente |

**Numero minimo di test case consigliato per la tesi:** 50 (10 per agente + 10 ambigui).

### Step 5.2 — Struttura tabella Coda "Risultati Valutazione Orion"

Tabella di output, una riga per ogni esecuzione di test:

| Colonna | Tipo | Descrizione |
|---|---|---|
| `Run ID` | Text | UUID del run |
| `Timestamp` | Date | Data/ora esecuzione |
| `Versione System Prompt` | Text | Tag/versione del system prompt testato (es. v1.0, v1.1) |
| `Test Case ID` | Relation → Test Suite | FK al test case |
| `Prompt` | Text | Prompt testato |
| `Agente Atteso` | Text | Dal test case |
| `Agente Prodotto` | Text | Output di Orion |
| `Complessità Attesa` | Text | Dal test case |
| `Complessità Prodotta` | Text | Output di Orion |
| `Confidence` | Number | Score di confidence del router |
| `Reasoning` | Text | Chain of Thought del router |
| `Agent Corretto` | Checkbox | `Agente Atteso == Agente Prodotto` |
| `Complexity Corretto` | Checkbox | `Complessità Attesa == Complessità Prodotta` |
| `Accuracy Agente (%)` | Formula | Calcolata da Coda |
| `Accuracy Complessità (%)` | Formula | Calcolata da Coda |

### Step 5.3 — Script di valutazione (`orion-eval/`)

```
orion-eval/
├── main.py           # entry point: legge Coda, chiama Orion, scrive risultati
├── coda_client.py    # wrapper Coda API (lettura test suite, scrittura risultati)
├── orion_client.py   # chiama l'endpoint di routing di Orion (non il chat completo)
├── report.py         # genera report testuale/CSV del run
├── config.py         # env vars: CODA_API_TOKEN, ORION_URL, TEST_TABLE_ID, RESULTS_TABLE_ID
└── requirements.txt
```

**Endpoint dedicato in Orion** (da aggiungere in Fase 1):
```
POST /api/orion/classify
Body: { "prompt": "...", "history": [] }
Response: { "agent": "...", "complexity": "...", "confidence": 0.0, "reasoning": "..." }
```
Questo endpoint espone solo il routing step, senza eseguire la risposta — ideale per il test automatizzato (economico: solo una Flash call per test case).

**Flusso dello script:**
1. Legge tutti i test case attivi dalla tabella Coda "Test Suite Orion"
2. Per ogni test case: chiama `POST /api/orion/classify`
3. Confronta l'output con `agente_atteso` e `complessità_attesa`
4. Scrive i risultati nella tabella "Risultati Valutazione Orion" (una riga per test case)
5. Stampa un summary: accuracy per agente, accuracy complessità, casi di clarification

**Come usarlo per iterare il system prompt:**
1. Modificare il system prompt del router in `orion-backend`
2. Fare redeploy (o testare in locale)
3. Lanciare lo script con `PROMPT_VERSION=v1.2`
4. Confrontare i risultati nella tabella Coda con le versioni precedenti

### Step 5.4 — Metriche di valutazione target per la tesi

| Metrica | Formula | Target |
|---|---|---|
| Agent Accuracy | `correct_agent / total` | ≥ 85% |
| Complexity Accuracy | `correct_complexity / total` | ≥ 80% |
| Clarification Rate | `clarification_asked / total` | < 15% |
| Mean Confidence (correct) | media confidence su casi corretti | ≥ 0.82 |
| Mean Confidence (wrong) | media confidence su casi errati | ≤ 0.65 |

L'ultima coppia di metriche valida la **calibrazione del confidence score**: un buon router deve essere più incerto quando sbaglia.

---

## 7. Fase 6 — Deploy e Go-Live

### Step 6.1 — Test environment

- [ ] Deploy su `test` branch → `c30-pj-test-ai-agents`
- [ ] Smoke test manuale (5 prompt per agente)
- [ ] Esecuzione valutazione su test suite Coda → target ≥ 85% agent accuracy

### Step 6.2 — Iterazione system prompt

- [ ] Analizzare i casi errati → identificare pattern
- [ ] Aggiornare system prompt del router
- [ ] Ripetere valutazione — confrontare versioni nella tabella Coda
- [ ] Documentare le iterazioni nella tesi (questa è la sezione sperimentale)

### Step 6.3 — Production

- [ ] Review finale del system prompt
- [ ] PR su `main` → deploy su `c30-pj-prod-ai-agents`
- [ ] Monitoring: `orion_routing_logs` per analisi post-deploy

---

## 8. Dipendenze e vincoli

| Dipendenza | Note |
|---|---|
| I backend degli agenti devono essere running | Orion non può funzionare se i target sono down — gestire con fallback |
| Token Entra ID forwarding | Il token dell'utente deve avere scope validi per tutti i backend target |
| Cloud Run internal networking | Usare URL interni (`.run.app`) non il load balancer pubblico per le chiamate Orion→agenti |
| Coda API token | Necessario per lo script di valutazione — non per il deploy di Orion stesso |
| `httpx` nel backend | Dipendenza aggiuntiva rispetto a Vera per le chiamate HTTP async verso i sub-agenti |

---

## 9. Decisioni architetturali aperte

| Decisione | Opzioni | Raccomandazione |
|---|---|---|
| Modello per routing step | Flash vs Pro | Flash (velocità, costo) — Pro solo se accuracy insufficiente |
| Confidence threshold | 0.50 / 0.60 / 0.70 | 0.60 — da calibrare con i risultati di valutazione |
| Conversation threading | History unica in Orion vs multi-backend | History unica in Orion (Opzione A) |
| Routing trasparente all'utente | Mostrare quale agente risponde o no | Sì — valore dimostrativo per la tesi |
| Streaming nell'endpoint proxy | Supportare SSE dal sub-agente o bufferizzare | Bufferizzare per semplicità (v1) |
| Versioning system prompt | File in repo vs DB | File in repo (tag git = versione) |
