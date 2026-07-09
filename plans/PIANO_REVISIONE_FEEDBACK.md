# Piano di revisione tesi — recepimento feedback prof (giugno–luglio 2026)

> Roadmap operativa per la revisione della tesi dopo i feedback dei prof:
> **primo giro** (mail di Bianca Raimondi e Saverio Giallorenzo del 4/6/2026 → Fasi 0–4)
> e **secondo giro** (colloquio con Bianca Raimondi del 9/7/2026 → Fase 5).
> **Aggiornare le checkbox a ogni sessione di lavoro.**

---

## 1. Contesto e decisioni prese (non rilitigare)

**Feedback ricevuto (4/6/2026):**
- **Raimondi:** background buono (soprattutto parte LLM); accorpare i capp. 3–6; dare più
  spazio al cap. 7 (il più importante scientificamente) su due assi:
  (a) prompt engineering con esempi concreti su dati aziendali + tecniche citate dalla letteratura;
  (b) ottimizzazione costo–qualità (tema di attuale interesse per la comunità).
- **Giallorenzo:** conferma, cap. 7 in particolare; razionalizzare la duplicazione
  architettura → implementazione → Orion ("presentare una sola volta e richiamare");
  fondere i capitoli in 1 o 2. Amministrativo: **Gabbrielli relatore, Giallorenzo e
  Raimondi correlatori**.

**Feedback ricevuto (colloquio Raimondi, 9/7/2026)** — dettaglio operativo in Fase 5:
- Indice più asciutto: ridurre gli "elenchi puntati" di sezioni, **max 4–5 sottosezioni**
  (il rilievo parte dal Background, ma vale per tutti i capitoli).
- "Spremere" la parte sperimentale.
- **Non dare mai per scontato che un argomento sia conosciuto**: Transformer sicuramente,
  encoder/decoder, attention mechanism; pretraining/fine-tuning ecc. con figure o esempi
  testuali (es. pretraining = nessuna label → mostrare sample); zero-shot/few-shot sempre
  con esempi, idealmente immagini (strumento suggerito: Draw.io; se immagini dal web,
  citarne la fonte).
- Citazioni dei paper: se il paper è solo su arXiv va bene arXiv; **se esiste anche la
  versione in conferenza/rivista, preferire quella**.
- Aggiungere citazioni in generale.
- Framework RAGAS: più dettaglio, con le specifiche tecniche usate e **1 esempio semplice
  ma concreto di valutazione di un sample**.
- Regola generale trasversale: **più esempi ci sono, meglio è.**

**Decisioni prese (sessione 9/6/2026):**
- Variante **a 2 capitoli**: la polpa descrittiva diventa "Suite di agenti" + "Orion".
- Struttura target a **6 capitoli** (da 8).
- Titolo tesi invariato.
- Background (cap. 2) invariato nei contenuti.
- La sezione "Lavori correlati" resta nel capitolo Orion (non migra nel background).
- Il rapporto descrittivo/valutazione passa da 68/14 pagine a ~55/28.
- **(14/6)** Tagliato il confronto sperimentale router **Flash vs Pro** (ex F3.1/F2.2d):
  non richiesto dai prof, chiudeva solo un limite auto-dichiarato. La scelta di
  Gemini Flash per il router resta motivata (latenza/costo) in 4.4.3 e Tab. decisioni,
  senza supporto sperimentale dedicato.
- **(14/6)** F2.1b: storico pre-v1.0 del prompt non recuperabile (repo a 1 commit);
  pivot a estratti di prompt engineering sugli agenti verticali (nuova Sez. 5.3.4)
  + leva costo–qualità dei classificatori di complessità in 5.6.

**Numeri della versione consegnata (tesi-piccinelli-davide-02062026.pdf):**
capp. 3–6 = pp. 21–88 (68 pp), cap. 7 = pp. 89–102 (14 pp), totale ~107 pp.

---

## 2. Stato avanzamento

| Fase | Descrizione | Stato |
|------|-------------|-------|
| F0   | Frontespizio (relatore/correlatori) | ✅ 9/6 (resta verifica titoli correlatori — Davide) |
| F1   | Ristrutturazione 8 → 6 capitoli | ✅ 9/6 (fusioni + deduplicazioni; rilettura suture fatta) |
| F2   | Espansione capitolo Valutazione (prompt eng. + costo–qualità) | ✅ **14/6 completata**: 5.3 + nuova 5.3.4 (PE sugli agenti) + 5.6 costo–qualità con ρ/S reali e worked example |
| F3   | Esperimenti e dati (richiedono Davide su GCP) | ⏳ F3.4/F3.6 fatte; F3.1/F3.5 tagliate; **resta solo F3.3 (token medi), opzionale** |
| F4   | Coerenza finale, compilazione, consegna ai prof | ✅ **9/7**: F4.4 chiusa — feedback ricevuto a voce da Raimondi (→ Fase 5) |
| F5   | Recepimento feedback Raimondi 9/7 (indice, background didattico, esempi/figure, bibliografia, RAGAS) | ⏳ da avviare |

