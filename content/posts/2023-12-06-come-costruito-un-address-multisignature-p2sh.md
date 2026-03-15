---
title: "Come è costruito un address MultiSignature P2SH?"
date: 2023-12-06T10:00:00+01:00
slug: "come-costruito-un-address-multisignature-p2sh"
draft: false
author: "Alessio Barnini"
description: "Ciao,"
images: ["https://cdn-images-1.medium.com/max/1200/1*MDt92rabXRQfxc96rDzXdQ.png"]
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

Ciao,

In questo articolo vedremo come è costruito un multisignature P2SH, **NON** SegWit.

Grazie agli articoli precedenti abbiamo potuto capire come e dove è costruito lo script.

Abbiamo infatti analizzato script conosciuti, quali il P2PK e il P2PKH.

In questo articolo andremo a costruire uno script, o se vi piace di più uno smart contract 2–3.

Che cosa significa un address 2–3?

Significa che, una transazione per essere valida deve avere almeno **due firme**, le quali possono essere comprovate **su tre chiavi pubbliche**.

Vi ricordate dove vengono inserite le condizioni da soddisfare?  
Le condizioni da soddisfare sono inserite nel **redeem script** durante la generazione dell’address. 
  
Cerchiamo quindi di dare forma al **redeem script**. **Il nostro obiettivo è avere la prova che due firme digitali siano valide, provandole su tre chiavi pubbliche**.

Quindi il mio script avrà sicuramente 3 chiavi pubbliche: 🔑 🔑 🔑.

Dobbiamo inoltre comunicare al nostro script, il numero minimo di firme che vogliamo avere per rendere la transazione valida, in questo caso 2.

- Aggiungiamo la condizione al nostro script: 2️⃣🔑 🔑 🔑

Altra condizione che dobbiamo dichiarare, è il numero massimo di chiavi che devono essere presenti nel nostro script, in questo caso 3.

- Aggiungiamo la condizione al nostro script: 2️⃣🔑 🔑 🔑3️⃣

Manca un ultimo elemento per completare lo script.

Se lo script fosse completo, indicheremo all’interprete di inserire nello stack il numero 2 (per ora pensiamolo come numero ma in realtà 2 è OP_2) all’interno dello stack, successivamente le 3 chiavi pubbliche, e il numero 3.

Manca effettivamente l’operazione da compiere!

Nello script P2PK, il controllo da fare è **OP_CHECKSIG**, nello script P2PKH il controllo da fare è un pò più complesso, ovvero la verifica dell’hash della chiave pubblica fornita e la verifica della firma utilizzando sempre l’operazione **OP_CHECKSIG**.

In questo caso non possiamo utilizzare OP_CHECKSIG perchè il suo compito è quello di verificare la firma digitale su una chiave pubblica e inserire 1 se la firma è verificata e 0 se la verifica non va a buon fine.

In questo modo però andremo a verificare una sola firma, il nostro compito invece è verificare 2 firme su 3 chiavi pubbliche. 
  
Leggendo la [documentazione](https://en.bitcoin.it/wiki/Script) troviamo l’operazione **OP_CHECKMULTISIG**.

Questa operazione controlla la firma ECDSA, ovvero la firma ottenuta dalla crittografia a curva ellittica sulle chiavi pubbliche messe a disposizione.

- Aggiungiamo la condizione al nostro script: 2️⃣🔑 🔑 🔑3️⃣OP_CHECKMULTISIG

Lo script, o per essere più precisi il redeem script è pronto.

I Passaggi successivi sono quelli che abbiamo analizzato negli articoli precedenti al fine di arrivare all’address.

Ovvero SHA256 RIPEMD160, Version Prefix e base58 checksum, per ottenere finalmente l’address, che inizierà con il numero 3 nell’ambiente di Mainnet, o con il numero 2 nell’ambiente di Testnet/Regtest

![📒Libro Bitcoin dalla teoria alla pratica (Amazon)📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)](https://cdn-images-1.medium.com/max/1200/1*MDt92rabXRQfxc96rDzXdQ.png)
*📒Libro Bitcoin dalla teoria alla pratica (Amazon)📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)*



