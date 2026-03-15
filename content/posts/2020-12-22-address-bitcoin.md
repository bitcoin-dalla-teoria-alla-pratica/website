---
title: "Address Bitcoin"
date: 2020-12-22T10:00:00+01:00
slug: "address-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Che cosa è lo stack?"
cover: "https://cdn-images-1.medium.com/max/1200/0*DQgE6OUhAceAOw2Y"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

#### Che cosa è lo stack?

![](https://cdn-images-1.medium.com/max/1200/0*DQgE6OUhAceAOw2Y)

Ciao,

abbiamo avuto l’idea di creare una nuova playlist per parlare degli address Bitcoin. Spesso sentiamo nomi come Pay to hash public key, oppure Pay to script hash, o ancora bech32.

Sono argomenti un pò impegnativi , per questo motivo utilizzeremo una lavagna per creare dei disegni per comprendere meglio l’argomento.

Per andare nel dettaglio e capire meglio Bitcoin, io e Alessandro abbiamo scritto 3 libri, [Bitcoin dalla teoria alla pratica](http://bit.ly/2ADHUN1), [Bitcoin in Action](prodotti/bitcoin-in-action/) e [Bitcoin 199 domande](https://bit.ly/3cmz07W).

Oltre a questo facciamo corsi live e offline che trovate su [bitcoininaction.com](http://bitcoininaction.com) in collaborazione con agli amici di [Bitcoin People.](https://www.bitcoinpeople.it/)

Partiamo parlando dicendo che non esistono address, ma esistono solo script. Gli address sono il risultato di funzioni crittografiche applicate sulla chiave pubblica.

Utilizzeremo come primo script, l’”address” **P2PK**.  
Pensiamo per un attimo al significato di Pay to Public Key.

Che cosa ci vuole comunicare? In italiano potremmo tradurla con *pagare a una chiave pubblica*.

Ed effettivamente è proprio quello che succede, quando si effettua una transazione, essa viene sbloccata confrontando la firma digitale su una chiave pubblica. 
  
Questo non dovrebbe sorprendere, perchè come abbiamo visto nei primi video, [forse proprio il primo video del canale](https://youtu.be/RU7LHPP4Lvk), la firma digitale si valida utilizzando la chiave pubblica derivata dalla chiave privata che ha generato quella firma.

Dobbiamo fare un passo indietro prima di parlare della generazione dell’address, dobbiamo chiarire i concetti di **Stack** e di validazione.

Lo stack è una sequenza di dati, inseriti uno sopra l’altro.  
Nel caso di Bitcoin si parla di stack **LIFO**, Last Input First output, quindi il primo elemento che entra è anche il primo ad uscire.

Un ulteriore particolarità è che lo stack è [**Reverse Polish**](https://en.wikipedia.org/wiki/Reverse_Polish_notation), ovvero gli operatori seguono l’operandi. 
  
Senza andare troppo nel dettaglio, vediamo un esempio.

L’operazione che vogliamo fare è una somma 2 + 2, quindi secondo l’annotazione polacca prima mettiamo 22 e poi l’operazione somma, OP_ADD.

![](/img/posts/address-bitcoin-2.webp)

![](https://cdn-images-1.medium.com/max/1200/1*4tcl_pEcUI2CZ1WRgZOSHQ.png)

Viene inserito il primo elemento nello stack. quando un elemento viene inserito nello stack si chiama operazione di push.

![](https://cdn-images-1.medium.com/max/1200/1*97pDz5H7frrGRkbrD4cojw.png)

Successivamente viene inserito il secondo operatore

Ed infine viene inserito l’operando che ha il compito di prendere i primi due elementi in top, quindi in cima allo stack, applicare la funzione della somma, e inserire il risultato nello stack. 
  
 Quindi l’operazione che farà saranno. POP di 2, POP di 2, PUSH di 4.

![](https://cdn-images-1.medium.com/max/1200/1*IZ9jSG3dCNKUFHgfM-9neA.png)

Questo è un primo passo per capire come vengono validate le transazioni.

Se volete approfondire questo argomento iscrivetevi al canale e visitate il nostro sito [corsobitcoin.com](http://corsobitcoin.com), dove trovate i nostri libri e i nostri contatti.

Ciao alla prossima
