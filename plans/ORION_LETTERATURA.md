# ORION — Riferimenti Accademici per la Tesi

Documento di riferimento bibliografico per la sezione "Letteratura" della tesi.  
Ultimo aggiornamento: 2026-05-05

---

## Note metodologiche

I paper sono organizzati per filone tematico, con una valutazione critica di ogni fonte.  
**Legenda affidabilità:**
- ✅ Paper verificato, ampiamente citato, altamente raccomandato
- ⚠️ Paper reale ma con avvertenze d'uso (vedi note)
- ❌ Riferimento problematico — non usare senza verifica

---

## Filone A — LLM Routing e Model Cascading

*Studia come instradare le query al modello giusto per bilanciare costo, latenza e qualità. È il filone più direttamente rilevante per il routing step di Orion.*

### A1. FrugalGPT
**Chen, L., Zaharia, M., & Zou, J. (2023).** FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance. *arXiv:2305.05176*

✅ **Raccomandato — paper fondamentale del filone.**  
Introduce il concetto di **LLM cascade**: usare modelli leggeri per query semplici e scalare a modelli più potenti solo quando necessario, con un "early-exit" basato sulla confidenza della risposta. Il meccanismo di Orion (Flash per routing, poi Flash o Sonnet per l'esecuzione in base alla complexity) è direttamente inquadrabile in questo framework.  
**Come citarlo:** sezione architettura, per giustificare teoricamente la scelta di usare modelli diversi in base alla stima di complessità.

### A2. RouteLLM
**Ong, I., et al. (2024).** RouteLLM: Learning to Route LLMs with Preference Data. *arXiv:2406.18665*  
*(LMSYS Org — gli stessi di Chatbot Arena / LMSYS)*

✅ **Raccomandato.**  
Formalizza il problema del routing come classificazione binaria strong/weak model. Propone e confronta diversi tipi di router: matrix factorization, similarity-based (embeddings), classificatori RF, e router basati su LLM. Fornisce una metodologia di valutazione (MMLU, MT-Bench) che puoi adattare per giustificare il tuo approccio di evaluation su Coda.  
**Come citarlo:** sezione "Router Design" — per posizionare la scelta di un LLM-based router rispetto alle alternative.

### A3. Parole chiave di ricerca per questo filone
Per trovare paper correlati su Google Scholar / arXiv:
- `LLM routing` `model cascading` `cost-aware LLM inference`
- `query complexity estimation LLM`
- `intent classification large language models`
- `LLM cascade early exit`

---

## Filone B — Multi-Agent Systems e Orchestrazione

*Studia come più LLM con ruoli specializzati collaborano. Orion come "manager agent" su un pool di agenti esperti.*

### B1. AutoGen
**Wu, Q., Bansal, G., et al. (2023).** AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. *arXiv:2308.08155*

✅ **Raccomandato.**  
Framework Microsoft che introduce il pattern "GroupChat" con un `GroupChatManager` (orchestratore) che instrada i messaggi agli agenti appropriati. Il tuo Orion implementa lo stesso pattern ma con routing LLM-based invece di rule-based. Citalo per mostrare che l'architettura si inserisce in un filone consolidato della ricerca.  
**Come citarlo:** sezione architettura, per il pattern orchestratore-agenti specializzati.

### B2. LLM-Based Multi-Agent Systems Survey
**Guo, T., et al. (2024).** Large Language Model based Multi-Agents: A Survey of Progress and Challenges. *arXiv:2402.01680*

✅ **Raccomandato — survey recente (2024) che copre esattamente il tuo dominio.**  
Categorizza le architetture multi-agente LLM (cooperative, competitive, hierarchical). Orion è classificabile come **hierarchical architecture** con un supervisor agent. Utile come riferimento generale per la sezione "Stato dell'arte".  
**Nota:** verifica sempre la versione più aggiornata su arXiv — i survey vengono spesso aggiornati.

### B3. ReAct
**Yao, S., et al. (2022).** ReAct: Synergizing Reasoning and Acting in Language Models. *arXiv:2210.03629* (ICLR 2023)

✅ **Raccomandato — paper fondativo del pattern Ragionamento + Azione.**  
Descrive il ciclo Thought → Action → Observation che è alla base del `### 🧠 RAGIONAMENTO` già presente in tutti gli agenti del progetto. Orion estende questo pattern aggiungendo un "Action" di tipo routing verso agenti esterni.  
**Come citarlo:** sezione "Chain of Thought nell'orchestratore".

### B4. ⚠️ Mixture of Experts (MoE)
**Jiang, A.Q., et al. (2024).** Mixtral of Experts. *arXiv:2401.04088*

⚠️ **Usare con cautela e precisione terminologica.**  
Il MoE originale è un'architettura **interna al modello** (a livello di layer transformer), non un'architettura a livello applicativo. Usare questo termine per descrivere Orion è una metafora, non una corrispondenza tecnica.  
**Raccomandazione:** se vuoi usare la terminologia MoE, citalo come "ispirazione concettuale" e specifica che Orion implementa un **application-level MoE** o **Mixture of Agents** (MoA), che è un termine più corretto per il livello architetturale in cui operi.

### B5. Mixture of Agents (MoA) — alternativa più corretta al MoE
**Wang, J., et al. (2024).** Mixture-of-Agents Enhances Large Language Model Capabilities. *arXiv:2406.04692*

✅ **Più corretto di MoE per il tuo caso d'uso.**  
Introduce esplicitamente il termine "Mixture of Agents" per architetture dove più LLM collaborano a livello applicativo. Semanticamente più vicino a Orion rispetto al MoE classico.

### B6. Parole chiave di ricerca
- `multi-agent LLM orchestration` `supervisor agent pattern`
- `hierarchical multi-agent system`
- `LLM task routing multi-agent`
- `specialist agent generalist orchestrator`

---

## Filone C — Stima dell'Incertezza e Human-in-the-Loop

*Come fa l'LLM a sapere di non sapere? Fondamento teorico per il confidence score e il meccanismo di clarification di Orion.*

### C1. Chain-of-Thought Prompting
**Wei, J., et al. (2022).** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022. arXiv:2201.11903*

✅ **Fondativo — base teorica del CoT nell'orchestratore.**  
Dimostra che forzare un modello a "pensare ad alta voce" prima di rispondere migliora l'accuracy su task di ragionamento. Il `reasoning` field nell'output strutturato del router di Orion è direttamente un'applicazione di questo principio.

### C2. ⚠️ Self-Consistency
**Wang, X., et al. (2022).** Self-Consistency Improves Chain of Thought Reasoning in Language Models. *arXiv:2203.11171* (ICLR 2023)

⚠️ **Rilevante ma costoso da implementare.**  
Propone di generare N ragionamenti CoT indipendenti e votare la risposta più consistente come proxy di confidenza. Teoricamente applicabile al routing di Orion (più call Flash → voto), ma il costo computazionale lo rende impraticabile in produzione. Citalo come "possibile miglioramento futuro" o nella discussione teorica del confidence score.

### C3. Confidence Calibration in LLMs
**Kadavath, S., et al. (2022).** Language Models (Mostly) Know What They Know. *arXiv:2207.05221*

✅ **Raccomandato per la sezione sul confidence score.**  
Studia la capacità degli LLM di stimare la propria incertezza. Dimostra che i modelli grandi (Claude, GPT-4) sono ragionevolmente calibrati quando esplicitamente interrogati sulla propria certezza. Supporta teoricamente la scelta di usare un confidence score generato dall'LLM stesso nel routing step.

### C4. Human-in-the-Loop / Active Learning
**Settles, B. (2012).** Active Learning. *Synthesis Lectures on Artificial Intelligence and Machine Learning.*

✅ **Reference classico per il meccanismo di clarification.**  
Il principio per cui Orion chiede all'utente di specificare quando la confidenza è bassa è riconducibile all'**active learning**: il sistema interroga l'oracolo (l'utente) solo quando il dato aggiuntivo ha il massimo valore informativo. Utile per inquadrare teoricamente la soglia di confidence.

