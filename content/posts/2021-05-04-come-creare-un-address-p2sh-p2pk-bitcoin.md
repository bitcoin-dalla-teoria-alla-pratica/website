---
title: "Come creare un address P2SH–P2PK Bitcoin"
date: 2021-05-04T10:00:00+01:00
slug: "come-creare-un-address-p2sh-p2pk-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Pay To Script Hash — Pay To Public Key"
cover: "/img/posts/come-creare-un-address-p2sh-p2pk-bitcoin-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

#### Pay To Script Hash — Pay To Public Key

![Come creare un address P2SH–P2PK](/img/posts/come-creare-un-address-p2sh-p2pk-bitcoin-1.webp)
*Come creare un address P2SH–P2PK*

Nell’[articolo precedente](https://bitcoin-in-action.medium.com/come-si-ottiene-address-bitcoin-p2sh-f009f28206b7) abbiamo analizzato ad alto livello come è costruito l’address P2SH, che cosa è il redeem script, che cosa è il redeem script hash e dove è posizionato per la generazione dell’address.

In questo articolo andiamo più nel dettaglio ed iniziamo a mettere il primo mattoncino per la generazione di un address P2SH-P2PK

Il nostro compitò sarà quindi quello di creare un **redeem script** che conterrà la **logica del P2PK** *classico*, il primo address che abbiamo analizzato in [questa playlist](https://www.youtube.com/playlist?list=PLpPLK7SGHncZVl_ZQkqyXGMDGWEx7U_et).

Il codice che stiamo per mostrare lo potete trovare nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/) e di conseguenza nel nostro GitHub di riferimento.

![Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](/img/posts/come-creare-un-address-p2sh-p2pk-bitcoin-2.webp)
*Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts*

Quindi andiamo a vedere con la pratica come è possibile creare un address P2SH-P2PK

#### In Action

Al momento non è possibile creare questo tipo di address da Bitcoin-core in quanto si preferisce utilizzare **P2SH-SegWit**, ma è comunque indispensabile per capire il corretto funzionamento.

Tralasciamo la generazione delle chiavi pubblica e privata e soffermiamoci alla costruzione del **redeem script**.

Come vedete per questo esempio utilizzo direttamente il libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/).

```bash
$ cat compressed_public_key_1.txt
```


Partendo da questa chiave pubblica andiamo a creare il **redeem script**, che sarà formato dalla **chiave pubblica** e dall’operation code **OP_CHECKSIG**, proprio come un normale P2PK.

```bash
PBLENGTH=$(char2hex.sh $(cat compressed_public_key_1.txt | wc -c))

#P2PK Script#PB LENGTH - PB - OP_CHECKSIG

SCRIPT=$PBLENGTH$(cat compressed_public_key_1.txt)"AC"

printf $SCRIPT > redeem_script.txt
```


Abbiamo quindi creato il Redeem script che contiene la la chiave pubblica, la sua relativa lunghezza e l’operation code **OP_CHECKSIG** rappresentato dall’esadeciamle **AC** Successivamente creiamo parte del scriptPubKey, ovvero il redeem script hash, ottenuto applicando le funzioni crittografiche **SHA256** e **RIPEMD160**.

```bash
#---------- scriptPubKey ---------

ADDR_SHA=`printf $SCRIPT | xxd -r -p | openssl sha256| sed 's/^.* //'`

ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed 's/^.* //'`

printf $ADDR_RIPEMD160 > scriptPubKey.txt
```


Il digest del redeem script lo troveremo nello scriptPubKey, come avremo modo di vedere successivamente. 
Ed infine applichiamo il version prefix e il base58 checksum, ottenendo così l’address P2SH-P2PK

```bash
#ADDRESS

VERSION_PREFIX_ADDRESS=C4

ADDR=`printf $VERSION_PREFIX_ADDRESS$ADDR_RIPEMD160 | xxd -p -r | base58 -c`

echo $ADDR > address_P2SH.txt
```


Avviando il nostro script possiamo verificare l’address il redeem script utilizzando il comando cat.

Possiamo verificare il nostro redeem script.

```bash
$ cat redeem_script.txt

210250a1991342dd7f57792df122baa02c6a5c98aa8daeb8e106ae7d2345d020f082AC
```


Il nostro scriptPubKey, o redeem script Hash

```bash
$ cat scriptPubKey.txt

3647d6bf3fb8e75f26f15888a471808cb4253afb
```


e il nostro address:

```bash
$ cat address_P2SH.txt

---------- 🔑 ADDRESS P2SH ---------

2MxCEY6QTacDQhHFx9rmNeXkpfXEQ17xZQM
```


Utilizzando il comando decodescript sul redeem script possiamo analizzare il nostro redeem script in formato assembly:

```bash
bitcoin-cli decodescript $(cat redeem_script.txt)

{

"asm": "02329013c3c2c6bd4a5b1597b008a1ce6e750aa43cf8d2e509e8497bc491c6cb64 OP_CHECKSIG",

"type": "pubkey",

"p2sh": "2MxWUqeZaaBgKyNMxx9PzLJywr8LqkRUUor",

"segwit": {

"asm": "0 83e34929132fffbdcffe251c289b68fb178fda06",

"hex": "001483e34929132fffbdcffe251c289b68fb178fda06",

"reqSigs": 1,

"type": "witness_v0_keyhash",

"addresses": [

  "bcrt1qs035j2gn9llmmnl7y5wz3xmglvtclksx2j0yk6"

],

"p2sh-segwit": "2N7G1k7HomEQA8GZemXQQN3JLRPUDY75Keq"

}

}
```


Nel prossimo articolo vedremo come è costruita una transazione!

Ciao alla prossima!



