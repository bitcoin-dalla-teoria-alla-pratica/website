---
title: "Esplorando le Differenze tra Transazioni Legacy e Descriptor in Bitcoin"
date: 2023-12-27T10:00:00+01:00
slug: "esplorando-le-differenze-tra-transazioni-legacy-e-descriptor-in-bitcoin"
draft: false
author: "Alessio Barnini"
description: "In questo articolo, esploreremo concretamente le differenze apportate dall’introduzione dell’aggiornamento descriptor a partire da Bitcoin…"
cover: "https://cdn-images-1.medium.com/max/1200/1*yX_9bACo1yXipSMncoJgPw.png"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

### Esplorando le Differenze tra Transazioni Legacy e Descriptor in Bitcoin

In questo articolo, esploreremo concretamente le differenze apportate dall’introduzione dell’aggiornamento descriptor a partire da Bitcoin Core 0.17.0 nel 2018.

Come sempre, gli esempi possono essere replicati utilizzando il nostro docker e il nostro repository.

Con l’aggiornamento descriptor, non è più possibile utilizzare `dumpprivkey` e quindi utilizzare la chiave privata per firmare le transazioni raw con il comando `signrawtransactionwithkey`.

Sarà invece il nodo a occuparsi di firmare la transazione utilizzando il comando `signrawtransactionwithwallet`.

In questo esempio, eseguiremo due transazioni: una dal descriptor a un indirizzo legacy e successivamente dall’indirizzo legacy al descriptor.

Creeremo due portafogli per gestire i due casi e avvieremo il nodo con la direttiva `-deprecatedrpc=create_bdb` per poter utilizzare i comandi legacy.

Questo esempio utilizza il nodo Bitcoin versione 26.

### Riproduzione dell’Esempio

Per replicare l’esperimento:

