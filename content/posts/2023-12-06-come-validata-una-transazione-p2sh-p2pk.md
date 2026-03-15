---
title: "Come è validata una transazione P2SH-P2PK"
date: 2023-12-06T10:00:00+01:00
slug: "come-validata-una-transazione-p2sh-p2pk"
draft: false
author: "Alessio Barnini"
description: "Ciao,"
cover: "https://cdn-images-1.medium.com/max/1200/0*__hAs5XcMI8LHyl-.jpeg"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

Ciao,

nell’articolo precedente abbiamo analizzato come avviene una transazione utilizzando il P2SH-P2PK.

![](https://cdn-images-1.medium.com/max/1200/1*dJZptxYmKPy_9PZO2Ufm-A.jpeg)

In questo articolo vogliamo andare ad analizzare come questa viene validata.

Come negli articoli precedenti, andremo ad analizzare lo stack grazie alla libreria [btcdeb](https://github.com/bitcoin-core/btcdeb) e utilizzeremo il codice del libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/). che potete trovare al nostro indirizzo [GitHub](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book).

La logica che abbiamo deciso di utilizzare nel libro per analizzare lo stack è quello di passare allo script un parametro **DEBUG=1** in modo tale da invocare la libreria btcdeb.

Ma analizziamola utilizzando la pratica

> In Action!

Come per gli esempi precedenti, partiremo utilizzando una blockchain con 0 blocchi, successivamente ne mineremo 101 per prendere il **reward** che sposteremo verso un nuovo indirizzo.

Se hai bisogno di analizzare step by step questi passaggi, ti consiglio ti leggere l’articolo precedente.

Il nostro compito è semplicemente avviare il file sh, con il comando.

```bash
$./main.sh debug=1
```

Il codice lo potete trovare nel nostro repository e nel nostro libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/).

Lo script si fermerà esattamente prima dell’invio della transazione in broadcast, cosi da poter verificare la sua validità.

Come per il P2PK e il P2PKH, lo stack parte vuoto, e i primi elementi che sono pushati (inseriti) sono quelli che troviamo nello scriptSig.

Che cosa troviamo nello scriptSig?

Se vi ricordate l’articolo precedente, nello scriptSig ci troviamo

- la firma digitale
- il redeem script in “chiaro”.

![Frame del video Bitcoin in Action — Come è formata una transazione P2SH-P2PK](https://cdn-images-1.medium.com/max/1200/0*__hAs5XcMI8LHyl-.jpeg)
*Frame del video Bitcoin in Action — Come è formata una transazione P2SH-P2PK*

Ci sono sempre questi elementi nello scriptSig?

No, dipende dallo script che si vuole utilizzare o che si crea. Per essere più precisi, **il redeem script in chiaro sarà sempre presente**, cambierà la prima parte.

In questo caso sarà sufficiente la firma digitale perchè è l’elemento che servirà per soddisfare la nostra transazione.

![](https://cdn-images-1.medium.com/max/1200/1*fgTLQmzMNN_qH1d8sIxpMQ.png)

Come riportato nella foto, sono stati inseriti nello stack la firma digitale e il redeem script.

Successivamente, si “passa” ad inserire gli elementi dello scriptPubKey, inserendo OP_HASH160, il quale, come già affrontato negli articoli precedenti, esegue il pop dell’elemento on top e applica la funzione crittografica SHA256 e RIPEMD160.

Il risultato viene inserito nello stack.

Vi ricordate come viene ottenuto il redeem script Hash?  
Viene ottenuto applicando lo SHA256 e il RIPEMD160, esattamente la stessa operazione dell’HASH160.

![](https://cdn-images-1.medium.com/max/1200/1*7tj6fHP9Uf1hmeCJH3t-aA.png)

Successivamente viene pushato il redeem script hash, contenuto nello scriptPubKey.

L’operazione successiva è **OP_EQUAL** la quale prende i primi due elementi on top e li verifica tra loro.

Se questi sono uguali inserisce 1, se invece sono diversi invalida la transazione.

Perchè questo controllo? Per prima cosa per rendere il P2SH **retro-compatibile** con quei miner che non avevo aggiornato.

Nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/) affrontiamo nel dettaglio questo tema.

Successivamente perchè confrontare due stringhe è sicuramente più veloce e ottimizzato che eseguire lo stack, perchè se l’hash del redeem script è diverso dall’hash del redeem script ottenuto dal redeem script in chiaro, è evidente che le operazioni al suo interno siano diverse, proprio perchè non è possibile ottenere digest uguali da input differenti.

![](https://cdn-images-1.medium.com/max/1200/1*JR3NFiPTqBVnirnBCB4img.png)

Se tuto va a buon fine, vedremo uno 01, ovvero il risultato ottenuto da OP_EQUAL, il quale poi viene rimosso dallo stack (pop) per eseguire il redeem script, e quindi il controllo vero e proprio, che risulta essere un normale P2PK, come già analizzato nei video precedenti.

Verrà quindi confrontata la firma digitale con la chiave pubblica fornita, grazie all’operation code OP_CHECKSIG

![](https://cdn-images-1.medium.com/max/1200/1*35gRlmG7ERLp-okAgirnRQ.png)

Il processo può sembrare macchinoso e difficile da capire, ma se si conosce la natura degli script, come ad esempio il P2PK e il P2PKH, il processo risulterà lineare