**Esito misurato (9/6 sera):** capp. 3–4 = pp. 21–82 (62 pp, dalle 68 della
versione consegnata); cap. 5 = pp. 83–104 (**22 pp, dalle 14 consegnate**):
nuova Sez. 5.3 "Il prompt del router: anatomia e tecniche" (3 listing del
prompt reale + tabella delle 9 tecniche mappate sulla letteratura) e nuova
Sez. 5.6 "Ottimizzazione costo–qualità" (RQ6, modello parametrico del
risparmio, breakdown EX per fascia con IC Wilson); Discussione spostata in
chiusura con risposta a RQ6 e nuovo limite dichiarato.

**Aggiornamento (14/6 sera):** completati asse (a) — PE sugli agenti (nuova Sez. 5.3.4, 6 listing
reali: header costituzionale, AllyCare schema/SQL/fiducia-tool, CooPolicy regole, SysAid SEARCH) —
e asse (b) — costo–qualità con numeri reali: ρ≈4 Gemini → **S≈2,9× (~65%)**; SysAid ρ≈6–10 →
3,6–4,6×; Tab. listini + worked example (~0,55 M req/anno: sempre-Pro ~€6,9k vs routing ~€2,4k →
**~€4,5k/anno risparmiati**); `cost_model.py` esteso (`--routing`); bib: listini Google/Anthropic.
F4.1 (abstract/§1.4/§1.6/conclusioni) e F4.2 fatte; **asciugatura prosa: descrittivo 62→59 pp**
(nessun contenuto/figura rimossi). **Stato: tot 128 pp, descrittivo 59, valutazione 27, compila pulito.**
Modifiche NON committate (Davide ci pensa). Prossimi: F0 (titoli/sessione), F4.4 (consegna),
opzionali → ridimensionare screenshot per 59→55 e F3.3 (token reali).

---

## 3. FASE 0 — Amministrativa

- [x] **F0.1** `main.tex` frontespizio: Relatore = Chiar.mo Prof. Maurizio Gabbrielli;
      Correlatori = Saverio Giallorenzo, Bianca Raimondi. *(fatto 9/6)*
      **TODO Davide:** verificare i titoli accademici corretti da riportare
      (Prof./Dott.ssa) per i due correlatori — segnaposto `% TODO F0.1` nel tex.
- [ ] **F0.2** "Sessione (da definire) 2026" nel frontespizio: resta da concordare con i prof.

---

## 4. FASE 1 — Ristrutturazione 8 → 6 capitoli

### 4.1 Nuova mappa dei file

| Nuovo file | Contenuto | Origine |
|---|---|---|
| `chapters/03_agenti.tex` | Cap. 3 — La suite di agenti verticali | fusione `03_agenti_architettura.tex` + `04_agenti_implementazione.tex` |
| `chapters/04_orion.tex` | Cap. 4 — Orion: l'orchestratore | fusione `05_orion_architettura.tex` + `06_orion_implementazione.tex` |
| `chapters/05_valutazione.tex` | Cap. 5 — Valutazione sperimentale | rinomina `07_valutazione.tex` (+ espansioni in F2) |
| `chapters/06_conclusioni.tex` | Cap. 6 — Conclusioni | rinomina `08_conclusioni.tex` |

I 4 file originari dei capp. 3–6 vengono rimossi (restano nella history git).

### 4.2 Nuovo capitolo 3 — "La suite di agenti verticali" (label `chap:agenti`)

Struttura sezione per sezione (tra parentesi la sezione di origine):

1. Intro capitolo — riscritta (fonde le due intro)
2. `3.1` Principi guida (ex 3.1.1)
3. `3.2` Architettura d'insieme (ex 3.1.2, fig. `fig1`)
4. `3.3` Fondazioni trasversali — stack (ex 4.1.1), organizzazione codice (ex 4.1.2,
   figg. `multirepo_tree` + `progetto-bitbucket`), IaC/CI-CD (ex 4.1.3, figg.
   `arch-terraform` + `gitflow`), identità/auth (ex 4.1.4, figg. `login1/2`)
5. `3.4` Il portale utente (ex 4.2, fig. `portale`)
6. `3.5` Vera = caso d'uso (ex 3.2) + routing modello (ex 4.3.1) + pattern esecuzione
   (ex 4.3.2) + citazioni (ex 4.3.3) + catena di sicurezza (ex 4.3.4, fig. `flusso-prompt-full`)
7. `3.6` CooPolicy = caso d'uso (ex 3.3) + multi-corpus (ex 4.4.1) + retrieval (ex 4.4.2)
   + metadati (ex 4.4.3) + generazione vincolata (ex 4.4.4) + ACL/proxy (ex 4.4.5)
