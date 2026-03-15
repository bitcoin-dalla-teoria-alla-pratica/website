---
title: "Transazione P2PKH nel Bitcoin Playground"
date: 2021-03-17T10:00:00+01:00
slug: "transazione-p2pkh-nel-bitcoin-playground"
draft: false
author: "Alessio Barnini"
description: "Dopo alcuni articoli di teoria, siamo arrivati alla pratica. In questo video analizzeremo come sia possibile creare una transazione P2PKH…"
cover: "/img/posts/transazione-p2pkh-nel-bitcoin-playground-7.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

Dopo alcuni articoli di teoria, siamo arrivati alla pratica. In questo video analizzeremo come sia possibile creare una transazione P2PKH utilizzando un nodo bitcoin in modalità Regtest.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-7.webp)

Per questo esempio utilizzeremo un progetto che stiamo portando avanti io a Alessandro, ovvero un [playground](https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/).

Faremo un video dettagliato prima possibile, ma per adesso vi basta pensare che è, accedendo dei container docker, abbiamo a disposizione due nodi, Hansel e Gretel, che parlano tra loro, e alcuni utility tra cui un blockchain explorer.

Se volete replicare l’esempio che stiamo per vedere, potete creare il vostro ambiente di lavoro, clonando il progetto e seguendo le istruzioni che trovate nella pagina del playground.

Creeremo una transazione P2PKH utilizzando il nodo **Bitcoin** con la versione 0.21.0 e analizzeremo come la transazione è validata.‌

Per rendere le cose più semplici da spiegare, partiremo da una blockchain *vuota*, quindi prima di lanciare i container, utilizzo il comando `./regtest-delete.sh`, e successivamente avvio i container con `docker-compose up`.

Il prossimo passaggio è sarà quello di entrare nel container di hansel, ovvero di un nodo:

```bash
$ docker exec -ti hansel bash‌
```


e verificare che la blockchain abbia 0 blocchi, utilizzando il comando:

```bash
$ bitcoin-cli getblockcount
```


‌La prima operazione che vado a fare è creare un wallet, con il comando:

```bash
$ bitcoin-cli createwallet "hansel"‌
```


Successivamente creo l’address del mittente e l’address del destinatario. Utilizzerò delle variabili d’ambiente per salvare il contenuto.

```bash
$ ADDR_MITT=$(bitcoin-cli getnewaddress 'mitt' 'legacy')

$ ADDR_DEST=$(bitcoin-cli getnewaddress 'dest' 'legacy')‌
```


In questo momento i miei wallet non hanno nessuna UTXO, ovvero non hanno nessun bitcoin disponibile, quindi mineremo 101 blocchi (in modo tale da soddisfare la `COINBASE_MATURITY`) utilizzando l'address `$ADDR_MITT`.

```bash
$ bitcoin-cli generatetoaddress 101 $ADDR_MITT > /dev/null
```


‌Adesso ho dei bitcoin a disposizione, o meglio delle UTXO, per visualizzarli posso usare la chiamata `listunspent`, la quale mi mostra tutte i saldi a disposizione.

Utilizzo anche il Json Parser, JQ, per aiutarmi a estrapolare solamente le informazioni necessarie per effettuare la transazione.

‌Per prima cosa salvo tutta la UTXO all’interno della variabile d’ambiente `$UTXO`

```bash
$ UTXO=$(bitcoin-cli listunspent | jq -r.[0])‌
```


Successivamente creo la transazione utilizzando la chiamata sendtoaddress, utilizzando una fee_rate e decidendo di sottrarre le fees direttamente dall’amount.

```bash
$ TXID=$(bitcoin-cli -named sendtoaddress address="$ADDR_DEST" amount=$(echo $UTXO | jq -r.amount) fee_rate=25 subtractfeefromamount=true)
```


‌Adesso possiamo finalmente analizzare la nostra transazione, la quale si troverà nella mempool, e quindi in attesa di essere minata.

‌Per analizzarla possiamo utilizzare il comando `getrawtransaction`, e utilizzare la TXID appena ottenuta

