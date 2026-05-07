# Contesto del progetto — Tesi magistrale Davide Piccinelli

> **A cosa serve questo file.** È una "memoria" portatile del progetto:
> contiene le decisioni prese, l'architettura, la struttura della tesi,
> i path utili. Quando si lavora da una nuova macchina (o si chiede aiuto
> a un assistente AI come Claude Code in una nuova sessione), basta
> leggere questo file per ricostruire il contesto in 2 minuti.
>
> Tenerlo aggiornato man mano che le decisioni evolvono.
>
> Ultimo aggiornamento: 2026-05-07.

---

## Info di base

- **Studente:** Davide Piccinelli — 1097568
- **Corso:** LM Informatica — UniBO
- **Azienda partner:** Coop Alleanza 3.0
- **Titolo (frontespizio LaTeX):** *Orchestrazione adattiva di agenti LLM in contesto enterprise: architettura, implementazione e valutazione*
- **Titolo della proposta consegnata 20/02/2026 (PDF):** *Progettazione e valutazione di un sistema multi-agente «democratizzato» basato su LLM in ambito enterprise, con integrazione di architetture RAG e Text-to-SQL su Google Cloud Platform*

---

## Architettura del sistema software (operativa)

```
Portal (auth Entra ID + routing esplicito per badge)
  ├── Vera                      → LLM + Google Search Grounding
  ├── Personal Docs             → LLM + Vertex AI RAG Engine (corpus per-utente isolato)
  ├── CooPolicy (docs-backend)  → LLM + Vertex AI RAG Engine (corpus policy aziendale condiviso)
  ├── NPS Agent (AllyCare)      → LLM + Text-to-SQL su BigQuery (dati survey NPS)
  ├── SysAid Agent (Gemini)     → LLM + Text-to-SQL su BigQuery (ticket SysAid)
  ├── SysAid Agent (Claude)     → Claude Sonnet 4.6 + Text-to-SQL (confronto multi-LLM)
  ├── Admin                     → Gestione utenti, quota, audit log, PII groups
  └── [TBD] Orion               → orchestratore, da costruire (vedi plans/ORION_ROADMAP.md)
```

**Decisioni architetturali fisse — non riaprire:**
- Vera NON ha RAG interno: usa Google Search grounding nativo di Vertex AI.
- Personal Docs e CooPolicy sono due servizi RAG SEPARATI (corpus
  per-utente isolato vs corpus condiviso).
- SysAid implementato in due varianti parallele (Gemini, Claude) per
  un confronto multi-LLM controllato.
- GCP + Gemini è irrevocabile per vincoli aziendali; Claude è ammesso
  solo per il confronto SysAid.

---

## Struttura della tesi (decisione 2026-05-07)

**Cambio di impasto rispetto a versioni precedenti**: Orion non è più
"prototipo nel cap. 4.9", è diventato il **contributo centrale** con 3
capitoli dedicati. Personal Docs è fuori scope tesi.

### 4 agenti trattati nella polpa
1. **Vera** — assistente generale + Web grounding
2. **CooPolicy** — RAG su corpus policy condiviso
3. **AllyCare / NPS** — Text-to-SQL su BigQuery
4. **SysAid** — Text-to-SQL, doppia variante Gemini vs Claude (confronto interno al capitolo)

Personal Docs **escluso** dalla tesi: non è instradato da Orion.

### 8 capitoli

```
Cap. 1 — Introduzione                                  ~10-12 pp
Cap. 2 — Background                                    ~25-30 pp
Cap. 3 — Suite di agenti: ARCHITETTURA      (POLPA A1)
Cap. 4 — Suite di agenti: IMPLEMENTAZIONE   (POLPA A2)
Cap. 5 — Orion: ARCHITETTURA                (POLPA B1)
Cap. 6 — Orion: IMPLEMENTAZIONE             (POLPA B2)
Cap. 7 — Orion: VALUTAZIONE sperimentale    (POLPA B3)
Cap. 8 — Conclusioni e sviluppi futuri                 ~6-8 pp
```

Conteggio polpa: 4×2 + 3 = **11 parti totali** (8 sui 4 agenti, 3 su Orion).

### Ordine di scrittura (raccomandato dal relatore)
polpa (3 → 4 → 5 → 6 → 7) → background (2) → conclusioni (8) →
introduzione (1) → abstract.

