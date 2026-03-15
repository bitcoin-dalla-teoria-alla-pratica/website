---
title: "Transazioni in regtest"
date: 2020-02-03T10:00:00+01:00
slug: "transazioni-in-regtest"
draft: false
author: "Alessio Barnini"
description: "Come posso creare una transazioni tra due nodi?"
images: ["https://cdn-images-1.medium.com/max/1200/1*EdeMc64B2AWgAXx2ODJNsw.png"]
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

### Transazioni in regtest

#### Come posso creare una transazioni tra due nodi?

[Nel tutorial precedente](https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353) abbiamo visto come sia possibile far comunicare due nodi sullo stesso computer e come si sincronizzano quando dei blocchi vengono minati.

Q: Quindi possiamo fare anche una transazione e vedere che essa sia propagata e capire tutti i passaggi che subisce prima che faccia parte della blockchain? 
R: Si.

Se volete avere un ambiente “pulito” potete cancellare le cartelle regtest dei rispettivi nodi, così da avere zero blocchi minati e nessun reward assegnato.

Inseriamo in entrambi i nodi l’opzione txindex=1 in modo tale da avere tutta l’indicizzazione delle transazioni.

> -txindex 
> Maintain a full transaction index, used by the getrawtransaction rpc 
> call (default: 0)

```bash
$ vim bitcoin_nodo2.conf
```

