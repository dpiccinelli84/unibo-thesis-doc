# Letteratura complessiva — Tesi Davide Piccinelli

> **Documento di lavoro.** Unifica le fonti di `bibliografia.md` (filoni 1-11)
> e `plans/ORION_LETTERATURA.md` (filoni Orion A-D), eliminando i duplicati
> e organizzando per filone tematico. Il file BibTeX corrispondente è
> `bibliography.bib`. Ultimo aggiornamento: 2026-05-07.

---

## Mappatura: dove ciascuna voce serve nella tesi

Le voci sono raggruppate **per filone tematico**. Per ogni voce sono
indicati: la **chiave BibTeX** da usare con `\cite{}`, l'**affidabilità**
(✅ confermato / ⚠️ usare con cautela), e il **capitolo della tesi** in
cui si prevede di citarla.

---

## Filone 1 — Fondamenti: Transformer e LLM

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `vaswani2017attention` | Vaswani et al., 2017 — *Attention is All You Need* | ✅ | 2.1 |
| `brown2020gpt3` | Brown et al., 2020 — *Language Models are Few-Shot Learners* (GPT-3) | ✅ | 1.1, 2.2 |
| `ouyang2022instructgpt` | Ouyang et al., 2022 — *InstructGPT, RLHF* | ✅ | 2.2 |
| `chang2023llmsurvey` | Chang et al., 2023 — *Survey on Evaluation of LLMs* | ✅ | 2.1, 2.5 |
| `xu2024hallucination` | Xu et al., 2024 — *Hallucination is Inevitable* | ✅ | 1.1, 2.2 |

---

## Filone 2 — Prompt engineering, ragionamento, tool use

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `wei2022cot` | Wei et al., 2022 — *Chain-of-Thought Prompting* | ✅ | 2.3, 5.2 |
| `yao2022react` | Yao et al., 2022 — *ReAct* | ✅ | 2.6, 3.x (agentic loop) |
| `wang2022selfconsistency` | Wang et al., 2022 — *Self-Consistency* | ⚠️ | 5.2 (discussa), 8 (futuro) |
| `sahoo2024prompteng_survey` | Sahoo et al., 2024 — *Prompt Engineering Survey* | ✅ | 7.6 (iterazione prompt) |

---

## Filone 3 — Retrieval-Augmented Generation (RAG)

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `lewis2020rag` | Lewis et al., 2020 — *RAG* | ✅ | 1.2, 2.4.2, 3.3 (CooPolicy) |
| `guu2020realm` | Guu et al., 2020 — *REALM* | ✅ | 2.4 |
| `gao2022hyde` | Gao et al., 2022 — *HyDE* | ✅ | 2.4.2 |
| `ma2023query_expansion` | Ma et al., 2023 — *Query Expansion by Prompting* | ✅ | 2.4.2, 3.3, 4.x (CooPolicy impl) |

---

## Filone 4 — Valutazione di sistemi RAG e LLM

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `es2023ragas` | Es et al., 2023 — *RAGAS* | ✅ | 2.5 |
| `ragas_docs` | RAGAS — documentazione del framework | ✅ | 2.5 (nota a piè) |
| `zheng2023llmjudge` | Zheng et al., 2023 — *LLM-as-a-Judge / MT-Bench* | ✅ | 2.5, 7.1, 7.7 |
| `liu2023agentbench` | Liu et al., 2023 — *AgentBench* | ✅ | 7.1, 7.7, 8.4 |
| `liang2022helm` | Liang et al., 2022 — *HELM* | ⚠️ | 7.7 (riferimento generale) |

---

## Filone 5 — Text-to-SQL

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `yu2018spider` | Yu et al., 2018 — *Spider* | ✅ | 2.4.3, 3.4-3.5 |
| `li2023bird` | Li et al., 2023 — *BIRD* | ✅ | 2.4.3, 3.4-3.5 |
| `pourreza2023dinsql` | Pourreza & Rafiei, 2023 — *DIN-SQL* | ✅ | 2.4.3, 3.4 |

---

## Filone 6 — Multi-Agent LLM e Orchestrazione

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `wu2023autogen` | Wu et al., 2023 — *AutoGen* | ✅ | 1.4, 2.6, 5.1, 8.1 |
| `guo2024multiagent` | Guo et al., 2024 — *LLM Multi-Agent Survey* | ✅ | 2.6 |
| `wang2024moa` | Wang et al., 2024 — *Mixture-of-Agents* | ✅ | 2.6, 5.1 |
| `jiang2024mixtral` | Jiang et al., 2024 — *Mixtral of Experts* | ⚠️ | 2.6 (per contrasto con MoA) |
| `langchain_docs` | LangChain — framework | ✅ | 2.6 (cenni) |
| `llamaindex_docs` | LlamaIndex — framework | ✅ | 2.6 (cenni) |
| `google_adk_docs` | Google Agent Development Kit | ✅ | 2.6, 8.1 (futuro) |

---

## Filone 7 — LLM Routing e ottimizzazione costo-qualità

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `chen2023frugalgpt` | Chen et al., 2023 — *FrugalGPT* | ✅ | 2.7, 5.1 |
| `ong2024routellm` | Ong et al., 2024 — *RouteLLM* | ✅ | 1.4, 2.7, 5.2 (alternative), 8.1 |
| `routellm_repo` | RouteLLM — repository ufficiale | ✅ | 2.7 (nota a piè) |

