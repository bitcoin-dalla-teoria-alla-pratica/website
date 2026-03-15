---
title: "Multisignature P2SH su Bitcoin, come è costruita la transazione"
date: 2023-12-06T10:00:00+01:00
slug: "multisignature-p2sh-su-bitcoin-come-costruita-la-transazione"
draft: false
author: "Alessio Barnini"
description: "Ciao,"
images: ["https://cdn-images-1.medium.com/max/1200/1*cq7lzrOb0ERo4u8QnISjKA.jpeg"]
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

Ciao,

Nel nostro precedente articolo, abbiamo esaminato la creazione del redeem script per un indirizzo P2SH 2–3.

In questo capitolo, esploreremo come lo stack viene risolto per rendere la transazione valida.

Come accennato in articoli precedenti, nello scriptPubKey della UTXO, troviamo l’hash del redeem script.

Attraverso le operazioni OP_HASH160 e OP_EQUAL, ottimizziamo il processo verificando l’hash prima di interpretare il redeem script.

![](https://cdn-images-1.medium.com/max/1200/1*cq7lzrOb0ERo4u8QnISjKA.jpeg)

Il formato dello scriptPubKey è il seguente: OP_HASH160 redeem script hash OP_EQUAL

![](https://cdn-images-1.medium.com/max/1200/1*yxyumxd3-_p5IUZnbRrZIw.png)

La sezione di input, lo scriptSig, conterrà le condizioni necessarie per validare la transazione.

Sappiamo già che lo scriptSig contiene il redeem script in chiaro, insieme alle firme corrispondenti.

Ricordando che lo script è di tipo 2–3, richiedendo almeno due firme, il redeem script sarà composto da 2 PB PB PB 3 OP_CHECKMULTISIG.

Di conseguenza, lo scriptSig assumerà la forma: OP_0 Signature Signature 2 PB PB PB 3 OP_CHECKMULTISIG, dove PB identifica le chiavi pubbliche.

La logica sottostante rimane simile agli script P2SH-P2PK o P2SH-P2PKH, con ovvie differenze nelle condizioni richieste per la validità.

Per quanto riguarda gli script multisignature, dobbiamo gestire un bug nell’operation code OP_CHECKMULTISIG.

Questo codice opera una pop (estrazione) in eccesso nello stack.

Per risolvere il problema, aggiungiamo un elemento inutile all’estrazione, che è OP_0.

Quindi, lo scriptSig finale avrà il seguente formato: OP_0 Signature Signature 2 PB PB PB 3 OP_CHECKMULTISIG.

Per ulteriori dettagli sul bug, ti invitiamo a consultare la documentazione sugli script di Bitcoin.

*Compares the first signature against each public key until it finds an ECDSA match. Starting with the subsequent public key, it compares the second signature against each remaining public key until it finds an ECDSA match. The process is repeated until all signatures have been checked or not enough public keys remain to produce a successful result. All signatures need to match a public key. Because public keys are not checked again if they fail any signature comparison, signatures must be placed in the scriptSig using the same order as their corresponding public keys were placed in the scriptPubKey or redeemScript. If all signatures are valid, 1 is returned, 0 otherwise. Due to a bug, one extra unused value is removed from the stack.*

Nel prossimo articolo, esploreremo il processo di validazione di una transazione multisignature.