### C5. ⚠️ Active Prompting
**Diao, S., et al. (2023).** Active Prompting with Chain-of-Thought for Large Language Models. *arXiv:2302.12246*

⚠️ **Attinente ma non perfettamente allineato.**  
Studia come selezionare i migliori esempi da includere nel few-shot prompting basandosi sull'incertezza del modello. Il collegamento con Orion è indiretto (la tua "incertezza" riguarda il routing, non la selezione degli esempi). Citalo se vuoi approfondire la sezione teorica, ma non è un riferimento primario.

### C6. Parole chiave di ricerca
- `LLM uncertainty estimation` `confidence calibration language models`
- `LLM self-evaluation` `LLM knows what it knows`
- `human-in-the-loop conversational AI`
- `clarification in task-oriented dialogue`

---

## Filone D — Valutazione degli LLM e LLMOps

*Metodologia per il sistema di test su Coda. Come valutare iterativamente le versioni del system prompt.*

### D1. MT-Bench / LLM-as-a-Judge
**Zheng, L., et al. (2023).** Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *arXiv:2306.05685* (NeurIPS 2023)

✅ **Raccomandato — direttamente applicabile al tuo sistema di valutazione.**  
Introduce il concetto di **LLM-as-a-Judge**: usare un LLM (es. Gemini Pro) come "giudice" per valutare la qualità delle risposte invece del solo match esatto. Puoi applicarlo al tuo evaluation script: oltre a confrontare `agent_prodotto == agent_atteso`, un giudice LLM può valutare se il `reasoning` del router è coerente e ben motivato.  
**Come citarlo:** sezione metodologia di valutazione.

