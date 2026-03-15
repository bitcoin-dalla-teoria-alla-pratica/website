---
title: "Merkle tree Bitcoin"
date: 2019-10-03T10:00:00+01:00
slug: "merkle-tree-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Lo sprint che serviva per il libro Bitcoin dalla teoria alla pratica"
images: ["https://cdn-images-1.medium.com/max/1200/1*mJwJypYxRp-ooQl_NZKhsw.png"]
tags:
  - "Bitcoin"
  - "Hash"
  - "Merkle Tree"
categories:
  - "Bitcoin"
---

---

### Merkle tree Bitcoin

#### Lo sprint che serviva per il [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica)

Durante lo studio di Bitcoin ci siamo imbattuti nel **Merkle tree** e dopo esser riusciti a capirlo e a replicarlo, abbiamo raggiunto il nostro obiettivo.

![Le prime prove (sbagliate) di “ricorstruzione” del merkle tree.](https://cdn-images-1.medium.com/max/1200/1*ACnsmvs8_EzEaiZV-YiS7Q.png)
*Le prime prove (sbagliate) di “ricorstruzione” del merkle tree.*

Ma vediamo che cosa è il **Merkle tree**. ---

> Estratto del capitolo 4 di Bitcoin dalla teoria alla pratica

[**Merkle tree**](http://bit.ly/2LpZYCF), o albero binario di hash, è una struttura dati molto efficiente per verificare l’integrità di una grande quantità di dati.

Siamo soliti immaginare un albero dalla radice posta in basso e dalle foglie poste in alto.

Questo dobbiamo invece immaginarcelo al contrario, la radice (merkle root) è in alto e le foglie sono in basso.

Il merkle root è costruito ricorsivamente facendo hash di ogni foglia, che a loro volta sono unite e “hashate” di nuovo, fino ad avere un unico hash che rappresenta l’impronta digitale delle transazioni di quel blocco.

L’hash utilizzato è sempre lo SHA256 e il merkle root è sempre di 32 bytes.

---

La chiave per capirlo e risolvere l’errore riportato nella prima immagine è stato stamparlo vuoto e unire a coppie le foglie, fino ad arrivare alla radice.

Così facendo abbiamo riprodotto dei merkle tree *particolari *dove è necessario fare hash di hash della stessa foglia. 
Vediamo un caso base per capire di cosa stiamo parlando.

---

> Estratto del capitolo 4 di Bitcoin dalla teoria alla pratica

![Figura 4.1 — Merkle tree — Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*FKCPGyCIV9oD1CBMQ_2psQ.png)
*Figura 4.1 — Merkle tree — Bitcoin dalla teoria alla pratica*

Immaginiamo di avere un merkle tree con 4 foglie, che rappresentano 4 transazioni (figura 4.1).

Partiamo dalla base “Ha”, che rappresenta l’hash della transazione. 
Quindi uniremo “Ha” con “Hb”.

Con “uniremo” si intende concatenare le stringhe. 
Quindi applicheremo la funzione **SHA256** per due volte alla stringa concatenata.

Perché due volte?  
Non c’è una spiegazione certa, ma il protocollo Bitcoin lavora così.

La stessa procedura viene effettuata per le foglie “Hc” e “Hd”. 
Siamo così saliti di un gradino verso la costruzione della root.

Il prossimo passo quale sarà? 
Lo stesso, uniremo il risultato dei due hash e applicheremo per due volte lo **SHA256**.

Siamo arrivati alla root, che sarà **sempre** di 32 bytes proprio perché è ottenuta dalla funzione di hash SHA256.

Piccola anticipazione per quanto riguarda la costruzione che andremo a fare sul nodo Bitcoin.

Le foglie iniziali sono nella rappresentazione [big endian](http://bit.ly/2ZXCjg1).

Dobbiamo cambiare l’ordine dei bytes in **little endian**, e infine cambiare nuovamente l’ordine dei bytes della root per ottenere la rappresentazione in **big endian**, così da confrontarla con quella del blocco originale, ottenendo la prova che il nostro lavoro sia andato a buon fine.

---

Possiamo tranquillamente dire che dal Merkle root è nato il nostro progetto!

![Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*mJwJypYxRp-ooQl_NZKhsw.png)
*Bitcoin dalla teoria alla pratica*
