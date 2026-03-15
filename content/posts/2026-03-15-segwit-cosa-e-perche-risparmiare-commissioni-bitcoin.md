---
title: "SegWit: cos'è e perché ti fa risparmiare sulle commissioni Bitcoin"
date: 2026-03-15T10:00:00+01:00
slug: "segwit-cosa-e-perche-risparmiare-commissioni-bitcoin"
draft: false
author: "Alessio Barnini"
description: "SegWit (Segregated Witness) è l'aggiornamento Bitcoin del 2017 che ha ridotto le commissioni dal 39% al 58% e risolto il bug della transaction malleability."
tags:
  - "Bitcoin"
  - "SegWit"
  - "Fee"
  - "Blockchain"
categories:
  - "Bitcoin"
conver: "img/che-cosa-è-segwit-bitcoin.webp"
---

Se bazzicate un po' nel mondo Bitcoin, vi sarà sicuramente capitato di sentire la parola **SegWit**. È l'abbreviazione di *Segregated Witness* (che in italiano suona come "Testimone isolato") ed è stato uno degli aggiornamenti più importanti per la rete.

Pensato nel 2015 da Pieter Wuille e attivato nell'agosto del 2017, questo aggiornamento è nato per risolvere due grossi problemi: i blocchi troppo pieni e un bug chiamato *transaction malleability*.

---

## Il problema dello spazio e il limite di 1 MB

All'inizio, il protocollo Bitcoin aveva una regola ferrea: un blocco non poteva pesare più di 1 megabyte. Con questo limite, la rete riusciva a gestire al massimo dalle 3 alle 7 transazioni al secondo — pochissime, se paragonate ai circuiti tradizionali.

Aumentare di colpo la grandezza del blocco (tramite *hard fork*) avrebbe richiesto hardware molto più potente per gestire la rete, minacciando la decentralizzazione che è il cuore di Bitcoin. Serviva un approccio più elegante.

---

## La soluzione: spostare la firma

L'idea vincente è stata quella di operare in modo "morbido" tramite *soft fork*. Si è deciso di prendere le firme digitali — il "testimone" che prova che quei Bitcoin sono tuoi — e spostarle in un campo separato chiamato `txinwitness`.

Questo ha prodotto due effetti:

- I vecchi nodi non aggiornati vedono la transazione senza firme, ma la considerano comunque valida, risparmiando spazio
- Spostando le firme, il bug della *transaction malleability* è risolto definitivamente: la firma non influenza più il TXID della transazione

---

## Una nuova unità di misura: il Block Weight

Con SegWit non si parla più di megabyte classici ma di **Block Weight**, che può arrivare a un massimo di 4 megabyte virtuali. Il calcolo del peso è asimmetrico:

- I dati "classici" pesano **4 unità**
- I dati SegWit (le firme nel `txinwitness`) pesano **1 unità**

Lo spazio reale medio di un blocco è così salito a circa **2,3 MB**. Più spazio significa più transazioni nello stesso blocco.

---

## Il vantaggio concreto: commissioni più basse

Le commissioni vengono calcolate sulla base della *vsize* (virtual size), ottenuta dividendo il peso totale della transazione per 4. Dato che le firme SegWit pesano un quarto rispetto al formato legacy, l'intera transazione diventa più "leggera" ai fini del calcolo.

Il risparmio sulle commissioni usando indirizzi nativi SegWit va dal **39% al 58%**.

---

## Come riconoscere un indirizzo SegWit

Gli indirizzi nativi SegWit usano il formato **Bech32** e iniziano sempre con `bc1`. Hanno alcune caratteristiche pratiche rispetto agli indirizzi legacy:

- **Solo minuscole** — più facili da leggere, meno errori di trascrizione
- **Rilevamento errori** — se digiti male fino a 5 caratteri, il wallet se ne accorge
- **QR Code più efficienti** — grazie all'assenza di maiuscole

---

## Conclusione

Se il tuo wallet non supporta indirizzi `bc1` o non applica commissioni ridotte sulle transazioni SegWit, vale la pena aggiornarlo o sostituirlo. I vantaggi in termini di spazio nei blocchi, correzione del bug della *transaction malleability* e risparmio sulle fee sono concreti e misurabili.
