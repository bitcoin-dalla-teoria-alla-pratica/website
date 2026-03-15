---
title: "Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?"
date: 2020-07-29T10:00:00+01:00
slug: "che-cosa-lo-scriptpubkey-come-si-valida-la-transazione-in-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Video completo nel nostro canale youtube Bitcoin in Action"
cover: "https://cdn-images-1.medium.com/max/2560/1*tNj7YomLo9VjdIK_YWSuUA.png"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### **Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin**? #### Video completo nel nostro canale youtube [Bitcoin in Action](https://www.youtube.com/watch?v=HaZCpfc7Vbg&feature=youtu.be)

![Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?](https://cdn-images-1.medium.com/max/2560/1*tNj7YomLo9VjdIK_YWSuUA.png)
*Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?*

Ciao,

Oggi rispondiamo a una domanda ricevuta dalla nostra pagina [facebook](https://www.facebook.com/satoshiwantsyou). Pietro ci scrive:

“Grazie per i contenuti che state producendo sto imparando moltissimo.

Mi collego al [video precedente](https://www.youtube.com/watch?v=IPpSCOy3yHg), dove avete parlato dello [scriptSig](https://www.youtube.com/watch?v=IPpSCOy3yHg).

Quindi vi domando, potete spiegarmi meglio che cosa è lo **scriptPubKey** e come si valida una transazione?”

Bene Pietro, prima di tutto, grazie per i complimenti siamo molto contenti di aiutare la community italiana e non solo.

Infatti i nostri articoli sono anche in lingua inglese e pubblicati su [hackernoon](https://hackernoon.com/how-do-miners-mine-a-block-a-proof-of-work-deep-dive-r63u3xoh), e proprio in questi giorni è uscito la traduzione del libro Bitcoin dalla teoria alla pratica ([Bitcoin from theory to practice](https://amzn.to/2Ym4gz6)) in lingua inglese.

La transazione è una delle parti più importante in Bitcoin ed è bene avere chiara la sua struttura.

Come detto nel video precedente, nelle transazioni **non SegWit**, nello scriptSig troviamo le condizioni che soddisfano lo scriptPubKey.

Facciamo un esempio semplice per capire come funziona lo scriptPubKey.

Immagina che nella tua UTXO, lo scriptPubKey contenga **4 OP_EQUAL**.

Questo significa che per sbloccare l’importo di quell’output, devi soddisfare quelle richieste.

Come si risolve questa uguaglianza?

La risposta più semplice è inserire nello scriptSig il numero 4.

Come puoi immaginare, queste condizioni sono un pò “facili” chiunque può sbloccare questa UTXO.

Trovami un numero uguale a 4…non ci bloccherei 1 bitcoin :), ecco perchè si utilizza la [firma digitale](https://youtu.be/RU7LHPP4Lvk) per bloccare in sicurezza bitcoin nella UTXO.

Analizzando la transazione **P2PKH** utilizzata nel video precedente, ricorderai che lo **scriptPubKey** è così formato:

```bash
OP_DUP OP_HASH160 <public key> OP_EQUALVERIFY OP_CHECKSIG
```

Questo significa che nello scriptSig devono essere presenti degli elementi che devono soddisfare lo scriptPubKey, in modo tale che nello stack sia presente un unico e ultimo elemento con valore 1.

Ok andiamo di pratica.

> in Action

Prendiamo in esame la transazione utilizzata nel [**video corso**](/prodotti/videocorso-teoria-pratica), così da sfruttarne le slide.

```bash
$ bitcoin-cli getrawtransaction 3446bb5b86fa410d6c8676b0f93e665d06d4a18c97c7d0f2d80460d9696b2325 2
```

Analizziamo il primo elemento del **vout**, il quale “blocca” 20 bitcoins. Per estrarre solo quella porzione di risultato possiamo utilizzare jq.

```bash
$ bitcoin-cli getrawtransaction 3446bb5b86fa410d6c8676b0f93e665d06d4a18c97c7d0f2d80460d9696b2325 2 | jq -r ‘.vout[0]’

{

“value”: 20,

“n”: 0,

“scriptPubKey”: {

“asm”: “OP_DUP OP_HASH160 5c9fcd1d188f8f5ebcbb2cd8b52f11290f44d634 OP_EQUALVERIFY OP_CHECKSIG”,

“hex”: “76a9145c9fcd1d188f8f5ebcbb2cd8b52f11290f44d63488ac”,

“reqSigs”: 1,

“type”: “pubkeyhash”,

“addresses”: [

“19SkbqGT3u82TkdyRQJZjTcwPeEoXBiwgs”

]

}

}
```

Lo scriptPubKey è quello che si legge in **asm**, o in **hex**. Sono equivalenti, in hex abbiamo **l’esadecimale** corrispondente delle op_code.

Prima di passare alle slide per spiegare nel dettaglio lo script, recuperiamo anche la transazione che ha consumato tale output.

```bash
$ bitcoin-cli getrawtransaction 7408ac2f0230e779946e03911300dc39c4a48d39327aeb6c2cb13e1670c36371 2

{

“txid”: “3446bb5b86fa410d6c8676b0f93e665d06d4a18c97c7d0f2d80460d9696b2325”,

“vout”: 0,

“scriptSig”: {

“asm”: “304502200f45eb016b79bbc87208096034f2b037be247194e5a7e466103ca694a36cc1ae0221008fbb9067c2e1cdb0832e732062a63c9627bb597ce991d68d75e3aed144984691[ALL] 04ddd9f1b0ec593795d802cd27c442f3dd3db562b331616e554a88dddff62bba572bd535c853d5ef195db0cba621255669a5569caaaeae3802066c70fb2463b89e”,

“hex”: “48304502200f45eb016b79bbc87208096034f2b037be247194e5a7e466103ca694a36cc1ae0221008fbb9067c2e1cdb0832e732062a63c9627bb597ce991d68d75e3aed144984691014104ddd9f1b0ec593795d802cd27c442f3dd3db562b331616e554a88dddff62bba572bd535c853d5ef195db0cba621255669a5569caaaeae3802066c70fb2463b89e”

},

“sequence”: 4294967295

},
```

Come faccio a sapere che l’elemento da prendere in considerazione è il secondo elemento dell’array?

Nella transazione, all’interno all’interno di vin trovo l’identificativo della UTXO di riferimento, ovvero la txid di riferimento.

```bash
$ bitcoin-cli getrawtransaction 7408ac2f0230e779946e03911300dc39c4a48d39327aeb6c2cb13e1670c36371 2 | jq -r '.vin[1]'

{

"txid": "3446bb5b86fa410d6c8676b0f93e665d06d4a18c97c7d0f2d80460d9696b2325",

"vout": 0,

"scriptSig": {

"asm": "304502200f45eb016b79bbc87208096034f2b037be247194e5a7e466103ca694a36cc1ae0221008fbb9067c2e1cdb0832e732062a63c9627bb597ce991d68d75e3aed144984691[ALL] 04ddd9f1b0ec593795d802cd27c442f3dd3db562b331616e554a88dddff62bba572bd535c853d5ef195db0cba621255669a5569caaaeae3802066c70fb2463b89e",

"hex": "48304502200f45eb016b79bbc87208096034f2b037be247194e5a7e466103ca694a36cc1ae0221008fbb9067c2e1cdb0832e732062a63c9627bb597ce991d68d75e3aed144984691014104ddd9f1b0ec593795d802cd27c442f3dd3db562b331616e554a88dddff62bba572bd535c853d5ef195db0cba621255669a5569caaaeae3802066c70fb2463b89e"

},

"sequence": 4294967295

}
```

Passiamo alle slide del [**video corso**](/prodotti/videocorso-teoria-pratica) che sicuramente ci aiutano.

Bitcoin utilizza lo Stack per validare le transazioni.

L’operazione di inserimento all’interno dello stack è conosciuta come **push**, l’operazione di estrazione è conosciuta come pop.

Quindi per prima cosa viene fatto push degli elementi dello scriptSig, conosciuto anche come unlocking script.

Push Signature

Push Public Key

Se non vi ricordate che cosa contiene lo scriptSig, [vi lascio il link nei video consigliati](https://youtu.be/IPpSCOy3yHg).

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*FPj1JmydHi0VZb_4LoW0ag.jpeg)
*Slide del video corso Bitcoin dalla teoria alla pratica*

Come puoi vedere stiamo analizzando una transazione Pay to public key hash.

Successivamente viene inserito nello stack **OP_DUP** che ha il compito di estrarre il primo elemento dallo stack, di duplicarlo e di fare push del risultato

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*LjE9B3RU4qNm5kCFuCUg3g.jpeg)
*Slide del video corso Bitcoin dalla teoria alla pratica*

Prossima operazione è **OP_HASH160**, la quale prende il primo elemento dello stack, quindi pop, e applica la funzione **SHA256** e **RIPEMD160** e fa push del risultato.

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*NjY3JniSEMgxPk0yUY4sKQ.jpeg)
*Slide del video corso Bitcoin dalla teoria alla pratica*

Vedendo con la pratica esegue:

```bash
printf $(echo 04ddd9f1b0ec593795d802cd27c442f3dd3db562b331616e554a88dddff62bba572bd535c853d5ef195db0cba621255669a5569caaaeae3802066c70fb2463b89e | xxd -r -p | openssl sha256| sed ‘s/^.* //’) |xxd -r -p | openssl ripemd160 | sed ‘s/^.* //’
```

Nota bene, l’operazione è fatta sulla chiave pubblica dello scriptSig.

Ma guarda un pò, il risultato è esattamente lo stesso di quello della UTXO.

Prossima operazione, push dell’elemento dello **scriptPubKey**, L’hash della chiave pubblica, ecco perchè si chiama Pay to Public key hash.

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*MAe0ZOkTyq7v9C-XSLl-Pw.jpeg)
*Slide del video corso Bitcoin dalla teoria alla pratica*

Prossima operazione **OP_EQUALVERIFY**.

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*D5G9xHJ_XgvIujt8JH7Ihw.jpeg)
*Slide del video corso Bitcoin dalla teoria alla pratica*

