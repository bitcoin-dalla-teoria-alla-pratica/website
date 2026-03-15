---
title: "Due nodi Bitcoin sullo stesso computer."
date: 2020-02-11T10:00:00+01:00
slug: "due-nodi-bitcoin-sullo-stesso-computer"
draft: false
author: "Alessio Barnini"
description: "Non essere asociale."
cover: "https://cdn-images-1.medium.com/max/1200/1*mJwJypYxRp-ooQl_NZKhsw.png"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Hash"
categories:
  - "Bitcoin"
---

---

#### Non essere asociale.

Durante lo studio di [**Bitcoin dalla teoria alla pratica**](prodotti/bitcoin-dalla-teoria-alla-pratica) e il [relativo video-corso](https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13) abbiamo fatto un pò di esperimenti.

Uno di questi è far comunicare due o più nodi sullo stesso computer.

Facendo riferimento all’articolo [precedente](https://medium.com/@bitcoindallateoriallapratica/tutorial-creare-una-transazione-in-bitcoin-467c94fad754?source=---------2------------------), utilizziamo un nuovo demone e cerchiamo di farli comunicare.

Sappiamo che di default le porte del demone di Bitcoin sono **18444** e la **18443**, per quanto riguarda l’ambiente di **regtest**.

```bash
Ambiente: Porta - Porta RPC

Mainnet:8333 - 8332Testnet:18333 - 18332Regtest:18444 - 18443
```

Quello che dobbiamo fare è creare un altro file di configurazione per il **secondo nodo** con un **datadir** differente e far comunicare i due nodi.

Passiamo alla action!

---

Questo è il mio percorso dove mi posizionerò

```bash
$ pwd

/Users/barno/Documents/bizantino
```

Al suo interno ho due cartelle, una un collegamento alla cartella di default di Bitcoin e l’altra è una cartella vuota pronta ad ospitare il secondo nodo.

```bash
$ ls -l

total 0

lrwxr-xr-x 1 barno staff 48 Jan 13 16:30 Bitcoin -> /Users/barno/Library/Application Support/Bitcoin

drwxr-xr-x 4 barno staff 128 Jan 13 17:23 Bitcoin_2
```

All’interno della cartella **Bitcoin_2** creo un file **bitcoin_nodo2.conf** e inserisco questa configurazione.

```bash
datadir=/Users/barno/Documents/bizantino/Bitcoin_2

debug=1

regtest=1

# Options only for mainnet

[main]

# Options only for testnet

[test]

# Options only for regtest

[regtest]

port=28444

rpcport=28443

addnode=localhost:18444
```

Come vedete sono stati cambiati la **porta** e la **rpcport**.  
Senza il file di configurazione sarebbe stato molto più prolisso e soggetto ad errori, come si può vedere dall’esempio sotto.

```bash
bitcoind -datadir=$PWD/regtest2 -regtest -debug=1 -rpcport=28443 -port=28444 -addnode=localhost:18444
```

Per avere informazioni sui parametri da utilizzare, potete sempre utilizzare **bitcoind -help** ---

![Le porte utilizzabili.](https://cdn-images-1.medium.com/max/1200/1*FT9Rm6eZoiAv6702qzWMtA.png)
*Le porte utilizzabili.*

- **-port** Listen for connections on < **port** > (default: 8333, testnet: 18333, 18444 regtest)
- **-rpcport** Listen for JSON-RPC connections on <port> (default: 8332, testnet: 18332, regtest: 18443)
- **-conf** =<file> Specify configuration file. Relative paths will be prefixed by datadir location. (default: bitcoin.conf)
- **-connect** =<ip> 
Connect only to the specified node; -noconnect disables automatic 
connections (the rules for this peer are the same as for 
-addnode). This option can be specified multiple times to connect 
to multiple nodes.

---

Passeremo al secondo nodo l’informazione necessaria per caricare il file di configurazione desiderato.

```bash
-conf=/Users/barno/Documents/bizantino/Bitcoin_2/bitcoin_nodo2.conf
```

avremo a disposizione due nodi sullo stesso computer.

> questo percorso sarà diverso nel vostro computer /Users/barno/Documents/bizantino/Bitcoin_2.

Lanciamo quindi il demone di *default *(quello che abbiamo configurato nel precedente [tutorial](https://medium.com/@bitcoindallateoriallapratica/tutorial-creare-una-transazione-in-bitcoin-467c94fad754?source=---------2------------------)) e il secondo demone

```bash
$ bitcoind $ bitcoind -conf=$PWD/bitcoin_nodo2.conf
```

*NB: utilizzo $PWD perchè sono nella stessa cartella del file bitcoin_nodo2.conf.* 
Per utilizzare il client del secondo demone devo passare sempre il parametro

```bash
-conf
```

Ehi vi vedete?

```bash
$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getconnectioncount1
```

Sì si vedono, infatti il comando che conta le connessioni ha come risultato 1! 
Adesso facciamo la grande prova, miniamo 101 blocchi sul nodo di default e verifichiamo se sul nodo 2 sono visibili.

Per prima cosa dobbiamo ottenere un address nel nodo di default.

```bash
$ ADDR=`bitcoin-cli getnewaddress`
```

Lo salvo direttamente nella variabile d’ambiente **ADDR** così da agevolare la scrittura dei comandi successivi.

Per visualizzare il valore di $ADDR, possiamo utilizzare **echo** 

```bash
$ echo $ADDR

2N6yRwpVGdFsD1gBBhGTE8ijVmNwiVz6myZ
```

Miniamo!

```bash
$ bitcoin-cli generatetoaddress 101 $ADDR
```

Otteniamo così un output molto corposo, ovvero 101 block header hash. 
Per verificare che i blocchi si siano propagati correttamente, conto il numero di blocchi sul secondo nodo.

```bash
$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getblockcount

101
```

Si! Stanno parlando e sono perfettamente sincronizzati.  
Dove sono salvate le relative blockchain? 
Nel demone di default troviamo i blocchi nel percorso predefinito:

```bash
/Users/barno/Library/Application Support/Bitcoin/regtest
```

Il secondo demone utilizza la -datadir specificata nel file di conf.

```bash
/Users/barno/Documents/bizantino/Bitcoin_2/regtest
```

Potrebbe essere interessante iniziare a fare delle transazioni tra due nodi? 
Direi di si!

![Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*mJwJypYxRp-ooQl_NZKhsw.png)
*Bitcoin dalla teoria alla pratica*
