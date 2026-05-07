La mia tesi, impostata nel progetto Latex in questa cartella, in sostanza è questo:
Ho creato per la mia cooperativa, coop alleanza, un sistema di agenti (assistenti) LLM: sono quelli presenti nella folder bitbucket/c30-ai-agents.

Come si può vedere dal codice presente nella folder, ho fatto tutto: creazione infrastruttura su GCP, configurazione accessi con Entra ID, etc, tutto quanto insomma.
Come parte "centrale" della tesi, prenderò la crezione di un agente che possa anche "orchestrare" gli altri agenti
La descrizione di come farlo è presente dentro 
/guides/ORION_ROADMAP.md, lì trovi anche il dettaglio di quali sono gli agenti da usare etc, Orion è ancora da creare e lo faremo prossimamente.

La tesi prende in esame un sottogruppo di agenti, unitamente alla creazione sia dell'orchestratore a nome "Orion" sia dell'impianto di testing delle performance dello stesso.

Voglio iniziare a scrivere la tesi, da cui il progetto Latex di questa folder;

Devo farlo seguento queste linee guida, fornite dal professore, che riporto qui:

"
Thesis Writing Tips
Questo documento offre linee guida e consigli pratici raccolte durante la supervisione di tesi e che si spera che possano aiutare gli studenti ad affrontare il processo di scrittura.
Questi suggerimenti si concentrano sugli aspetti pratici della scrittura di una tesi piuttosto che sugli elementi “strategici” come la selezione di un supervisore, la definizione di un argomento, la definizione di tempistiche per rispettare le scadenze di laurea (particolarmente quando i risultati potrebbero essere incerti, come spesso accade in ricerca) o nel determinare potenziali risultati, incluso il voto finale.
Questi sono aspetti unici e personali del lavoro di tesi che si estendono oltre il processo di scrittura stesso. Quando si cerca orientamento su queste questioni, raccomando di discuterne apertamente sia con i propri colleghi (che potrebbero condividere preoccupazioni simili e/o offrire consigli preziosi) sia con i membri del corpo docente (ricercatori e professori) che sono lì per aiutare gli studenti a identificare i loro interessi e tracciare un percorso per perseguirli.

Scrivere una Tesi
Scrivere una tesi (per una laurea triennale o magistrale) è un’impresa significativa che dimostra la capacità di uno studente di condurre ricerca indipendente, fornendo al contempo un’opportunità di lavorare su e contribuire allo stato dell’arte del proprio campo.
Gli studenti del Dipartimento di Informatica - Scienza e Ingegneria dell’Università di Bologna devono usare i file sorgente e le linee guida di formattazione disponibili alla pagina dedicata.


https://corsi.unibo.it/magistrale/informatica/tesi-in-latex

>>> nota mia: tutto quanto presente alla pagina sopra è stato riportato nella folder /guide-unibo-scrittura-tesi


Struttura della Tesi
Le tesi hanno generalmente quattro parti, spesso ciascuna corrispondente a uno (o più) capitolo/i:

Introduzione: un capitolo conciso che stabilisce il contesto della tesi, identifica il/i problema/i affrontato/i e delinea come il lavoro affronta queste questioni — evidenziando efficacemente i contributi. Questo capitolo può essere difficile da strutturare e potrebbe richiedere una guida specifica, discussa alla fine di questo documento.

Background: questo capitolo fornisce ai lettori la conoscenza essenziale necessaria per comprendere il contesto della tesi, i problemi affrontati e le tecniche/strumenti su cui la tesi è costruita — essenzialmente, tutto ciò che è richiesto per afferrare i contributi. Per completezza, si potrebbe includere una revisione della letteratura che esamina i lavori esistenti che hanno tentato di risolvere problemi simili, i loro approcci e la loro efficacia. Pur non essendo obbligatoria, quest’ultima parte aiuta a posizionare i contributi all’interno del campo.

La Polpa: (non chiamate il/i capitolo/i in questo modo 😀): questi capitoli presentano i contributi in profondità, spiegando la metodologia della soluzione e fornendo i dettagli tecnici necessari sia per validare l’approccio che per convincere i lettori della solidità dei risultati.

Conclusione: un altro capitolo breve, che conclude la tesi. Riassume principalmente i contributi nel contesto più ampio del loro campo (come stabilito nell’introduzione), potenzialmente evidenziando dettagli tecnici che distinguono il lavoro di tesi dalla ricerca esistente. Questo capitolo è anche dove si discutono possibili estensioni future, sia perché i contributi affrontano solo parzialmente il/i problema/i generale/i sia perché estendere il lavoro di tesi potrebbe aiutare a risolvere altri problemi correlati.

Scrivere i Capitoli della Tesi (!IMPORTANTE!)
Mentre i lettori tipicamente procedono attraverso una tesi dall’inizio alla fine, questo non significa che si debba scriverla in quell’ordine. In effetti, saltare direttamente all’introduzione può essere difficile perché il resto delle idee per gli altri capitoli stanno ancora turbinando nella propria testa piuttosto che essere organizzate ordinatamente in capitoli.

Per questa ragione, generalmente raccomando di iniziare il processo di scrittura con la polpa e di farlo insieme allo sviluppo del lavoro di tesi come appunti strutturati — non come un diario quotidiano (“Giorno X: Oggi ho implementato…”), ma come note tecniche organizzate che, una volta completato il lavoro, catturano tutti gli aspetti chiave del contributo.

Questo approccio assicura che si abbiano note complete per descrivere efficacemente il proprio lavoro e aiuta a evitare situazioni in cui si deve cercare di ricordare dettagli di lavori completati mesi prima della scrittura — nel migliore dei casi, questo potrebbe significare sprecare tempo rivedendo il codice per ricordare certe decisioni di design; nel peggiore dei casi, potrebbe significare fallire nel riportare o indovinare erroneamente dettagli sugli esperimenti che non possono essere replicati prima della scadenza della tesi.

