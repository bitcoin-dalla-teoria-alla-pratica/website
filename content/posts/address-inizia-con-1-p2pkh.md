---
title: "Perché il mio address inizia con 1?"
date: 2020-07-01T12:26:24+01:00
draft: false

tags:
  - "Script"
  - "Crittografia"
---

<section><section><section><section><section>
<section>
<hr />
<p>Ciao,</p>
<p>oggi rispondiamo a Marco che ci domanda:</p>
<p>Perché il mio address inizia con il numero 1? Ho visto altri address che iniziato con il numero 3, che differenze ci sono?</p>
<p>Allora Marco, il tuo address inizia con il numero 1 perchè sta utilizzando lo script Pay to Public key hash (<strong>P2PKH</strong>). L’address si ricava utilizzando delle funzioni crittografiche proprio sullo script che stiamo utilizzando, in <strong>P2PKH</strong> si ottiene il prefisso 1 dopo aver applicato SHA256 e RIPEMD160 sulla chiave pubblica compressa, preceduto dal version prefix di riferimento. Nel video corso e nel nostro libro si ottiene un address <strong>P2PKH</strong> partendo da una chiave privata, generata da zero.</p>
<p>Quando invece vedi address che iniziano con il numero 3, significa che la persona sta utilizzando un address Pay to script hash (P2SH), ed infine se vedi un address che inizia con bc1, significa che sta utilizzando SegWit.</p>
<p>In realtà non esistono address, ma esistono digest di script, il quale prende il nome di address.</p>
<p>Gli script quindi sono nati grazie a nuove implementazioni da parte della community Bitcoin al fine di migliorarne le prestazioni.</p>
<p>Vediamo con un esempio l’address P2PKH. Ad un certo punto vi lancio una sfida, dove in palio c’è una copia del libro Bitcoin dalla teoria alla pratica.</p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/--oq3SbK2xQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>Per questo esempio utilizzeremo l’ambiente mainnet.Se non hai <a style="background-color: var(--mdc-theme-surface,#fff);" href="https://medium.com/@satoshiwantsyou/come-si-utilizza-un-nodo-bitcoin-ff0e0a785886" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou/come-si-utilizza-un-nodo-bitcoin-ff0e0a785886">un nodo guarda questo articolo</a>
</figure>
<p>Utilizzo il metodo <strong>getnewaddress</strong>:</p>
<pre>$ bitcoin-cli getnewaddress “” “legacy”</pre>
<pre>1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU</pre>
<p>Ottengo così un address P2PKH. Il secondo parametro lasciato vuoto, rappresenta la label, utile per cercare un address particolare all’interno di Bitcoin core. Per ispezionare più a fondo l’address ottenuto, è possibile utilizzare il metodo <strong>getaddressinfo</strong>:</p>
<pre>$ bitcoin-cli getaddressinfo 1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU</pre>
<pre>{</pre>
<pre>“address”: “1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU”,</pre>
<pre>“scriptPubKey”: “76a9149917a0e372343fde946253d1c60c7f479925b1e288ac”,</pre>
<pre>“ismine”: true,</pre>
<pre>“solvable”: true,</pre>
<pre>“desc”: “pkh([5975a740/0'/0'/2']02413df2a3977bb663c4fc7418e7e004129c5cfc2d3d2bb6c9210ea8ee13769610)#wsy7apvp”,</pre>
<pre>“iswatchonly”: false,</pre>
<pre>“isscript”: false,</pre>
<pre>“iswitness”: false,</pre>
<pre>“pubkey”: “02413df2a3977bb663c4fc7418e7e004129c5cfc2d3d2bb6c9210ea8ee13769610”,</pre>
<pre>“iscompressed”: true,</pre>
<pre>“label”: “”,</pre>
<pre>“ischange”: false,</pre>
<pre>“timestamp”: 1588801569,</pre>
<pre>“hdkeypath”: “m/0'/0'/2'”,</pre>
<pre>“hdseedid”: “27eae26f0861d81dfde79537fdbb0b8273f00211”,</pre>
<pre>“hdmasterfingerprint”: “5975a740”,</pre>
<pre>“labels”: [</pre>
<pre>{</pre>
<pre>“name”: “”,</pre>
<pre>“purpose”: “receive”</pre>
<pre>}</pre>
<pre>]</pre>
<pre>}</pre>
<p>il quale restituisce un pò di informazioni, tra cui la chiave pubblica compressa , la derivation path e lo scriptPubKey.</p>
<p>Nello <strong>scriptPubKey</strong> è possibile trovare lo script da soddisfare per sbloccare la UTXO di riferimento. Per <strong>UTXO</strong> si intente la Unspent transaction output.</p>
<p>Sfruttando un altro metodo messo a disposizione da Bitcoin core, possiamo approfondire ulteriormente lo script.</p>
<pre>$ bitcoin-cli decodescript 76a9149917a0e372343fde946253d1c60c7f479925b1e288ac</pre>
<pre>{</pre>
<pre>“asm”: “OP_DUP OP_HASH160 9917a0e372343fde946253d1c60c7f479925b1e2 OP_EQUALVERIFY OP_CHECKSIG”,</pre>
<pre>“reqSigs”: 1,</pre>
<pre>“type”: “pubkeyhash”,</pre>
<pre>“addresses”: [</pre>
<pre>“1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU”</pre>
<pre>],</pre>
<pre>“p2sh”: “3Ae5soRJUqiqZgfvFxVaLTZs2PrdqvjDTL”,</pre>
<pre>“segwit”: {</pre>
<pre>“asm”: “0 9917a0e372343fde946253d1c60c7f479925b1e2”,</pre>
<pre>“hex”: “00149917a0e372343fde946253d1c60c7f479925b1e2”,</pre>
<pre>“reqSigs”: 1,</pre>
<pre>“type”: “witness_v0_keyhash”,</pre>
<pre>“addresses”: [</pre>
<pre>“bc1qnyt6pcmjxslaa9rz20guvrrlg7vjtv0ztsmjag”</pre>
<pre>],</pre>
<pre>“p2sh-segwit”: “3Mi5vTHySS8iCRpK2TWnTXsxU8FTDHQ3SQ”</pre>
<pre>}</pre>
<pre>}</pre>
<p>Le informazioni che otteniamo sono molto interessanti.</p>
<p>Abbiamo i diversi tipi di address, quindi <strong>P2SH</strong>, <strong>Wrapped Segwit</strong> e <strong>SegWit</strong> nativo.</p>
<p> Alla prima riga abbiamo lo script <strong>P2PKH</strong>, <strong>asm</strong> significa assembly. Le OP che si leggono sono le operation code del linguaggio script. Ogni volta che si utilizza un <strong>P2PKH</strong>, Sarà effettuato <strong>HASH160</strong> sulla chiave pubblica il quale digest deve essere identico a quello della UTXO di riferimento.</p>
<p>Per questo prende il nome di <strong>Public key hash</strong>. Ovviamente poi viene verificata anche la firma grazie all’op code <strong>OP_CHECKSIG</strong>.</p>
<p>Come premesso all’inizio del video, l’address è il digest dello <strong>SHA256</strong> e del <strong>RIPEMD160</strong> della chiave pubblica compressa preceduta dal version prefix. Nella wiki di <a href="https://en.bitcoin.it/wiki/List_of_address_prefixes" target="_blank" rel="noopener noreferrer" data-href="https://en.bitcoin.it/wiki/List_of_address_prefixes">Bitcoin</a> vediamo che per ottenere un address per l’ambiente mainnet dobbiamo utilizzare un byte di 0.</p>
<p>Quindi con l’aiuto di variabili d’ambiente, salvo il digest dello <strong>SHA256</strong> della chiave pubblica compressa all’interno della variabile d’ambiente <strong>ADDR_SHA</strong></p>
<pre>$ ADDR_SHA=`printf 02413df2a3977bb663c4fc7418e7e004129c5cfc2d3d2bb6c9210ea8ee13769610 | xxd -r -p | openssl sha256| sed ‘s/^.* //’`</pre>
<p>Utilizzo il <strong>digest</strong> appena ottenuto per ottenere il digest della funzione crittografica <strong>ripemd160</strong></p>
<pre>$ ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed ‘s/^.* //’`</pre>
<p>ed infine ottengo l’address, utilizzando <strong>base58</strong> comprensivo di checksum. <strong>Base58</strong> non è una funzione crittografica ma un encoding.</p>
<pre>$ printf 00$ADDR_RIPEMD160 | xxd -p -r | base58 -c</pre>
<pre>1ExUh5vqcUjuuocAgnSyAJ74iBiRHBwnAU</pre>
<p>Ottenendo l’address <strong>mainnet</strong>.</p>
<p>E qui la sfida, come ottengo l’address di testnet?</p>
<p>Chi posta (sul nostro <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">canale youtube</a>) la risposta corretta per primo, riceve in omaggio il libro Bitcoin dalla teoria alla pratica!</p>
<p>Grazie a questo esempio abbiamo capito perchè <strong>P2PKH</strong> inizia con il numero 1. Vi ricordo che il più veloce a rispondere al commento con la risposta esatta riceverà gratuitamente una copia di <strong>Bitcoin dalla teoria alla pratica</strong>, che copre molto più dettagliatamente la generazione dell’address.</p>
<p>Ciao alla prossima</p>
</section><section>
<hr />
<p> — –</p>
<p>🐙 GitHub:<a href="https://bit.ly/2Lj3yeY" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/2Lj3yeY"> https://bit.ly/2Lj3yeY</a></p>
<p> — –</p>
<p>📖 Libro Bitcoin dalla teoria alla pratica (Amazon): <a href="https://amzn.to/2Ldym0F" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ldym0F">https://amzn.to/2Ldym0F</a></p>
<p>📖 Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin): <a href="http://bit.ly/2ADHUN1" target="_blank" rel="noopener noreferrer" data-href="http://bit.ly/2ADHUN1">http://bit.ly/2ADHUN1</a></p>
<p>📖 <a href="https://amzn.to/2Ym4gz6" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ym4gz6">Book Bitcoin from theory to practice</a>: <a href="https://amzn.to/2Ym4gz6" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ym4gz6">https://amzn.to/2Ym4gz6</a></p>
<p> — –</p>
<p>🎥 Video Corso Bitcoin dalla teoria alla pratica: <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">https://bit.ly/3cUJDyZ</a></p>
<p> — –</p>
<p>📖 Tascabile Bitcoin 199 domande (Amazon): <a href="https://amzn.to/3ckIkJj" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3ckIkJj">https://amzn.to/3ckIkJj</a></p>
<p>📖 Tascabile Bitcoin 199 domande (pagamento in bitcoin): <a href="https://bit.ly/3cmz07W" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cmz07W">https://bit.ly/3cmz07W</a></p>
<p> — –</p>
<p>📖 Pocket Bitcoin 199 questions (Amazon): <a href="https://amzn.to/3fB4Kbs" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3fB4Kbs">https://amzn.to/3fB4Kbs</a></p>
<p>📖 Pocket Bitcoin 199 questions (pagamento in bitcoin): <a href="https://bit.ly/2SUNzYz" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/2SUNzYz">https://bit.ly/2SUNzYz</a></p>
<p> — –</p>
<p>► Sito ufficiale: <a href="https://www.corsobitcoin.com/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/">https://www.corsobitcoin.com/</a></p>
<p>► Twitter: <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">https://twitter.com/satoshiwantsyou</a></p>
<p>► Facebook: <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">https://www.facebook.com/satoshiwantsyou</a></p>
<p>► Linkedin: <a href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica">https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica</a></p>
<p>► Medium: <a href="https://medium.com/@satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou">https://medium.com/@satoshiwantsyou</a></p>
<p>► Instagram: <a href="https://www.instagram.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou">https://www.instagram.com/satoshiwantsyou</a></p>

</section>
<section>
</section>
</section></section></section></section></section><section></section>