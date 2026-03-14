---
title: "Transazione P2PKH nel Bitcoin Playground!"
date: 2021-03-17T10:21:28+01:00
draft: false


tags:
  - "Script"
  - "Crittografia"
---




<figure class="wp-block-gallery columns-1 is-cropped"><ul class="blocks-gallery-grid"><li class="blocks-gallery-item"><figure><img src="https://www.corsobitcoin.com/wp-content/uploads/2021/03/Youtube-2-1024x576.png" alt="" data-id="13537" data-full-url="https://www.corsobitcoin.com/wp-content/uploads/2021/03/Youtube-2.png" data-link="https://www.corsobitcoin.com/?attachment_id=13537" class="wp-image-13537"/></figure></li></ul></figure>

<figure class="ip iq ir is it iu fb fc paragraph-image">
<div class="iv iw ah ix w iy" tabindex="0" role="button">
<div class="fb fc jz">
<div class="jd s ah je">
<div class="ka jg s">
<div class="ec iz ff et eq ja w dv jb jc">
<p class="graf graf--p">Dopo alcuni articoli di teoria, siamo arrivati alla pratica. In questo video analizzeremo come sia possibile creare una transazione P2PKH utilizzando un nodo bitcoin in modalità Regtest.</p>
<p class="graf graf--p">Per questo esempio utilizzeremo un progetto che stiamo portando avanti io a Alessandro, ovvero un <a class="markup--anchor markup--p-anchor" href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/" target="_blank" rel="noopener noreferrer" data-href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/">playground</a>. Faremo un video dettagliato prima possibile, ma per adesso vi basta pensare che è, accedendo dei container docker, abbiamo a disposizione due nodi, Hansel e Gretel, che parlano tra loro, e alcuni utility tra cui un blockchain explorer.</p>
<p class="graf graf--p">Se volete replicare l’esempio che stiamo per vedere, potete creare il vostro ambiente di lavoro, clonando il progetto e seguendo le istruzioni che trovate nella pagina del playground.</p>
<p> </p>
</div>
</div>
</div>
</div>
</div>
</figure>
<p><iframe src="https://www.youtube.com/embed/_9C958OkcMs" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe></p>
<p> </p>

<p>Creeremo una transazione P2PKH utilizzando il nodo <strong>Bitcoin</strong> con la versione 0.21.0 e analizzeremo come la transazione è validata.‌</p>

<p>Per rendere le cose più semplici da spiegare, partiremo da una blockchain <em>vuota</em>, quindi prima di lanciare i container, utilizzo il comando&nbsp;<code>./regtest-delete.sh</code>, e successivamente avvio i container con <code>docker-compose up</code>. Il prossimo passaggio è sarà quello di entrare nel container di hansel, ovvero di un nodo:</p>

<pre class="wp-block-preformatted">$ docker exec -ti hansel bash‌</pre>

<p>e verificare che la blockchain abbia 0 blocchi, utilizzando il comando:</p>

<pre class="wp-block-preformatted">$ bitcoin-cli getblockcount</pre>

<p>‌La prima operazione che vado a fare è creare un wallet, con il comando:</p>

<pre class="wp-block-preformatted">$ bitcoin-cli createwallet "hansel"‌</pre>

<p>Successivamente creo l’address del mittente e l’address del destinatario. Utilizzerò delle variabili d’ambiente per salvare il contenuto.</p>

<pre class="wp-block-preformatted">$ ADDR_MITT=$(bitcoin-cli getnewaddress 'mitt' 'legacy')</pre>

<pre class="wp-block-preformatted">$ ADDR_DEST=$(bitcoin-cli getnewaddress 'dest' 'legacy')‌</pre>

<p>In questo momento i miei wallet non hanno nessuna UTXO, ovvero non hanno nessun bitcoin disponibile, quindi mineremo 101 blocchi (in modo tale da soddisfare la <code>COINBASE_MATURITY</code>) utilizzando l'address <code>$ADDR_MITT</code>.</p>

<pre class="wp-block-preformatted">$ bitcoin-cli generatetoaddress 101 $ADDR_MITT &gt; /dev/null</pre>

<p>‌Adesso ho dei bitcoin a disposizione, o meglio delle UTXO, per visualizzarli posso usare la chiamata <code>listunspent</code>, la quale mi mostra tutte i saldi a disposizione. Utilizzo anche il Json Parser, JQ, per aiutarmi a estrapolare solamente le informazioni necessarie per effettuare la transazione.</p>

<p>‌Per prima cosa salvo tutta la UTXO all’interno della variabile d’ambiente <code>$UTXO</code></p>

<pre class="wp-block-preformatted">$ UTXO=$(bitcoin-cli listunspent | jq -r .[0])‌</pre>

<p>Successivamente creo la transazione utilizzando la chiamata sendtoaddress, utilizzando una fee_rate e decidendo di sottrarre le fees direttamente dall’amount.</p>