Mentre si raffinano questi capitoli della polpa, suggerisco di elencare nel capitolo background i concetti tecnici che appaiono e necessitano di spiegazione per il pubblico non esperto (vedi sotto, sull’esercizio della “macchina del tempo”), poiché questa raccolta categorizzata forma il contenuto del capitolo sulla conoscenza di background. Una volta stabilita la struttura della sezione background, raccogliere le informazioni necessarie — presentate in modo conciso per dare ai lettori solo ciò di cui hanno essenzialmente bisogno per comprendere il lavoro di tesi — diventa relativamente semplice.

Con i capitoli della “polpa” e del background pronti, diventa molto più facile scrivere la conclusione, seguita dall’introduzione. Raccomando di affrontare prima la conclusione principalmente perché permette più dettagli tecnici dell’introduzione. Inoltre, aver completato tutti gli altri capitoli rende la scrittura dell’introduzione significativamente più facile poiché la struttura e il contenuto della tesi sono già stabiliti e si può fare riferimento a quest’ultimo per guidare la scrittura dei contenuti dell’introduzione.

Strutturare l’Introduzione
Ho notato che una delle parti più difficili dello scrivere una tesi è formulare un’introduzione convincente. Dopo tutto, i Romani sapevano già che “Dimidium facti, qui coepit, habet” o “Chi ben comincia è a metà dell’opera”.

Infatti, se si scrive un’introduzione efficace, si stanno dando al lettore tutte le informazioni necessarie per convincerlo degli aspetti e della validità del lavoro di tesi. Tuttavia, raggiungere quel punto è tutt’altro che facile e richiede una strutturazione efficiente per guidare il lettore dall’essere un completo estraneo al lavoro a poter apprezzare i suoi contributi.

Per questa ragione, mentre non suggerisco di seguire un modello specifico per gli altri capitoli, includo sotto un layout di base per l’introduzione che ho visto funzionare efficacemente per la maggior parte degli studenti.

L’introduzione di solito inizia situando il lavoro di tesi nel campo più ampio dell'informatica, restringendo gradualmente il focus verso il/i problema/i specifico/i che portano alla/e domanda/e di ricerca che motivano il lavoro. Questo tipo di presentazioni tendono a formare una sorta di “imbuto” che guida un lettore non esperto (ma con un background di informatica a livello di laurea triennale/magistrale) dal contesto ampio ai problemi e contributi della tesi.

Come esercizio, di solito consiglio agli studenti di considerare il compito come se dovessero spiegare ai loro colleghi il loro lavoro di tesi o (in modo più introspettivo e fantascientifico) come se avessero una macchina del tempo, tornassero indietro nel tempo, e dovessero spiegare i loro contributi di tesi a se stessi prima di iniziare a lavorarci, cioè, come completi novizi. Il loro compito è introdurre la loro tesi, mirando a presentare il lavoro in modo chiaro e accessibile che un non esperto possa comprendere, riflettendo sulla conoscenza e prospettiva che il loro interlocutore ha, prima di addentrarsi nei dettagli del lavoro (ponderando quali sono quelli più e meno importanti, lasciando questi ultimi ai capitoli della “polpa”1), e capendo come spiegare l’importanza e il contesto del lavoro, considerando la conoscenza e prospettiva del loro interlocutore. Nel farlo, è utile concentrarsi sull’offrire una narrativa che colmi il divario tra la comprensione più generica e superficiale e le intuizioni acquisite dopo aver finito il lavoro.

È usuale concludere questo capitolo con una breve presentazione della struttura dei capitoli rimanenti, che aiuta i lettori a navigare il documento e comprendere come i suoi contributi si compongono.

In particolare, è importante descrivere i contributi senza addentrarsi troppo nei dettagli di cui il lettore ha poca o nessuna conoscenza e avrebbe difficoltà a posizionare nella prospettiva generale che sta costruendo della tesi, cioè, spiegare le tecniche/metodologie/strumenti/framework chiave impiegati/presentati ma tralasciare dettagli che sono troppo specifici (ad esempio, le configurazioni specifiche usate per eseguire gli esperimenti) o non peculiari/nuovi rispetto al lavoro di tesi (ad esempio, l’uso di una tecnica standard e/o software specifico per implementare/eseguire gli esperimenti). ↩ ↩2
"

FINE PARTE DEL PROF

Detto questo, la mia "polpa" vorrei che si dividesse innanzitutto in 2 macro parti:
una per i singoli agenti
una per l'orchestrazione

Ogni singolo agente avrà architettura e implementazione
L'orchestratore Orion avrà architettura, implementazione, e valutazione.

Quindi sarà un totale di 2x4 per gli agenti, cioè 8 parti, +3 per l'orchestratore, totale 11 parti di "polpa"

Quindi per favore, con tutta la calma del mondo, leggi tutti i documenti che ti ho citato e per favore imbastisci:
- il progetto Latex con già indicato dove andare a scrivere cosa
- La quantità di grafici che credi sia giusto inserire e dove

Infine, in /plans/ORION_LETTERATURA.md trovi la letteratura che vorrei usare, specificamente per la parte di orchestrazione: tutta l'altra letteratura che vorrei usare invece è dentro github/unibo/prova-finale/bibliografia.md
ti chiedo anche di fare quindi un nuovo elenco "letteratura complessiva" che sia da usare nella bibliografia del

Ovviamente fammi sapere se ti pare tutto corretto o se hai proposte diverse, e se ti sembra fattibile.
leggi tutto con calma