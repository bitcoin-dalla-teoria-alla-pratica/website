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
cover: "/img/posts/che-cosa-e-segwit-bitcoin.webp"
---

Se bazzicate un po' nel mondo Bitcoin, vi sarà sicuramente capitato di sentire la parola **SegWit**. È l'abbreviazione di *Segregated Witness* — "Testimone isolato" — ed è stato uno degli aggiornamenti più importanti per la rete. Pensato nel 2015 da Pieter Wuille e attivato nell'agosto del 2017.

Il problema di partenza era semplice: un blocco Bitcoin non può pesare più di 1 megabyte. Con questo limite, la rete reggeva al massimo 3-7 transazioni al secondo — pochissime. Aumentare la dimensione dei blocchi d'un colpo avrebbe richiesto hardware sempre più potente e minacciato la decentralizzazione. Bisognava trovare un'altra strada.

## La firma si sposta, e tutto cambia

L'idea di SegWit è questa: prendere le firme digitali — il "testimone" che prova che quei Bitcoin sono tuoi — e spostarle in un campo separato chiamato `txinwitness`. I vecchi nodi non aggiornati vedono la transazione senza firme ma la considerano valida lo stesso, e ci guadagnano spazio. In più, la firma non influenza più il TXID della transazione: il bug della *transaction malleability*, risolto.

Con SegWit nasce anche una nuova unità di misura, il **Block Weight**, che può arrivare a 4 megabyte virtuali. I dati classici pesano 4 unità, i dati SegWit (le firme) pesano solo 1. Risultato: lo spazio reale medio di un blocco è salito a circa **2,3 MB**, con più transazioni per blocco.

## Meno commissioni, indirizzi che iniziano con bc1

Le commissioni Bitcoin si calcolano sulla *vsize* (virtual size), ottenuta dividendo il peso totale per 4. Dato che le firme SegWit pesano un quarto rispetto al formato legacy, la transazione risulta più leggera ai fini del calcolo. Il risparmio usando indirizzi nativi SegWit va dal **39% al 58%**.

Gli indirizzi nativi SegWit usano il formato **Bech32** e iniziano sempre con `bc1`. Sono solo minuscole, rilevano fino a 5 caratteri errati e producono QR code più compatti. Se il tuo wallet usa ancora indirizzi che iniziano con `1` (P2PKH) o `3` (P2SH), stai probabilmente pagando commissioni più alte del necessario. Vale la pena controllare.

Se vuoi approfondire come funzionano gli indirizzi Bitcoin prima di SegWit, puoi leggere [come è costruito un indirizzo P2PKH](/posts/ottenere-un-address-p2pkh-e-come-e-costruito-in-action/) oppure [l'introduzione a P2SH](/posts/introduzione-a-p2sh-bitcoin/).
