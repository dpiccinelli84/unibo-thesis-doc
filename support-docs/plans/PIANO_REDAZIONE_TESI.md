# Piano di redazione della tesi

> Documento di piano. Cattura le decisioni prese il **2026-05-07** sulla
> struttura definitiva, gli agenti scelti, le figure pianificate e
> l'ordine di scrittura. Lo scaffolding LaTeX è già impostato in
> `chapters/` coerentemente con questo piano.

---

## 1. Decisioni fisse

### 1.1 Quattro agenti nella polpa
La tesi tratta **4 agenti** verticali (non 6):

1. **Vera** — assistente generale + Web grounding (Google Search)
2. **CooPolicy** — RAG su corpus di policy aziendali condiviso
3. **AllyCare / NPS** — Text-to-SQL su BigQuery (sondaggi NPS)
4. **SysAid** — Text-to-SQL su BigQuery (ticketing), in **doppia variante**
   Gemini 2.5 vs Claude Sonnet 4.6, trattata come confronto multi-modello
   *interno* al capitolo (non come 5° agente).

**Esclusi** dalla tesi:
- *Personal Docs* (RAG per-utente): non instradato da Orion nel
  `ORION_ROADMAP.md`. Resta operativo nella suite ma fuori scope tesi.
- *Admin*: menzionato per completezza ma non analizzato in profondità.

**Motivazione:** sono esattamente i 4 target di routing dell'orchestratore
Orion (`self`, `coopolicy`, `allycare`, `sysaid_*`). Tenere fuori Personal
Docs stringe il focus della tesi sul contributo originale (orchestrazione).

### 1.2 Orion al centro della tesi
L'orchestratore **Orion** è il contributo originale e occupa **3 capitoli**
dedicati:
- Cap. 5 — Architettura
- Cap. 6 — Implementazione
- Cap. 7 — Valutazione sperimentale

Riferimento di progetto: `plans/ORION_ROADMAP.md`.

### 1.3 Conteggio della "polpa" — 11 parti

- **8 parti** sui 4 agenti = 4 agenti × (architettura + implementazione)
  → sezioni `3.2-3.5` + `4.2-4.5`
- **3 parti** su Orion = capitoli `5`, `6`, `7`

= **11 parti di polpa totali**, come richiesto.

---

## 2. Struttura definitiva — 8 capitoli

```
Cap. 1 — Introduzione                                  ~10-12 pp
Cap. 2 — Background                                    ~25-30 pp
Cap. 3 — La suite di agenti: architettura              POLPA A1
         3.1 Principi guida e architettura d'insieme
         3.2 Vera                  (architettura)
         3.3 CooPolicy             (architettura)
         3.4 AllyCare / NPS        (architettura)
         3.5 SysAid                (architettura, incl. confronto Gem/Sonnet)
         3.6 Alternative scartate
Cap. 4 — La suite di agenti: implementazione           POLPA A2
         4.1 Stack, monorepo, IaC, sicurezza
         4.2 Vera                  (implementazione)
         4.3 CooPolicy             (implementazione)
         4.4 AllyCare / NPS        (implementazione)
         4.5 SysAid                (implementazione, due varianti)
         4.6 Admin (cenni)
Cap. 5 — Orion: architettura                           POLPA B1
Cap. 6 — Orion: implementazione                        POLPA B2
Cap. 7 — Orion: valutazione sperimentale               POLPA B3
Cap. 8 — Conclusioni e sviluppi futuri                 ~6-8 pp
```

I file LaTeX corrispondenti sono in `chapters/`:
`00_abstract.tex`, `01_introduzione.tex`, `02_background.tex`,
`03_agenti_architettura.tex`, `04_agenti_implementazione.tex`,
`05_orion_architettura.tex`, `06_orion_implementazione.tex`,
`07_orion_valutazione.tex`, `08_conclusioni.tex`.

---

## 3. Ordine di scrittura (consigliato dal relatore)

Il prof raccomanda di NON scrivere in ordine sequenziale. Ordine corretto:

| Step | Capitolo | Quando |
|---|---|---|
| 1 | Cap. 3 e Cap. 4 (suite di agenti) | il codice esiste, scrivere come "appunti tecnici strutturati" mentre il lavoro è fresco |
| 2 | Cap. 5 e Cap. 6 (Orion arch + impl) | parallelamente allo sviluppo di Orion (vedi `ORION_ROADMAP.md` Fase 1-3) |
| 3 | Cap. 7 (valutazione) | mentre i test su Coda producono risultati (Fase 5 del roadmap) |
| 4 | Cap. 2 (background) | dopo la polpa: raccogliere i concetti che riappaiono nei capp. 3-7 |
| 5 | Cap. 8 (conclusioni) | dopo background: tollera più dettagli tecnici dell'introduzione |
| 6 | Cap. 1 (introduzione) | a struttura nota: forma a "imbuto", esercizio della "macchina del tempo" |
| 7 | Abstract | per ultimo, quando i numeri di Cap. 7 sono definitivi |

---

## 4. Piano figure (~22-26 figure totali)

Ogni voce è già marcata nei file `.tex` come blocco `\begin{figure}`
commentato pronto da scommentare. Nomi file in `img/` con prefisso
`figXX_<slug>.pdf` (XX = numero capitolo).

### Cap. 1 — Introduzione (2)
| # | Figura | Tipo | Posizione |
|---|---|---|---|
| 1.1 | Imbuto narrativo: contesto → problema → contributi | concettuale | sez. 1.1 |
| 1.2 | Sintesi visuale dei contributi (3 layer) | concettuale | sez. 1.4 |

