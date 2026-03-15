---
title: "Che cosa è la Proof of Work?"
date: 2019-03-18T10:00:00+01:00
slug: "che-cosa-la-proof-of-work"
draft: false
author: "Alessio Barnini"
description: "Una delle parti fondamentali di Bitcoin è la Proof of Work (PoW)."
images: ["https://cdn-images-1.medium.com/max/1200/1*H73RAozblI4FlhzcHwDjUw.png"]
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Che cosa è la Proof of Work?

Una delle parti fondamentali di Bitcoin è la Proof of Work (PoW).

In che cosa consiste la PoW ?

La proof of work è il processo con il quale il miner inserisce le transazioni all’interno del blocco e riesce ad ottenere un** block header hash** minore della difficoltà (**target**) imposta in quel momento storico dalla rete, aggiudicandosi così un *posto* nella blockchain, ed il reward.

![Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”](https://cdn-images-1.medium.com/max/1200/1*C50yTKsDThJw_8lmSvuYOA.gif)
*Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”*

La difficoltà viene “*tarata*” ogni 2016 blocchi, in modo tale che un blocco sia minato in media ogni 10 minuti.

Perchè ogni 10 minuti?

**Per evitare fork** troppo frequenti per fork non si intende hard fork o soft fork, ma si intende quando due miners forniscono contemporaneamente una PoW valida.

I due blocchi hanno di fatto lo stesso padre, o meglio lo stesso** previous block hash**

**E per la sicurezza.**

Se fosse facile minare blocchi, ci sarebbe meno sicurezza, in quanto i miners con tanta potenza di calcolo, potrebbero crearli in autonomia, fino ad arrivare a fare il famoso attacco del 51%.

Che cosa fa esattamente il miner per vincere il PoW ed aggiudicarsi il reward?

Ogni miner crea un** candidate block** con le transazioni prese della** mempool**, e cerca di ottenere un** block header hash** minore del** target** imposto in quel momento storico dalla rete.

Se il miner non riesce ad ottenere l’hash più basso del target, deve provare nuovamentel miner però deve cambiare qualche parametro d’ingresso per ottenere un** digest** differente.

> Digest è il risultato ottenuto da una funzione crittografica

Diventa di fondamentale importanza il** nonce**, valore all’interno di ogni blocco, in particolar modo nel block header.

Perchè è cosi importante?   
Perchè se il miner usasse sempre lo stesso input otterrebbe sempre lo stesso output, o meglio, lo stesso digest.

Quindi cambia il valore del nonce per fare una nuova prova e cercare di vincere la** PoW.**

Se due input diversi dessero lo stesso output, saremmo davanti ad un problema chiamato** collisione**

> In crittografia, una collisione hash è una situazione che avviene quando due diversi input producono lo stesso output tramite una funzione hash.

Quali sono i valori che il miner utilizza per fare il** PoW** ?

Il miner fa il doppio** SHA256** di tutti gli elementi del block header.

Per essere più precisi:

- versionHex
- previousblockhash
- merkleroot
- time
- bits
- nonce

Il risultato che deve ottenere è un hash minore del target (il bits è il target nella sua forma compatta).  
Se riesce a vince il** PoW**, dopo moltissimi tentativi, il blocco diventa parte della blockchain, e il suo hash è esattamente l’hash che ha fatto vincere il miner.

Prima di essere “ammesso” alla blockchain, il blocco viene verificato ancora, controllando i parametri necessari per essere conforme al protocollo, inclusa la coinbase, transazione che il miner crea per aggiudicarsi il reward.

Per concludere possiamo dire che, per trovare la soluzione al** PoW,** il miner impiega molto tempo, mentre per verificare che l’hash trovato sia sotto la difficoltà imposta ci vuole pochissimo tempo, proprio perchè non abbiamo il problema della collisione.
