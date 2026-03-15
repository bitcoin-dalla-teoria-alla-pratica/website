---
title: "Bitcoin dalla teoria alla pratica"
date: 2019-01-01T12:00:00+01:00
draft: false
price: "36,63€"
weight: 3
tipo: "Libro"
cover: "img/bitcoin-dalla-teoria-alla-pratica.webp"
---

Siamo sempre stati convinti che per capire veramente il potenziale di una qualsiasi tecnologia dobbiamo provarla con mano, vedendo con i nostri occhi i risultati che possiamo ottenereuesto libro analizza dettagliatamente il protocollo Bitcoin, mettendo in pratica la teoria con esempi concreti e reali.

Non è necessario essere un programmatore per capire che è arrivato il momento di unirsi alla rivoluzione tecnologica.

*The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.*

Bitcoinenaro dei nerds? Oro digitale?
Forse, sicuramente rivoluzione sociale.

Questo il pensiero dei due autori dopo aver messo in pratica, con esempi reali e concreti, il protocollo Bitcoin.
Il loro mantra è: “Per comprendere profondamente una qualsiasi tecnologia dobbiamo toccarla con mano, vedendo con i nostri occhi i risultati che possiamo ottenere”.
Non si sono accontentati di sapere superficialmente che cosa è una transazione e come viene identificata nella blockchain, oppure perché viene utilizzato il merkle tree, o ancora come sono gestite le chiavi private nel wallet deterministicoanno voluto ottenere i risultati passo passo spiegandone tutte le sfumature.

Allacciate le cinture, state per intraprendere un viaggio nel cypherspazio, al vostro ritorno sarete consapevoli, vi renderete conto del perché Bitcoin ha le carte in regola per spostare gli equilibri.

Non è necessario essere un minatore per fare mining come non è necessario essere programmatore per capire che non c’è più tempo per ignorarlo.

Il treno sta fischiando: investite l’asset più prezioso a vostra disposizione, il tempo, e prendete posto in carrozza per raggiungere il futuro decentralizzato dove la globalizzazione ci sta portando.

## Capitoli

1. **Storia e termini base**: In questo capitolo parleremo della storia di Bitcoin e dei termini base. Scopriremo che cos'è un movimento cypherpunk, che cos'è un sistema centralizzato e una rete P2P. Per capire la rivoluzione dobbiamo partire dalle basi e dare merito a tutte le persone che hanno reso questa tecnologia il futuro.

2. **Crittografia**: La crittografia proviene dal greco e significa "scrittura nascosta". Può essere usata per cifrare dei messaggi, quindi nasconderli, oppure per verificare che un messaggio non sia stato manomesso e che sia stato inviato dal mittente voluto.

3. **Blockchain**: Come possiamo definire la blockchain? Le definizioni più gettonate sono "un libro mastro distribuito", "un database immutabile", o ancora "un raccoglitore di transazioni ordinate temporalmente". Queste definizioni hanno tutte qualcosa di vero: la blockchain è immutabile, raccoglie transazioni, è distribuita e ogni blocco è marcato temporalmente.

4. **Merkle tree**: Il Merkle tree è una struttura dati ad albero in cui ogni nodo foglia contiene l'hash di un dato, e ogni nodo interno contiene l'hash dei suoi figli. In Bitcoin viene usato per organizzare le transazioni all'interno di un blocco in modo efficiente e verificabile.

5. **Bloom filters**: I Bloom filters sono una struttura dati probabilistica che permette di verificare se un elemento appartiene a un insieme in modo rapido e con poco consumo di memoria. In Bitcoin vengono usati dai nodi SPV per filtrare le transazioni rilevanti senza rivelare esattamente quale informazione si sta cercando.

6. **Big endian – Little endian**: Quando lavoriamo con dati binari dobbiamo sapere in che ordine vengono scritti i byte. Big endian scrive il byte più significativo per primo, Little endian al contrario. Bitcoin usa entrambe le convenzioni a seconda del contesto, ed è fondamentale saperle distinguere per interpretare correttamente i dati on-chain.

7. **Merkle block message**: Il Merkle block message è il messaggio che un full node invia a un nodo SPV in risposta a una richiesta filtrata. Contiene il block header e il Merkle path necessario per verificare che una transazione sia inclusa nel blocco senza scaricare l'intera blockchain.

