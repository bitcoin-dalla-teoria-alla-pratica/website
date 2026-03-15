---
title: "Come viene validata la transazione P2PK"
date: 2021-01-01T10:00:00+01:00
slug: "come-viene-validata-la-transazione-p2pk"
draft: false
author: "Alessio Barnini"
description: "Nell’articolo precedente abbiamo spiegato con la teoria come viene validata una transazione P2PK, adesso con l’aiuto del tool btcdeb…"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### **La transazione di Satoshi Nakamoto**![https://www.youtube.com/watch?v=SMDeoY9x3HY](/img/posts/come-viene-validata-la-transazione-p2pk-1.webp)
*https://www.youtube.com/watch?v=SMDeoY9x3HY*

[Nell’articolo precedente](/posts/come-si-valida-una-transazione-p2pk/) abbiamo spiegato con la teoria come viene validata una transazione P2PK, adesso con l’aiuto del tool [btcdeb](https://github.com/bitcoin-core/btcdeb), analizziamolo con la pratica.

Vogliamo quindi analizzare la transazione avvenuta nel blocco 170, tra Hal Finney e Satoshi Nakamoto.

Se non siamo a conoscenza dell’esadecimale della transazione è necessario recuperarlo dal suo blocco. e dato che non sappiamo neanche l’hash del blocco, lo recuperiamo tramite la sua altezza.

```bash
$ bitcoin-cli getblockhash 170
```


```bash
00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee
```


Adesso possiamo recuperare le transazioni.

```bash
$ bitcoin-cli getblock 00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee
```


```bash
{
```


```bash
"hash": "00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee",
```


```bash
"confirmations": 662339,
```


```bash
"strippedsize": 490,
```


```bash
"size": 490,
```


```bash
"weight": 1960,
```


```bash
"height": 170,
```


```bash
"version": 1,
```


```bash
"versionHex": "00000001",
```


```bash
"merkleroot": "7dac2c5666815c17a3b36427de37bb9d2e2c5ccec3f8633eb91a4205cb4c10ff",
```


```bash
"tx": [
```


```bash
"b1fea52486ce0c62bb442b530a3f0132b826c74e473d1f2c220bfa78111c5082",
```


```bash
"f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16"
```


```bash
],
```


```bash
"time": 1231731025,
```


```bash
"mediantime": 1231716245,
```


```bash
"nonce": 1889418792,
```


```bash
"bits": "1d00ffff",
```


```bash
"difficulty": 1,
```


```bash
"chainwork": "000000000000000000000000000000000000000000000000000000ab00ab00ab",
```


```bash
"nTx": 2,
```


```bash
"previousblockhash": "000000002a22cfee1f2c846adbd12b3e183d4f97683f85dad08a79780a84bd55",
```


```bash
"nextblockhash": "00000000c9ec538cab7f38ef9c67a95742f56ab07b0a37c5be6b02808dbfb4e0"
```


```bash
}
```


Le transazioni sono due, sappiamo però dai video precedenti, che la prima transazione è sempre la coinbase.

Analizziamo quindi la seconda transazione.

```bash
$ bitcoin-cli getrawtransaction f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16 2 | jq
```


```bash
{
```


```bash
"txid": "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16",
```


```bash
"hash": "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16",
```


```bash
"version": 1,
```


```bash
"size": 275,
```


```bash
"vsize": 275,
```


```bash
"weight": 1100,
```


```bash
"locktime": 0,
```


```bash
"vin": [
```


```bash
{
```


```bash
"txid": "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9",
```


```bash
"vout": 0,
```


```bash
"scriptSig": {
```


```bash
"asm": "304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d09[ALL]",
```


```bash
"hex": "47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901"
```


```bash
},
```


```bash
"sequence": 4294967295
```


```bash
}
```


```bash
],
```


```bash
"vout": [
```


```bash
{
```


```bash
"value": 10,
```


```bash
"n": 0,
```


```bash
"scriptPubKey": {
```


```bash
"asm": "04ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84c OP_CHECKSIG",
```


```bash
"hex": "4104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac",
```


```bash
"type": "pubkey"
```


```bash
}
```


```bash
},
```


```bash
{
```


```bash
"value": 40,
```


```bash
"n": 1,
```


```bash
"scriptPubKey": {
```


```bash
"asm": "0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3 OP_CHECKSIG",
```


```bash
"hex": "410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac",
```


```bash
"type": "pubkey"
```


```bash
}
```


```bash
}
```


```bash
],
```


```bash
"hex": "0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000",
```


```bash
"blockhash": "00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee",
```


```bash
"confirmations": 662340,
```


```bash
"time": 1231731025,
```


```bash
"blocktime": 1231731025
```


```bash
}
```


Analizzando il vout possiamo vedere i due output generati da questa transazione, entrambi sono **pubkey**. 
Il primo output ha 10 bitcoin, e la seconda transazione, che rappresenta il resto, è di 40 bitcoin.

Sono sicuro che rappresenti il resto perchè nello scriptPubKey troviamo la stessa chiave pubblica della transazione in ingresso, cioè **0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3** Analizziamo la transazione in ingresso, che troviamo nel vin:

```bash
$ bitcoin-cli getrawtransaction 0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9 2 | jq
```


```bash
{
```


```bash
"txid": "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9",
```


```bash
"hash": "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9",
```


```bash
"version": 1,
```


```bash
"size": 134,
```


```bash
"vsize": 134,
```


```bash
"weight": 536,
```


```bash
"locktime": 0,
```


```bash
"vin": [
```


```bash
{
```


```bash
"coinbase": "04ffff001d0134",
```


```bash
"sequence": 4294967295
```


```bash
}
```


```bash
],
```


```bash
"vout": [
```


```bash
{
```


```bash
"value": 50,
```


```bash
"n": 0,
```


```bash
"scriptPubKey": {
```


```bash
"asm": "0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3 OP_CHECKSIG",
```


```bash
"hex": "410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac",
```


```bash
"type": "pubkey"
```


```bash
}
```


```bash
}
```


```bash
],
```


```bash
"hex": "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0134ffffffff0100f2052a0100000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000",
```


```bash
"blockhash": "000000008d9dc510f23c2657fc4f67bea30078cc05a90eb89e84cc475c080805",
```


```bash
"confirmations": 662502,
```


```bash
"time": 1231473279,
```


```bash
"blocktime": 1231473279
```


```bash
}
```


Come vedete nel in **hex** troviamo la stessa chiave pubblica, nel prossimo video vedremo come identificarla meglio.

Cerchiamo invece di capire come lo stack viene validato sfruttando **btcdeb**.

Il software si aspetta la transazione d’ingresso, e la transazione di uscita per costruire lo stack.

Per fare questo possiamo utilizzare le variabile d’ambiente.

Chiamerò TX_IN la transazione in ingresso e TX_OUT la transazione in uscita, quella che contiene due output.

```bash
➜ ~ $ TX_IN=$(bitcoin-cli getrawtransaction 0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9)
```


```bash
➜ ~ $ TX_OUT=$(bitcoin-cli getrawtransaction f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16)
```


Per verificare il valore delle variabili d’ambiente, possiamo utilizzare il comando echo.

```bash
➜ ~ $ echo $TX_IN
```


```bash
01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0134ffffffff0100f2052a0100000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000
```


Utilizziamo quindi il programma btcdeb.

```bash
$ btcdeb --tx=$TX_OUT --txin=$TX_IN
```


![](/img/posts/come-viene-validata-la-transazione-p2pk-2.webp)

Come mostrato nei [video precedenti dove veniva utilizzata la lavagna](https://www.youtube.com/playlist?list=PLpPLK7SGHncZVl_ZQkqyXGMDGWEx7U_et), il primo elemento che viene inserito nello stack è lo **scriptSig**, che in questo caso contiene la firma digitale.

l’operazione che viene effettuata è un’operazione di **PUSH**.

![](/img/posts/come-viene-validata-la-transazione-p2pk-3.webp)

Successivamente sono effettuate altre due operazioni di PUSH, quindi la chiave pubblica non compressa.

Successivamente l’operation code **OP_CHECKSIG** ha il compito di fare **POP** di due elementi in top, quindi in cima alla pila, verificare firma, e *pushare* 1 se la firma è valida, 0 altrimenti

![](/img/posts/come-viene-validata-la-transazione-p2pk-4.webp)

La firma è valida, quindi il numero che viene inserito l’elemento 1.

Lo stack è stato eseguito con successo dato che l’ultimo e unico elemento dello stack è 1, il quale rappresenta la buon riuscita del programma.

![www.corsobitcoin.com](/img/posts/come-viene-validata-la-transazione-p2pk-5.webp)
*www.corsobitcoin.com*

