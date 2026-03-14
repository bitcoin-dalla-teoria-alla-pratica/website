---
title: "Che cosa è lo SHA256?"
date: 2020-06-18T14:17:03+01:00
draft: false


tags:
  - "Crittografia"
  - "Mining & Blockchain"
---




<section>
<section>
<section>
<section>
<section>

<hr>

Ciao,
Una delle domande ricorrenti che ci viene fatta durante i nostri corsi è: Che cosa è l’algoritmo SHA256 e dove viene utilizzato?
In Bitcoin l’algoritmo SHA256 viene utilizzato in molti scenari, dalla creazione dell’address, al calcolo della TXID fino ad arrivare all’identificativo del blocco, o per meglio dire, nella proof of work.
SHA è l’acronimo di <strong>Secure Hash Algorithm</strong>, il suo scopo è prendere in ingresso una dei byte, ad esempio una stringa, quindi del testo, di una lunghezza arbitraria e restituire un’altra stringa lunga sempre lunga 256 bit, dato che stiamo utilizzando SHA256.
È un algoritmo<strong> One Way (senza funzione inversa)</strong>, questo significa che dal risultato ottenuto, chiamato digest (spesso si usa erroneamente il termine hash al posto di digest), non è possibile risalire al messaggio originale, chiamato anche anche messaggio in chiaro. Diciamo che risalire al messaggio in chiaro è talmente improbabile che possiamo dire che è impossibile, questo perchè il digest contiene troppe poche informazioni per effettuare questa operazione.
Una volta lessi che è come trovare un atomo nell’universo, credo che sia difficile.
Cerchiamo di fare chiarezza con un esempio.
<blockquote>In Action</blockquote>
<figure>
<iframe style="background-color: var(--mdc-theme-surface,#fff);" src="https://www.youtube.com/embed/oooUGOTfVx0" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
Bene, creiamo subito un digest, utilizzando il messaggio in chiaro <strong>bitcoininaction</strong>
<pre>$ printf bitcoininaction | openssl dgst -sha256</pre>
<pre>(stdin)= b76b7041106a75de9fa4fbf880b3886cc114cbfd570e1a17adb58b937afee351</pre>
Dal digest è quindi impossibile capire che il messaggio in chiaro fosse bitcoininaction.
Che cosa succede se applico nuovamente la funzione crittografica SHA256 a <a href="http://bitcoininaction.com" target="_blank" rel="noopener noreferrer" data-href="http://bitcoininaction.com">bitcoininaction</a>?
Se la vostra risposta è stata: Ottengo lo stesso risultato, avete dato la risposta esatta.
<pre>$ printf bitcoininaction | openssl dgst -sha256</pre>
<pre>(stdin)= b76b7041106a75de9fa4fbf880b3886cc114cbfd570e1a17adb58b937afee351</pre>
Che cosa succede se cambio leggermente il messaggio in chiaro, ad esempio <a href="http://bitcoininaction.com/" target="_blank" rel="noopener noreferrer" data-href="http://bitcoininaction.com/">bitcoininaction.com</a>?
<pre>$ printf bitcoininaction.com | openssl dgst -sha256</pre>
<pre>(stdin)= 41dbcc447756ddd2c32ac99c76ef6f090fa0a63da5a6ecfda3311936f85daa85</pre>
Ottengo un digest completamente diverso. È per questo motivo che è molto veloce verificare un digest se si è in possesso del messaggio in chiaro. Ogni messaggio in chiaro su cui è applicato l’algoritmo SHA256 produce un digest unico. Se due messaggi diversi producessero lo stesso digest avremo un fenomeno chiamato collisione.
Ok, tutto interessante, ma voglio vedere almeno un esempio di Bitcoin!
Otteniamo quindi l’hash della transazione effettuata nel video “<a href="https://www.youtube.com/watch?v=d4H3dAnMbiA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/watch?v=d4H3dAnMbiA">Posso scrivere nella blockchain</a>”.
Per fare questa operazione dobbiamo effettuare due volte la funzione crittografica SHA256 e ottenere la sua rappresentazione in little endian. Molto brevemente Big Endian e Little Endian coinvolgono l’ordine dei byte.
<ul>
 	<li><em>big-endian</em>: Si ha la memorizzazione dal byte più significativo per finire col meno significativo.</li>
 	<li><em>little endian</em>: Si ha la memorizzazione dal byte meno significativo per finire col più significativo.</li>
