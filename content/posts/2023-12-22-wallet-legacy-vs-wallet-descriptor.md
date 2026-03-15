---
title: "Wallet Legacy vs. Wallet Descriptor"
date: 2023-12-22T10:00:00+01:00
slug: "wallet-legacy-vs-wallet-descriptor"
draft: false
author: "Alessio Barnini"
description: "In questo articolo, ci immergeremo nell’analisi delle differenze tra i wallet legacy e i wallet descriptor di Bitcoin. Potresti non…"
cover: "https://cdn-images-1.medium.com/max/1200/0*gmKbASHkI79mPZaa.jpg"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

In questo articolo, ci immergeremo nell’analisi delle differenze tra i wallet legacy e i wallet descriptor di Bitcoin.

Potresti non essertene accorto, ma a partire da **Bitcoin Core 0.17.0 nel 2018**, è stata implementata questa significativa funzionalità, destinata a rendere obsoleti i wallet legacy nel prossimo futuro.

![](https://cdn-images-1.medium.com/max/1200/0*gmKbASHkI79mPZaa.jpg)

#### Un Aggiornamento Silenzioso, Ma Cruciale

L’avvento dei wallet descriptor è stato un aggiornamento silenzioso per gli utenti, ma la sua influenza si riflette in una maggiore sicurezza e flessibilità.

Questo progresso nell’ecosistema Bitcoin è stato ben documentato nell’articolo “[Output Script Descriptors](https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md)” scritto dallo sviluppatore Ava Chown, che fornisce una panoramica approfondita delle migliorìe introdotte.

#### Descrizione dei Wallet: Legacy vs. Descriptor

Una delle differenze chiave tra i Legacy Wallets e i nuovi Descriptor Wallets è l’approccio nello sviluppo.

Questi ultimi sono progettati per supportare il linguaggio Bitcoin Script, mentre i Legacy Wallets sono stati concepiti basandosi sul concetto di chiavi.

#### Cambiamenti nei Comandi RPC

Con l’avvento dei Descriptor Wallets, sono stati apportati cambiamenti significativi ai comandi RPC.

Ad esempio, i comandi **dumpprivkey** e signrawtransactionwithkey sono stati sostituiti dal più moderno **signrawtransactionwithwallet** Questo cambiamento è parte integrante dell’approccio più sicuro adottato dai Descriptor Wallets.

#### Maggiore Sicurezza con Descriptor Wallets

Una delle caratteristiche distintive dei Descriptor Wallets è quella di non esporre la chiave privata attraverso il comando **dumpprivkey**.

Questa scelta è mirata a proteggere gli utenti da possibili manovre errate o compromissioni di sicurezza.

Inoltre, i Descriptor Wallets risolvono il problema critico legato alle chiavi non rinforzate.

Prima, se un attaccante avesse ottenuto l’extended public key (xpub) e una chiave privata non hardned, avrebbe potuto dedurre la chiave privata dell’extended public key.

Ciò implicava la possibilità di ottenere ogni chiave derivabile da essa, sia hardned che non hardned.

Per ulteriori approfondimenti sulla tematica hardned e non hardned, si consiglia di libro [Bitcoin dalla Teoria alla Pratica](https://amzn.to/2Ldym0F)

![Bitcoin dalla Teoria alla Pratica](https://cdn-images-1.medium.com/max/1200/1*akOVx54flkLJDFyLTuD4uA.png)
*Bitcoin dalla Teoria alla Pratica*

#### Il Futuro dei Wallet Bitcoin

L’avvento dei Descriptor Wallets rappresenta un passo avanti cruciale nella creazione di portafogli più sicuri e flessibili.

Con i wallet legacy destinati a essere deprecati nelle versioni future, è fondamentale comprendere e adottare le nuove tecnologie per mantenere un ambiente di gestione delle chiavi più sicuro ed efficiente.