8. **Merkle block message a senso unico**: Approfondiamo il Merkle block message analizzando come il percorso di verifica funziona in una sola direzione, dal nodo foglia fino alla radice. Questo meccanismo garantisce l'integrità della transazione con un numero minimo di hash da verificare.

9. **Tipi di blockchain**: Non tutte le blockchain sono uguali. In questo capitolo distinguiamo tra blockchain pubbliche, private e consortili, analizzando le differenze architetturali, i casi d'uso e perché Bitcoin rappresenta il modello di blockchain pubblica per eccellenza.

10. **Blockchain fork**: Un fork della blockchain avviene quando due miner trovano un blocco valido contemporaneamente, creando due rami concorrenti. Scopriamo come la rete risolve questa situazione, perché accade frequentemente e cosa succede al blocco orfano.

11. **I miners**: I miner sono i nodi della rete che si occupano di creare nuovi blocchi raccogliendo le transazioni dalla mempool e risolvendo il Proof of Work. In questo capitolo analizziamo il loro ruolo, i loro incentivi economici e come interagiscono con il resto della rete.

12. **Proof of Work – Primi passi**: La Proof of Work è il meccanismo con cui un miner dimostra di aver speso energia computazionale per trovare un hash valido. In questo capitolo introduciamo il concetto, spieghiamo il ruolo del nonce e perché questo processo è fondamentale per la sicurezza di Bitcoin.

13. **Calcolare la difficoltà**: La difficoltà della rete Bitcoin si aggiusta ogni 2016 blocchi per mantenere un tempo medio di mining di 10 minuti. In questo capitolo vediamo come viene calcolata, quale formula usa il protocollo e perché questo meccanismo di aggiustamento è essenziale per la stabilità della rete.

14. **Difficoltà di un blocco passato**: Analizziamo come leggere e interpretare la difficoltà di un blocco già minato, decodificando il campo `bits` del block header e convertendolo nel valore target effettivo. Un esercizio pratico per capire come funziona il protocollo nel mondo reale.

15. **Bizantini all'attacco**: Il problema dei generali bizantini descrive la sfida di raggiungere il consenso in un sistema distribuito dove alcuni partecipanti possono essere disonesti. Scopriamo come Bitcoin ha risolto questo problema millenario attraverso il Proof of Work e la regola della catena più lunga.

16. **Hard fork – Soft fork**: Un hard fork introduce modifiche al protocollo incompatibili con le versioni precedenti, mentre un soft fork è retrocompatibile. In questo capitolo analizziamo le differenze, gli esempi storici più importanti e le implicazioni politiche e tecniche di ciascun tipo di aggiornamento.

17. **Cripto gratis**: Quando avviene un hard fork, i possessori di Bitcoin ricevono spesso una quantità equivalente della nuova criptovaluta. In questo capitolo analizziamo come funziona questo meccanismo, cosa significa per la sicurezza della rete e come gestirlo praticamente.

18. **Wallet – Introduzione**: Il wallet Bitcoin non contiene bitcoin, ma le chiavi per spenderli. In questo capitolo introduciamo i concetti fondamentali: chiave privata, chiave pubblica e indirizzo, spiegando la relazione tra loro e perché la custodia delle chiavi è la vera responsabilità dell'utente.

19. **Chiave privata**: La chiave privata è un numero casuale a 256 bit che rappresenta la proprietà dei bitcoin. In questo capitolo vediamo come viene generata, quali formati esistono, come viene protetta e perché la sua sicurezza è l'elemento più critico di tutto il sistema.

20. **Chiave pubblica**: La chiave pubblica viene derivata dalla chiave privata tramite la crittografia a curva ellittica. In questo capitolo analizziamo la matematica alla base della derivazione, le proprietà della curva secp256k1 usata da Bitcoin e perché è impossibile risalire alla chiave privata partendo dalla chiave pubblica.

21. **Bitcoin address**: L'indirizzo Bitcoin è una rappresentazione compatta della chiave pubblica, ottenuta tramite una serie di operazioni di hashing. In questo capitolo vediamo come viene costruito, perché si usa l'hash invece della chiave pubblica diretta e come si verifica la sua validità tramite il checksum.

