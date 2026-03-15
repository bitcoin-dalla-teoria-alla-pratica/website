---
title: "Da dove inizio per imparare Bitcoin?"
date: 2020-01-20T10:00:00+01:00
slug: "da-dove-inizio-per-imparare-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Regtest, la blockchain locale"
cover: "/img/posts/da-dove-inizio-per-imparare-bitcoin-1.webp"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Da dove inizio per imparare Bitcoin?

#### Regtest, la blockchain locale

Molte persone vorrebbero imparare a utilizzare il protocollo Bitcoin, oppure vorrebbero aumentare la propria conoscenza e non sanno da dove iniziare.

Noi siamo sempre stati convinti che per capire realmente una qualsiasi tecnologia dobbiamo metterla in pratica.

Abbiamo già scritto una guida per permettere di sincronizzare l’intera blockchain in un dispositivo esterno come [Raspberry](/posts/come-avere-un-fullnode-bitcoin-con-raspberry-pi/), ma per prove più “quick and dirty” vi consigliamo di utilizzare la [**regtest**](https://bitcoin.org/en/glossary/regression-test-mode).

![La sandbox, dove puoi fare le tue prove senza farti male :)](/img/posts/da-dove-inizio-per-imparare-bitcoin-2.webp)
*La sandbox, dove puoi fare le tue prove senza farti male :)*

Che cosa è la regtest? 
Potremo definire la regtest la **blockchain locale**. 
È il punto di partenza per sviluppare applicazioni basate su blockchain e/o per iniziare a studiarla.  
Se sei uno sviluppatore questo non ti dovrebbe sorprendere, solitamente abbiamo 4 ambienti durante lo sviluppo di una qualsiasi applicazione, locale, dev, staging, prod.

Quindi possiamo replicare l’ambiente di produzione Bitcoin sul proprio computer, compreso il lavoro sporco del miner.  
Stai calmo, i bitcoin che mini non valgono niente! 
 
Ecco come fare. 
Scarica l’ultima versione di Bitcoin demon. (ad oggi 0.19.0.1)

```bash
$ curl -O https://bitcoin.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-osx64.tar.gz
```


Per prima cosa verifichiamo che il checksum ottenuto con l’algoritmo SHA256 sul pacchetto *tar* appena scaricato sia fedele a quello che troviamo all’interno di SHA256SUM.ASC, così da essere sicuri di aver scaricato il pacchetto desiderato.

```bash
$ sha256sum --check SHA256SUMS.asc --ignore-missing
```


risultato:

```bash
bitcoin-0.19.0.1-osx64.tar.gz: OKsha256sum: WARNING: 20 lines are improperly formatted
```


*NB: tutti i file e i comandi sono eseguiti all’interno della stessa cartella.*

Scarichiamo anche le relative firme per verificare l’integrità del pacchetto.

> [Se non sei pratico di PGP, guarda questo articolo!](/posts/pretty-good-privacy/)

```python
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc$ wget https://bitcoin.org/laanwj-releases.asc$ gpg --import laanwj-releases.asc$ gpg --verify SHA256SUMS.asc

gpg: Signature made Sun Nov 24 10:14:42 2019 CET

gpg:using RSA key 90C8019E36C2E964
```


```sql
gpg: Good signature from "Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>" [unknown]
```


Adesso che siamo sicuri di aver scaricato il pacchetto giusto, possiamo estrarlo con il comando

Estraiamo quindi il pacchetto che abbiamo scaricato:

```bash
$ tar -xvf bitcoin-0.19.0.1-osx64.tar.gz
```


e spostare l’eseguibili nel percorso $PATH di default.

```bash
$ sudo mkdir -p /usr/local/bin$ sudo cp bitcoin-0.19.0.1/bin/bitcoin* /usr/local/bin/.
```


In questo modo potremo richiamare il demone e il client Bitcoin da qualsiasi percorso, così da evitare di inserire il percorso assoluto o relativo dell’eseguibile.

Per verificare che tutto sia corretto, potete lanciare il comando.

```bash
$ bitcoind --versionBitcoin Core version v0.19.0.1
```


Se volete verificare il percorso del vostro demone potete utilizzare il comando [**which**](https://www.geeksforgeeks.org/which-command-in-linux-with-examples/).

```bash
$ which bitcoind/usr/local/bin/bitcoind
```


Ok, siamo pronti per lanciare il nostro demone e utilizzare la regtest. 
per farlo è sufficiente passare come parametro **-regtest**.

```bash
$ bitcoind -regtest
```


Otteniamo cosi un pò di output, ovvero il log del nostro nodo. 
In un altra finestra del terminale possiamo iniziare ad utilizzarlo tramite il client che abbiamo già spostato precedentemente nel percorso $PATH.

```bash
$ bitcoin-cli -regtest getblockcount0
```


Come vedete non abbiamo nessun blocco, infatti la blockchain è “vergine”. 
Dove viene salvata la blockchain?  
Per il sistema operativo OSX la puoi trovare nel percorso:

```bash
~/Library/Application Support/Bitcoin/
```


Per linux e windows, vi rimando alla pagina wiki di riferimento. 
[https://en.bitcoin.it/wiki/Data_directory](https://en.bitcoin.it/wiki/Data_directory).

Adesso con il comando:

```bash
$ bitcoin-cli help
```


Hai la lista di comandi da utilizzare per iniziare a divertirti!

Con questo piccolo tutorial puoi anche seguire il nostro libro [Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica) disponibile sia su [Amazon](https://amzn.to/2MOj1av) sia sul nostro [sito ufficiale corsobitcoin.com.](prodotti/bitcoin-dalla-teoria-alla-pratica)

![Bitcoin dalla teoria alla pratica](/img/posts/da-dove-inizio-per-imparare-bitcoin-1.webp)
*Bitcoin dalla teoria alla pratica*
