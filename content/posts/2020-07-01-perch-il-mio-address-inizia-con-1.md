---
title: "Perché il mio address inizia con 1?"
date: 2020-07-01T10:00:00+01:00
slug: "perch-il-mio-address-inizia-con-1"
draft: false
author: "Alessio Barnini"
description: "Video completo disponibile su youtube."
cover: "/img/posts/perch-il-mio-address-inizia-con-1-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

### Perché il mio address inizia con 1?

#### Video completo disponibile su [youtube](https://youtu.be/--oq3SbK2xQ).

![](/img/posts/perch-il-mio-address-inizia-con-1-1.webp)

Ciao,

oggi rispondiamo a Marco che ci domanda:

Perché il mio address inizia con il numero 1? Ho visto altri address che iniziato con il numero 3, che differenze ci sono?

Allora Marco, il tuo address inizia con il numero 1 perchè sta utilizzando lo script Pay to Public key hash ( **P2PKH** ).

L’address si ricava utilizzando delle funzioni crittografiche proprio sullo script che stiamo utilizzando, in **P2PKH** si ottiene il prefisso 1 dopo aver applicato SHA256 e RIPEMD160 sulla chiave pubblica compressa, preceduto dal version prefix di riferimento.

Nel video corso e nel nostro libro si ottiene un address **P2PKH** partendo da una chiave privata, generata da zero.

Quando invece vedi address che iniziano con il numero 3, significa che la persona sta utilizzando un address Pay to script hash (P2SH), ed infine se vedi un address che inizia con bc1, significa che sta utilizzando SegWit.

In realtà non esistono address, ma esistono digest di script, il quale prende il nome di address.

Gli script quindi sono nati grazie a nuove implementazioni da parte della community Bitcoin al fine di migliorarne le prestazioni.

Vediamo con un esempio l’address P2PKH. Ad un certo punto vi lancio una sfida, dove in palio c’è una copia del libro Bitcoin dalla teoria alla pratica.

> In action

Per questo esempio utilizzeremo l’ambiente mainnet.Se non hai [un nodo guarda questo articolo](https://medium.com/@satoshiwantsyou/come-si-utilizza-un-nodo-bitcoin-ff0e0a785886)

Utilizzo il metodo **getnewaddress**:

```bash
$ bitcoin-cli getnewaddress “” “legacy”

1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU
```


Ottengo così un address P2PKH.

Il secondo parametro lasciato vuoto, rappresenta la label, utile per cercare un address particolare all’interno di Bitcoin core.

Per ispezionare più a fondo l’address ottenuto, è possibile utilizzare il metodo **getaddressinfo**:

```bash
$ bitcoin-cli getaddressinfo 1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU

{

“address”: “1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU”,

“scriptPubKey”: “76a9149917a0e372343fde946253d1c60c7f479925b1e288ac”,

“ismine”: true,

“solvable”: true,

“desc”: “pkh([5975a740/0'/0'/2']02413df2a3977bb663c4fc7418e7e004129c5cfc2d3d2bb6c9210ea8ee13769610)#wsy7apvp”,

“iswatchonly”: false,

“isscript”: false,

“iswitness”: false,

“pubkey”: “02413df2a3977bb663c4fc7418e7e004129c5cfc2d3d2bb6c9210ea8ee13769610”,

“iscompressed”: true,

“label”: “”,

“ischange”: false,

“timestamp”: 1588801569,

“hdkeypath”: “m/0'/0'/2'”,

“hdseedid”: “27eae26f0861d81dfde79537fdbb0b8273f00211”,

“hdmasterfingerprint”: “5975a740”,

“labels”: [

{

“name”: “”,

“purpose”: “receive”

}

]

}
```


il quale restituisce un pò di informazioni, tra cui la chiave pubblica compressa , la derivation path e lo scriptPubKey.

Nello **scriptPubKey** è possibile trovare lo script da soddisfare per sbloccare la UTXO di riferimento. Per **UTXO** si intente la Unspent transaction output.

Sfruttando un altro metodo messo a disposizione da Bitcoin core, possiamo approfondire ulteriormente lo script.

```bash
$ bitcoin-cli decodescript 76a9149917a0e372343fde946253d1c60c7f479925b1e288ac

{

“asm”: “OP_DUP OP_HASH160 9917a0e372343fde946253d1c60c7f479925b1e2 OP_EQUALVERIFY OP_CHECKSIG”,

“reqSigs”: 1,

“type”: “pubkeyhash”,

“addresses”: [

“1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU”

],

“p2sh”: “3Ae5soRJUqiqZgfvFxVaLTZs2PrdqvjDTL”,

“segwit”: {

“asm”: “0 9917a0e372343fde946253d1c60c7f479925b1e2”,

“hex”: “00149917a0e372343fde946253d1c60c7f479925b1e2”,

“reqSigs”: 1,

“type”: “witness_v0_keyhash”,

“addresses”: [

“bc1qnyt6pcmjxslaa9rz20guvrrlg7vjtv0ztsmjag”

],

“p2sh-segwit”: “3Mi5vTHySS8iCRpK2TWnTXsxU8FTDHQ3SQ”

}

}
```


Le informazioni che otteniamo sono molto interessanti.

Abbiamo i diversi tipi di address, quindi **P2SH**, **Wrapped Segwit** e **SegWit** nativo.

Alla prima riga abbiamo lo script **P2PKH**, **asm** significa assembly.

Le OP che si leggono sono le operation code del linguaggio script.

Ogni volta che si utilizza un **P2PKH**, Sarà effettuato **HASH160** sulla chiave pubblica il quale digest deve essere identico a quello della UTXO di riferimento.

Per questo prende il nome di **Public key hash**. Ovviamente poi viene verificata anche la firma grazie all’op code **OP_CHECKSIG**.

Come premesso all’inizio del video, l’address è il digest dello **SHA256** e del **RIPEMD160** della chiave pubblica compressa preceduta dal version prefix.

Nella wiki di [Bitcoin](https://en.bitcoin.it/wiki/List_of_address_prefixes) vediamo che per ottenere un address per l’ambiente mainnet dobbiamo utilizzare un byte di 0.

Quindi con l’aiuto di variabili d’ambiente, salvo il digest dello **SHA256** della chiave pubblica compressa all’interno della variabile d’ambiente **ADDR_SHA** 

```bash
$ ADDR_SHA=`printf 02413df2a3977bb663c4fc7418e7e004129c5cfc2d3d2bb6c9210ea8ee13769610 | xxd -r -p | openssl sha256| sed ‘s/^.* //’`
```


Utilizzo il **digest** appena ottenuto per ottenere il digest della funzione crittografica **ripemd160** 

```bash
$ ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed ‘s/^.* //’`
```


ed infine ottengo l’address, utilizzando **base58** comprensivo di checksum. **Base58** non è una funzione crittografica ma un encoding.

```bash
$ printf 00$ADDR_RIPEMD160 | xxd -p -r | base58 -c

1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU
```


Ottenendo l’address **mainnet**.

E qui la sfida, come ottengo l’address di testnet?

Chi posta (sul nostro [canale youtube](https://www.youtube.com/BitcoinInAction)) la risposta corretta per primo, riceve in omaggio il libro Bitcoin dalla teoria alla pratica!

Grazie a questo esempio abbiamo capito perchè **P2PKH** inizia con il numero 1.

Vi ricordo che il più veloce a rispondere al commento con la risposta esatta riceverà gratuitamente una copia di **Bitcoin dalla teoria alla pratica**, che copre molto più dettagliatamente la generazione dell’address.

Ciao alla prossima
