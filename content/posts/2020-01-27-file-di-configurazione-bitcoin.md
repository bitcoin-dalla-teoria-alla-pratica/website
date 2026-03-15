---
title: "File di configurazione Bitcoin"
date: 2020-01-27T10:00:00+01:00
slug: "file-di-configurazione-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Cerchiamo di mantenere pulito"
cover: "/img/posts/file-di-configurazione-bitcoin-1.webp"
tags:
  - "Bitcoin"
  - "Nodi"
categories:
  - "Bitcoin"
---

---

#### Cerchiamo di mantenere pulito

Nell’[articolo precedente](https://medium.com/@bitcoindallateoriallapratica/da-dove-inizio-per-imparare-bitcoin-e103dc219eec?source=your_stories_page---------------------------) abbiamo installato il nodo Bitcoin sul proprio computer e abbiamo passato come parametro -regtest per interagire in locale.

Un parametro non è cosi scomodo da passare ogni volta che vogliamo fare delle chiamate, ma quando il comando da eseguire diventa

```bash
bitcoind -datadir=$PWD/regtest2 -regtest -debug=1 -rpcport=28443 -port=28444 -addnode=localhost:18444
```


non è il massimo.

Fortunatamente possiamo utilizzare un file di configurazione per gestire uno o più nodi sullo stesso computer.

Nel repository ufficiale Bitcoin possiamo trovare un esempio di file di [configurazione](https://github.com/bitcoin/bitcoin/blob/master/share/examples/bitcoin.conf).

Degno di nota anche questo [link](https://jlopp.github.io/bitcoin-core-config-generator/) che ti aiuta a crearlo realtime.

Di default il nodo Bitcoin effettua una ricerca del file **bitcoin.conf** nella [datadir di default](https://en.bitcoin.it/wiki/Data_directory). Nel Mac è **~/Library/Application Support/Bitcoin**.

Così, creando il file **bitcoin.conf** all’interno della cartella di default possiamo impostare il parametro regtest senza doverlo passare come parametro.

```bash
regtest=1# Options only for mainnet

[main]# Options only for testnet

[test]# Options only for regtest

[regtest]
```


Adesso possiamo utilizzare il client senza passare nessun parametro.

```bash
$ bitcoin-cli getblockcount

0
```


Otteniamo lo stesso risultato del [tutorial precedente](https://medium.com/@bitcoindallateoriallapratica/da-dove-inizio-per-imparare-bitcoin-e103dc219eec?source=your_stories_page---------------------------).

Nel prossimo tutorial vedremo come far comunicare due o più nodi sullo stesso computer!

![configurazione base per bitcoin.conf](/img/posts/file-di-configurazione-bitcoin-1.webp)
*configurazione base per bitcoin.conf*
