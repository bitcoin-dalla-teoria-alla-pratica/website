---
title: "Bitcoin Multisig: La Tua Guida Sicura e Affidabile alla Firma delle Transazioni"
date: 2024-03-22T11:14:42+01:00
draft: false


tags:
  - "Script"
  - "Multisig"
---




<p>Nel nostro viaggio nel mondo del Bitcoin, affrontiamo oggi un altro passaggio cruciale: la firma delle transazioni per gli indirizzi Multisig P2SH. Sei pronto a immergerti nel processo?</p>

<p>Come sempre, useremo l'ambiente Docker per garantire un'esperienza sicura e isolata mentre impariamo insieme.</p>

<p><strong>Passo dopo Passo: Mettiamoci all'Opera!</strong></p>

<p>Per cominciare, utilizzeremo i wallet descriptor, strumento fondamentale per gestire gli indirizzi. Avviamo quindi un'istanza regtest e creiamo un wallet dedicato:</p>


```bash
bitcoin-cli stop && sleep 5 && rm -Rf $HOME/.bitcoin/regtest && bitcoind && sleep 5
bitcoin-cli -named createwallet wallet_name="bitcoin in action"
```


<p>Una volta pronto, recuperiamo l'indirizzo creato in precedenza e miniamo 101 blocchi per avere a disposizione 50 Bitcoin:</p>


```bash
ADDR_MITT=`bitcoin-cli getnewaddress "mittente" "legacy"`
# Recuperiamo l'indirizzo P2SH
ADDR_DEST=`cat address_P2SH.txt`

# Miniamo 101 blocchi per ottenere il reward
bitcoin-cli generatetoaddress 101 $ADDR_MITT >> /dev/null
```


<p>Con il reward ottenuto, salviamo le informazioni necessarie per creare la prossima transazione verso l'indirizzo multisignature:</p>


```bash
TXID=$(bitcoin-cli listunspent 1 101 '["'$ADDR_MITT'"]' | jq -r '.[0].txid')
VOUT=$(bitcoin-cli listunspent 1 101 '["'$ADDR_MITT'"]' | jq -r '.[0].vout')
AMOUNT=$(bitcoin-cli listunspent 1 101 '["'$ADDR_MITT'"]' | jq -r '.[0].amount-0.001')
```


<p>Successivamente, creiamo la transazione grezza e ne esaminiamo i dettagli:</p>


```bash
printf  "\n \e[31m######### TX_DATA #########\e[39m \n"
TX_DATA=`bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_DEST'":'$AMOUNT'}]'`
bitcoin-cli decoderawtransaction $TX_DATA | jq
```


<p>Una volta ispezionati i dettagli, procediamo con la firma e l'invio:</p>


```bash
TX_DATA_SIGNED=$(bitcoin-cli signrawtransactionwithwallet $TX_DATA | jq -r '.hex')
TXID=`bitcoin-cli sendrawtransaction $TX_DATA_SIGNED`
bitcoin-cli generatetoaddress 6 $ADDR_MITT
```


<p>Ora, con i Bitcoin disponibili dall'indirizzo P2SH, creiamo l'output della transazione e recuperiamo le chiavi private:</p>


```bash
AMOUNT=`bitcoin-cli getrawtransaction $TXID 2 | jq -r '.vout[0].value-0.0001'`
VOUT=0

PK1=`cat compressed_private_key_WIF_1.txt`
PK2=`cat compressed_private_key_WIF_2.txt`
PK3=`cat compressed_private_key_WIF_3.txt`
```


<p>Dopo l'importazione del descriptor e il recupero del redeem script, siamo pronti a creare e firmare la transazione:</p>


```bash
CHECKSUM=$(bitcoin-cli getdescriptorinfo "sh(multi(2,$PK1,$PK2,$PK3))" | jq -r .checksum)
bitcoin-cli importdescriptors '[{ "desc": "sh(multi(2,'$PK1','$PK2','$PK3'))#'$CHECKSUM'", "timestamp": "now", "internal": true }]'

REDEEM=`cat redeem_script.txt`
```


<p>Infine, creiamo e firmiamo la transazione:</p>


```bash
SCRIPTPUBKEY="A914"`cat scriptPubKey.txt`"87"
TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'","redeemScript":"'$REDEEM'"}]' '[{"'$ADDR_MITT'":'$AMOUNT'},{"data":"636f72736f626974636f696e2e636f6d0a"}]')
TX_SIGNED=$(bitcoin-cli signrawtransactionwithwallet $TX_DATA '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'","redeemScript":"'$REDEEM'"}]'  | jq -r '.hex')
```


<p>Con la transazione firmata, è tempo di inviarla:</p>


```bash
bitcoin-cli generatetoaddress 6 $ADDR_MITT
```


<p>Dopo aver completato la transazione, possiamo esaminarne la validità passo dopo passo utilizzando btcdeb.</p>

<p><strong>Conclusione</strong></p>

<p>Con questo tutorial, hai imparato come firmare transazioni Multisig Bitcoin in modo sicuro e affidabile. Ricorda sempre di seguire attentamente ogni passaggio per garantire la sicurezza delle tue operazioni.</p>

<p>Per approfondimenti e ulteriori esempi, unisciti a noi nel nostro libro "Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</p>