Esegue il pop dei due elementi in testa allo stack, li verifica, e se sono uguali non esegue nessun push nello stack, altrimenti fallisce.

Guarda un pò chi è rimasto! Una chiave pubblica e una firma, mi è sembrato di averli già rivisti!

E la prossima operazione da fare è **OP_CHECKSIG**! Coincidenze?

Che cosa farà mai questa operazione?

Pop di due elementi dallo stack, verifica della firma, e se è la firma è valida esegue un push con il valore 1, ovvero true. Altrimenti lo stack fallisce

Ed ecco che l’ultimo e unico valore dello stack è 1, validando la transazione.

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*cp9Gh1FBBkFCs3fyEvyrIg.jpeg)
*Slide del video corso Bitcoin dalla teoria alla pratica*

---

L’argomento della validazione dello stack, lo stack stesso e le operation code sono argomenti molto ampi e meritano dei video e delle spiegazioni più dettagliate che affrontiamo [**nel video corso che trovate su Vimeo**](https://vimeo.com/r/2Lua/SGVxMVI5ZT) a metà prezzo, quindi accattateville!

Spero comunque di aver risposto alla tua domanda

Ciao alla prossima!

![Slide del video corso Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*Ie1fV9fLDKQhQ6yOkg82PA.gif)
*Slide del video corso Bitcoin dalla teoria alla pratica*

![Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*np_2Pm2tYyXmG5ozGQFxKA.jpeg)
*Bitcoin dalla teoria alla pratica*