8. `3.7` AllyCare = caso d'uso (ex 3.4) + schema injection (ex 4.5.1) + tool/loop ADK
   (ex 4.5.2) + disciplina ragionamento (ex 4.5.3)
9. `3.8` SysAid = caso d'uso + pluralità modello (ex 3.5.1 + 3.5.2) + backend unificato
   (ex 4.6.1) + code path Gemini (ex 4.6.2) + code path Sonnet (ex 4.6.3)
10. `3.9` Pannello di amministrazione (ex 4.7)
11. `3.10` Alternative scartate (ex 3.6)

**Deduplicazioni nel cap. 3:** *(tutte fatte 9/6)*
- [x] Le 4 doppie introduzioni per agente (caso d'uso nel vecchio cap. 3 + ripartenza nel
      vecchio cap. 4) diventano una sezione unica per agente.
- [x] I rimandi interni "Cap. \ref{chap:agenti-architettura}" diventano riferimenti di
      sezione (`sec:agenti-principi` ecc.).
- [x] Caption di `fig:multirepo_tree`: il rimando al vecchio cap. 6 diventa `chap:orion`.

### 4.3 Nuovo capitolo 4 — "Orion: l'orchestratore" (label `chap:orion`)

1. Intro capitolo — riscritta
2. `4.1` Motivazione e visione architetturale (ex 5.1)
3. `4.2` Panoramica architetturale (ex 5.2, figg. `orion1` + `diagrammaconorion`)
   + **un paragrafo** sui 4 nuovi repository (compressione di ex 6.1: **niente seconda
   figura con l'elenco repo**, solo elenco inline + rimando a `fig:multirepo_tree`)
4. `4.3` Lavori correlati e posizionamento (ex 5.3, tab. `tab:orion-related`)
5. `4.4` Il routing step (ex 5.4 + ex 6.2.1 fusi):
   - output strutturato: **un solo listing** (il modello Pydantic `RouterOutput` + firma
     `classify`, ex `lst:classify-signature`; si elimina il listing JSON duplicato
     `lst:router-schema`) + la description list dei 5 campi (ex 5.4.1)
   - logica confidence/clarification (ex 5.4.2, fig. `orion2`)
   - scelta del modello (ex 5.4.3)
   - implementazione di `classify()`: le 4 fasi di ex 6.2.1 **asciugate** (la fase
     "output strutturato" non ripete enum/schema già descritti sopra) + fallback
     deterministico + paragrafo breve sull'endpoint `/api/orion/classify` (ex 6.2.4)
     con rimando al cap. 5
6. `4.5` Agent proxy e normalizzazione (ex 5.5 + ex 6.2.2 fusi: le 4 decisioni
   architetturali assorbono tabella endpoint e payload; fig. `orion3`)
7. `4.6` Conversation threading e gestione della storia (ex 5.6)
8. `4.7` Integrazione nel flusso di chat e sicurezza (ex 6.2.3, fig.
   `flusso-prompt-full-orion`; il testo richiama la catena di Vera senza ripeterla)
9. `4.8` Frontend (ex 6.3: badge di routing + renderer adattivo, figg. `routing1`,
   `approfondimenti-routing`, `routing3`)
10. `4.9` Admin panel (ex 6.4): le pagine standard = **una frase di richiamo** al pannello
    di Vera (`sec:agenti-admin-impl`); restano solo le 4 pagine specifiche di Orion.
    **La descrizione della pagina Eval (ex 6.4.1) migra nel cap. 5** (un rimando qui).
11. `4.10` Infrastruttura e persistenza (ex 6.5 + 6.6 fusi e asciugati; fig. `orion-er`;
    il pattern `create_all` = una frase con rimando al cap. 3)
12. `4.11` Decisioni architetturali e loro motivazione (ex 5.7, tab. `tab:orion-decisioni`
    — chiusura del capitolo)

**Deduplicazioni nel cap. 4:** *(tutte fatte 9/6)*
- [x] Elenco repository non ripetuto (−1 figura/listing).
- [x] Schema output router: un solo listing (−1 listing).
- [x] Routing step e proxy descritti una sola volta ciascuno.
- [x] Framework di valutazione descritto SOLO nel cap. 5 (ex 6.4.1 eliminata qui).
- [x] Pagine admin standard non rielencate.

### 4.4 Rinumerazione, label e riferimenti incrociati

Label di capitolo:

| Vecchio | Nuovo |
|---|---|
| `chap:agenti-architettura`, `chap:agenti-implementazione` | `chap:agenti` |
| `chap:orion-architettura`, `chap:orion-implementazione` | `chap:orion` |
| `chap:orion-valutazione`, `chap:conclusioni`, `chap:background`, `chap:introduzione` | invariati |

I label di sezione/figura/tabella restano invariati (sopravvivono alla fusione).

File con `\ref` da aggiornare (censiti con grep, sessione 9/6): *(tutti fatti 9/6)*
- [x] `01_introduzione.tex` — contributi (1.4) e sez. 1.6 "Struttura della tesi"
      riscritte per 6 capitoli.
- [x] `02_background.tex` — `chap:agenti-architettura` → `chap:agenti`.
- [x] `06_conclusioni.tex` (ex 08) — i 2 riferimenti ai capitoli fusi.
- [x] `05_valutazione.tex` (ex 07) — rimando a `subsec:orion-impl-eval` risolto in
      `subsec:eval-admin-page`; titolo capitolo → "Valutazione sperimentale".
- [x] `00_abstract.tex` — verificato: non cita la struttura a capitoli, invariato.
- [x] `main.tex` — lista `\input` aggiornata.

Nota tecnica adottata: i label dei capitoli/sezioni eliminati che erano ancora
referenziati altrove (`sec:agenti-vera-impl`, `sec:agenti-sysaid-impl`,
`subsec:orion-impl-proxy`, `sec:orion-impl-db`, ecc.) sopravvivono come **label
doppi** sulla sezione fusa corrispondente: nessun `\ref` esterno si è rotto.

### 4.5 Verifica di chiusura Fase 1

- [x] `latexmk` senza errori; biber ok (9/6: PDF 118 pp).
- [x] Zero "undefined references" / "multiply defined" in `main.log` (9/6).
- [x] Figure e tabelle tutte conservate (unica rimozione voluta: il listing-figura
      con l'elenco repo duplicato del vecchio cap. 6).
- [x] Rilettura dei punti di sutura (9/6 sera): sistemate le ripetizioni
      introdotte dalla fusione nei cappelli di SysAid, CooPolicy e AllyCare
      (doppio "X è l'agente...", doppio rimando a `subsec:bg-text2sql`).

---

## 5. FASE 2 — Espansione capitolo 5 "Valutazione sperimentale"

Obiettivo: da 14 a ~25–30 pagine. Struttura target:

```
5.1 Domande di ricerca            (ex 7.1 + NUOVA RQ6 costo–qualità)
5.2 Metodologia                   (ex 7.2; assorbe la pagina Eval ex 6.4.1)
5.3 Prompt engineering del router: iterazioni e tecniche   [NUOVA — richiesta Raimondi (a)]
5.4 Risultati del routing         (ex 7.3 + run aggiuntive da F3)
5.5 Qualità degli agenti verticali (ex 7.5 + breakdown per modello)
5.6 Ottimizzazione costo–qualità  [NUOVA — richiesta Raimondi (b)]
5.7 Valutazione economica complessiva (ex 7.6, SaaS vs consumo)
5.8 Discussione e limiti          (ex 7.4 aggiornata)
```

### 5.3 — Sezione "Prompt engineering del router" (F2.1)

- [x] **F2.1a** *(fatto 9/6)* Tre estratti del prompt v1.0 reale in tesi
      (`lst:prompt-regole`, `lst:prompt-confidence`, `lst:prompt-agente`), con
      `literate` per gli accenti nei listings e `\lstlistingname` = "Listato".
- [x] **F2.1b** *(risolto diversamente 14/6)* Lo storico pre-v1.0 NON è recuperabile
      (repo `unibo-thesis-src` a 1 commit, repo aziendale non disponibile). **Pivot:**
      invece della cronologia temporale, nuova **Sez. 5.3.4** "Prompt engineering negli
      agenti verticali: estratti reali" con 6 listing reali (header costituzionale;
      AllyCare schema+glossario, regole SQL, gerarchia verità/fiducia tool; CooPolicy
      regole non negoziabili; SysAid SEARCH/DATETIME) mappati sulla letteratura già
      citata, + leva costo–qualità (default asimmetrico dei classificatori di
      complessità: AllyCare "high", SysAid/CooPolicy "low") in 5.6. Risponde alla
      richiesta (a) di Raimondi. Rimosso il `% TODO F3.5` dalla chiusura di 5.3.
- [x] **F2.1c** *(fatto 9/6, Tab. `tab:eval-tecniche` con 9 tecniche)* Mappatura
      esplicita tecnica ↔ letteratura (voci già in `bibliography.bib`):
      - role prompting + delimitatori → survey Sahoo 2024 (`sahoo2024prompteng_survey`)
      - esempi per agente nel prompt del router → few-shot/in-context (`brown2020gpt3`)
      - campo `reasoning` obbligatorio → Chain-of-Thought (`wei2022cot`)
      - `response_schema` JSON vincolato → guided generation (`willard2023outlines`)
      - clarification sotto soglia → deferral/active prompting (`diao2023activeprompting`,
        `settles2012active`), human-in-the-loop
      - regole negative e di precedenza (Regola 8) → survey + esempio aziendale concreto
- [x] **F2.1d** *(fatto 9/6)* Tecniche degli agenti verticali in Tab.
      `tab:eval-tecniche` + paragrafo "effetti riscontrabili" (tool-trust, SQL
      eseguibile 23/25 e 25/25, enum che azzera i target inventati).
- [x] **F2.1e** Nessuna nuova voce bib necessaria: tutte le citazioni usano chiavi
      già presenti.

### 5.6 — Sezione "Ottimizzazione costo–qualità" (F2.2)

- [x] **F2.2a** *(fatto 9/6)* RQ6 attiva ("Il routing per complessità preserva la
      qualità delle risposte riducendo il costo?") con risposta parziale in 5.8.1.
- [x] **F2.2b** *(fatto 9/6)* Inquadramento FrugalGPT/RouteLLM nell'apertura di 5.6.
- [x] **F2.2c** *(completata 14/6)* Distribuzione low/high dal gold: **104/120
      low (86,7%), 16/120 high (13,3%)**; modello S = ρ/(f_low + f_high·ρ).
      **ρ istanziato con listini reali** (F3.6 fatta): coppia Gemini Flash↔Pro
      ρ≈4,0–4,2 (quasi mix-indipendente) → **S≈2,9× (~65%)**; coppia Flash↔Sonnet
      (SysAid) ρ≈6–10 → **S≈3,6–4,6× (~72–78%)**. Tab. `tab:eval-prezzi` (listini)
      + worked example `tab:eval-cq-saving` (~0,55 M req/anno: sempre-Pro ~€6,9k vs
      routing ~€2,4k → ~€4,5k/anno risparmiati) + paragrafo sensibilità + overhead
      router quantificato (S incl. router ≈2,3×). `cost_model.py` esteso
      (`request_cost`, `routing_savings`, flag `--routing`). Bib: `gcp_gemini_pricing`,
      `anthropic_pricing`. **Resta solo F3.3** (token medi reali) per trasformare il
      profilo di token assunto (4000 in / 800 out) in misurato — opzionale.
- [x] **F2.2e** *(fatto 9/6 — F3.4 risolta senza rerun)* I CSV `results/` del 29/05
      contengono già la colonna `complexity`; identificate le run citate in tesi
      (allycare_171107: 20/25 + exec 23/25; sysaid_171814: 21/25 + exec 25/25) e
      calcolato il breakdown (IC Wilson verificati a macchina):
      AllyCare low 14/17 (82,4%), high 6/8 (75,0%); SysAid low 12/16 (75,0%),
      **high 9/9 (100%)** → Tab. `tab:eval-cq-breakdown` con paragrafo "Limiti del
      breakdown" (campioni piccoli, fasce non confrontabili tra loro, etichetta
      gold come proxy del code path).
- [x] **F2.2f** *(fatto 9/6)* Raccordo costo-per-richiesta ↔ costo-di-adozione in
      chiusura di 5.6.

### Robustezza risultati (F2.3)

- [ ] **F2.3a** Ampliare la trattazione di calibrazione/clarification quando arrivano
      i dati del gold standard esteso (F3.2): oggi RQ3/RQ4 poggiano su 1 solo errore
      (debolezza ammessa in ex 7.4.2).
- [ ] **F2.3b** Valutare la misura di varianza intra-run (N esecuzioni dello stesso
      test case) già suggerita nei limiti — economica: 120 × N chiamate Flash.

---

## 6. FASE 3 — Esperimenti e dati (richiedono Davide su GCP/ambiente)

- [x] ~~**F3.1 Run eval del router con Gemini 2.5 Pro**~~ — **TAGLIATA (14/6)**:
      confronto Flash vs Pro non richiesto dai prof (chiudeva solo un limite
      auto-dichiarato). Rimossi anche F2.2d e i relativi `% TODO`/limite nel .tex.
      Numerazione F3.2–F3.6 invariata. Vedi "Decisioni prese".
- [ ] **F3.2 Gold standard esteso sugli ambigui** (per F2.3a).
      +20–25 casi categoria *Ambiguous* (oggi 7/120) costruiti su sovrapposizioni reali
      SysAid↔AllyCare e Self↔CooPolicy; rerun v1.1 → robustezza RQ3/RQ4.
- [ ] **F3.3 Query su `chat_logs`** (per F2.2c) — **ORA OPZIONALE**: token in/out medi
      per agente e modello, per sostituire il profilo assunto (4000 in / 800 out) con
      valori misurati. Non cambia S/% (dipendono da ρ e dalla distribuzione), solo la
      precisione delle cifre annue in €. (La query SQL la prepara Claude se serve.)
- [x] **F3.4 Verifica CSV SysAid** *(risolta 9/6 senza rerun)*: i CSV riportano già
      la complessità per caso; breakdown calcolato e inserito in tesi (vedi F2.2e).
- [x] ~~**F3.5 Iterazioni storiche del prompt**~~ — **TAGLIATA (14/6)**: versioni
      precedenti non recuperabili (repo anonimizzato a 1 commit, niente git history;
      repo aziendale `c30-ai-agents` non presente). Sostituita dal pivot "estratti di
      prompt engineering sugli agenti" — vedi F2.1b.
- [x] **F3.6 Prezzi listino** *(fatta 14/6)*: Gemini 2.5 Flash $0,30/$2,50, Pro
      $1,25/$10,00 (Vertex/Google, ufficiale), Claude Sonnet 4.6 $3,00/$15,00
      (Anthropic) per Mtok. In Tab. `tab:eval-prezzi`; fonti in bibliografia.
      **TODO Davide:** confermare contro la fatturazione Vertex reale (eventuali sconti
      enterprise) e il cambio EUR/USD usato (~0,92) — non cambia gli ordini di grandezza.

---

## 7. FASE 4 — Coerenza finale e consegna

- [x] **F4.1** *(fatto 14/6)* Aggiornati: abstract (aggiunti prompt engineering +
      trade-off costo–qualità), §1.4 contributo 3 (esteso a prompt engineering e
      costo–qualità, restano 3 contributi), §1.6 struttura (cap. 5 "su più piani"),
      conclusioni (catalogo PE + risultato costo–qualità ≈2,9×). Costo–qualità NON
      promosso a 4° contributo: integrato nel 3° (coerente con la figura `contributi`).
- [x] **F4.2** *(passata mirata 14/6)* Le ripetizioni cap. 3 ↔ cap. 5 ("fiducia nel
      tool", "gerarchia della verità", regole CooPolicy) sono volute: cap. 3 descrive
      l'implementazione, la nuova 5.3.4 ne mostra l'estratto con rimando a cap. 3 (non
      riscrive). Nessuna duplicazione accidentale introdotta.
- [x] **F4.3** *(fatto 14/6)* Compila pulito (exit 0, zero undefined/multiply-defined);
      tabelle 5.8/5.9 in `.lot`. **Asciugatura prosa eseguita** (~13 passaggi: principi,
      architettura, 4 cappelli caso d'uso, quota/ragionamento/retry, alternative, catena di
      sicurezza, storia/proxy di Orion) → **descrittivo da 62 a 59 pp, nessun contenuto/figura
      rimossi**. Conteggi: tot **128 pp**; Valutazione (cap. 5) = **27 pp** (target 25–30 ✓);
      descrittivo (cap. 3+4) = **59 pp**. Rapporto descr./valut. da 68/14 a **59/27**.
      **Deciso (14/6): si resta a 59 per ora.** Ultimo gap (59→55) non dalla prosa ma dal
      ridimensionamento degli screenshot oversize (7 a `height=0.85\textheight`, generano pagine
      semivuote) → ~3–4 pp recuperabili senza perdere testo. *(da valutare con Davide.)*
- [x] **F4.4** *(chiusa 9/7)* Colloquio con Bianca Raimondi avvenuto: ricevuto il
      secondo giro di feedback (appunti Davide), recepito nella **Fase 5**.

---

## 8. FASE 5 — Recepimento feedback Raimondi (colloquio 9/7/2026)

Filo conduttore del feedback: la tesi è tecnicamente solida ma deve diventare più
**didattica e autocontenuta** (lettore non esperto di LLM) e più **navigabile**
(indice asciutto). Regola trasversale: *più esempi ci sono, meglio è*.

### F5.1 — Indice: max 4–5 sottosezioni, meno elenchi

Stato attuale (dal `.toc`): cap. 1 = 6 sezioni; **cap. 2 = 11 sezioni**;
**cap. 3 = 10 sezioni (+24 sottosezioni)**; **cap. 4 = 11 sezioni**; cap. 5 = 8 sezioni.

- [ ] **F5.1a** Decidere la leva (le due si combinano):
      (i) **raggruppare le sezioni** in macro-sezioni (~4–5 per capitolo);
      (ii) **abbassare `tocdepth` a 1** in `main.tex` (le subsection spariscono
      dall'indice stampato ma restano nel testo) — quick win, non risolve però gli
      11 titoli di primo livello dei capp. 2 e 4.
- [ ] **F5.1b** Bozza di raggruppamento da validare con Davide:
      - **Cap. 2 (11 → 5):** 2.1 Transformer e LLM (ex 2.1+2.2) · 2.2 Prompt
        engineering e output strutturato (ex 2.3) · 2.3 Grounding e valutazione
        RAG (ex 2.4+2.5) · 2.4 Agenti, multi-agente, routing e incertezza
        (ex 2.6+2.7+2.8) · 2.5 Piattaforma enterprise: sicurezza, identità, cloud
        (ex 2.9+2.10+2.11). Nota: con le espansioni F5.2–F5.5 le nuove sezioni
        crescono di sottosezioni: restare comunque ≤5 per sezione.
      - **Cap. 3 (10 → 4):** 3.1 Principi e architettura d'insieme (ex 3.1+3.2) ·
        3.2 Fondazioni trasversali, incluso il portale (ex 3.3+3.4) · 3.3 I quattro
        agenti (ex 3.5–3.8 come subsection) · 3.4 Admin panel e alternative
        scartate (ex 3.9+3.10).
      - **Cap. 4 (11 → 5):** 4.1 Motivazione, panoramica, lavori correlati
        (ex 4.1+4.2+4.3) · 4.2 Routing step (ex 4.4) · 4.3 Proxy, storia, flusso
        di chat (ex 4.5+4.6+4.7) · 4.4 Frontend e admin panel (ex 4.8+4.9) ·
        4.5 Infrastruttura e decisioni architetturali (ex 4.10+4.11).
      - **Cap. 5 (8 → 5):** 5.1 RQ e metodologia (ex 5.1+5.2) · 5.2 Prompt del
        router e risultati (ex 5.3+5.4) · 5.3 Qualità agenti verticali (ex 5.5) ·
        5.4 Costo–qualità ed economia (ex 5.6+5.7) · 5.5 Discussione (ex 5.8).
- [ ] **F5.1c** Attenzione tecnica: i label di sezione esistenti sopravvivono come
      label doppi (stessa tecnica della Fase 1); `placeins` con opzione `[section]`
      cambia il posizionamento dei float quando si fondono sezioni → ricontrollare
      la resa delle figure dopo il raggruppamento.
- [ ] **F5.1d** Nel testo: ridurre gli elenchi puntati dove non necessari
      (candidati: principi guida in 3.1 — 7 voci description; stack in 3.3.1;
      elenchi del background), convertendo in prosa o accorpando le voci minori.

### F5.2 — Background: Transformer, encoder/decoder, attention (niente dato per scontato)

Oggi §2.1 liquida tutto in due paragrafi senza figura.

- [ ] **F5.2a** Espandere §2.1: spiegare a livello intuitivo self-attention
      (query/key/value, multi-head) e la differenza encoder vs decoder vs
      decoder-only, con un esempio testuale (es. quale parola "attende" a quale
      in una frase italiana).
- [ ] **F5.2b** **Figura architettura Transformer** (Draw.io, `diagrams/`):
      encoder/decoder a blocchi con attention evidenziata; in alternativa figura
      ridisegnata da Vaswani et al. con fonte citata in caption.

### F5.3 — Pretraining, fine-tuning, RLHF: figure o esempi testuali

Oggi §2.2 descrive le fasi senza esempi ("pretraining no label → mettere sample").

- [ ] **F5.3a** Un esempio testuale per fase: pretraining = corpus senza label +
      next-token su una frase campione; instruction tuning = coppia (istruzione,
      risposta) di esempio; RLHF = coppia di risposte A/B con preferenza umana.
- [ ] **F5.3b** Eventuale figura unica "pipeline a tre fasi" (pretraining →
      instruction tuning → RLHF) in Draw.io.

### F5.4 — Zero-shot / few-shot / CoT: sempre esempi, idealmente immagini

- [ ] **F5.4a** In §2.3, per ciascuna tecnica un mini-esempio completo input→output;
      per few-shot mostrare il prompt con 2 esempi in-context + il nuovo input.
      Preferire esempi del dominio della tesi (es. classificazione di un ticket),
      che preparano il lettore al prompt del router (già few-shot in 5.3.2).
- [ ] **F5.4b** Eventuale figura comparativa zero vs few-shot (Draw.io); se si usa
      un'immagine dal web, **fonte obbligatoria** in caption e bibliografia.

### F5.5 — RAGAS: specifiche tecniche + 1 esempio concreto di valutazione

Oggi §2.5 è solo un elenco di 4 metriche.

- [ ] **F5.5a** In §2.5, spiegare *come* si calcolano le metriche: faithfulness =
      decomposizione della risposta in claim + verifica di ciascun claim contro il
      contesto recuperato (score = frazione supportata); answer relevancy =
      domande rigenerate dalla risposta e similarità con la domanda originale.
- [ ] **F5.5b** **Esempio concreto di un sample**: domanda → chunk recuperati →
      risposta → claim estratti → verdetto per claim → score (es. 2/3 supportati
      → faithfulness 0,67). Ideale: un caso reale anonimizzato dalla valutazione
      di CooPolicy (coerente col vincolo "nessun numero inventato").
- [ ] **F5.5c** In §5 (eval-rag), esplicitare le **specifiche tecniche usate**:
      judge = Gemini 2.5 Pro, grounding giudicato sugli snippet da 300 caratteri,
      formule/prompt di giudizio usati dagli script di `evaluation/`, e rimandare
      all'esempio di F5.5b.

### F5.6 — Bibliografia: preferire la versione pubblicata ad arXiv

- [ ] **F5.6a** Passata su `bibliography.bib`: per ogni voce oggi "arXiv preprint",
      cercare la versione in conferenza/rivista e, se esiste, aggiornare venue e
      URL/DOI. Candidati individuati (da verificare uno a uno):
      `chang2023llmsurvey` → ACM TIST 2024; `wang2022selfconsistency` → ICLR 2023;
      `es2023ragas` → EACL 2024 (demo); `liu2023agentbench` → ICLR 2024;
      `pourreza2023dinsql` → NeurIPS 2023; `wu2023autogen` → COLM 2024;
      `guo2024multiagent` → IJCAI 2024 (survey); `wang2024moa` → ICLR 2025;
      `ong2024routellm` → ICLR 2025; `diao2023activeprompting` → ACL 2024;
      `perez2022promptinjection` → NeurIPS 2022 ML Safety Workshop.
- [ ] **F5.6b** Voci per cui arXiv basta ("se è solo su arXiv, basta quella"):
      `xu2024hallucination`, `kadavath2022knowsknows`, `willard2023outlines`,
      `jiang2024mixtral`, `chen2023frugalgpt`, `sahoo2024prompteng_survey`,
      `team2024gemini` — verificare che non siano nel frattempo apparse in venue.
- [ ] **F5.6c** Voci già `@inproceedings` con venue corretta (vaswani, brown,
      ouyang, wei, yao, lewis, guu, zheng, yu2018spider, li2023bird): dove
      possibile sostituire l'URL arXiv con il link/DOI dei proceedings
      ("meglio trovare la versione lì collegata").

### F5.7 — Aggiungere citazioni (punti scoperti censiti)

- [ ] **F5.7a** §2.1: n-grammi / RNN / LSTM oggi senza riferimenti (candidati:
      Bengio et al. 2003 per i neural LM; Hochreiter & Schmidhuber 1997 per LSTM);
      LLaMA nominato senza cite (Touvron et al. 2023).
- [ ] **F5.7b** §2.4.2: hybrid search/BM25, query expansion e HyDE oggi senza
      riferimenti (candidati: Robertson & Zaragoza 2009 per BM25; Gao et al.,
      ACL 2023 per HyDE).
- [ ] **F5.7c** Le nuove parti didattiche F5.2–F5.5 portano citazioni proprie;
      passata finale per altri concetti citati "a memoria" nel testo.

### F5.8 — "Spremere" la parte sperimentale

Appunto sintetico del colloquio; lettura più coerente con il feedback di giugno
(la valutazione è il capitolo scientificamente più importante): **estrarre ancora
più valore dal materiale sperimentale esistente**, in linea con "più esempi è meglio".

- [ ] **F5.8a** Mostrare 1–2 sample end-to-end della valutazione del routing:
      test case reale → output strutturato del router (agent/complexity/confidence/
      reasoning) → verdetto (dati già nei CSV `results/` e in `orion_eval_results`).
- [ ] **F5.8b** Mostrare 1 sample Text-to-SQL: domanda → query generata vs query
      gold → confronto result-set (dai gold standard di `evaluation/`).
- [ ] **F5.8c** L'esempio RAGAS di F5.5b copre il piano RAG.
- [ ] **F5.8d** Rivalutare le opzionali rimaste in questa chiave: F2.3a/F3.2
      (gold esteso ambigui), F2.3b (varianza intra-run), F3.3 (token medi reali).
- [ ] **F5.8e** Se al prossimo contatto emerge che "spremere" significava invece
      *comprimere*, ripiegare su: asciugare 5.2 (metodologia) e ridimensionare gli
      screenshot dell'admin panel — da chiarire con Raimondi (Teams).

---

## 9. Vincoli di scrittura (sempre validi)

1. **Nessun numero inventato**: ogni dato nuovo in tesi deve provenire da una run reale
   o da una fonte verificabile. Dove il dato manca → commento `% TODO F3.x` nel .tex.
2. Estratti di prompt/codice: dal repo **anonimizzato** `unibo-thesis-src`.
3. Stile: coerente con la prosa esistente (italiano, corsivi per i tecnicismi inglesi,
   citazioni biblatex `\cite{}`).
4. Il PDF deve restare compilabile e presentabile a ogni fine sessione: le sezioni
   non ancora scritte vivono come scalette in commento LaTeX, non come pagine vuote.
5. **(9/7)** Figure: preferire diagrammi propri (Draw.io, sorgenti in `diagrams/`);
   immagini prese dal web solo con fonte citata in caption e in bibliografia.
6. **(9/7)** Ogni concetto tecnico introdotto nel background deve avere almeno un
   esempio concreto o una figura: non dare mai per scontato che il lettore lo conosca.
