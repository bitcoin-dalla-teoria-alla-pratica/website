---
title: "Pizza day in SegWit"
date: 2020-05-22T10:00:00+01:00
slug: "pizza-day-in-segwit"
draft: false
author: "Alessio Barnini"
description: "Scopri il video su youtube — Bitcoin in Action"
cover: "/img/posts/pizza-day-in-segwit-1.webp"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### **Pizza day in SegWit** #### Scopri il video su youtube — Bitcoin in Action

![Scopri il video su Bitcoin in Action](/img/posts/pizza-day-in-segwit-1.webp)
*Scopri il video su Bitcoin in Action*

Oggi, 22 Maggio 2020, è il 10° anniversario del pizza day.

Di che cosa si tratta? L’utente Laszlo scrisse su [bitcoin talk](https://bitcointalk.org/index.php?topic=137.msg1141) che avrebbe pagato 10.000 bitcoin per chi gli avesse consegnato 2 pizze belle grandi, così da mangiarla anche il giorno dopo.

![Post originale di Laszlo](/img/posts/pizza-day-in-segwit-2.webp)
*Post originale di Laszlo*

Il messaggio “provocatorio” fu accettato da un utente, che noi chiameremo Luigi, stereotipo del pizzaiolo italiano all’estero.

Spesso si sente parlare che Laszlo ha pagato più di 90 milioni di dollari per una pizza! Certo convertiti al giorno d’oggi è esattamente così, ma che cosa dire per le fee?

Analizzando la transazione con un qualsiasi [explorer](https://btc.bitaps.com/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d) possiamo vedere che le fee ammontano a quasi 0.99 bitcoin, quasi 9 mila dollari al tasso attuale !

Quindi ci siamo chiesti, quando avrebbe speso di fee se Laszlo avesse usato segwit?

Per rispondere alla domanda, che questa volta ci siamo auto-fatti, lo abbiamo messo in pratica.

Sappiamo che le fee dipendono da vari fattori, tra cui anche la congestione del network, cercheremo di avvicinarsi il più possibile alla transazione del 2010.

---

> In Action!

Cerchiamo di replicare tutti gli importi che l’utente Laszlo ha utilizzato per generare la transazione.

Per fare questo utilizzeremo due nodi regtest, in modo tale da utilizzare la chiamata [**sendtoaddress**](https://bitcoin-rpc.github.io/en/doc/0.17.99/rpc/wallet/sendtoaddress/).

Entrambi i nodi partono con una blockchain con zero blocchi e sono in collegamento tra di loro, quindi quando un nodo minerà un blocco, l’altro nodo si sincronizzerà.

Sono stati creati 3 Address Segwit.

- Un address per il miner e salvata nella variabile d’ambiente $MINER
- Un address per Laszlo e salvata nella variabile d’ambiente $LASZLO
- Un address per Luigi e salvata nella variabile d’ambiente $LUIGI

Mineremo 1000 blocchi, così’ da avere un reward sufficiente da trasferire a Laszlo.

Gli importi sono gli stessi che aveva Laszlo durante quella transazione per cercare di replicare più fedelmente possibile.

Quando Laszlo avrà ricevuto tutto il suo importo, dal nodo secondario, possiamo finalmente fare la transazione verso Luigi, consumando tutti gli input.

Analizzando la transazione possiamo verificare il suo peso in byte e vsize.

Attenzione, dopo l’attivazione di segwit, le fee si pagano su vsize.

il calcolo del vsize si effettua facendo la divisione per 4 del totale di weight e si considera l’intero successivo.

Il weight si ha moltiplicando *4 tutti gli elementi non segwit.

Quindi il vsize è 4070.

Quanto pesa la transazione legacy?

Possiamo fare lo stesso procedimento ma utilizzando address legacy. Quindi ricreare la transazione di LASZLO con gli stessi input e inviarla verso LUIGI.

Il vsize in questo caso è 8896, più del doppio.

Come vedete il vsize e i byte corrispondono, proprio perchè non esistono byte segwit che hanno un peso di 1, ma tutti i byte sono legacy, e hanno peso 4.

---

Quindi possiamo dedurre che, facendo la stessa transazione con lo stesso numero di input, l’utente Laszlo avrebbe speso meno della metà in termini di fee.

È sempre una cifra interessante, ma ricordatevi che le fee non dipendono dall’ammontare dell’importo spostato, ma da quanti byte, o meglio vsize è composta.

Ricorda che il codice è disponibile nel nostro repository 🐙 [GitHub](https://bit.ly/2Lj3yeY)!

Ciao!
