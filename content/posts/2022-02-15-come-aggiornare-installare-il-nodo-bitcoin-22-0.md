---
title: "Come aggiornare/installare il nodo Bitcoin 22.0"
date: 2022-02-15T10:00:00+01:00
slug: "come-aggiornare-installare-il-nodo-bitcoin-22-0"
draft: false
author: "Alessio Barnini"
description: "Ciao!
Oggi vediamo come aggiornare o installare il nodo Bitcoin versione 22.0.
Questa verisone porta diversi cambiamenti che potete leggere…"
cover: "/img/posts/come-aggiornare-installare-il-nodo-bitcoin-22-0-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Hash"
categories:
  - "Bitcoin"
---

---

### Come aggiornare/installare il nodo Bitcoin 22.0

Ciao! 
Oggi vediamo come aggiornare o installare il nodo Bitcoin versione 22.0. 
Questa verisone porta diversi cambiamenti che potete leggere nel change log relativo [https://bitcoin.org/en/releases/22.0/](https://bitcoin.org/en/releases/22.0/)

In questo articolo ci concentriamo sull’aggiornamento di un nodo su OSX, lo stesso che abbiamo utilizzato nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)](https://amzn.to/3pJcXj1).

Per aggiornarlo in altri sistemi operativi sarà sufficiente cambiare il pacchetto da scaricare.

Aggiorneremo il nodo direttamente da terminale, perchè? 
Così se avete la necessità di aggiornare un nodo [raspberry](/posts/come-avere-un-fullnode-bitcoin-con-raspberry-pi/), avete una traccia da seguire.

![Cliccami per un nodo su raspberry](/img/posts/come-aggiornare-installare-il-nodo-bitcoin-22-0-1.webp)
*Cliccami per un nodo su raspberry*

Per praticità utilizzo due variabili d’ambiente, cosi che questo tutorial possa avere lunga vita!

```bash
$ VERSION=22.0

$ SO=osx64
```


Il passo successivo è scaricare il pacchetto desiderato.

```bash
wget https://bitcoincore.org/bin/bitcoin-core-$VERSION/bitcoin-$VERSION-$SO.tar.gz
```


Scarico i relativi SHA256 dei pacchetti che mi serviranno a verificare l’integrità del pacchetto che ho scaricato

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-$VERSION/SHA256SUMS
```


Scarico le firme PGP

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-$VERSION/SHA256SUMS.asc
```


Successivamente le importo e verifo le firme sul pacchetto scaricato

```bash
$ gpg --verify SHA256SUMS.asc SHA256SUMS
```


Posso finalmente scompattare l’archivio

```bash
$ tar -xvf bitcoin-$VERSION-$SO.tar.gz
```


Sposto i file all’interno di un percorso eseguibile, in questo caso /usr/local/bin/ Se vuoi conoscere i percorsi eseguibili: echo $PATH

```bash
$ sudo cp bitcoin-$VERSION/bin/bitcoin* /usr/local/bin/.
```


Se tutto è andato a buon fine, dovresti vedere la nuova versione scaricata utilizzando il comando:

```bash
$ bitcoind -versionBitcoin Core version v22.0.0
```


Per sapere il percorso del tuo demone

```bash
$ which bitcoind/usr/local/bin/bitcoind
```


Non ti resta che avviare nuovamente demone

```bash
bitcoind
```


![Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)](/img/posts/come-aggiornare-installare-il-nodo-bitcoin-22-0-2.webp)
*Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)*



