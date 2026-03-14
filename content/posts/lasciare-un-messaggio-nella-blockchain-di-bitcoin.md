---
title: "Come lasciare un messaggio nella blockchain di Bitcoin."
date: 2020-06-10T12:47:03+01:00
draft: false


tags:
  - "UTXO"
  - "Script"
---




<section>
<section>
<section>
<section>
<hr />
</section>
<h3><strong>Posso scrivere nella blockchain?</strong></h3>
<h4>Video completo nel <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">canale youtube Bitcoin in Action</a></h4>
<section>
<figure><img src="https://cdn-images-1.medium.com/max/1200/1*ZcxKPepq9_InlwDZ8sjnXQ.png" data-image-id="1*ZcxKPepq9_InlwDZ8sjnXQ.png" data-width="1920" data-height="1080" />&nbsp;
<figcaption>Video completo nel <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">canale youtube Bitcoin in Action</a></figcaption></figure>
<p>Ciao,
Oggi rispondiamo a Luca che ci domanda.
È Possibile scrivere nella blockchain?</p>
<p>Sì, è possibile scrivere nella blockchain, possiamo lasciare un messaggio utilizzando un op code chiamato OP_RETURN, che rende la <strong>UTXO associata (non tutti gli UTXO della tx)</strong>, quindi l’unspent transaction output, inspendibile. Puoi scrivere al massimo 80 bytes.</p>
<p>L’operazione di scrittura viene spesso definita come “timestamping delle informazioni scritte” perchè la transazione che le contiene farà parte di un blocco al quale è associata una marca temporale, un timestamp per l’appunto.</p>
<p>Ricorda però che ogni volta che aggiungiamo delle informazioni alla transazione, aumentiamo il suo peso pagando di conseguenza più fee.</p>
<p>Quando potrebbe essere utile? Ad esempio se vuoi lasciare una fingerprint di un documento marcato temporalmente.</p>
<p>Per questo esempio utilizzeremo la testnet così da poter vedere il messaggio in un explorer.</p>
<blockquote>In Action
</blockquote>
<iframe width="560" height="315" src="https://www.youtube.com/embed/d4H3dAnMbiA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<p>Come prima cosa ottengo un address SegWit dal mio nodo testnet.</p>
<pre>$ bitcoin-cli getnewaddress “” “bech32”</pre>
<pre>tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d</pre>
<p>Otteniamo quindi dei bitcoin dal servizio faucet <a href="https://bitcoinfaucet.uo1.net/send.php" target="_blank" rel="noopener noreferrer" data-href="https://bitcoinfaucet.uo1.net/send.php">https://bitcoinfaucet.uo1.net/send.php</a></p>
<p>Possiamo verificare che la txid sia in mempool con la chiamata:</p>
<pre>$ bitcoin-cli getrawmempool | grep c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a</pre>
<p>dove c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a rappresenta la mia txid ottenuta dal servizio faucet.</p>
<p>Appena la transazione è minata possiamo recuperare la UTXO con il comando listunspent.</p>
<pre>$ bitcoin-cli listunspent 1 101 ‘[“tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d”]’ | jq</pre>
<pre>[</pre>
<pre>{</pre>
<pre>“txid”: “c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a”,</pre>
<pre>“vout”: 1,</pre>
<pre>“address”: “tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d”,</pre>
<pre>“label”: “”,</pre>
<pre>“scriptPubKey”: “00141a10dfb322436bc2177358a8fd876e6ebf5658a3”,</pre>
<pre>“amount”: 0.00100000,</pre>
<pre>“confirmations”: 6,</pre>
<pre>“spendable”: true,</pre>
<pre>“solvable”: true,</pre>
<pre>“desc”: “wpkh([3a46ecca/0'/0'/4']020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f)#kxjva7dw”,</pre>
<pre>“safe”: true</pre>
<pre>}</pre>
<pre>]</pre>
<p>Dopo di che recupero la chiave privata del mio indirizzo, indispensabile per firmare la transazione.</p>
<pre>$ bitcoin-cli dumpprivkey tb1qrggdlvezgd4uy9mntz50mpmwd6l4vk9rm4ft3d</pre>
<pre>cPHTHs7ERe6jDYiitj9eLVswsX3RpeKMB19eXYjpLb4CkEHd7drq</pre>
<p>Generiamo il messaggio che vogliamo inserire nella blockchain, ad esempio <a href="http://corsocompleto.bitcoininaction.com" target="_blank" rel="noopener noreferrer" data-href="http://corsocompleto.bitcoininaction.com">corsocompleto.bitcoininaction.com</a> nel suo formato esadecimale.</p>
<pre>$ printf “corsocompleto.bitcoininaction.com” | xxd -ps</pre>
<pre>636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d</pre>
<p>Per creare la transazione devo usare il metodo createrawtransaction. Utilizzando help possiamo analizzare tutti i parametri a nostra disposizione.</p>
<p>bitcoin-cli help createrawtransaction</p>
<p>Il destinatario della transazione è l’address del faucet</p>
<pre>2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE</pre>
<p>Ho tutto il necessario per creare la mia transazione utilizzando la chiamata createrawtransaction.</p>
<p>Come valore di data inserisco l’esadecimale che voglio scrivere nella blockchain, il quale mi creerà una UTXO OP_RETURN.</p>
<pre>$ bitcoin-cli createrawtransaction ‘[{“txid”:”c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a”,”vout”:1}]’ ‘[{“2NGZrVvZG92qGYqzTLjCAewvPZ7JE8S8VxE”:0.00099000},{“data”:”636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d”}]’</pre>
<pre>02000000019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d00000000</pre>
<p>In questo caso effettuo una sola transazione nella quale sposto tutto il mio input, non necessito quindi di un change address, ovvero di un indirizzo di resto, dato che il resto non è presente. Inoltre non ho utilizzato tutto il mio output perchè parte di questo è destinato alle fee.</p>
<p>La transaction data è stata quindi creata. Il prossimo step è firmarla e inviarla verso il secondo indirizzo. il metodo da utilizzare è signrawtransactionwithkey</p>
<pre>$ bitcoin-cli signrawtransactionwithkey 02000000019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d00000000 ‘[“cPHTHs7ERe6jDYiitj9eLVswsX3RpeKMB19eXYjpLb4CkEHd7drq”]’ ‘[{“txid”:”c5ce66d638f1b8ca702dfb8f7d1da7a6707d9c6497212dc66829c99f69b28b9a”,”vout”:1,”scriptPubKey”:”00141a10dfb322436bc2177358a8fd876e6ebf5658a3",”amount”:0.00100000}]’</pre>
<pre>{</pre>
<pre>“hex”: “020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000”,</pre>
<pre>“complete”: true</pre>
<pre>}</pre>
<p>La transazione è stata firmata con successo, possiamo adesso inviare la transazione, utilizzando il medito sendrawtransaction.</p>
<pre>$ bitcoin-cli sendrawtransaction 020000000001019a8bb2699fc92968c62d2197649c7d70a6a71d7d8ffb2d70cab8f138d666cec50100000000ffffffff02b88201000000000017a914ffd0dbb44402d5f8f12d9ba5b484a2c1bb47da42870000000000000000236a21636f72736f636f6d706c65746f2e626974636f696e696e616374696f6e2e636f6d0247304402205688399cb5a230f050330e2bc6d04d9864d459f85fec48a0118ca31be9239d530220228d7c04fe9e6eea3690033c01ed222284efaa01b28a9a7cae809bdb32d7ce7a0121020d12775323bbdaf0cb6e9a2b44ae7a591ef5872364e80e363a93d283c10b9e4f00000000</pre>
<pre>edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548</pre>
<p>Ottenendo cosi la transaction id.</p>
<p>Adesso possiamo utilizzare un qualsiasi explorer per verificare la transazione, ad esempio <a href="https://tbtc.bitaps.com/" target="_blank" rel="noopener noreferrer" data-href="https://tbtc.bitaps.com/">https://tbtc.bitaps.com/</a> e inseriamo la <a href="https://tbtc.bitaps.com/edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548" target="_blank" rel="noopener noreferrer" data-href="https://tbtc.bitaps.com/edee419f93521f43259b763ffb42e4b882504534494381b7e18057015a27c548">transaction id</a> appena ottenuta.</p>
<p>La transazione è stata inviata correttamente ed è in attesa di essere minata. Contiene giustamente due output, uno verso il destinatario e l’altro è un OP_RETURN con il nostro messaggio.</p>
<p>Abbiamo visto con esempi pratici come sia possibile scrivere nella blockchain, utilizzando l’operation code OP_RETURN che rende l’UTXO associato inspendibile. È comunque sconsigliato scrivere nella blockchain se non strettamente necessario.</p>
<p>Per ottimizzare, in termini di fee e spazio occupato, le scritture sulla blockchain di Bitcoin si consiglia di utilizzare <a href="https://opentimestamps.org/" target="_blank" rel="noopener noreferrer" data-href="https://opentimestamps.org/">OpenTimestamps</a> invece che reinventare la ruota!</p>
<p>Ciao alla prossima</p>
</section><section>
<hr />
<p>🎥 <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">Canale youtube — Bitcoin in Action</a></p>
<p>—</p>
<p>📖 <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a>
—
📖 <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a></p>
<p>📖 <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a>
—
🎥 <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a></p>
<p>—</p>
<p>I nostri social:
► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a> , <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a href="https://www.linkedin.com/company/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/satoshiwantsyou">Linkedin</a>, <a href="https://medium.com/@satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou/">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a></p>
<p>Television isn’t a good idea (Radio Stations)
Email isn’t a good idea (Post offices)
Amazon isn’t a good idea (Retail stores)
Bitcoin isn’t a good idea (Central banks)</p>
<p>In <strong>crypto</strong> we trust</p>
</section>
</section><section>
</section>
</section>
</section><section></section>