</ul>
La transazione è stata fatta nella blockchain di testnet e ha come txid: <a href="https://tbtc.bitaps.com/edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548" target="_blank" rel="noopener noreferrer" data-href="https://tbtc.bitaps.com/edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548">edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548</a>
Recuperiamo quindi la transazione con il comando getrawtransaction.
<pre><strong>$</strong> bitcoin-cli getrawtransaction edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548 2</pre>
<pre>{</pre>
<pre>“txid”: “edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548”,</pre>
<pre>“hash”: “12cf1e132b1d775f5403a875592b447a825f493c0eecdf6bbaa8f5e759c1c71d”,</pre>
<pre>...</pre>
<pre>“hex”: “020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000”,</pre>
<pre>...</pre>
<pre>}</pre>
L’hash è <strong>12cf1e132b1d775f5403a875592b447a825f493c0eecdf6bbaa8f5e759c1c71d</strong> ed è quella che noi dobbiamo ottenere. Dobbiamo applicare l’algoritmo SHA256 per due volte e ottenere la sua rappresentazione in little endian.
Ottengo il primo digest.
<pre>$ printf 020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000 | xxd -r -p | sha256sum -b</pre>
<pre>33bf8e3e54327c84758e3442ccea54cfef3621ee4d7276cc1bdcde301d4c4796</pre>
Applichiamo nuovamente lo SHA256 al digest ottenuto, per ottenere il secondo digest.
<pre>$ printf 33bf8e3e54327c84758e3442ccea54cfef3621ee4d7276cc1bdcde301d4c4796 | xxd -r -p | sha256sum -b</pre>
<pre>1dc7c159e7f5a8ba6bdfec0e3c495f827a442b5975a803545f771d2b131ecf12</pre>
Ed infine otteniamo la sua rappresentazione in little endian
<pre><strong>$</strong> printf 1dc7c159e7f5a8ba6bdfec0e3c495f827a442b5975a803545f771d2b131ecf12 | tac -rs ..</pre>
<pre>12cf1e132b1d775f5403a875592b447a825f493c0eecdf6bbaa8f5e759c1c71d</pre>
Il risultato coincide!
Quello che abbiamo appena messo in pratica è solo un caso di dove e come il protocollo Bitcoin utilizza questo tipo di Algoritmo, ovviamente non è l’unico algoritmo ad essere utilizzato, ad <strong>RIPEMD-160</strong> viene usato durante la generazione degli address. Come sempre il codice è disponibile nel nostro repository GitHub che trovare in descrizione e vi invito a lasciare domande nei commenti e se vi va iscrivetevi.
Ciao alla prossima
🎥 <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">Canale youtube — Bitcoin in Action</a>
—
🐙 GitHub:<a href="https://bit.ly/2Lj3yeY" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/2Lj3yeY"> https://bit.ly/2Lj3yeY</a>
—
📖 <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a>
—
📖 <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a>
📖 <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a>
—
🎥 <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a>
—
I nostri social:
► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a>&nbsp;, <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a href="https://www.linkedin.com/company/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/satoshiwantsyou">Linkedin</a>, <a href="https://medium.com/@satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou/">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a>
Television isn’t a good idea (Radio Stations)
Email isn’t a good idea (Post offices)
Amazon isn’t a good idea (Retail stores)
Bitcoin isn’t a good idea (Central banks)
In <strong>crypto</strong> we trust</figure>
</section>
</section>
</section>
</section>
</section>
<section></section>