- Clona il [nostro repository](https://github.com/bitcoin-dalla-teoria-alla-pratica/bitcoin-in-action-youtube-docker).

```bash
docker exec -it bitcoin-in-action-youtube zsh
```

- Entra nel container e spostati nella cartella Video 13 — P2PKH legacy vs P2PKH descriptor.

```bash
./main.sh
```

#### In Azione

I nostri esempi si basano sempre sulla regtest, sia qui che nei nostri libri [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://amzn.to/3pJcXj1)e [Libro Bitcoin dalla teoria alla pratica](https://amzn.to/2Ldym0F)

![https://linktr.ee/satoshiwantsyou](https://cdn-images-1.medium.com/max/1200/1*QfBGF4Pcd3vgzH4Fx_wP5Q.jpeg)
*https://linktr.ee/satoshiwantsyou*

Dopo aver lanciado docker compo

```bash
docker-compose up
```

entriamo nel container con il comando

```bash
docker exec -it bitcoin-in-action-youtube bash
```

Per prima cosa, fermiamo e puliamo tutta la regtest con il seguente comando:

```bash
bitcoin-cli stop && sleep 5 && rm -Rf $HOME/.bitcoin/regtest && bitcoind -deprecatedrpc=create_bdb && sleep 5
```

Dobbiamo avviarlo con `bitcoind -deprecatedrpc=create_bdb` per avere la possibilità di utilizzare i comandi legacy.

Successivamente, creiamo due portafogli: uno legacy e uno descriptor, e creiamo due indirizzi.

Partiamo facendo la transazione dal Descriptor al Legacy:

```bash
bitcoin-cli -named createwallet wallet_name="biaDescriptor"bitcoin-cli -named createwallet wallet_name="biaLegacy" descriptors="false"ADDR_DESC=`bitcoin-cli -rpcwallet="biaDescriptor" getnewaddress "" "legacy"`ADDR_LEGACY=`bitcoin-cli -rpcwallet="biaLegacy" getnewaddress "" "legacy"`
```

Da notare che “legacy” qui si riferisce agli indirizzi legacy, non ai portafogli legacy. Gli indirizzi legacy sono quelli che iniziano con 1 nella mainnet e con m/n nella testnet/regtest.

Successivamente, mineremo 101 blocchi per ottenere un reward da spendere:

```bash
bitcoin-cli generatetoaddress 101 $ADDR_DESC >> /dev/null
```

Recuperiamo quindi le UTXO dell’indirizzo collegato al portafoglio descriptor:

```bash
UTXO=`bitcoin-cli -rpcwallet="biaDescriptor" listunspent 1 101 '["'$ADDR_DESC'"]'`
```

Quando abbiamo più di un portafoglio, dobbiamo specificare con `-rpcwallet` a quale portafoglio ci stiamo riferendo. In questo caso, immagazziniamo la lista degli UTXO nella variabile d’ambiente UTXO.

Nel mio caso, l’output di `$UTXO` sarà:

```bash
[ { "txid": "d2be3c5230c6a3e65c9f1b00c45b27b87126623c3a64720bbda301985897000a", "vout": 0, "address": "mhWDh6GAhuCGLjAZeT8HikfRgRtXRmfBuU", "label": "", "scriptPubKey": "76a91415ccb044249a2c23fc6e8b88a3826b4cfa6f3fe088ac", "amount": 50, "confirmations": 101, "spendable": true, "solvable": true, "desc": "pkh([ebaa1b3b/44h/1h/0h/0/0]03f05c3456b1790be65cdd9b976fa1746711b50491a7165335b4435298ee10a96f)#ly95qp65", "parent_descs": [ "pkh(tpubD6NzVbkrYhZ4Y1YBXnXsfxHZyDneWSBzrZqMmHqk1YDJkALiaREhzFnxobkgqtqXvz1PVSfbL1Kqx9i1CndiWwYKBnjpcqU1f5Mcz85ecty/44h/1h/0h/0/*)#5ufyz2pg" ], "safe": true }]
```

Se stai utilizzando il nostro docker, all’interno c’è anche un block explorer ([btc-rpc-explorer](http://localhost:3002/tx/d2be3c5230c6a3e65c9f1b00c45b27b87126623c3a64720bbda301985897000)) e puoi quindi analizzare la UTXO generata utilizzando ([http://localhost:3002/tx/d2be3c5230c6a3e65c9f1b00c45b27b87126623c3a64720bbda301985897000](http://localhost:3002/tx/d2be3c5230c6a3e65c9f1b00c45b27b87126623c3a64720bbda301985897000)), dove `d2be3c5230c6a3e65c9f1b00c45b27b87126623c3a64720bbda301985897000a` è la UTXO spendibile.

Questo link funzionerà solo se stai utilizzando il nostro docker.

Grazie a Jq, posso immagazzinare all’interno delle variabili d’ambiente il codice necessario per effettuare la transazione:

```bash
TXID=$(echo $UTXO | jq -r '.[0].txid')VOUT=$(echo $UTXO | jq -r '.[0].vout')AMOUNT=$(echo $UTXO | jq -r '.[0].amount-0.009')TOTAL_UTXO_AMOUNT=$(echo $UTXO | jq -r '.[0].amount')TXIN=`bitcoin-cli getrawtransaction $TXID`
```

Dall’amount tolgo una “cifra simbolica” destinata alla fee. Sono quindi pronto a creare la transazione:

```bash
TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_LEGACY'":'$AMOUNT'}]')
```

A questo punto, abbiamo il “nuovo” metodo inserito con l’aggiornamento descriptor, ovvero `createrawtransaction`:

```bash
TX_SIGNED=$(bitcoin-cli -rpcwallet="biaDescriptor" signrawtransactionwithwallet $TX_DATA | jq -r '.hex')
```

In questo caso, non passo la chiave privata, ma sarà il metodo `signrawtransactionwithwallet` a preoccuparsi di firmare la transazione con la relativa chiave privata.

Il risultato è salvato all’interno di `TX_SIGNED`.

Successivamente, viene inviata la transazione:

```bash
bitcoin-cli sendrawtransaction $TX_SIGNED
```

Facciamo ora l’operazione inversa, dal legacy al descriptor. Abbiamo già dei bitcoin spendibili grazie alla transazione appena creata, quindi l’operazione sarà più veloce.

Recupero le informazioni necessarie per creare la transazione:

```bash
UTXO=`bitcoin-cli -rpcwallet="biaLegacy" listunspent 1 101 '["'$ADDR_LEGACY'"]'`TXID=$(echo $UTXO | jq -r '.[0].txid')VOUT=$(echo $UTXO | jq -r '.[0].vout')AMOUNT=$(echo $UTXO | jq -r '.[0].amount-0.009')TOTAL_UTXO_AMOUNT=$(echo $UTXO | jq -r '.[0].amount')SCRIPTPUBKEY=$(echo $UTXO | jq -r '.[0].scriptPubKey')TXIN=`bitcoin-cli getrawtransaction $TXID`
```

In questo caso, useremo `-rpcwallet=”biaLegacy”`. Successivamente, prendo la chiave privata con il comando `dumpprivkey`:

```bash
PK=$(bitcoin-cli -rpcwallet="biaLegacy" dumpprivkey $ADDR_LEGACY)
```

Sono quindi pronto ad inviare la transazione. Creo la transazione:

```bash
TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_DESC'":'$AMOUNT'}]')
```

La firmo con la chiave privata e aggiungo anche lo `scriptPubKey`:

```bash
TX_SIGNED=$(bitcoin-cli signrawtransactionwithkey $TX_DATA '["'$PK'"]' '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'"}]' | jq -r '.hex')
```

Infine, invio la transazione in broadcast:

```bash
TXSPENT=$(bitcoin-cli sendrawtransaction $TX_SIGNED)
```

Ci sono quindi due differenze principali:

1. Non è possibile dare il `dumpprivkey` dal portafoglio descriptor, che è ora di default in Bitcoin. Se proviamo a fare il dump, otterremo un errore:

```bash
bitcoin-cli -rpcwallet="biaDescriptor" dumpprivkey $ADDR_DESCerror code: -4error message:Only legacy wallets are supported by this command
```

2. La seconda differenza è il metodo da chiamare per firmare la transazione: da `signrawtransactionwithkey` a `signrawtransactionwithwallet`.

Alla luce di queste differenze sostanziali tra l’utilizzo di indirizzi legacy e descriptor in Bitcoin, emergono nuove prospettive sulla gestione delle transazioni e sulla sicurezza delle chiavi private.

L’evoluzione del protocollo continua ad offrire agli utenti nuovi strumenti per interagire in modo sicuro e flessibile.

---

Per ulteriori informazioni e per immergerti nel mondo di Bitcoin, visita il nostro linktree: [https://linktr.ee/satoshiwantsyou](https://linktr.ee/satoshiwantsyou)