22. **I formati**: Bitcoin utilizza diversi formati per rappresentare chiavi e indirizzi: WIF, compressed, uncompressed, Base58Check e Bech32. In questo capitolo analizziamo ciascun formato, quando viene usato e come riconoscerli a colpo d'occhio.

23. **Wallet deterministici e non**: Un wallet non deterministico genera chiavi casuali indipendenti tra loro, mentre un wallet deterministico le deriva tutte da un unico seed. In questo capitolo confrontiamo i due approcci, i vantaggi del backup con una sola frase e perché i wallet HD sono diventati lo standard.

24. **Dall'entropia al seed phrase**: La seed phrase è una sequenza di parole che rappresenta l'entropia iniziale del wallet. In questo capitolo vediamo come viene generata secondo lo standard BIP39, come l'entropia viene convertita in parole dalla wordlist e perché 12 o 24 parole sono sufficienti per proteggere tutti i tuoi bitcoin.

25. **Dal seed phrase al seed**: La seed phrase non è direttamente il seed usato per derivare le chiavi. In questo capitolo analizziamo il processo di derivazione tramite la funzione PBKDF2, il ruolo della passphrase opzionale e come si ottiene il seed a 512 bit che è il punto di partenza dell'albero HD.

26. **Creare le chiavi HD wallet**: Un HD wallet genera una struttura ad albero di chiavi partendo dal master seed. In questo capitolo vediamo come viene creata la master private key e il master chain code, i due elementi fondamentali da cui dipende l'intera gerarchia del wallet.

27. **Child key derivation**: La Child Key Derivation (CKD) è il processo con cui si derivano chiavi figlio da una chiave genitore. In questo capitolo analizziamo l'algoritmo HMAC-SHA512 alla base del processo, il ruolo del chain code e come ogni livello dell'albero viene generato in modo deterministico.

28. **Purpose**: Il campo Purpose è il primo livello della gerarchia BIP44 e indica lo standard di derivazione usato dal wallet. In questo capitolo vediamo perché è stato introdotto, come distingue tra BIP44, BIP49 e BIP84, e come garantisce l'interoperabilità tra wallet diversi.

29. **CKD hardened**: La derivazione hardened crea chiavi figlio che non possono essere derivate conoscendo solo la chiave pubblica estesa del genitore. In questo capitolo vediamo quando usarla, qual è la differenza matematica rispetto alla derivazione normale e perché i primi livelli della gerarchia HD usano sempre la derivazione hardened.

30. **CKD non hardened**: La derivazione non hardened permette di generare chiavi figlio pubbliche partendo dalla chiave pubblica estesa del genitore, senza mai esporre la chiave privata. In questo capitolo vediamo i casi d'uso pratici, come funziona nei wallet watch-only e i rischi di sicurezza da conoscere.

31. **Extended public keys**: Una extended public key (xpub) contiene la chiave pubblica e il chain code, e permette di derivare tutte le chiavi pubbliche figlio di un ramo senza conoscere la chiave privata. In questo capitolo vediamo come viene codificata, come usarla per generare indirizzi di ricezione e i rischi per la privacy che comporta.

32. **Extended private keys**: Una extended private key (xprv) contiene la chiave privata e il chain code, e permette di derivare l'intero albero di chiavi di un wallet. In questo capitolo vediamo la sua struttura, come viene codificata in Base58Check e perché va protetta con la stessa cura del seed.

33. **Introduzione alle transazioni**: Una transazione Bitcoin è il messaggio con cui il proprietario di bitcoin autorizza il loro trasferimento. In questo capitolo introduciamo la struttura generale, il concetto di input e output, e come una transazione viene propagata, verificata e inclusa in un blocco.

34. **UTXO**: L'Unspent Transaction Output è il modello contabile di Bitcoin. In questo capitolo vediamo come funziona il set UTXO, perché Bitcoin non usa saldi ma output non spesi, come il database Chainstate mantiene traccia di tutti gli UTXO esistenti e perché questo modello è fondamentale per la verifica delle transazioni.