**Dettaglio operativo completo** (incl. tabella delle ~26 figure):
`plans/PIANO_REDAZIONE_TESI.md`.

---

## Stack tecnologico del sistema software

- **LLM:** Gemini 2.5 Flash/Pro via Vertex AI; Claude Sonnet 4.6 via Anthropic SDK (solo SysAid Sonnet)
- **Grounding Vera:** Google Search Grounding API (Vertex AI native)
- **Grounding Personal Docs / CooPolicy:** Vertex AI RAG Engine
- **Embedding:** `text-multilingual-embedding-002` (italiano)
- **Auth:** Microsoft Entra ID (MSAL) → JWT locale; badge Bronze/Silver/Gold/Admin
- **DB:** Cloud SQL PostgreSQL 16 (sistema), BigQuery (NPS, SysAid)
- **Sicurezza:** Model Armor (Responsible AI + prompt injection), Cloud DLP (PII italiane custom)
- **CI/CD:** Bitbucket → Cloud Build → Cloud Run
- **IaC:** Terraform multi-env (test/prod)

---

## Path da conoscere

### Repo della tesi (questo)
- **Path:** `/home/dave/workspace/github/unibo-thesis-doc/`
- **Remote:** https://github.com/dpiccinelli84/unibo-thesis-doc

File chiave nel repo:
- `main.tex` — entry point LaTeX (8 capitoli, biblatex/biber)
- `chapters/` — 9 file capitolo con scaffolding completo (sezioni, marcatori figura, citazioni `\cite{}` in commento)
- `bibliography.bib` — 46 voci BibTeX in 12 filoni
- `letteratura-complessiva.md` — mappatura per filone (affidabilità + capitolo)
- `descrizione-tesi.md` — descrizione lunga + linee guida del relatore
- `plans/PIANO_REDAZIONE_TESI.md` — piano operativo (struttura, figure, ordine di scrittura)
- `plans/ORION_ROADMAP.md` — roadmap implementativa di Orion (sez. 1-9)
- `plans/ORION_LETTERATURA.md` — bibliografia specifica orchestrazione
- `guide-unibo-scrittura-tesi/` — template UniBO + guide PDF di riferimento

### Codebase del sistema software
- **Path:** `/home/dave/workspace/bitbucket/c30-ai-agents/`
- Monorepo con i backend FastAPI e i frontend React di tutti gli agenti.

### Documenti tesi precedenti (alcuni superati)
- **Path:** `/home/dave/workspace/github/unibo/prova-finale/`
- `Proposta di prova finale Davide Piccinelli 2026.pdf` — proposta consegnata il 20/02/2026
- `bozza-tesi.md`, `elenco-capitoli.md`, `bibliografia.md` — impostazione precedente (6 agenti, Orion solo prototipo): SUPERATA dalla nuova in `plans/PIANO_REDAZIONE_TESI.md` di questo repo
- `architettura-sistema.png` — diagramma architettura (da riusare come fig. 3.1)

---

## Compilazione del progetto LaTeX

```bash
# Compilazione completa (genera main.pdf)
latexmk -pdf main.tex

# Pulizia degli ausiliari (mantiene main.pdf)
latexmk -c

# Pulizia totale (rimuove anche main.pdf)
latexmk -C
```

Toolchain richiesta: `pdflatex`, `biber`, `latexmk`. Su Debian/Ubuntu:
`sudo apt install texlive-full latexmk biber`.

---

## Riferimenti chiave per la tesi

Lista completa: `letteratura-complessiva.md`. Voci primarie:

- Vaswani et al. 2017 — Transformer
- Lewis et al. 2020 — RAG
- Yao et al. 2022 — ReAct
- Wei et al. 2022 — Chain-of-Thought
- Wu et al. 2023 — AutoGen (pattern orchestratore)
- Guo et al. 2024 — Multi-agent LLM survey
- Chen 2023 / Ong 2024 — FrugalGPT / RouteLLM
- Kadavath et al. 2022 — confidence calibration
- Liu 2023 / Zheng 2023 — AgentBench / LLM-as-a-Judge
- Es et al. 2023 — RAGAS
- Xu et al. 2024 — Hallucination is Inevitable

---

## Preferenze di lavoro

- Risposte in italiano.
- Comunicazione diretta, senza fronzoli.
- Quando si chiede un'analisi, va data approfondita (non sintesi superficiale).