### Cap. 2 — Background (4)
| # | Figura | Tipo |
|---|---|---|
| 2.1 | Tre meccanismi di grounding affiancati (Web, RAG, Text-to-SQL) | schema |
| 2.2 | Pipeline RAG canonica (chunking → embedding → retrieval → gen) | schema |
| 2.3 | Tassonomia multi-agent (cooperative, hierarchical, competitive) | schema |
| 2.4 | Ciclo ReAct (Thought → Action → Observation) | schema |

### Cap. 3 — Architettura agenti (6)
| # | Figura | Tipo |
|---|---|---|
| 3.1 | **Architettura d'insieme della suite** (riusare `architettura-sistema.png` esistente) | architetturale |
| 3.2 | Sequence auth federata Entra ID | sequence |
| 3.3 | Flusso request Vera (DLP → Web grounding → SSE) | sequence |
| 3.4 | Pipeline RAG di CooPolicy (query expansion → retrieval → gen) | sequence |
| 3.5 | Agentic loop NPS (run_sql / analyze / chart) | sequence |
| 3.6 | Doppia variante SysAid affiancata (Gemini vs Sonnet) | architetturale |

### Cap. 4 — Implementazione agenti (3)
| # | Figura | Tipo |
|---|---|---|
| 4.1 | Albero del monorepo (estratto) | listato |
| 4.2 | Pipeline CI/CD (Cloud Build → Artifact Registry → Cloud Run) | schema |
| 4.3 | Catena di sicurezza pre-generazione (DLP + Model Armor) | schema |

### Cap. 5 — Orion architettura (3)
| # | Figura | Tipo |
|---|---|---|
| 5.1 | **Architettura ad alto livello di Orion** | architetturale |
| 5.2 | Routing decision flow (3 fasce di confidence) | flowchart |
| 5.3 | Sequence diagram di un turno completo | sequence |

### Cap. 6 — Orion implementazione (2)
| # | Figura | Tipo |
|---|---|---|
| 6.1 | Mockup pagina RouterMetrics dell'admin panel | mockup/screenshot |
| 6.2 | Schema ER del database Orion (con `orion_routing_logs`) | ER |

### Cap. 7 — Orion valutazione (5)
| # | Figura | Tipo | **Dato reale?** |
|---|---|---|---|
| 7.1 | Schema della test suite Coda (estratto) | tabella/schema | no |
| 7.2 | **Bar chart accuracy per agente** | grafico dati | **sì** |
| 7.3 | **Calibrazione confidence: corretti vs errati (istogramma)** | grafico dati | **sì** |
| 7.4 | **Timeline accuracy per versione di system prompt** | grafico dati | **sì** |
| 7.5 | **Distribuzione latenza routing step (boxplot p50/p95/p99)** | grafico dati | **sì** |

> Le 4 figure di Cap. 7 con dati reali sono il **fulcro** della valutazione
> sperimentale — sono quelle che dimostrano la solidità del lavoro.

### Cap. 8 — Conclusioni (1, opzionale)
| # | Figura | Tipo |
|---|---|---|
| 8.1 | Roadmap evoluzioni future (timeline) | concettuale |

**Totale: 26 figure** (25 se si omette la 8.1 opzionale).

---

## 5. Bibliografia: 46 voci in 12 filoni

File: `bibliography.bib` (BibTeX) + `letteratura-complessiva.md`
(mappatura per filone con affidabilità ✅/⚠️ e capitolo della tesi).

**Voci primarie** (ordine di importanza per la tesi):
1. `vaswani2017attention` — Transformer (cap. 2)
2. `lewis2020rag` — RAG (cap. 2, 3)
3. `wei2022cot` — Chain-of-Thought (cap. 5)
4. `yao2022react` — ReAct (cap. 2, 3)
5. `wu2023autogen` — pattern orchestratore (cap. 5)
6. `guo2024multiagent` — survey multi-agent (cap. 2)
7. `chen2023frugalgpt` + `ong2024routellm` — routing (cap. 5, 8)
8. `kadavath2022knowsknows` — confidence calibration (cap. 5, 7)
9. `liu2023agentbench` — valutazione agenti (cap. 7)
10. `zheng2023llmjudge` — LLM-as-a-Judge (cap. 7)
11. `es2023ragas` — valutazione RAG (cap. 2)
12. `xu2024hallucination` — limiti LLM (cap. 1, 2)

---

## 6. Aspetti stilistici e regole di redazione

- **Citazioni inline** ovunque: ogni affermazione tecnica non banale
  va ancorata con `\cite{}`. Stile biblatex numerico (è già configurato
  in `main.tex`).
- **Progettazione separata da implementazione**: cap. 3 = decisioni
  e motivazioni, cap. 4 = "come è stato realizzato".
  Stesso pattern per Orion (cap. 5 vs cap. 6).
- **Figure numerate per capitolo** (es. `fig:vera_flow` in Cap. 3,
  `fig:orion_sequence` in Cap. 5): label coerenti con il numero.
- **Lunghezza target**: ~150-180 pagine totali per una tesi magistrale
  ben dimensionata.
- **No "polpa" come titolo di capitolo** (linea-guida del prof, scherzo a parte).

---

## 7. Riferimenti operativi

- Roadmap implementativa Orion: `plans/ORION_ROADMAP.md`
- Letteratura specifica orchestrazione: `plans/ORION_LETTERATURA.md`
- Bibliografia complessiva: `letteratura-complessiva.md`
- Linee guida prof: `descrizione-tesi.md` (sezione tra virgolette)
- Documenti tesi precedenti: `/home/dave/workspace/github/unibo/prova-finale/`
  (`bozza-tesi.md`, `elenco-capitoli.md`, `bibliografia.md`)
- Codice della suite: `/home/dave/workspace/bitbucket/c30-ai-agents/`
