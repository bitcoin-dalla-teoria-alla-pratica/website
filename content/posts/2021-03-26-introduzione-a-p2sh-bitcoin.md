---
title: "Introduzione a P2SH Bitcoin"
date: 2021-03-26T10:00:00+01:00
slug: "introduzione-a-p2sh-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Pay to Public Key"
cover: "/img/posts/introduzione-a-p2sh-bitcoin-2.webp"
tags:
  - "BIP"
  - "Bitcoin"
  - "Bitcoin Script"
categories:
  - "Bitcoin"
---

---

### **Introduzione a P2SH** #### Pay to Public Key

![](/img/posts/introduzione-a-p2sh-bitcoin-2.webp)

Dopo aver analizzato gli script **P2PK** (Pay to Public key) e **P2PKH** (Pay to Public key Hash) siamo arrivato al P2SH (Pay to script hash), gli address che iniziano con il numero 3.

Come la parola stessa ci suggerisce, andiamo a pagare alla *vista* di un hash di uno script.

Questo tipo di script è affrontato in modo molto dettagliato nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/).

![Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts.](/img/posts/introduzione-a-p2sh-bitcoin-2.webp)
*Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts.*

Andiamo per gradi.

Questo script è una evoluzione del **P2MS** (pay to multi sig) uno script che non ha avuto lunga vita a causa delle sue limitazioni, come ad esempio la costruzione dello script a carico del destinatario e non del mittente.

Prima di introdurre la *costituzione* dello script è bene ricordare due elementi fondamentali. Lo **scriptSig** e lo **ScriptPubKey**.

Nello scriptSig ci sono gli elementi necessari per soddisfare lo scriptPubKey, il quale è locato nella UTXO di riferimento.

Lo **P2PKH** si presenta così:

- lo **scriptSig** è formato da: Signature, Public key compressa.
- lo **scriptPubKey** è formato dalle operation code OP_DUP OP_HASH PBH OP_EQUALVERIFY OP_CHECKSIG dove PBH rappresenta l’hash della chiave pubblica compressa.

Lo **P2SH** è invece formato in questo modo:

- Lo scriptSig è formato da signatures {serialized script}
- Lo scriptPubKey è formato da OP_HASH160 [20-byte-hash-value] OP_EQUAL

![](/img/posts/introduzione-a-p2sh-bitcoin-3.webp)

Che cosa sono il serialized Script e 20-byte hash?

Premettendo che, in questi articoli andremo ad analizzare solo template riconosciuti da bitcoin-core, non andremo quindi a creare script custom, i quali invece sono affrontati nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/).

Il serialised script, viene descritto nel [Il BIP0016](http://bit.ly/3blePHt), Bitcoin Improve Proposal (2013), e rappresenta lo script da eseguire al fine di ottenere una transazione valida.

Questo è conosciuto anche come **redeem script**.

Il suo hash è ottenuto dall’op_code HASH160, ovvero il digest della funzione crittografica SHA256 e RIPEMD160, è posizionato nello scriptPubKey.

Che cosa può contenere il redeem script? Può contenere qualsiasi cosa, come scritto in precedenza, anche script custom.  
Ci sono dei template *standard, *che vengono riconosciuti da Bitcoin core al momento della firma, tra questi troviamo i vari Wrap di P2PK, P2PKH, Multisig e SegWit (non nativo).

La cosa interessante da sottolineare è che, quando andiamo a pagare a un address P2SH, se questo non ha mai fatto nessuna transazione, non sapremo mai che condizioni sono necessarie per sbloccare il suo UTXO, proprio perchè nel suo ScriptPubKey troviamo l’hash del redeem script.

Solo al momento di una sua spesa, potremo andare ad analizzare il suo redeem script, nel suo scriptSig di riferimento, proprio perchè *in chiaro.*

Nel prossimo articolo andremo nel dettaglio della costruzione dell’address P2SH Wrap P2PK.

Ciao!

---



