---
title: "Due transazioni con lo stesso txid."
date: 2019-04-29T10:00:00+01:00
slug: "due-transazioni-con-lo-stesso-txid"
draft: false
author: "Alessio Barnini"
description: "Un pò di tempo fa il protocollo Bitcoin fece nascere due transazioni con lo stesso identificativo. 
Cercando la transazione con id…"
images: ["https://cdn-images-1.medium.com/max/1200/1*bJPPcNzZUvTdh3qJrcOgCA.jpeg"]
tags:
  - "BIP"
  - "Bitcoin"
  - "Bitcoin Script"
categories:
  - "Bitcoin"
---

---

### Due transazioni con lo stesso txid

![Two bad — master of the universe](https://cdn-images-1.medium.com/max/1200/1*bJPPcNzZUvTdh3qJrcOgCA.jpeg)
*Two bad — master of the universe*

Un pò di tempo fa il protocollo **Bitcoin** fece *nascere* due transazioni con lo stesso identificativo.  
Cercando la transazione con id e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468:

```bash
bitcoin-cli getrawtransaction e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468 true
```

Risultato:

```bash
...{ "txid": "e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468",

... altre informazioni...

 "blockhash": "00000000000743f190a18c5577a3c2d2a1f610ae9601ac046a38084ccb7cd721", "confirmations": 481756, "time": 1289781379, "blocktime": 1289781379}
```

Otteniamo l’hash del blocco che contiene la transazione. 
Analizziamo un altro blocco.

```bash
bitcoin-cli getblock 00000000000271a2dc26e7667f8419f2e15416dc6955e5a6c6cdf3f2574dd08e
```

Risultato:

```bash
{ “hash”: “00000000000271a2dc26e7667f8419f2e15416dc6955e5a6c6cdf3f2574dd08e”,... “tx”: [ “e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468” ],...}
```

Come è possibile che una transazione sia inclusa dentro a due blocchi? Siamo davanti al tanto temuto **double spending**? No. 
Partiamo dicendo che il protocollo Bitcoin non vieta la possibilità di creare due transazioni con lo stesso **txid**, ma sicuramente non porta benefici.

- Il primo indizio è che la transazione che stiamo esaminando è una **coinbase**. - Il secondo indizio è che è stato lo stesso miner a risolvere entrambi i blocchi.
- Il terzo indizio è che entrambi i reward erano di 50 bitcoin.

Come si forma la transaction id?  
Applicando la funzione crittografica SHA256 per due volte sulla transaction data e girando l’ordine dei bytes in little-endian. La transaction data è formata da:

- La version della transazione
- Numero di input
- Input (scriptsig)
- Numero di output
- Output (scriptPubKey)
- Locktime

La transaction data della txid che stiamo esaminando è la seguente:

```bash
01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff060456720e1b00ffffffff0100f2052a01000000434104124b212f5416598a92ccec88819105179dcb2550d571842601492718273fe0f2179a9695096bff94cd99dcccdea7cd9bd943bfca8fea649cac963411979a33e9ac00000000
```

Facendo il doppio SHA256 e girando l’ordine dei bytes in little endian, otteniamo la txid incriminata.

```bash
printf `printf 01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff060456720e1b00ffffffff0100f2052a01000000434104124b212f5416598a92ccec88819105179dcb2550d571842601492718273fe0f2179a9695096bff94cd99dcccdea7cd9bd943bfca8fea649cac963411979a33e9ac00000000 | xxd -r -p | sha256sum -b | xxd -r -p | sha256sum -b` | tac -rs..

risultato:e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468
```

Esatto, le due transazioni hanno lo stesso identico transaction data, ecco perchè hanno lo stesso txid! 
Per evitare questo problema è stato introdotto il [BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki), che obbliga ad inserire l’altezza del blocco all’interno dello scriptSig, risolvendo così il problema.

![Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”](https://cdn-images-1.medium.com/max/1200/1*Zb2RB6CyI0_vELiO44iqmQ.png)
*Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”*
