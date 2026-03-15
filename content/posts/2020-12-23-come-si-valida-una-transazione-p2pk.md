---
title: "Come si valida una transazione P2PK?"
date: 2020-12-23T10:00:00+01:00
slug: "come-si-valida-una-transazione-p2pk"
draft: false
author: "Alessio Barnini"
description: "I 3 concetti base da conoscere"
cover: "https://cdn-images-1.medium.com/max/1200/1*yeFVeMUJlY8jeHJMFYmmzg.jpeg"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

#### I 3 concetti base da conoscere

![Come si valida una transazione P2PK?](https://cdn-images-1.medium.com/max/1200/1*yeFVeMUJlY8jeHJMFYmmzg.jpeg)
*Come si valida una transazione P2PK?*

Nel [video precedente](https://www.youtube.com/watch?v=gJgavv8wIYs)abbiamo introdotto lo **Stack** e abbiamo capito che viene utilizzato per validare la transazione. 
L’obiettivo di questa serie è spiegare gli address, quindi partiremo con l’analisi dell’address P2PK.

In realtà è sbagliato dire l’address P2PK, proprio perchè non esiste nessun address P2PK.

Analizzando la prima transazione nel blocco 170, molti [explorer](https://btc.bitaps.com/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16) riportano l’address: [1Q2TWHE3GMdB6BZKafqwxXtWAWgFt5Jvm3](https://btc.bitaps.com/1Q2TWHE3GMdB6BZKafqwxXtWAWgFt5Jvm3) ma in realtà non è corretto.

L’address che si vede è un address P2PKH, mentre lo script P2PK non ha nessun address specifico. A quell’epoca si pagava a uno scriptPubKey e non a un address- 
  
Andiamo quindi per gradi, cercando di capire funzionava, ai tempi del buon Hal Finney e di Satoshi Nakamoto, il P2PK.

```bash
"vin": [

{

"txid": "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9",

"vout": 0,

"scriptSig": {

"asm": "304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d09[ALL]",

"hex": "47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901"

},

"sequence": 4294967295

}

],

"vout": [

{

"value": 10.00000000,

"n": 0,

"scriptPubKey": {

"asm": "04ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84c OP_CHECKSIG",

"hex": "4104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac",

"type": "pubkey"

}

},

{

"value": 40.00000000,

"n": 1,

"scriptPubKey": {

"asm": "0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3 OP_CHECKSIG",

"hex": "410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac",

"type": "pubkey"

}

}

],
```

Come per tutti le derivazioni, il punto di partenza è sempre la generazione della chiave privata utilizzando la curva ellittica secp256k1 utilizzata in Bitcoin.

Una delle parti fondamentali della generazione della chiave privata è l’entropia, più l’entropia è casuale più sicura sarà la chiave privata.

Successivamente viene *trasformata* nel formato [DER](http://fileformats.archiveteam.org/wiki/DER).

Per adesso quello che ci interessa a noi è avere una chiave privata per derivare una chiave pubblica.

Per questa spiegazione, noi utilizzeremo solo la chiave pubblica non compressa, proprio come la prima transazione avvenuta in Bitcoin.

Ma vediamo come viene validata la transazione:

Lo scriptSig viene inserito, si dice *pushato* all’interno dello stack, successivamente viene pushato lo scriptPubKey.

In questo caso lo **scriptSig** è rappresentato dalla firma digitale e lo scriptPubKey è rappresentato dalla **chiave pubblica**.

Una transazione è valida quando nello stack rimane un solo e unico elemento con valore 1, ovvero true.

Inserendo la firma e la chiave pubblica, come fa il software a validare la transazione? Bitcoin utilizza un linguaggio di programmazione chiamato [Script](https://en.bitcoin.it/wiki/Script), da qui anche il sottotitolo del nostro [libro](prodotti/bitcoin-in-action/).

Bitcoin Script ha un funzione, o per meglio dire un’operation code, che verifica una firma sulla chiave pubblica.

L’operation in questione è **OP_CHECKSIG**.

Ora è più chiaro? Nello scriptPubKey ci dovrà essere quindi la chiave pubblica e successivamente lo OP_CHECKSIG.

Che compito ha OP_CHECKSIG? Il suo compito è quello di fare due volte la funzione di **pop**, quindi estrarre **i primi due valori on top** dallo stack e verificare se la firma è valida, se è valida, esegue il push del valore 1, altrimenti 0.

![Estratti del videohttps://www.youtube.com/watch?v=iVWMaGO3m48](https://cdn-images-1.medium.com/max/1200/1*DV72p9lsHS2bNwOi5CsG0A.png)
*Estratti del videohttps://www.youtube.com/watch?v=iVWMaGO3m48*

![Estratti del videohttps://www.youtube.com/watch?v=iVWMaGO3m48](https://cdn-images-1.medium.com/max/1200/1*htlIJ-QVw0XAmoDMVXuksQ.png)
*Estratti del videohttps://www.youtube.com/watch?v=iVWMaGO3m48*

![Estratti del videohttps://www.youtube.com/watch?v=iVWMaGO3m48](https://cdn-images-1.medium.com/max/1200/1*zi78pygLASkw9AZMQEw6hw.png)
*Estratti del videohttps://www.youtube.com/watch?v=iVWMaGO3m48*
