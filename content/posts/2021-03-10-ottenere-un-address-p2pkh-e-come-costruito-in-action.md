---
title: "Ottenere un address P2PKH e come è costruito (In Action!)"
date: 2021-03-10T10:00:00+01:00
slug: "ottenere-un-address-p2pkh-e-come-costruito-in-action"
draft: false
author: "Alessio Barnini"
description: "Negli articoli precedenti abbiamo visto come un address P2PKH viene generato e come una transazione viene validata. È arrivato il momento…"
cover: "https://cdn-images-1.medium.com/max/1200/1*yGricoohTXDxTqZrN3VRlA.jpeg"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

### **Ottenere un address P2PKH e come è costruito (In Action!)** Negli articoli precedenti abbiamo visto come un address P2PKH viene generato e come una transazione viene validata. È arrivato il momento di fare sul serio, creeremo un address P2PKH e analizzeremo step by step la transazione e come questa viene validata.

Vi ricordo velocemente che l’address P2PKH (pay to public key hash) ha nel suo scriptPubKey, l’hash della sua chiave pubblica compressa.

Nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)](https://amzn.to/3pJcXj1) analizziamo e creiamo un address P2PKH manualmente, partendo dalla generazione della chiave privata.  
 In questo esempio, invece, utilizzeremo il metodo getnewaddress per ottenere un address dal nostro nodo di regtest.

![📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)](https://cdn-images-1.medium.com/max/1200/1*yGricoohTXDxTqZrN3VRlA.jpeg)
*📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)*