![Configurazione nodo 2](https://cdn-images-1.medium.com/max/1200/1*rRinDepzLOWMv7d0lbjScw.png)
*Configurazione nodo 2*

stessa operazione per il nodo di default il cui percorso (default) nel mio computer è:

```bash
/Users/barno/Library/Application Support/Bitcoin/bitcoin.conf
```

Avviamo di nuovo entrambi i nodi. 
Se avete cancellato la cartella regtest (come me), dovete seguire i passaggi del [tutorial precedente](https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353) così da avere a disposizione 50 bitcoin su un’indirizzo. 
*Già 50 bitcoin, nessun halving era ancora stato fatto.*

Ottengo quindi 3 indirizzi, 2 dal nodo di default (bizantino) e 1 dal nodo2.

```bash
$ ADDR=`bitcoin-cli getnewaddress bizantino`$ ADDR_RESTO=`bitcoin-cli getnewaddress bizantino_resto`$ ADDR_DEST=`bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getnewaddress destinatario`
```

Dal nome delle variabili d’ambiente scelte si capisce il loro scopo. 
Mino 101 blocchi per ottenere 50 bitcoin con l’indirizzo $ADDR. 
Perché proprio 101? Per ottenere un reward spendibile e soddisfare la **COINBASE_MATURITY**.

```bash
$ bitcoin-cli generatetoaddress 101 $ADDR
```

Adesso entrambi i nodi devono avere 101 blocchi, se così non fosse torna al [tutorial precedente](https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353).

Con il comando **listunpsent** otteniamo tutte le UTXO disponibili.

```bash
$ bitcoin-cli listunspent

[{"txid": "75b91cf262c98bdd57b0c3f2ec1a2597cceadc0cc2ef0a103e1a0013d81e332f","vout": 0,"address": "2MvXFfHyxr1U4icdyw1nWM3FZdraXMsfMAq","label": "bizantino","redeemScript": "00147700ead177801037c5ec0ad20d1cf7637fe55fde","scriptPubKey": "a91423f06dcefe3a139e930f059e99b47e9bf908c17f87","amount": 50.00000000,"confirmations": 101,"spendable": true,"solvable": true,"desc": "sh(wpkh([87aac41a/0'/0'/0']03d5f548512ed8f90773e531440fd4ce1843ee5ddf1097b7731a4464803df468c4))#qksqangj","safe": true}]
```

Quello che interessa a noi per fare la transazione è la **txid** e il **vout**, per questo le salviamo in due variabili d’ambiente.

```bash
$ TXID=75b91cf262c98bdd57b0c3f2ec1a2597cceadc0cc2ef0a103e1a0013d81e332f

$ VOUT=0
```

Siamo pronti a creare la transazione utilizzando il comando **createrawtransaction**.

Sposteremo 1 bitcoin verso il destinatario, e 48.998 bitcoin verso l’indirizzo di resto.

Una bella mancia per il miner! 
Il risultato che otteniamo, la transaction data, la salviamo dentro la variabile d’ambiente TX_DATA.

```bash
$ TX_DATA=`bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_RESTO'":48.998},{"'$ADDR_DEST'":1}]'`
```

Per vedere il contenuto della variabile d’ambiente,

```bash
$ echo $TX_DATA
```

NB: Nel libro [**Bitcoin dalla teoria alla pratica**](prodotti/bitcoin-dalla-teoria-alla-pratica) e nel [**video-corso**](https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13) viene analizzato byte per byte la **transaction data**.

Quello che dobbiamo fare adesso è firmare la transazione con la chiave privata di $ADDR che posso ottenere con il comando **dumpprivkey**. ```bash
$ PK=`bitcoin-cli dumpprivkey $ADDR`
```

Attenzione, non deriviamo la chiave privata dalla chiave pubblica ($ADDR) ma la otteniamo da una serie di indirizzi già pronti per il nostro wallet.  
Per maggiori informazioni guarda il comando dumpwallet.

Bene, firmiamo la transazione.

```bash
$ bitcoin-cli signrawtransactionwithkey $TX_DATA '["'$PK'"]'

{

"hex": "020000000001012f331ed813001a3e100aefc20cdceacc97251aecf2c3b057dd8bc962f21cb97500000000171600147700ead177801037c5ec0ad20d1cf7637fe55fdeffffffff02808cf1230100000017a91489734e8089e307b4ac82eab729519abb2674cb168700e1f5050000000017a9143166112f2219dfd7bdfbabab70bef4ecab850a4587024730440220439be864b4520e29360341b429e9f16da89c5c44e98205025fb3b496e8b296990220638894c61364c3acca31b8acb80314b356713de0f8d11cfa03985bb8ae8c91cb012103d5f548512ed8f90773e531440fd4ce1843ee5ddf1097b7731a4464803df468c400000000",

"complete": true

}
```

Per comodità salviamo dentro la variabile d’ambiente TX_DATA_SIGNED il valore di hex. 
Inviamo la transazione.

```bash
$ bitcoin-cli sendrawtransaction $TX_DATA_SIGNED

d24f8de59e839ee3956f27b44ce8ed980405725acde903e5494450934f9a4db2
```

Quello che otteniamo è la TXID. 
Che cosa succede adesso? La transazione è stata inviata ma non è ancora stata minata, quindi dove si trova? 
Nella mempool! 
Dobbiamo essere in grado di verificare la sua presenza in entrambi i nodi.

![Estratto dellibroecorsoBitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*EdeMc64B2AWgAXx2ODJNsw.png)
*Estratto dellibroecorsoBitcoin dalla teoria alla pratica*

```bash
$ bitcoin-cli getrawmempool

[

"d24f8de59e839ee3956f27b44ce8ed980405725acde903e5494450934f9a4db2"

]

$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getrawmempool

[

"d24f8de59e839ee3956f27b44ce8ed980405725acde903e5494450934f9a4db2"

]
```

Esatto, entrambi i nodi hanno a disposizione la transazione ed entrambi potrebbero minarla. Per verificare il candidate block il comando è **getblocktemplate**. ```bash
$ bitcoin-cli getblocktemplate '{"rules": ["segwit"]}'
```

Quindi la transazione è **verificata** ma **non confermata**. 
Possiamo trovare conferma dell’asserzione appena fatta con il comando **getwalletinfo** sul nodo2.

```bash
$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getwalletinfo

{..."balance": 0.00000000,"unconfirmed_balance": 1.00000000,"immature_balance": 0.00000000,"txcount": 1,...}
```

Possiamo leggere **“unconfirmed_balance”**: 1 ! 
Bene, miniamo facendo 6 blocchi così da rendere la transazione sicura.

```bash
$ bitcoin-cli generatetoaddress 6 $ADDR
```

Bene, la mempool è vuota e il destinatario ha a disposizione 1 bitcoin!

```bash
$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getwalletinfo..."balance": 1.00000000,...
```

Possiamo verificare le operazioni sui log dei demoni, oppure utilizzando tail sul file di log.

```bash
$ tail -F regtest/debug.log
```

Ci provo?

```bash
$ bitcoin-cli sendrawtransaction $TX_DATA_SIGNED

error code: -27error message:Transaction already in block chain
```

Il double spending non è andato a buon fine.

---

Con questo piccolo tutorial è possibile iniziare a studiare il protocollo Bitcoin e a seguire il libro [**Bitcoin dalla teoria alla pratica**](prodotti/bitcoin-dalla-teoria-alla-pratica) o se preferisci il [**video-corso**](https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13) **.**