<pre class="wp-block-preformatted">$ TXID=$(bitcoin-cli -named sendtoaddress address="$ADDR_DEST" amount=$(echo $UTXO | jq -r .amount) fee_rate=25 subtractfeefromamount=true)</pre>

<p>‌Adesso possiamo finalmente analizzare la nostra transazione, la quale si troverà nella mempool, e quindi in attesa di essere minata.</p>

<p>‌Per analizzarla possiamo utilizzare il comando <code>getrawtransaction</code>, e utilizzare la TXID appena ottenuta</p>

<pre class="wp-block-preformatted">$ bitcoin-cli getrawtransaction $TXID 2 | jq</pre>

<p>‌Nel libro <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" rel="noreferrer noopener" target="_blank">Libro Bitcoin dalla teoria alla pratica</a> e <a href="https://bit.ly/38RtF9x" rel="noreferrer noopener" target="_blank">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</a>&nbsp;, spieghiamo byte per byte la transazione. Grazie al nostro docker, è possibile visualizzare la blockchain locale a anche la transazione che è in mempool.‌</p>

<p>In questo caso la nostra transazione ha come ID <code>49021cb4a1ebb0c74feaa3a9df2ea7e3e74afeb50df9a630023e8822786add73</code>, inserendola nel campo di ricerca otteniamo un qualcosa di simile:</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*bN27G2JpbjEX9q8R" alt=""/></figure>

<p>Enter a caption for this image (optional)</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*T39vSZow5NCYPzat" alt=""/></figure>

<p>Enter a caption for this image (optional)</p>

<p>‌Come possiamo analizzare lo stack e la sua esecuzione?</p>

<p>‌Utilizziamo il progetto btcdeb! I vostri parametri potrebbero cambiare, ma se avete seguito alla lettera il tutorial, lanciando questo comando, lo stack si popolerà.</p>

<pre class="wp-block-preformatted">$ btcdeb --tx=$(bitcoin-cli getrawtransaction $TXID) --txin=$(bitcoin-cli getrawtransaction $(echo $UTXO | jq -r .txid))‌</pre>

<p>Al momento dell’avvio lo stack è vuoto, e premendo e digitando step, si effettua l’operazione successiva.‌</p>

<p>In questo caso con step, si inserisce prima lo scriptSig, ovvero la firma e successivamente la chiave pubblica compressa.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*-sLbsoN2loXlqKBD" alt=""/></figure>

<p>I vostri valori saranno sicuramente diversi, ma la logica non cambia.‌</p>

<p>Successivamente abbiamo lo scriptPubKey. Il primo elemento che inseriamo è <code>OP_DUP</code>, che come abbiamo visto nelle precedenti lezioni, duplica l'elemento on top, quindi la nostra chiave pubblica non compressa.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*LuBMgRKdTVUj5RE3" alt=""/></figure>

<p>Successivamente, l’operazione che si effettua è <code>HASH160</code>, che ha il compito di prendere l'elemento on top e applicare la funzione crittografica <code>SHA256</code> e <code>RIPEMD160</code>.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*t2_RmtsNIoDKcWTE" alt=""/></figure>

<p>‌Successivamente si inserisce l’hash della chiave pubblica compressa.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*5E9nmNLjOesNnZeM" alt=""/></figure>

<p>La prossima OP_CODE è <code>OP_EQUALVERIFY</code>, la quale ha il compito di verificare due elementi, e se sono uguale non inserire niente, altrimenti invalida lo stack.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*WACV8rfFHnf4uW95" alt=""/></figure>

<p>In questo caso sono uguali, e quindi non viene inserito niente e lo stack è ancora valido. Ultimo OP_CODE, <code>OP_CHECKSIG</code>, come è facile intuire, controlla la firma confrontandola utilizzando la chiave pubblica corrispondente.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*jrWlxNm4Iqi0DeVU" alt=""/></figure>

<p>Se non ricordi come si verifica la firma digitale, <a href="https://www.youtube.com/watch?v=RU7LHPP4Lvk&amp;list=PLpPLK7SGHncab_so9rB7lY3aKe2-Mqs5y&amp;index=18" rel="noreferrer noopener" target="_blank">guarda questo video</a>.‌</p>

<p>Le operazioni che si effettuano sono, POP della chiave pubblica, pop della firma, e verifica della firma stessa. Se la verifica va a buon fine, si pusha 1, validando la transazione.‌</p>

<p>Le operazioni che abbiamo fatto, sono le stesse che abbiamo visto nel video <a href="https://youtu.be/DW_YSbIGi1g" rel="noreferrer noopener" target="_blank">“Come si valida una Transazione P2PKH”</a>.‌</p>

<p>Di seguito è riportata la lavagna utilizzata durante quel video:</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*kJbcJz7xmccihlbU" alt=""/></figure>

<p>Che cosa ci rimane da fare?‌</p>

<p>Minare!</p>

<pre class="wp-block-preformatted">$ bitcoin-cli generatetoaddress 1 $ADDR_MITT</pre>