### D2. AgentBench
**Liu, X., et al. (2023).** AgentBench: Evaluating LLMs as Agents. *arXiv:2308.03688*

✅ **Raccomandato per inquadrare il tuo test suite.**  
Propone un benchmark strutturato per agenti LLM con task eterogenei. Il tuo sistema di test su Coda è un'applicazione domain-specific dello stesso principio: un gold standard di prompt etichettati, esecuzione automatica, raccolta metriche. Citalo per mostrare che il tuo approccio è metodologicamente fondato.

### D3. ⚠️ HELM
**Liang, P., et al. (2022).** Holistic Evaluation of Language Models. *arXiv:2211.09110*

⚠️ **Troppo generale per il tuo caso d'uso specifico.**  
HELM è un framework di benchmark molto ampio (accuracy, calibration, fairness, ecc.) pensato per valutare modelli in modo olistico. Il tuo evaluation è più specifico (routing accuracy). Puoi citarlo nel contesto della "metodologia di valutazione" come riferimento del campo, ma non è il tuo paper principale.

### D4. Prompt Engineering Survey
**Sahoo, P., et al. (2024).** A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications. *arXiv:2402.07927*

✅ **Utile per la sezione sull'ottimizzazione del system prompt del router.**  
Survey completo delle tecniche di prompt engineering. Inquadra il tuo processo iterativo di miglioramento del system prompt (testare → valutare su Coda → aggiornare → ripetere) come un'attività di **prompt optimization** con feedback empirico.

### D5. Parole chiave di ricerca
- `LLM evaluation benchmark` `prompt evaluation methodology`
- `LLM-as-a-judge` `automatic LLM evaluation`
- `LLMOps` `system prompt versioning`
- `gold standard evaluation NLP`

---

## Riepilogo: paper primari consigliati

Questi sono i paper su cui costruire il nucleo della sezione letteratura. Gli altri sono approfondimenti.

| # | Paper | Anno | Perché è primario |
|---|---|---|---|
| 1 | FrugalGPT (Chen et al.) | 2023 | Fondamento teorico del routing per complessità |
| 2 | RouteLLM (Ong et al.) | 2024 | Stato dell'arte specifico sul routing LLM |
| 3 | AutoGen (Wu et al.) | 2023 | Pattern orchestratore-agenti specializzati |
| 4 | LLM Multi-Agent Survey (Guo et al.) | 2024 | Survey di riferimento per lo stato dell'arte |
| 5 | ReAct (Yao et al.) | 2022 | Base teorica del CoT nel routing |
| 6 | Calibration (Kadavath et al.) | 2022 | Fondamento teorico del confidence score |
| 7 | LLM-as-a-Judge (Zheng et al.) | 2023 | Metodologia di valutazione |
| 8 | AgentBench (Liu et al.) | 2023 | Framework per il test suite |

---

## Revisione critica delle fonti proposte dall'altro LLM

| Fonte proposta | Giudizio | Note |
|---|---|---|
| FrugalGPT | ✅ Confermato | Paper fondamentale, usarlo come anchor del filone A |
| RouteLLM | ✅ Confermato | Aggiungere dettaglio: è LMSYS org, non solo "2024" |
| AutoGen | ✅ Confermato | Verificare versione paper vs versione GitHub (divergono) |
| MoE / Mixtral | ⚠️ Usare con cautela | Sostituire con "Mixture of Agents" (Wang et al. 2024) per correttezza terminologica |
| Self-Reflection / Uncertainty | ⚠️ Vago | Specificare Kadavath et al. 2022 — paper concreto sul tema |
| Active Prompting | ⚠️ Indiretto | Usarlo come approfondimento, non come riferimento primario |
| LLM-as-a-Judge (Zheng et al.) | ✅ Confermato | Già incluso in D1 — ottimo paper |
| AgentBench | ✅ Confermato | Direttamente applicabile al test suite su Coda |
| HELM | ⚠️ Troppo generale | Non escluderlo ma non è un riferimento primario per il tuo caso |
| Active Learning (Settles) | ✅ Aggiunto | Buona base teorica per il meccanismo di clarification |
