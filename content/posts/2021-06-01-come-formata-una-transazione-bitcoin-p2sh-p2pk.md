---
title: "Come è formata una transazione Bitcoin P2SH-P2PK"
date: 2021-06-01T10:00:00+01:00
slug: "come-formata-una-transazione-bitcoin-p2sh-p2pk"
draft: false
author: "Alessio Barnini"
description: "Video disponibile sul canale YouTube Bitcoin in Action"
cover: "/img/posts/come-formata-una-transazione-bitcoin-p2sh-p2pk-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

#### Video disponibile sul canale [YouTube Bitcoin in Action](https://youtu.be/wMvFm2GJtcI)

Ciao,

Negli articoli precedenti abbiamo analizzato come è costruito un [address P2SH-P2PK](https://bitcoin-in-action.medium.com/come-creare-un-address-p2sh-p2pk-bitcoin-2ed875f9fd7e), e in questa introduzione andremo invece ad analizzare come è costruita la transazione.

![Frame del video Bitcoin in Action —Come è formata una transazione P2SH-P2PK](/img/posts/come-formata-una-transazione-bitcoin-p2sh-p2pk-1.webp)
*Frame del video Bitcoin in Action —Come è formata una transazione P2SH-P2PK*

Nell’immagine della lavagna è riportata una simil transazione, ovvero come poi verrà eseguito lo script.

Nello **scriptSig**, ovvero la parte dell’input della transazione, troviamo le condizioni necessarie per soddisfare lo **scriptPubKey** della **UTXO** di riferimento.

Avendo preso come riferimento un [**P2SH–P2PK**](https://youtu.be/SzlTMdp7txE) nello scriptSig è presente la firma digitale e il redeem script in chiaro.  
Esatto, il redeem script, è posizionato nello **scriptSig**, gli stessi elementi che sono stati utilizzati per [creare l’address](https://bitcoin-in-action.medium.com/come-creare-un-address-p2sh-p2pk-bitcoin-2ed875f9fd7e) negli articoli precedenti.

Nello scriptPubKey è invece presente l’operation code OP_HASH160 il redeem script hash e l’operation code OP_EQUAL.

Lo script sarà sempre così? Lo scriptPubKey avrà sempre questa forma OP_HASH160 Redeem Script Hash OP_EQUAL.

La parte che andrà a cambiare sarà lo **scriptSig**, in base allo script utilizzato.

Ad esempio, per lo script **P2PKH**, nello scriptSig troveremo la firma digitale e la chiave pubblica, esattamente come una normale [P2PKH](https://bitcoin-in-action.medium.com/transazione-p2pkh-nel-bitcoin-in-action-playground-c9df028d4930).

Come vedremo nei video successivi la transazione sarà validata in questo modo:

— –SCRIPTSIG

– PUSH della firma digitale

– PUSH del redeem script

— –SCRIPTPUBKEY

– HASH160 sul redeem script

– PUSH del redeem script HASH

– OP_EQUAL il quale confronta i due digest on top, ovvero il redeem script

Se tutto va a buon fine il redeem script viene *deserializzato* e viene validata la transazione.

La transazione validata step by step è spiegata nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/).

![Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](/img/posts/come-formata-una-transazione-bitcoin-p2sh-p2pk-2.webp)
*Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts*

Ciao e alla prossima!