Per prima cosa avviamo il nostro nodo regtest. (Se non sai come installarlo [guarda questo articolo](https://bitcoin-in-action.medium.com/come-si-utilizza-un-nodo-bitcoin-ff0e0a785886))

```bash
$ bitcoind
```

Richiediamo quindi un address P2PKH, utilizzando il comando getnewsaddress. Per sapere che parametri accetta, è possibile utilizzare il comando **help**.

```bash
$ bitcoin-cli help getnewaddress

getnewaddress ( "label" "address_type" )
```

Bene, accetta come parametri una label, facoltativa, e il tipo di address voluto. Il P2PKH è un address legacy, per questo utilizzeremo il comando:

```bash
$ bitcoin-cli getnewaddress "P2PKH bitcoin in action" "legacy"

mfXmGhk1qovdUdtyWbuA5MKdpTiC4Ybz4C
```

Abbiamo ottenuto un address che inizia o con N o con M, nel mio caso con M.

Vi ricordate perchè? Durante la costruzione dell’address inseriamo un [address prefixes](https://en.bitcoin.it/wiki/List_of_address_prefixes).

In questo caso è stato il software bitcoin core a farlo per noi.

Se l’address P2PKH è destinato alla mainnet il primo carattere sarà 1, se invece l’address ha come destinazione la testnet o la regtest, l’address avrà come primo carattere la m o la n.

Analizziamo meglio l’address. Per comodità salvo l’address nella variabile d’ambiente ADDR, in modo tale da non dovermi portare in “giro” 34 caratteri esadecnmali. Per fare questa operazione digito:

```bash
ADDR=mfXmGhk1qovdUdtyWbuA5MKdpTiC4Ybz4C
```

Per poi verificare il contenuto di ADDR, utilizzo il comando echo, richiamando la variabile preceduta dal simbolo del dollaro.

```bash
$ echo $ADDR

mfXmGhk1qovdUdtyWbuA5MKdpTiC4Ybz4C
```

Per comodità salvo anche l’address prefix del P2PKH per l’ambiente di regtest.

```bash
PREFIX=6F
```

Adesso possiamo utilizzare il metodo getaddressinfo , che come è facile intuire, restituisce una serie di informazioni relative all’address.

```bash
$ bitcoin-cli getaddressinfo $ADDR

{

"address": "mfXmGhk1qovdUdtyWbuA5MKdpTiC4Ybz4C",

"scriptPubKey": "76a914002736d4bb3c8a6bed4957a92047a46acbcc5aa988ac",

"ismine": true,

"solvable": true,

"desc": "pkh([664e540a/0'/0'/1']03844e497f4b43968c90a493fafcc33ecedcd49ff94e2a534143761d3040a54991)#hkffnnyc",

"iswatchonly": false,

"isscript": false,

"iswitness": false,

"pubkey": "03844e497f4b43968c90a493fafcc33ecedcd49ff94e2a534143761d3040a54991",

"iscompressed": true,

"label": "P2PKH bitcoin in action",

"ischange": false,

"timestamp": 1612087963,

"hdkeypath": "m/0'/0'/1'",

"hdseedid": "cf10b47c5eb95369ee420118c2c3e4ed86f9f9a3",

"hdmasterfingerprint": "664e540a",

"labels": [

{

"name": "P2PKH bitcoin in action",

"purpose": "receive"

}

]

}
```

La chiamata restituisce un pò di informazioni, noi ci concentreremo su, scriptPubKey e Public Key.

Come abbiamo analizzato nei video precedenti, sappiamo che nello scriptPubKey, c’è l’hash160 della chiave pubblica compressa.

Sappiamo inoltre che la public key che lèggiamo dalla chiamata getaddressinfo, è una public key compressa, perchè non inizia con il byte 04.

Vi ricordate come si ottiene l’address P2PKH? Ecco la lavagna di qualche lezione precedente.

![](https://cdn-images-1.medium.com/max/1200/1*0Ivg36SaVDiAs8DcUOWsVA.png)

Adesso abbiamo a disposizione, , l’address prefix e la chiave pubblica compressa. Applicando la funzione crittografica

hash160, che include lo SHA256 e successivamente il RIPEMD160. saremo in grado di ottenere il nostro address!

Per fare questo, utilizziamo ancora una variabile d’ambiente, ad esempio PB, per salvare il valore della chiave pubblica.

```bash
PB=03844e497f4b43968c90a493fafcc33ecedcd49ff94e2a534143761d3040a54991
```

Oppure per prenderla in maniera dinamica, possiamo anche utilizzare Jq.

```bash
PB=$(bitcoin-cli getaddressinfo $ADDR | jq -r '.pubkey')
```

Applichiamo la funzione crittografica SHA256

```bash
ADDR_SHA=`printf $PB | xxd -r -p | openssl sha256| sed 's/^.* //'`

echo "digest SHA256 "$ADDR_SHA
```

Al digest ottenuto, applichiamo la funzione crittografica ripemd160

```bash
ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed 's/^.* //'`

echo "digest RIPEMD160 "$ADDR_RIPEMD160
```

Come vedete, per comodità ho utilizzato delle variabili d’ambiente.

Che cosa manca per ottenere l’address? Applicare l’encoding base58 checksum.

```bash
$ ADDR_2=$(printf $PREFIX$ADDR_RIPEMD160 | xxd -p -r | base58 -c)

$ echo $ADDR_2

mfXmGhk1qovdUdtyWbuA5MKdpTiC4Ybz4C
```

L’address che ottengo è lo stesso che ho ottenuto con la chiamata getnewsaddress.

Vi ricordate che cosa contiene lo scriptPubKey?

Contiene anche l’hash160 della chiave pubblica. quello che noi abbiamo calcolato all’interno della variabile d’ambiente ADDR_RIPEMD160.

```bash
$ echo $ADDR_RIPEMD160

002736d4bb3c8a6bed4957a92047a46acbcc5aa9
```

Analizziamo nuovamente la chiamata getaddressinfo sfruttando jq

```bash
$ bitcoin-cli getaddressinfo $ADDR | jq -r '.scriptPubKey'

76a914002736d4bb3c8a6bed4957a92047a46acbcc5aa988ac
```

Infatti troviamo corrispondenza! 
Nel prossimo video vedremo come creare una transazione e come questa viene validata!

Ciao e alla prossima!