35. **Struttura della transazione**: Una transazione Bitcoin è composta da version, inputs, outputs e locktime. In questo capitolo analizziamo ogni campo nel dettaglio, vediamo come viene serializzata in formato esadecimale e come interpretare una transazione reale estratta dalla blockchain.

36. **Fees**: Le fee sono la differenza tra il totale degli input e il totale degli output di una transazione. In questo capitolo vediamo come vengono calcolate, perché esistono, come influenzano la priorità di inclusione in un blocco e come stimare la fee ottimale in base alle condizioni della mempool.

37. **Input**: Un input è il riferimento a un UTXO precedente che si vuole spendere. In questo capitolo analizziamo i campi che compongono un input: txid, vout, scriptSig e sequence, e vediamo come il nodo verifica che chi firma abbia effettivamente il diritto di spendere quell'output.

38. **Serialized input transaction**: In questo capitolo vediamo come un input viene serializzato in byte, analizzando il formato esadecimale campo per campo. Un esercizio pratico fondamentale per capire come funziona realmente il protocollo Bitcoin a livello di dati.

39. **Output**: Un output definisce la destinazione dei bitcoin e le condizioni necessarie per spenderli in futuro tramite lo scriptPubKey. In questo capitolo analizziamo i campi che compongono un output, i diversi tipi di locking script e come un output diventa un UTXO disponibile nel set globale.

40. **Output in action**: Mettiamo in pratica quanto appreso sugli output analizzando transazioni reali sulla blockchain. In questo capitolo vediamo come decodificare il valore in satoshi, interpretare lo scriptPubKey e identificare il tipo di output direttamente dai dati esadecimali.

41. **Quanti locking script esistono?**: Bitcoin supporta diversi tipi di locking script: P2PK, P2PKH, P2SH, P2WPKH, P2WSH e P2TR. In questo capitolo facciamo una panoramica di tutti i formati esistenti, le loro caratteristiche, quando sono stati introdotti e quali sono oggi i più usati.

42. **Script**: Bitcoin Script è un linguaggio stack-based non Turing-completo usato per definire le condizioni di spesa degli output. In questo capitolo introduciamo il funzionamento dello stack, i principali opcode e come scriptPubKey e scriptSig interagiscono durante la verifica di una transazione.

43. **Verificare lo script**: In questo capitolo vediamo passo per passo come un nodo esegue la verifica di uno script, simulando l'esecuzione dello stack con esempi concreti. Capire questo processo è fondamentale per comprendere come Bitcoin garantisce che solo il legittimo proprietario possa spendere un UTXO.

44. **Coinbase**: La transazione coinbase è la prima transazione di ogni blocco e non ha input reali. In questo capitolo vediamo come viene costruita dal miner, come include il block reward e le fee delle transazioni, il campo coinbase data e perché i bitcoin della coinbase non sono spendibili per 100 blocchi.

45. **Coinbase vs UTXO**: In questo capitolo confrontiamo la transazione coinbase con una transazione normale, evidenziando le differenze strutturali e le regole speciali che la governano. Un'analisi che chiarisce come nascono i nuovi bitcoin e come entrano nel set UTXO.

46. **Creare la transazione**: In questo capitolo vediamo come costruire una transazione Bitcoin da zero, selezionando gli UTXO da spendere, definendo gli output, calcolando le fee e serializzando il tutto nel formato corretto pronto per essere firmato e trasmesso alla rete.

47. **Firmare la transazione**: La firma di una transazione avviene tramite l'algoritmo ECDSA applicato alla chiave privata del mittente. In questo capitolo vediamo come viene calcolato il sighash, come viene prodotta la firma DER, come viene inserita nello scriptSig e come un nodo la verifica usando la chiave pubblica.

48. **END.**: Sei arrivato alla fine del corso. Hai percorso l'intero stack tecnologico di Bitcoin, dalla storia alle firme digitali. Ora hai gli strumenti per leggere la blockchain, costruire transazioni e capire perché Bitcoin funziona esattamente come funziona. La rivoluzione è cominciata. 👊

<br>
<a href="https://www.amazon.it/Bitcoin-Dalla-teoria-alla-pratica/dp/B07SNNNL2P" target="_blank" class="button">Acquista su Amazon</a>