---

## Filone 8 — Stima dell'incertezza, Active Learning, Human-in-the-Loop

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `kadavath2022knowsknows` | Kadavath et al., 2022 — *Mostly Know What They Know* | ✅ | 2.7, 5.2, 7.4 |
| `settles2012active` | Settles, 2012 — *Active Learning* | ✅ | 5.2 (clarification), 2.7 |
| `diao2023activeprompting` | Diao et al., 2023 — *Active Prompting* | ⚠️ | (opzionale, approfondimento) |

---

## Filone 9 — Sicurezza, privacy, prompt injection

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `perez2022promptinjection` | Perez & Ribeiro, 2022 — *Ignore Previous Prompt* | ✅ | 2.8, 4.1 |
| `gcp_modelarmor` | Google Cloud Model Armor | ✅ | 2.8, 4.1 |
| `gcp_dlp` | Google Cloud Sensitive Data Protection (DLP) | ✅ | 2.8, 4.1 |

---

## Filone 10 — Identity federation e protocolli

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `rfc6749oauth2` | RFC 6749 — OAuth 2.0 | ✅ | 2.9, 3.1.3 |
| `oidc1_0core` | OpenID Connect Core 1.0 | ✅ | 2.9, 3.1.3 |
| `rfc7519jwt` | RFC 7519 — JWT | ✅ | 2.9 |
| `msft_entra_id` | Microsoft Entra ID — docs | ✅ | 2.9, 3.1.3 |
| `msft_msal` | Microsoft MSAL | ✅ | 2.9, 4.1.4 |

---

## Filone 11 — Usabilità (cenni, eventuale appendice)

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `brooke1996sus` | Brooke, 1996 — *SUS* | ✅ | (eventuale appendice usabilità) |
| `nielsen2000fiveusers` | Nielsen, 2000 — *5 utenti* | ✅ | (idem) |

> **Nota:** la valutazione di usabilità (SUS) era presente nella bozza-tesi.md
> originaria. Nella nuova struttura focalizzata su Orion, è opzionale: può
> essere inserita nel Cap. 7 (valutazione) come una sotto-sezione complementare,
> oppure spostata in appendice. Decisione da prendere quando i dati saranno
> disponibili.

---

## Filone 12 — Infrastruttura cloud e servizi managed

| Chiave BibTeX | Riferimento | Aff. | Cap. tesi |
|---|---|---|---|
| `gcp_vertexai` | Google Vertex AI — overview | ✅ | 2.10, 4.1 |
| `gcp_vertex_rag` | Google Vertex AI RAG Engine | ✅ | 2.4.2, 3.3 |
| `gcp_grounding` | Grounding with Google Search | ✅ | 2.4.1, 3.2 |
| `gcp_cloudrun` | Google Cloud Run | ✅ | 2.10, 4.1 |
| `gcp_cloudsql` | Google Cloud SQL | ✅ | 2.10, 6.5 |
| `gcp_bigquery` | Google BigQuery | ✅ | 2.10, 3.4-3.5 |
| `terraform_docs` | HashiCorp Terraform | ✅ | 2.10, 4.1.3 |
| `anthropic_docs` | Anthropic Claude API | ✅ | 4.5.2 (SysAid Sonnet) |

---

## Riepilogo e voci primarie

**Voci totali nel BibTeX:** ~46.

**Paper "primari"** sui quali costruire il nucleo argomentativo (ordine
di importanza per la tesi):

1. `vaswani2017attention` — fondazione del Transformer (cap. 2)
2. `lewis2020rag` — fondazione del RAG (cap. 2, 3)
3. `wei2022cot` — Chain-of-Thought, base del reasoning del router (cap. 5)
4. `yao2022react` — pattern ReAct degli agenti (cap. 2, 3)
5. `wu2023autogen` — pattern orchestratore-agenti specializzati (cap. 5)
6. `guo2024multiagent` — survey di riferimento per posizionare Orion (cap. 2)
7. `chen2023frugalgpt` + `ong2024routellm` — filone routing (cap. 5, 8)
8. `kadavath2022knowsknows` — fondazione del confidence score (cap. 5, 7)
9. `liu2023agentbench` — metodologia di valutazione agenti (cap. 7)
10. `zheng2023llmjudge` — LLM-as-a-Judge per la valutazione (cap. 7)
11. `es2023ragas` — valutazione RAG (cap. 2)
12. `xu2024hallucination` — limite strutturale degli LLM (cap. 1, 2)

Tutti gli altri sono di supporto, riferimenti tecnici di prodotto o
approfondimenti.

---

## Voci eliminate / scelte non incluse

- **HELM** (`liang2022helm`): inserito come riferimento di cornice
  ma non come paper primario; il framework è troppo ampio per la
  valutazione specifica di Orion.
- **Active Prompting** (`diao2023activeprompting`): mantenuto in
  bibliografia come approfondimento ma non citato esplicitamente nei
  capitoli (può essere usato in espansione del cap. 5 se serve).
- **Personal Docs** (RAG per-utente): non ha un capitolo dedicato in
  questa stesura. Se in futuro si volesse reintegrarlo, le voci RAG
  (filone 3) sono già pronte.
