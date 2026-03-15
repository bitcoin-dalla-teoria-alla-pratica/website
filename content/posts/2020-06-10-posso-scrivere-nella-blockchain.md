---
title: "Posso scrivere nella blockchain?"
date: 2020-06-10T10:00:00+01:00
slug: "posso-scrivere-nella-blockchain"
draft: false
author: "Alessio Barnini"
description: "Video completo nel canale youtube Bitcoin in Action"
cover: "/img/posts/posso-scrivere-nella-blockchain-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

#### Video completo nel [canale youtube Bitcoin in Action](https://www.youtube.com/BitcoinInAction)

![Video completo nelcanale youtube Bitcoin in Action](/img/posts/posso-scrivere-nella-blockchain-1.webp)
*Video completo nelcanale youtube Bitcoin in Action*

Ciao, 
Oggi rispondiamo a Luca che ci domanda. 
È Possibile scrivere nella blockchain?

Sì, è possibile scrivere nella blockchain, possiamo lasciare un messaggio utilizzando un op code chiamato OP_RETURN, che rende la **UTXO associata (non tutti gli UTXO della tx)**, quindi l’unspent transaction output, inspendibile.

Puoi scrivere al massimo 80 bytes.

L’operazione di scrittura viene spesso definita come “timestamping delle informazioni scritte” perchè la transazione che le contiene farà parte di un blocco al quale è associata una marca temporale, un timestamp per l’appunto.

Ricorda però che ogni volta che aggiungiamo delle informazioni alla transazione, aumentiamo il suo peso pagando di conseguenza più fee.

Quando potrebbe essere utile? Ad esempio se vuoi lasciare una fingerprint di un documento marcato temporalmente.

Per questo esempio utilizzeremo la testnet così da poter vedere il messaggio in un explorer.

> In Action

Come prima cosa ottengo un address SegWit dal mio nodo testnet.

```bash
$ bitcoin-cli getnewaddress “” “bech32”

tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d
```


Otteniamo quindi dei bitcoin dal servizio faucet [https://bitcoinfaucet.uo1.net/send.php](https://bitcoinfaucet.uo1.net/send.php)

Possiamo verificare che la txid sia in mempool con la chiamata:

```bash
$ bitcoin-cli getrawmempool | grep c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a
```


dove c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a rappresenta la mia txid ottenuta dal servizio faucet.

Appena la transazione è minata possiamo recuperare la UTXO con il comando listunspent.

```bash
$ bitcoin-cli listunspent 1 101 ‘[“tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d”]’ | jq

[

{

“txid”: “c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a”,

“vout”: 1,

“address”: “tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d”,

“label”: “”,

“scriptPubKey”: “00141a10dfb322436bc2177358a8fd876e6ebf5658a3”,

“amount”: 0.00100000,

“confirmations”: 6,

“spendable”: true,

“solvable”: true,

“desc”: “wpkh([3a46ecca/0'/0'/4']020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f)#kxjva7dw”,

“safe”: true

}

]
```


Dopo di che recupero la chiave privata del mio indirizzo, indispensabile per firmare la transazione.

```bash
$ bitcoin-cli dumpprivkey tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d

cPHTHs7ERe6jDYiitj9eLVswsX3RpeKMB19eXYjpLb4CkEHd7drq
```


Generiamo il messaggio che vogliamo inserire nella blockchain, ad esempio [corsocompleto.bitcoininaction.com](http://corsocompleto.bitcoininaction.com) nel suo formato esadecimale.

```bash
$ printf “corsocompleto.bitcoininaction.com” | xxd -ps

636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d
```


Per creare la transazione devo usare il metodo createrawtransaction. Utilizzando help possiamo analizzare tutti i parametri a nostra disposizione.

```bash
$ bitcoin-cli help createrawtransaction
```


Il destinatario della transazione è l’address del faucet

```bash
2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE
```


Ho tutto il necessario per creare la mia transazione utilizzando la chiamata createrawtransaction.

Come valore di data inserisco l’esadecimale che voglio scrivere nella blockchain, il quale mi creerà una UTXO OP_RETURN.

```bash
$ bitcoin-cli createrawtransaction ‘[{“txid”:”c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a”,”vout”:1}]’ ‘[{“2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE”:0.00099000},{“data”:”636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d”}]’

02000000019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d00000000
```


In questo caso effettuo una sola transazione nella quale sposto tutto il mio input, non necessito quindi di un change address, ovvero di un indirizzo di resto, dato che il resto non è presente.

Inoltre non ho utilizzato tutto il mio output perchè parte di questo è destinato alle fee.

La transaction data è stata quindi creata. Il prossimo step è firmarla e inviarla verso il secondo indirizzo. il metodo da utilizzare è signrawtransactionwithkey

```bash
$ bitcoin-cli signrawtransactionwithkey 02000000019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d00000000 ‘[“cPHTHs7ERe6jDYiitj9eLVswsX3RpeKMB19eXYjpLb4CkEHd7drq”]’ ‘[{“txid”:”c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a”,”vout”:1,”scriptPubKey”:”00141a10dfb322436bc2177358a8fd876e6ebf5658a3",”amount”:0.00100000}]’

{

“hex”: “020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000”,

“complete”: true

}
```


La transazione è stata firmata con successo, possiamo adesso inviare la transazione, utilizzando il metodo sendrawtransaction.

```bash
$ bitcoin-cli sendrawtransaction 020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000

edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548
```


Ottenendo cosi la transaction id.

Adesso possiamo utilizzare un qualsiasi explorer per verificare la transazione, ad esempio [https://tbtc.bitaps.com/](https://tbtc.bitaps.com/) e inseriamo la [transaction id](https://tbtc.bitaps.com/edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548) appena ottenuta.

![Il messaggio nella blockchain di Bitcoin — corsocompleto.bitcoininaction.com](/img/posts/posso-scrivere-nella-blockchain-2.webp)
*Il messaggio nella blockchain di Bitcoin — corsocompleto.bitcoininaction.com*

La transazione è stata inviata correttamente ed è in attesa di essere minata. Contiene giustamente due output, uno verso il destinatario e l’altro è un OP_RETURN con il nostro messaggio.

Abbiamo visto con esempi pratici come sia possibile scrivere nella blockchain, utilizzando l’operation code **OP_RETURN** che rende l’UTXO associato inspendibile.

È comunque sconsigliato scrivere nella blockchain se non strettamente necessario.

Per ottimizzare, in termini di fee e spazio occupato, le scritture sulla blockchain di Bitcoin si consiglia di utilizzare [OpenTimestamps](https://opentimestamps.org/) invece che reinventare la ruota!

Ciao alla prossima
