---
title: "Bitcoin blockchain fork"
date: 2019-03-21T10:00:00+01:00
slug: "bitcoin-blockchain-fork"
draft: false
author: "Alessio Barnini"
description: "Forse vi potrà sorprendere che la blockchain Bitcoin subisce dei fork molto frequentemente."
cover: "/img/posts/bitcoin-blockchain-fork-2.webp"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Hash"
categories:
  - "Bitcoin"
---

---

Forse vi potrà sorprendere che la blockchain Bitcoin subisce dei fork molto frequentemente.

Per proseguire dobbiamo chiarire anche la differenza tra Nodo e Miner

---

**I Full node** come sappiano hanno l’intera blockchain scaricata.

Stanno in ascolto su altri nodi e verificano che una transazione sia valida confrontandola proprio con la blockchain che hannoer essere più precisi con LevelDb **Chainstate**

Se tale transazione viene verificata viene passata ad un altro nodo, e aggiorna la propria **mempool**, dove sono “ospitate” tutte le transazioni **unconfirmed**na transazione è **unconfirmed** quando non è ancora inclusa nel blocco, di fatto non fa ancora parte della blockchain

---

**I miners** stanno in ascolto sulle nuove transazioni, prendendo le transazioni da includere nel blocco dalla **mempool**

Il loro compito è creare blocchi di transazioni valide e risolvere il PoW dietro ricompensa BTCna volta risolto mandano il blocco in broadcast, cioè nella rete

---

> Per adesso possiamo dire che i Miners a differenza dei fullnode creano blocchi.

Come sappiamo la blockchain è un sistema decentralizzato e come dicevamo i nodi hanno al suo interno la replica esatta della blockchain.

Essendo un sistema decentralizzato può essere che il nodo A abbia ricevuto il **tip**, ovvero il blocco più in alto, il più nuovo, mentre il nodo B non abbia ancora ricevuto lo stesso blocco, proprio perchè essendo una rete decentralizzata, **le informazioni si propagano come dei cerchi nell’acqua e quindi non simultaneamente**.

Il miner per creare il blocco deve risolvere il **Proof Of Work.**(PoW)

![Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”](/img/posts/bitcoin-blockchain-fork-3.webp)
*Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”*

Bene il miner con i capelli verdi è Alessio, il miner con i capelli neri è Marco.

Immaginiamo che per risolvere il PoW i miners devono risolvere l’addizione 1+1.

Alessio e Marco trovano la soluzione al problema 1+1 contemporaneamente, risolvendo di fatto il PoW in maniera corretta e creando cosi il blocco da mandare in broadcast

Il nodo Paolo riceve il blocco di Alessio e verifica che sia corretto, una volta verificato lo inoltra ai nodi vicini

Il nodo di Michela invece riceve per primo il blocco di Marco e verifica che sia corretto, una volta verificato lo inoltra ai nodi vicini

Se Michela adesso ricevesse il blocco di Alessio **non potrà considerarlo valido** in quanto il padre di Alessio è lo stesso padre di Marco, ovvero il blocco celeste, e invece il nodo Michela sta tentando di aggiungerlo come figlio del blocco di Marco, cioè il blocco rosso.

![](/img/posts/bitcoin-blockchain-fork-3.webp)

Entrambi i blocchi, verdi e rossi sono validi al momento, entrambi hanno il **previousBlockhash** il valore hash del blocco celeste, quindi hanno lo stesso padre.

E adesso che succede?

I miners stanno continuando a lavorare sul prossimo blocco

Un nuovo blocco è stato trovato, e ha come  **previousblockhash**, l’hash del blocco verde, cioè il blocco minato da Alessio

Il blocco quindi viene mandato in broadcast e i nodi vengono aggiornati, tranne quelli con il blocco rosso, proprio perchè il **previousblockhash** del blocco viola (il nuovo blocco scoperto)non “combacia” con l’hash del blocco rosso.

A questo punto i miners vedono che c’è un ramo più lungo rispetto all’altro

Quindi abbandonano il ramo con il blocco rosso e cominciano a minare il ramo con il blocco viola appena aggiunto

Anche i fullnode si mettono dalla parte della blockchain più lunga.

Il blocco rosso, sarà considerato **orfano** e le sue transazioni re-inserite nella **mempool** e ricontrollate.

Da notare che solitamente il fork avviene con un massimo di un blocco, proprio come l’esempio che abbiamo visto.

Quindi possiamo affermare che il ramo più lungo vince, diventando la main chaine vogliamo essere ancora più corretti vince il ramo dove è stata accumulata più **Proof of Work**

---

![Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”](/img/posts/bitcoin-blockchain-fork-2.webp)
*Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”*