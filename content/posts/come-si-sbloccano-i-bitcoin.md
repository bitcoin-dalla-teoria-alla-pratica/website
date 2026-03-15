---
title: "Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?"
date: 2020-07-29T16:39:04+01:00
draft: false


tags:
  - "Script"
  - "Crittografia"
---




<p>Oggi rispondiamo a una domanda ricevuta dalla nostra pagina <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noreferrer noopener">Facebook</a>. Pietro ci scrive:</p>

<blockquote class="wp-block-quote"><p>“Grazie per i contenuti che state producendo sto imparando moltissimo. Mi collego al <a data-href="https://www.youtube.com/watch?v=IPpSCOy3yHg" href="https://www.youtube.com/watch?v=IPpSCOy3yHg" target="_blank" rel="noopener noreferrer">video precedente</a>, dove avete parlato dello <a data-href="https://www.youtube.com/watch?v=IPpSCOy3yHg" href="https://www.youtube.com/watch?v=IPpSCOy3yHg" target="_blank" rel="noopener noreferrer">scriptSig</a>. Quindi vi domando, potete spiegarmi meglio che cosa è lo <strong>scriptPubKey</strong> e come si valida una transazione?”</p></blockquote>

<p>Bene Pietro, prima di tutto grazie per i complimenti! Siamo molto contenti di aiutare la community italiana e non solo. Infatti i nostri articoli sono anche in lingua inglese e pubblicati su <a data-href="https://hackernoon.com/how-do-miners-mine-a-block-a-proof-of-work-deep-dive-r63u3xoh" href="https://hackernoon.com/how-do-miners-mine-a-block-a-proof-of-work-deep-dive-r63u3xoh" target="_blank" rel="noopener noreferrer">hackernoon</a>, e proprio in questi giorni è uscito la traduzione del libro Bitcoin dalla teoria alla pratica (<a data-href="https://amzn.to/2Ym4gz6" href="https://amzn.to/2Ym4gz6" target="_blank" rel="noopener noreferrer">Bitcoin from theory to practice</a>) in lingua inglese.</p>

<p>La transazione è una delle parti più importante in Bitcoin ed è bene avere chiara la sua struttura. Come detto nel video precedente, nelle transazioni <strong>non SegWit</strong>, nello scriptSig troviamo le condizioni che soddisfano lo scriptPubKey.</p>

<p>Facciamo un esempio semplice per capire come funziona lo scriptPubKey.</p>

<p>Immagina che nella tua UTXO, lo scriptPubKey contenga <strong>4 OP_EQUAL</strong>.</p>

<p>Questo significa che per sbloccare l’importo di quell’output, devi soddisfare quelle richieste.</p>

<h3>Come si risolve questa uguaglianza?</h3>

<p>La risposta più semplice è inserire nello scriptSig il numero 4.</p>

<p>Come puoi immaginare, queste condizioni sono un pò “facili” chiunque può sbloccare questa UTXO.</p>

<p>Trovami un numero uguale a 4…non ci bloccherei 1 bitcoin&nbsp;:), ecco perchè si utilizza la <a href="https://youtu.be/RU7LHPP4Lvk" target="_blank" rel="noopener noreferrer" data-href="https://youtu.be/RU7LHPP4Lvk">firma digitale</a> per bloccare in sicurezza bitcoin nella UTXO.</p>

<p>Analizzando la transazione <strong>P2PKH</strong> utilizzata nel video precedente, ricorderai che lo <strong>scriptPubKey</strong> è così formato:</p>


```bash
OP_DUP OP_HASH160  OP_EQUALVERIFY OP_CHECKSIG
```


<p>Questo significa che nello scriptSig devono essere presenti degli elementi che devono soddisfare lo scriptPubKey, in modo tale che nello stack sia presente un unico e ultimo elemento con valore 1.</p>

<p>Ok andiamo di pratica.</p>

<h2>In action!</h2>

<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://www.youtube.com/watch?v=HaZCpfc7Vbg&amp;feature=emb_title
</div></figure>

<p>Prendiamo in esame la transazione utilizzata nel&nbsp;<a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener"><strong>video corso</strong></a>, così da sfruttarne le slide.</p>


```bash
$ bitcoin-cli getrawtransaction 3446bb5b86fa410d6c8676b0f93e665d06d4a18c97c7d0f2d80460d9696b2325 2
```


<p>Analizziamo il primo elemento del&nbsp;<strong>vout</strong>, il quale “blocca” 20 bitcoins. Per estrarre solo quella porzione di risultato possiamo utilizzare jq.</p>


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


<p>Lo scriptPubKey è quello che si legge in&nbsp;<strong>asm</strong>, o in&nbsp;<strong>hex</strong>. Sono equivalenti, in hex abbiamo&nbsp;<strong>l’esadecimale</strong>&nbsp;corrispondente delle op_code.</p>

<p>Prima di passare alle slide per spiegare nel dettaglio lo script, recuperiamo anche la transazione che ha consumato tale output.</p>


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


<p>Come faccio a sapere che l’elemento da prendere in considerazione è il secondo elemento dell’array?</p>