```bash
$ bitcoin-cli getrawtransaction $TXID 2 | jq
```


‌Nel libro [Libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica) e [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://bit.ly/38RtF9x) , spieghiamo byte per byte la transazione.

Grazie al nostro docker, è possibile visualizzare la blockchain locale a anche la transazione che è in mempool.‌

In questo caso la nostra transazione ha come ID `49021cb4a1ebb0c74feaa3a9df2ea7e3e74afeb50df9a630023e8822786add73`, inserendola nel campo di ricerca otteniamo un qualcosa di simile:

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-2.webp)

Enter a caption for this image (optional)

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-3.webp)

Enter a caption for this image (optional)

‌Come possiamo analizzare lo stack e la sua esecuzione?

‌Utilizziamo il progetto btcdeb! I vostri parametri potrebbero cambiare, ma se avete seguito alla lettera il tutorial, lanciando questo comando, lo stack si popolerà.

```bash
$ btcdeb --tx=$(bitcoin-cli getrawtransaction $TXID) --txin=$(bitcoin-cli getrawtransaction $(echo $UTXO | jq -r.txid))‌
```


Al momento dell’avvio lo stack è vuoto, e premendo e digitando step, si effettua l’operazione successiva.‌

In questo caso con step, si inserisce prima lo scriptSig, ovvero la firma e successivamente la chiave pubblica compressa.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-8.webp)

I vostri valori saranno sicuramente diversi, ma la logica non cambia.‌

Successivamente abbiamo lo scriptPubKey.

Il primo elemento che inseriamo è `OP_DUP`, che come abbiamo visto nelle precedenti lezioni, duplica l'elemento on top, quindi la nostra chiave pubblica non compressa.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-5.webp)

Successivamente, l’operazione che si effettua è `HASH160`, che ha il compito di prendere l'elemento on top e applicare la funzione crittografica `SHA256` e `RIPEMD160`.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-9.webp)

‌Successivamente si inserisce l’hash della chiave pubblica compressa.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-7.webp)

La prossima OP_CODE è `OP_EQUALVERIFY`, la quale ha il compito di verificare due elementi, e se sono uguale non inserire niente, altrimenti invalida lo stack.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-10.webp)

In questo caso sono uguali, e quindi non viene inserito niente e lo stack è ancora valido.

Ultimo OP_CODE, `OP_CHECKSIG`, come è facile intuire, controlla la firma confrontandola utilizzando la chiave pubblica corrispondente.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-11.webp)

Se non ricordi come si verifica la firma digitale, [guarda questo video](https://www.youtube.com/watch?v=RU7LHPP4Lvk&list=PLpPLK7SGHncab_so9rB7lY3aKe2-Mqs5y&index=18).‌

Le operazioni che si effettuano sono, POP della chiave pubblica, pop della firma, e verifica della firma stessa. Se la verifica va a buon fine, si pusha 1, validando la transazione.‌

Le operazioni che abbiamo fatto, sono le stesse che abbiamo visto nel video [“Come si valida una Transazione P2PKH”](https://youtu.be/DW_YSbIGi1g).‌

Di seguito è riportata la lavagna utilizzata durante quel video:

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-10.webp)

Che cosa ci rimane da fare?‌

Minare!

```bash
$ bitcoin-cli generatetoaddress 1 $ADDR_MITT
```


‌A questo punto, utilizzando il nostro [explorer](http://localhost:8094/), potete analizzare l’ultimo blocco minato, il quale conterrà 2 transazioni, la coinbase e la transazione appena creata.

![](/img/posts/transazione-p2pkh-nel-bitcoin-playground-12.webp)

Se volete divertivi con il nostro playground, ecco il link! [https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/](https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/)

Ciao alla Prossima!

![Bitcoin In Action — SegWit, Bitcoin Script e Smart ContractseBitcoin dalla teoria alla pratica](/img/posts/transazione-p2pkh-nel-bitcoin-playground-12.webp)
*Bitcoin In Action — SegWit, Bitcoin Script e Smart ContractseBitcoin dalla teoria alla pratica*

–––––