<p>‌A questo punto, utilizzando il nostro <a href="http://localhost:8094/" rel="noreferrer noopener" target="_blank">explorer</a>, potete analizzare l’ultimo blocco minato, il quale conterrà 2 transazioni, la coinbase e la transazione appena creata.</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/0*Ist7i7jvWgtc2QMs" alt=""/></figure>

<p>Se volete divertivi con il nostro playground, ecco il link! <a href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/" rel="noreferrer noopener" target="_blank">https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground/</a></p>

<p>Ciao alla Prossima!</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/1*xJ46DzU4Jtgee-KGw6ezFA.jpeg" alt=""/><figcaption><a href="https://bit.ly/38RtF9x" rel="noreferrer noopener" target="_blank">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</a> e <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" rel="noreferrer noopener" target="_blank">Bitcoin dalla teoria alla&nbsp;pratica</a></figcaption></figure>

<p>–––––</p>

<p>🐳 <a href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground" rel="noreferrer noopener" target="_blank">Playground Bitcoin in Action</a></p>

<p>🎥 <a href="https://www.youtube.com/BitcoinInAction" rel="noreferrer noopener" target="_blank">Bitcoin in Action (YouTube)</a></p>

<p>—</p>

<p>🐙 GitHub:<a href="https://bit.ly/2Lj3yeY" rel="noreferrer noopener" target="_blank"> https://bit.ly/2Lj3yeY</a></p>

<p>–––</p>

<p>📕 <a href="https://amzn.to/3pJcXj1" rel="noreferrer noopener" target="_blank">Bitcoin In Action – SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></p>

<p>📕 <a href="https://bit.ly/38RtF9x" rel="noreferrer noopener" target="_blank">Bitcoin In Action – SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a></p>

<p>–––</p>

<p>📒 <a href="https://amzn.to/2MOj1av" rel="noreferrer noopener" target="_blank">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>&nbsp;📒 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" rel="noreferrer noopener" target="_blank">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a><br>&nbsp;📒 <a href="https://amzn.to/2Ym4gz6" rel="noreferrer noopener" target="_blank">Book Bitcoin from theory to practice (Amazon)</a></p>

<p>📒 <a href="https://bit.ly/3ijAyC4" rel="noreferrer noopener" target="_blank">Book Bitcoin from theory to practice (accept bitcoin)</a><br>&nbsp; — <br>&nbsp;🎥 <a href="https://bit.ly/3cUJDyZ" rel="noreferrer noopener" target="_blank">Video Corso Bitcoin dalla teoria alla pratica</a></p>

<p>—&nbsp;<br>&nbsp;📙 <a href="https://amzn.to/3ckIkJj" rel="noreferrer noopener" target="_blank">Tascabile Bitcoin 199 domande (Amazon)</a><br>&nbsp;📙 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" rel="noreferrer noopener" target="_blank">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a></p>

<p>📙 <a href="https://amzn.to/3fB4Kbs" rel="noreferrer noopener" target="_blank">Pocket Book Bitcoin 199 questions (Amazon)</a><br>&nbsp;📙 <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" rel="noreferrer noopener" target="_blank">Pocket </a><a href="https://www.amazon.it/dp/1078155585" rel="noreferrer noopener" target="_blank">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" rel="noreferrer noopener" target="_blank">Bitcoin 199 questions (accept bitcoin)</a><br>&nbsp; — <br>&nbsp;► ITA: <a href="https://twitter.com/satoshiwantsyou" rel="noreferrer noopener" target="_blank">Twitter</a>&nbsp;, <a href="https://www.facebook.com/satoshiwantsyou" rel="noreferrer noopener" target="_blank">Facebook</a>, <a href="https://bitcoin-in-action.medium.com/" rel="noreferrer noopener" target="_blank">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" rel="noreferrer noopener" target="_blank">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" rel="noreferrer noopener" target="_blank">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica" rel="noreferrer noopener" target="_blank">GitHub</a></p>

<p>► ENG: <a href="https://twitter.com/btc_in_action" rel="noreferrer noopener" target="_blank">Twitter</a>&nbsp;, <a href="https://www.facebook.com/bitcoininaction/" rel="noreferrer noopener" target="_blank">Facebook</a>, <a href="https://medium.com/@bitcoin_in_action" target="_blank" rel="noreferrer noopener">Medium</a>, <a href="https://www.instagram.com/bitcoin_in_action/" rel="noreferrer noopener" target="_blank">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" rel="noreferrer noopener" target="_blank">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica" rel="noreferrer noopener" target="_blank">GitHub</a></p>

<p>Television isn’t a good idea (Radio Stations)<br>&nbsp;Email isn’t a good idea (Post offices)<br>&nbsp;Amazon isn’t a good idea (Retail stores)<br>&nbsp;Bitcoin isn’t a good idea (Central banks)</p>

<p>In <strong>crypto</strong> we trust</p>