<p>Nella transazione, all’interno all’interno di vin trovo l’identificativo della UTXO di riferimento, ovvero la txid di riferimento.</p>


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


<p>Passiamo alle slide del&nbsp;<a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener"><strong>video corso</strong></a>&nbsp;che sicuramente ci aiutano.</p>

<p>Bitcoin utilizza lo Stack per validare le transazioni.</p>

<p>L’operazione di inserimento all’interno dello stack è conosciuta come&nbsp;<strong>push</strong>, l’operazione di estrazione è conosciuta come pop.</p>

<p>Quindi per prima cosa viene fatto push degli elementi dello scriptSig, conosciuto anche come unlocking script.</p>

<p>Push Signature</p>

<p>Push Public Key</p>

<p>Se non vi ricordate che cosa contiene lo scriptSig, <a href="https://youtu.be/IPpSCOy3yHg" target="_blank" rel="noreferrer noopener">vi lascio il link nei video consigliati</a>.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2020/11/1_FPj1JmydHi0VZb_4LoW0ag.jpeg" alt="Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?" class="wp-image-13450"/><figcaption><a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener">Slide del video corso Bitcoin dalla teoria alla pratica</a></figcaption></figure>

<p>Come puoi vedere stiamo analizzando una transazione Pay to public key hash.</p>

<p>Successivamente viene inserito nello stack <strong>OP_DUP</strong> che ha il compito di estrarre il primo elemento dallo stack, di duplicarlo e di fare push del risultato.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2020/11/1_LjE9B3RU4qNm5kCFuCUg3g.jpeg" alt="Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?" class="wp-image-13451"/><figcaption><a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener">Slide del video corso Bitcoin dalla teoria alla pratica</a></figcaption></figure>

<p>Prossima operazione è <strong>OP_HASH160</strong>, la quale prende il primo elemento dello stack, quindi pop, e applica la funzione <strong>SHA256</strong> e <strong>RIPEMD160</strong> e fa push del risultato.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2020/11/1_NjY3JniSEMgxPk0yUY4sKQ.jpeg" alt="Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?" class="wp-image-13452"/><figcaption><a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener">Slide del video corso Bitcoin dalla teoria alla pratica</a></figcaption></figure>

<p>Vedendo con la pratica esegue:</p>


```bash
printf $(echo 04ddd9f1b0ec593795d802cd27c442f3dd3db562b331616e554a88dddff62bba572bd535c853d5ef195db0cba621255669a5569caaaeae3802066c70fb2463b89e | xxd -r -p | openssl sha256| sed ‘s/^.* //’) |xxd -r -p | openssl ripemd160 | sed ‘s/^.* //’
```


<p>Nota bene, l’operazione è fatta sulla chiave pubblica dello scriptSig.</p>

<p>Ma guarda un pò, il risultato è esattamente lo stesso di quello della UTXO.</p>

<p>Prossima operazione, push dell’elemento dello <strong>scriptPubKey</strong>, L’hash della chiave pubblica, ecco perché si chiama Pay to Public key hash.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2020/11/1_MAe0ZOkTyq7v9C-XSLl-Pw.jpeg" alt="Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?" class="wp-image-13453"/><figcaption><a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener">Slide del video corso Bitcoin dalla teoria alla pratica</a></figcaption></figure>

<p>Prossima operazione <strong>OP_EQUALVERIFY</strong>.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2020/11/1_D5G9xHJ_XgvIujt8JH7Ihw.jpeg" alt="Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?" class="wp-image-13454"/><figcaption><a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener">Slide del video corso Bitcoin dalla teoria alla pratica</a></figcaption></figure>

<p>Esegue il pop dei due elementi in testa allo stack, li verifica, e se sono uguali non esegue nessun push nello stack, altrimenti fallisce.</p>

<p>Guarda un pò chi è rimasto! Una chiave pubblica e una firma, mi è sembrato di averli già rivisti!</p>

<p>E la prossima operazione da fare è&nbsp;<strong>OP_CHECKSIG</strong>! Coincidenze?</p>

<h3>Che cosa farà mai questa operazione?</h3>

<p>Pop di due elementi dallo stack, verifica della firma, e se è la firma è valida esegue un push con il valore 1, ovvero true. Altrimenti lo stack fallisce</p>

<p>Ed ecco che l’ultimo e unico valore dello stack è 1, validando la transazione.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2020/11/1_cp9Gh1FBBkFCs3fyEvyrIg.jpeg" alt="Che cosa è lo scriptPubKey? Come si valida la transazione in Bitcoin?" class="wp-image-13455"/><figcaption><a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noreferrer noopener">Slide del video corso Bitcoin dalla teoria alla pratica</a></figcaption></figure>

<p>L’argomento della validazione dello stack, lo stack stesso e le operation code sono argomenti molto ampi e meritano dei video e delle spiegazioni più dettagliate che affrontiamo&nbsp;<a href="https://vimeo.com/r/2Lua/SGVxMVI5ZT" target="_blank" rel="noreferrer noopener"><strong>nel video corso che trovate su Vimeo</strong></a>&nbsp;a metà prezzo, quindi accattateville!</p>

<p>Spero comunque di aver risposto alla tua domanda</p>

<p>Ciao alla prossima!</p>
