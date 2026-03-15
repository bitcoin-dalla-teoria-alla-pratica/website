---
title: "Bitcoin Core Gui Vs Cli ⚔️"
date: 2020-12-10T10:00:00+01:00
slug: "bitcoin-core-gui-vs-cli"
draft: false
author: "Alessio Barnini"
description: "Vantaggi e svantaggi."
cover: "/img/posts/bitcoin-core-gui-vs-cli-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

### **Bitcoin Core Gui Vs Cli** ⚔️

#### Vantaggi e svantaggi.

![](/img/posts/bitcoin-core-gui-vs-cli-1.webp)

Ciao,

Oggi rispondiamo a Roberto che durante una nostra chiacchierata mi ha suggerito di far vedere la GUI di bitcoin-core.

Non avevo mai utilizzato la parte grafica, ma mi rendo conto che alcune persone potrebbero preferire la GUI.

> L’ **interfaccia grafica**, nota anche come **GUI** (dall’[inglese](https://it.wikipedia.org/wiki/Lingua_inglese) *Graphical User Interface*), in [informatica](https://it.wikipedia.org/wiki/Informatica) è un tipo di [interfaccia utente](https://it.wikipedia.org/wiki/Interfaccia_utente) che consente l’[interazione uomo-macchina](https://it.wikipedia.org/wiki/Interazione_uomo-computer) in modo visuale utilizzando rappresentazioni grafiche

Tuttavia il mio consiglio è quello di prendere confidenza con il terminale, perchè se installiamo, ad esempio, un nodo su un [raspberry](https://bitcoin-in-action.medium.com/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f?source=your_stories_page-------------------------------------) molto probabilmente ci connetteremo in SSH.

In questo articolo metteremo in comunicazione la GUI e la riga di comando, così da creare una mini blockchain sul nostro computer.  
Per questo esempio utilizzeremo la regtest.

#### In Action

Ho già installato il nodo sul mio computer, se hai bisogno di installare bitcoin-core, fai riferimento a [questo video](https://youtu.be/dyFDDH0IOnU).

Prima di avviare Bitcoin-core, specifico di voler utilizzare la **regtest**. Mi sposto nella cartella di default del mac e creo o modifico il file di configurazione.  
Se voi non avete la cartella di default Bitcoin, potete crearla, il percorso predefinito del mac è:

```bash
$ cd $HOME/Library/Application\ Support/Bitcoin
```

Per gli altri sistemi operativi, fare rifermineto [alla wiki di Bitcoin](https://en.bitcoin.it/wiki/Data_directory).

Di seguito è riportata la configurazione del mio nodo:

```bash
regtest=1

daemon=1

txindex=1

# Options only for mainnet

[main]

# Options only for testnet

[test]

# Options only for regtest

[regtest]
```

Eliminiamo la cartella regtest, se esiste, così da partire da una blockchain vuota. Avviamo quindi Bitcoin-core versione grafica.  
Io per farlo digito:

```bash
$ bitcoin-qt
```

Dato che ho spostato l’eseguibile nel mio file $PATH. Se non sai come fare, guarda [questo video](https://youtu.be/keeEdwPigZs)

![Bitcoin Core](/img/posts/bitcoin-core-gui-vs-cli-2.webp)
*Bitcoin Core*

La regtest è vuota, quindi la blockchain contiene un solo blocco, il **genesis block**.  
Otteniamo le sue informazioni, così da prendere confidenza con la GUI. Selezionando Window -> console, si aprirà una nuova finestra nella quale abbiamo la possibilità di eseguire dei comandi.

![Bitcoin Core – Window Console](https://cdn-images-1.medium.com/max/1200/1*75XsDPoLery9oj6ug-DfEw.png)
*Bitcoin Core – Window Console*

Digitando **help** abbiamo tutta la lista del comandi. 
Utilizzando **getblockhash 0** abbiamo la possibilità di ottenere l’hash del blocco genesi, e con il comando **getblock 0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206** possiamo analizzarlo.

![Bitcoin-Core — Genesis Block](https://cdn-images-1.medium.com/max/1200/1*mk5EaHjWlJ-3HYLOfglMgg.png)
*Bitcoin-Core — Genesis Block*

Tutto molto simile alla versione bash ovviamente. L’unica differenza degna di nota è che si omette il comando **bitcoin-cli**. 
Avviamo un secondo nodo, questa volta da terminale. Per prima cosa creo un’altra cartella sempre nel percorso di default, che chiamerò **regtest-cli**.

```bash
$ mkdir regtest-cli
```

Questa cartella ospiterà la blockchain e tutti i dati del **secondo nodo**. 
Per avviarlo abbiamo bisogno di creare un’altro file di configurazione nel quale dichiariamo la **datadir**, le **porte** differenti, e aggiungeremo l’ip e la porta del nodo con l’interfaccia grafica.

Creo quindi un file con il nome bitcoin.conf_2 con questa configurazione:

```bash
regtest=1

datadir=/Users/barno/Documents/Bitcoin-in-action-book/Bitcoin/regtest-cli

# Options only for mainnet

[main]

# Options only for testnet

[test]

# Options only for regtest

[regtest]

daemon=1

rpcport=28443

port=28444

addnode=localhost:18444
```

> Le porte di default della regtest sono 18444 e 18443 che al momento sono occupate dalla versione grafica.

Avviamo il demone bash

```bash
$ bitcoind --conf=bitcoin.conf_2
```

Appena avviamo, vediamo che nell’interfaccia grafica si ha un nodo collegato.

![Bitcoin-core GUI con un nodo collegato](https://cdn-images-1.medium.com/max/1200/1*0DPzLULK8dYnx1cDYME7kg.png)
*Bitcoin-core GUI con un nodo collegato*

Siamo noi!

Verifichiamo a quanti nodi siamo connessi con il demone da riga di comando, che da questo momento chiameremo **nodo2**.

```bash
$ bitcoin-cli —-conf=bitcoin.conf_2 getconnectioncount

1
```

Siamo connessi a un nodo, alla GUI.

Possiamo ottenere più informazioni del nodo aggiunto con **addnode** con il comando **getaddednodeinfo**.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getaddednodeinfo

[

{

"addednode": "localhost:18444",

"connected": true,

"addresses": [

{

"address": "[::1]:18444",

"connected": "outbound"

}

]

}

]
```

Ma come funziona il bootstrap di un nodo Bitcoin? Nella modalità mainnet i nodi si collegano ad altri nodi con questa logica:

- Address database (peers.dat)
- User-specified (-addnode and -connect)
- DNS seeding
- Hard-coded seeds
- From other peers (“getaddr” and “addr” messages)

Quindi prendono gli indirizzi dei nodi dal file peers.dat, successivamente verificano se ci sono dei nodi specificati dall’utente, proprio come abbiamo fatto noi, e, se i peers falliscono, si connettono a dei [DNS](https://github.com/bitcoin/bitcoin/blob/1e17114917f29da114cb90f52579ddb911a1a856/src/chainparams.cpp#L121) e a dei seeds [hardcodati nel codice](https://github.com/bitcoin/bitcoin/blob/d4159984c360001d9469fd54512bf0da4b02c4fd/src/chainparamsseeds.h).

Miniamo 211 blocchi dal nodo2.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 generatetoaddress 211 $(bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "" "bech32") >> /dev/null
```

Per sapere quanti blocchi contiene la blockchain possiamo utilizzare la chiamata getblockcount

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getblockcount

211
```

Il risultato che otteniamo è 211. Come posso verificare che la GUI sia *syncata*?

Utilizzando Window->information troviamo una schermata che ci comunica i blocchi, che anche in questo caso risultano essere 211.

![Bitcoin-core Syncata](https://cdn-images-1.medium.com/max/1200/1*GnPUqKWsanXVEt3ylPhy6w.png)
*Bitcoin-core Syncata*

Torniamo nel nodo2 e creiamo una transazione. Per prima cosa verifico il saldo con la chiamata getwalletinfo.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getwalletinfo

{

"walletname": "",

"walletversion": 169900,

"balance": 5550.00000000,

"unconfirmed_balance": 0.00000000,

"immature_balance": 3450.00000000,

"txcount": 211,

"keypoololdest": 1606752619,

"keypoolsize": 999,

"keypoolsize_hd_internal": 1000,

"paytxfee": 0.00000000,

"hdseedid": "50aacc53d11feb46bf8a159d1fb4fdb0ecc18e06",

"private_keys_enabled": true,

"avoid_reuse": false,

"scanning": false

}
```

La chiamata restituisce anche i bitcoin *non maturi*, ovvero quelli che non hanno ancora passato la [coinbase_maturity, ovvero 101 conferme](https://github.com/bitcoin/bitcoin/blob/78dae8caccd82cfbfd76557f1fb7d7557c7b5edb/src/consensus/consensus.h#L19).

Per avere il balance confermato, possiamo utilizzare la chiamata **getbalance**.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getbalance

5550.00000000
```

Inviamo 1 bitcoin all’address del nodo GUI, per prima cosa ottengo un nuovo address.

![Ottengo l’address dal nodo GUI](https://cdn-images-1.medium.com/max/1200/1*3vxv5fXtQaybWuDRCzMsSA.png)
*Ottengo l’address dal nodo GUI*

Seleziono **receive** e clicco create a *new receive address*. Il software mi restituisce un address SegWit nativo.  
Quale è stato il comando che ha eseguito? È stato **getnewaddres**. Replichiamolo nel nodo2.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "" "bech32"

bcrt1qg887l3jc0q3wmn9ldwtamn5cqhz63gyw4vy84g
```

Ed ecco ottenuto l’address anche con il nodo2, che ovviamente è diverso dal nodo GUI.

Inviamo quindi 1 bitcoin dal nodo2 al nodo GUI, utilizzando il metodo **sendtoaddress**, il quale ha il compito di aggregare per noi le UTXO fino ad arrivare all’importo desiderato impostando automaticamente le fees.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 sendtoaddress bcrt1qfak36m9lmm3uup9s4v2rkd0yeld7vgz9q6fvld 1

dde7dc0f4dca1c83fc86ac64a1c5522ecfeedb8f9c64bc013bf4cffce52cf4b7
```

La transazione è stata inviata, quindi adesso si trova nella **mempool**. Nella GUI, nella sezione transaction, possiamo verificare tutte le informazioni della transazione.

![Bitcoin Core — Mempool](/img/posts/bitcoin-core-gui-vs-cli-8.webp)
*Bitcoin Core — Mempool*

Come è possibile ottenere le stesse informazioni dal nodo2? Utilizzando la chiamata **getrawtransaction** specificando una risultato più verboso, utilizzando la **txid** ottenuta dalla chiamata sendtoaddress.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getrawtransaction dde7dc0f4dca1c83fc86ac64a1c5522ecfeedb8f9c64bc013bf4cffce52cf4b7 2

{

"txid": "dde7dc0f4dca1c83fc86ac64a1c5522ecfeedb8f9c64bc013bf4cffce52cf4b7",

"hash": "cd43d5f44c108b6ccad6649929bfd5c616d22082310a7dff4c5998d1b2052be7",

"version": 2,

"size": 222,

"vsize": 141,

"weight": 561,

"locktime": 211,

"vin": [

{

"txid": "fb75baa7271a6c0c30002ba8587df3370aed4192c6ecd25a65a2f3ec36802033",

"vout": 0,

"scriptSig": {

"asm": "",

"hex": ""

},

"txinwitness": [

"304402200e6705b7ddb830422aee5b300a02b34bb46330698e0cd462220c190b0526e6e70220620f13fcbd17de115517a047e5b8c5c5b88b39aba4873af79af2dffc0cdaec7101",

"039434ddae8e96297683ff1117935682bfea0d4b7725ee037c3aa323cb04711a53"

],

"sequence": 4294967294

}

],

"vout": [

{

"value": 1.00000000,

"n": 0,

"scriptPubKey": {

"asm": "0 4f6d1d6cbfdee3ce04b0ab143b35e4cfdbe62045",

"hex": "00144f6d1d6cbfdee3ce04b0ab143b35e4cfdbe62045",

"reqSigs": 1,

"type": "witness_v0_keyhash",

"addresses": [

"bcrt1qfak36m9lmm3uup9s4v2rkd0yeld7vgz9q6fvld"

]

}

},

{

"value": 48.99997180,

"n": 1,

"scriptPubKey": {

"asm": "0 8e54cf6eaefcd27c9297ed512ec3e6e0901287b1",

"hex": "00148e54cf6eaefcd27c9297ed512ec3e6e0901287b1",

"reqSigs": 1,

"type": "witness_v0_keyhash",

"addresses": [

"bcrt1q3e2v7m4wlnf8ey5ha4gjaslxuzgp9pa3mce9ja"

]

}

}

],

"hex": "0200000000010133208036ecf3a2655ad2ecc69241ed0a37f37d58a82b00300c6c1a27a7ba75fb0000000000feffffff0200e1f505000000001600144f6d1d6cbfdee3ce04b0ab143b35e4cfdbe62045fc051024010000001600148e54cf6eaefcd27c9297ed512ec3e6e0901287b10247304402200e6705b7ddb830422aee5b300a02b34bb46330698e0cd462220c190b0526e6e70220620f13fcbd17de115517a047e5b8c5c5b88b39aba4873af79af2dffc0cdaec710121039434ddae8e96297683ff1117935682bfea0d4b7725ee037c3aa323cb04711a53d3000000"

}
```

Questa chiamata restituisce molte più informazioni, nella GUI sono riportate solo quelle di interesse.

Che cosa ci resta da fare? Minare dei blocchi! Utilizziamo la GUI per questo.

Prima otteniamo un altro indirizzo.

![Bitcoin Core — Indirizzo Miner](https://cdn-images-1.medium.com/max/1200/1*xvTcHcEfZMABcWVX43qkYA.png)
*Bitcoin Core — Indirizzo Miner*

Questo indirizzo sarà il nostro miner. **bcrt1qcad9r6cn037p3una2fum7v5jwgc2zgm8ssw7un** Utilizziamo ancora la console della GUI. Miniamo 10 blocchi con il comando **generatetoaddress**.

![](https://cdn-images-1.medium.com/max/1200/1*YlB_EouKjkXK1RzQk7bv9g.png)

![Bitcoin Core — 10 blocchi minati](/img/posts/bitcoin-core-gui-vs-cli-11.webp)
*Bitcoin Core — 10 blocchi minati*

Abbiamo minato 10 blocchi! Adesso mi aspetto di vedere il la transazione fatta dal nodo2 confermata!

![Bitcoin Core — Transazione Confermata](https://cdn-images-1.medium.com/max/1200/1*LpdkvHi-vt1q04oOVy0ENQ.png)
*Bitcoin Core — Transazione Confermata*

Esatto! la prima transazione è stata minata e ha 10 conferme.

Nella schermata vediamo altri blocchi minati con dei reward.

Nel primo blocco vediamo un reward un pò più *corposo*, perchè? Perchè è il blocco che contiene la nostra transazione.

Ricorda che il **reward** del miner è composta, dal reward impostato dal protocollo che cambia ogni 210.000 blocchi e dalle fees.

Perchè qui non abbiamo 50 bitcoin di reward? In regtest l’halving non avviene ogni 210.000 blocchi. Per saperne di più guarda [questo video](https://youtu.be/nFrN-jROnMI).

Facciamo anche l’operazione inversa, inviamo 0.5 bitcoin dalla GUI al nodo2.

Otteniamo un address dal nodo2, aggiungiamo anche una label. Io aggiungerò “barno”.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "barno" "bech32"

bcrt1qtc00wzrcae86rvyacanwd5l9t6fek4h8a6vna4
```

Spostiamoci nella tab *send* e inseriamo i valori desiderati.

![Bitcoin Core — Transazione](https://cdn-images-1.medium.com/max/1200/1*fNd2Lpu9XlI0SvJMI6yWuA.png)
*Bitcoin Core — Transazione*

Ci viene proposto un popup per confermare la transazione

![Bitcoin Core — Conferma](https://cdn-images-1.medium.com/max/1200/1*KyAcWa8ynO0qOF658GZvNQ.png)
*Bitcoin Core — Conferma*

Confermiamo.

Dove sarà adesso la transazione? Di nuovo nella **mempool**! 
Dato che sappiamo che è prensente una sola transazione, possiamo utilizzare **getrawmempool** dal nodo2.

```bash
bitcoin-cli --conf=bitcoin.conf_2 getrawmempool

[

"20f2b335d8775d1237523b1f6583ea809716f74e82773c5ad285cbb66a5b3e91"

]
```

![Bitcoin Core GUI – Mempool](https://cdn-images-1.medium.com/max/1200/1*72uwDX-QBJDen84eBFM3iA.png)
*Bitcoin Core GUI – Mempool*

Troviamo infatti corrispondenza con la GUI.

Adesso possiamo aspettarci dei bitcoin non confermati con nell’address del nodo2.

Abbiamo la verifica utilizzando il metodo **listreceivedbyaddress** passando come parametro 0, il quale rappresenta le conferme.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 listreceivedbyaddress 0

[

{

"address": "bcrt1qtc00wzrcae86rvyacanwd5l9t6fek4h8a6vna4",

"amount": 0.50000000,

"confirmations": 0,

"label": "barno",

"txids": [

"20f2b335d8775d1237523b1f6583ea809716f74e82773c5ad285cbb66a5b3e91"

]

}

]
```

Non ci resta che minare! Mineremo utilizzando il nodo2.

```bash
$ bitcoin-cli --conf=bitcoin.conf_2 generatetoaddress 11 $(bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "" "bech32") >> /dev/null
```

Facendo nuovamente doppio click sulla transazione possiamo leggere che la transazione è stata minata e confermata!

![Bitcoin core – Transazione minata e confermata](https://cdn-images-1.medium.com/max/1200/1*xWYCAZ6wlbqOm1ENPrhNAQ.png)
*Bitcoin core – Transazione minata e confermata*

Verifichiamo l’homepage della GUI.

![Bitcoin Core GUI — Homepage](/img/posts/bitcoin-core-gui-vs-cli-17.webp)
*Bitcoin Core GUI — Homepage*

Abbiamo un saldo disponibile di 0.49 bitcoin e un 250 bitcoin + fees immaturi. A questo punto sappiamo perchè!

Per concludere: 
La GUI facilita alcune operazioni ma ne nasconde altre, la riga di comando è sicuramente meno user friendly ma è molto più consigliata in quanto su ogni sistema che andrete a lavorare non vi sentirete spaesati!

Ciao!

![📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)](https://cdn-images-1.medium.com/max/1200/1*mFeOGVPcT3_CeHYzgoV2Dg.jpeg)
*📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)*

