---
title: "Che cosa è lo SHA256?"
date: 2020-06-18T10:00:00+01:00
slug: "che-cosa-lo-sha256"
draft: false
author: "Alessio Barnini"
description: "Scopri il video sul canale Bitcoin in Action!"
images: ["https://cdn-images-1.medium.com/max/1200/1*zU6Md7J1cTqpbZ13EYnPAw.png"]
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Che cosa è lo SHA256?

#### [Scopri il video sul canale Bitcoin in Action!](https://www.youtube.com/BitcoinInAction?sub_confirmation=1)

![Scopri il video sul canale Bitcoin in Action](https://cdn-images-1.medium.com/max/1200/1*zU6Md7J1cTqpbZ13EYnPAw.png)
*Scopri il video sul canale Bitcoin in Action*

Ciao,

Una delle domande ricorrenti che ci viene fatta durante i nostri corsi è: Che cosa è l’algoritmo SHA256 e dove viene utilizzato?

In Bitcoin l’algoritmo SHA256 viene utilizzato in molti scenari, dalla creazione dell’address, al calcolo della TXID fino ad arrivare all’identificativo del blocco, o per meglio dire, nella proof of work.

SHA è l’acronimo di **Secure Hash Algorithm**, il suo scopo è prendere in ingresso una dei byte, ad esempio una stringa, quindi del testo, di una lunghezza arbitraria e restituire un’altra stringa lunga sempre lunga 256 bit, dato che stiamo utilizzando SHA256.

È un algoritmo **One Way (senza funzione inversa)**, questo significa che dal risultato ottenuto, chiamato digest (spesso si usa erroneamente il termine hash al posto di digest), non è possibile risalire al messaggio originale, chiamato anche anche messaggio in chiaro.

Diciamo che risalire al messaggio in chiaro è talmente improbabile che possiamo dire che è impossibile, questo perchè il digest contiene troppe poche informazioni per effettuare questa operazione.

Una volta lessi che è come trovare un atomo nell’universo, credo che sia difficile.

Cerchiamo di fare chiarezza con un esempio.

> In Action

Bene, creiamo subito un digest, utilizzando il messaggio in chiaro **bitcoininaction** ```bash
$ printf bitcoininaction | openssl dgst -sha256

(stdin)= b76b7041106a75de9fa4fbf880b3886cc114cbfd570e1a17adb58b937afee351
```

Dal digest è quindi impossibile capire che il messaggio in chiaro fosse bitcoininaction.

Che cosa succede se applico nuovamente la funzione crittografica SHA256 a [bitcoininaction](http://bitcoininaction.com)?

Se la vostra risposta è stata: Ottengo lo stesso risultato, avete dato la risposta esatta.

```bash
$ printf bitcoininaction | openssl dgst -sha256

(stdin)= b76b7041106a75de9fa4fbf880b3886cc114cbfd570e1a17adb58b937afee351
```

Che cosa succede se cambio leggermente il messaggio in chiaro, ad esempio [bitcoininaction.com](http://bitcoininaction.com/)?

```bash
$ printf bitcoininaction.com | openssl dgst -sha256

(stdin)= 41dbcc447756ddd2c32ac99c76ef6f090fa0a63da5a6ecfda3311936f85daa85
```

Ottengo un digest completamente diverso. È per questo motivo che è molto veloce verificare un digest se si è in possesso del messaggio in chiaro. Ogni messaggio in chiaro su cui è applicato l’algoritmo SHA256 produce un digest unico. Se due messaggi diversi producessero lo stesso digest avremo un fenomeno chiamato collisione.

Ok, tutto interessante, ma voglio vedere almeno un esempio di Bitcoin!

Otteniamo quindi l’hash della transazione effettuata nel video “[Posso scrivere nella blockchain](https://www.youtube.com/watch?v=d4H3dAnMbiA)”.

Per fare questa operazione dobbiamo effettuare due volte la funzione crittografica SHA256 e ottenere la sua rappresentazione in little endian. Molto brevemente Big Endian e Little Endian coinvolgono l’ordine dei byte.

- *big-endian*: Si ha la memorizzazione dal byte più significativo per finire col meno significativo.
- *little endian*: Si ha la memorizzazione dal byte meno significativo per finire col più significativo.

La transazione è stata fatta nella blockchain di testnet e ha come txid: [edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548](https://tbtc.bitaps.com/edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548)

Recuperiamo quindi la transazione con il comando getrawtransaction.

```bash
$ bitcoin-cli getrawtransaction edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548 2

{

“txid”: “edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548”,

“hash”: “12cf1e132b1d775f5403a875592b447a825f493c0eecdf6bbaa8f5e759c1c71d”,

...

“hex”: “020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000”,

...

}
```

L’hash è **12cf1e132b1d775f5403a875592b447a825f493c0eecdf6bbaa8f5e759c1c71d** ed è quella che noi dobbiamo ottenere. Dobbiamo applicare l’algoritmo SHA256 per due volte e ottenere la sua rappresentazione in little endian.

Ottengo il primo digest.

```bash
$ printf 020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000 | xxd -r -p | sha256sum -b

33bf8e3e54327c84758e3442ccea54cfef3621ee4d7276cc1bdcde301d4c4796
```

Applichiamo nuovamente lo SHA256 al digest ottenuto, per ottenere il secondo digest.

```bash
$ printf 33bf8e3e54327c84758e3442ccea54cfef3621ee4d7276cc1bdcde301d4c4796 | xxd -r -p | sha256sum -b

1dc7c159e7f5a8ba6bdfec0e3c495f827a442b5975a803545f771d2b131ecf12
```

Ed infine otteniamo la sua rappresentazione in little endian

```bash
$ printf 1dc7c159e7f5a8ba6bdfec0e3c495f827a442b5975a803545f771d2b131ecf12 | tac -rs..

12cf1e132b1d775f5403a875592b447a825f493c0eecdf6bbaa8f5e759c1c71d
```

Il risultato coincide!

Quello che abbiamo appena messo in pratica è solo un caso di dove e come il protocollo Bitcoin utilizza questo tipo di Algoritmo, ovviamente non è l’unico algoritmo ad essere utilizzato, ad **RIPEMD-160** viene usato durante la generazione degli address. Come sempre il codice è disponibile nel nostro repository GitHub che trovare in descrizione e vi invito a lasciare domande nei commenti e se vi va iscrivetevi.

Ciao alla prossima
