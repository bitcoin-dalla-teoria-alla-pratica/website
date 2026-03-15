---
title: "Bitcoin In Action: SegWit, Bitcoin Script & Smart Contracts"
date: 2020-01-01T12:00:00+01:00
draft: false
price: "41,90€"
weight: 1
tipo: "Libro"
cover: "img/libro-bitcoin-segwit-script-smart-contracts.webp"
---

Bitcoin In Action accompagna il lettore attraverso l’aggiornamento di Bitcoin SegWit e l’utilizzo del linguaggio di programmazione Bitcoin Script.

Alzare il cofano, controllare ogni singolo bit, accendere la macchina e guardare se e come funzionacco che cosa farà il lettore, grazie alla teoria sarà in grado di replicare ogni singolo esempio con il supporto di file appositamente preparati dagli autori, iniziando così a prendere conoscenza del mondo programmable money, di cui tutti parlano ma che pochi hanno le capacità di spiegarlo.

Il libro è il sequel di Bitcoin – Dalla teoria alla pratica, indispensabile per seguire Bitcoin In Actionogliamo rimanere ancora a guardare?

Per seguire questo nuovo testo è indispensabile il primo libro, Bitcoin dalla teoria alla pratica, proprio perché non saranno spiegati concetti già affrontati precedentemente —come ad esempio il mining— quindi la proof of work, il problema dei generai bizantini o la blockchain, quindi hard fork e soft fork, ma abbiamo deciso di andare giù nella buca del Bianconiglio. 🐰

L’obiettivo del libro è quello di spiegare, sempre utilizzando la pratica, gli aggiornamenti più corposi del protocollo Bitcoin, analizzando prima le problematichenfatti il primo capitolo è dedicato alla transaction malleability, la quale viene risolta con l’aggiornamento SegWit.

Una sezione completamente dedicata ai timelocks, dove è necessario prendere confidenza con Bitcoin Script e lo stackrriveremo infine a creare degli smart contracts in grado di sbloccare dei fondi solo se determinate condizioni sono verificate, utilizzando delle operation code come OP_IF, OP_ELSE o per meglio dire le operation code del flow control.

Un libro molto corposo che porta due novità fondamentali rispetto al precedente: le mappe mentali e la pratica.

## Capitoli

1. **I bit del mestiere: Prepariamo il nostro banco di lavoro**: Prima di sporcarci le mani con transazioni reali, dobbiamo configurare gli strumenti giusti. In questo capitolo prepariamo l'ambiente di lavoro: librerie, terminale, e tutto ciò che serve per seguire gli esempi pratici del corso senza inciampare nei dettagli tecnici.

2. **Transaction malleability**: Una transazione Bitcoin firmata può essere modificata da terzi prima di essere confermata, senza invalidare la firma. In questo capitolo scopriamo come funziona questo bug storico, perché ha bloccato lo sviluppo di Lightning Network per anni e come SegWit lo ha risolto definitivamente.

3. **P2MS – Pay to Multi Signature**: Il multisig nella sua forma più primitiva. In questo capitolo analizziamo il primo script multifirma di Bitcoin, come funziona il meccanismo M-di-N, i suoi limiti pratici — dimensione dello script, costi elevati e mancanza di privacy — e perché è stato rapidamente superato da soluzioni più eleganti.

4. **P2SH – Pay to Script Hash**: Con P2SH l'onere di fornire lo script di spesa passa dal mittente al destinatario. In questo capitolo vediamo come funziona questo cambiamento architetturale, come l'hash dello script diventa l'indirizzo di ricezione e perché P2SH ha reso il multisig praticabile per il mondo reale.

5. **P2SH Multisig – Pay To Script Hash**: Il multisig moderno, quello che trovi nei cold wallet e nei servizi di custodia. In questo capitolo costruiamo un indirizzo P2SH 2-di-3 da zero, analizziamo il redeem script, vediamo come viene risolto lo stack durante la verifica e perché questo standard è ancora oggi ampiamente usato.

6. **Firmare una transazione legacy**: In questo capitolo firmiamo una transazione legacy passo per passo: selezione degli UTXO, costruzione degli input e output, calcolo del sighash, firma ECDSA e serializzazione finale. Un percorso completo che ti permette di capire esattamente cosa succede dietro le quinte di ogni wallet.

7. **Firmare una transazione P2SH Multisig**: Firmare una transazione multisig richiede la coordinazione di più chiavi private. In questo capitolo vediamo come raccogliere le firme, come assemblarle nello scriptSig nel corretto ordine, come gestire il bug di OP_CHECKMULTISIG con OP_0 e come trasmettere la transazione alla rete.

8. **SegWit – Segregated Witness**: SegWit è l'aggiornamento più importante nella storia di Bitcoin dopo il genesis block. In questo capitolo analizziamo perché è stato necessario, cosa significa separare il witness dagli input, come cambia la struttura della transazione, il nuovo calcolo del peso in vbyte e tutti i vantaggi che ha portato alla rete.

9. **Firmare una transazione SegWit**: Il processo di firma di una transazione SegWit è diverso da quello legacy: il sighash include il valore dell'input, risolvendo la transaction malleability. In questo capitolo costruiamo e firmiamo una transazione P2WPKH da zero, analizzando il nuovo formato di serializzazione witness campo per campo.

10. **Timelocks: Presto che è tardi!**: I timelocks permettono di bloccare i bitcoin fino a un certo momento nel tempo o a una certa altezza di blocco. In questo capitolo analizziamo i quattro tipi di timelock — nLockTime, nSequence, CLTV e CSV — le loro differenze, come vengono verificati dal protocollo e i casi d'uso reali come i payment channel di Lightning Network.

11. **Advanced Script: Gli smart contracts di Bitcoin**: Bitcoin Script non è solo per pagamenti semplici. In questo capitolo esploriamo gli script avanzati: HTLC, script condizionali con OP_IF, contratti con timelock combinati e le basi degli smart contract su Bitcoin. Scopriamo fino a dove si può spingere il linguaggio stack-based più robusto e battle-tested della storia.


*101110, 01, 0x.*
*01000111 01110010 01100001 01111010 01101001 01100101*

<br>
<a href="https://www.amazon.it/Bitcoin-Action-SegWit-Script-Contracts/dp/B08NL5ZV6X" target="_blank" class="button">Acquista su Amazon</a>
