---
title: "Come creare una transazione P2SH-P2PK"
date: 2021-10-04T10:00:00+01:00
slug: "come-creare-una-transazione-p2sh-p2pk"
draft: false
author: "Alessio Barnini"
description: "Come inviare la transazione step by step"
images: ["https://cdn-images-1.medium.com/max/1200/1*imG__98FnJWdFN9KT0cgRQ.jpeg"]
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

Ciao,

Nell’articolo precedente abbiamo analizzato come si costruisce un address Bitcoin P2SH il quale script è il P2PK.

In questo video, andremo ad analizzare come viene creata la transazione, e quindi come viene popolato lo **scriptSig**.

Per questo esempio utilizzeremo ancora il codice che abbiamo messo a disposizione per il libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/). il quale potete trovare al nostro indirizzo [GitHub](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book).

---

In Action

Abbiamo già il nostro address, che abbiamo ottenuto con i passaggi spiegati con l’articolo precedente. Per comodità lo ricreiamo lanciando il file

```bash
sh create_p2sh_address_p2pk.sh
```

Se avete bisogno di approfondire tematiche quali **Redeem script**, **redeem script hash**, vi consiglio l’articolo precedente.

Andiamo nel vivo della transazione.

Se state utilizzando la versione 0.19.0 di bitcoin–core potrebbe essere necessario creare un wallet per utilizzare un address del nodo stesso.

L’address ottenuto dal wallet sarà il destinatario, mentre l’address P2SH-P2PK, creato precedentemente sarà il miner.

```bash
$ bitcoin-cli createwallet "bia"
```

Associamo anche il nome **bia** al wallet, ovvero Bitcoin In Action, fantasia mostruosa :).

Successivamente per comodità salviamo in variabile d’ambiente il mittente-miner, ovvero l’address P2SH e il destinatario, che in questo caso è un address legacy, un normale P2PKH, affrontato nei articoli precedenti.

```bash
$ ADDR_P2SH=`cat address_P2SH.txt`

$ ADDR_DEST=`bitcoin-cli getnewaddress "" "legacy"`
```

Miniamo quindi 101 blocchi, per ottenere 50 bitcoin di reward da utilizzare per il nostro esempio.

Per comodità, ogni esempio che andiamo a replicare, utilizziamo una **regtest** vuota, in modo tale da poter creare transazioni più facilmente.

```bash
$ bitcoin-cli generatetoaddress 101 $ADDR_P2SH >> /dev/null
```

Il passo successivo è importare l’address P2SH nel nodo con il comando importaddress.

Perché questa operazione? Dato che l’address non è ottenuto dal wallet del nodo, ma è stato ottenuto dall’esterno, abbiamo la necessità di importarlo cosi da analizzare le UTXO

```bash
$ bitcoin-cli importaddress $ADDR_P2SH
```

Utilizzando il comando listuspent possiamo analizzare le UTXO dell’address selezionato, ovvero il P2SH.

```bash
$ UTXO=`bitcoin-cli listunspent 1 101 '["'$ADDR_P2SH'"]'`
```

Il risultato di tale chiamata viene inserito nella variabile d’ambiente UTXO. Per analizzare il suo contenuto possiamo utilizzare il comando echo.

```bash
$ echo $UTXO
```

Per creare una transazione ho bisogno di:

- la Txid della UTXO di riferimento. In questo caso ne usiamo soltanto una.
- Il vout, ovvero l’indice della UTXO di riferimento
- L’amount.
- PK: la chiave privata per firmare la transazione.

Successivamente, a differenza di una transazione legacy, avrò bisogno di:

- Redeem script: ovvero le condizioni, IN CHIARO, necessarie per sbloccare la UTXO di riferimento
- lo scriptPubKey, dato da OP_HASH160 redeem script hash OP_EQUAL

Bene, con l’auto di JQ, un json parser che abbiamo ampiamente utilizzato durante i libri e durante i nostri video, andiamo a salvare in variabili d’ambiente quelle che sono le informazioni necessarie appena descritte.

```bash
$ TXID=$(echo $UTXO | jq -r '.[0].txid')

$ VOUT=$(echo $UTXO | jq -r '.[0].vout')

$ AMOUNT=$(echo $UTXO | jq -r '.[0].amount-0.009')

$ PK=`cat compressed_private_key_WIF_1.txt`

$ REDEEM=`cat redeem_script.txt`

$ SCRIPTPUBKEY="A914"`cat scriptPubKey.txt`"87"
```

Dove:

- A9 corrisponde a OP_HASH160
- 14 alla lunghezza del redeem script Hash
- 87 corrisponde a OP_EQUAL

Siamo pronti per creare la transazione.

```bash
TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_DEST'":'$AMOUNT'}]')
```

Il risultato viene salvato nella variabile d’ambiente TX_DATA. grazie al comando echo è possibile visualizzare il contenuto.

$TX_DATA sarà argomento della prossima funzione, ovvero signrawtransactionwithkey.

Per firmarla utilizzando, a differenza del P2PKH, anche il redeem script e il redeem script hash.

```bash
TX_SIGNED=$(bitcoin-cli signrawtransactionwithkey $TX_DATA '["'$PK'"]' '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'","redeemScript":"'$REDEEM'"}]' | jq -r '.hex')
```

Anche in questo caso abbiamo salvato nella variabile d’ambiente il risultato restituito dalla funzione signrawtransactionwithkey.

Non ci resta che inviarla in broadcast, utilizzando la funzione sendrawtransaction.

```bash
$ bitcoin-cli sendrawtransaction $TX_SIGNED
```

E tutto è andato a buon fine!  
Ma come viene validata?

Nel prossimo articolo andremo, step by step nella validazione, il codice è disponibile nel [GitHub](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book) del libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](prodotti/bitcoin-in-action/).

Ciao e alla prossima!

![📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)](https://cdn-images-1.medium.com/max/1200/1*imG__98FnJWdFN9KT0cgRQ.jpeg)
*📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)*



