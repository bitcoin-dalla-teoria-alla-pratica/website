---
title: "Bitcoin Core Gui Vs Cli ⚔️"
date: 2020-12-09T18:52:24+01:00
draft: false


tags:
  - "Nodo & Network"
  - "SegWit"
---




<img class="aligncenter wp-image-13476 size-large" src="https://www.corsobitcoin.com/wp-content/uploads/2020/12/Youtube_c64-1024x576.png" alt="Bitcoin Cli VS GUI" width="640" height="360" />
<p class="graf graf--p">Ciao,</p>
<p class="graf graf--p">Oggi rispondiamo a Roberto che durante una nostra chiacchierata mi ha suggerito di far vedere la GUI di bitcoin-core.</p>
<p class="graf graf--p">Non avevo mai utilizzato la parte grafica, ma mi rendo conto che alcune persone potrebbero preferire la GUI.</p>

<blockquote class="graf graf--blockquote">L’<strong class="markup--strong markup--blockquote-strong">interfaccia grafica</strong>, nota anche come <strong class="markup--strong markup--blockquote-strong">GUI</strong> (dall’<a class="markup--anchor markup--blockquote-anchor" title="Lingua inglese" href="https://it.wikipedia.org/wiki/Lingua_inglese" target="_blank" rel="noopener noreferrer" data-href="https://it.wikipedia.org/wiki/Lingua_inglese">inglese</a> <em class="markup--em markup--blockquote-em">Graphical User Interface</em>), in <a class="markup--anchor markup--blockquote-anchor" title="Informatica" href="https://it.wikipedia.org/wiki/Informatica" target="_blank" rel="noopener noreferrer" data-href="https://it.wikipedia.org/wiki/Informatica">informatica</a> è un tipo di <a class="markup--anchor markup--blockquote-anchor" title="Interfaccia utente" href="https://it.wikipedia.org/wiki/Interfaccia_utente" target="_blank" rel="noopener noreferrer" data-href="https://it.wikipedia.org/wiki/Interfaccia_utente">interfaccia utente</a> che consente l’<a class="markup--anchor markup--blockquote-anchor" title="Interazione uomo-computer" href="https://it.wikipedia.org/wiki/Interazione_uomo-computer" target="_blank" rel="noopener noreferrer" data-href="https://it.wikipedia.org/wiki/Interazione_uomo-computer">interazione uomo-macchina</a> in modo visuale utilizzando rappresentazioni grafiche</blockquote>
<p class="graf graf--p">Tuttavia il mio consiglio è quello di prendere confidenza con il terminale, perchè se installiamo, ad esempio, un nodo su un <a class="markup--anchor markup--p-anchor" href="https://bitcoin-in-action.medium.com/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f?source=your_stories_page-------------------------------------" target="_blank" rel="noopener noreferrer" data-href="https://bitcoin-in-action.medium.com/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f?source=your_stories_page-------------------------------------">raspberry</a> molto probabilmente ci connetteremo in SSH.</p>
<p class="graf graf--p">In questo articolo metteremo in comunicazione la GUI e la riga di comando, così da creare una mini blockchain sul nostro computer.
Per questo esempio utilizzeremo la regtest.</p>

<h4 class="graf graf--h4">In Action</h4>
<iframe src="https://www.youtube.com/embed/iNSh-bhKovE" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<p class="graf graf--p">Ho già installato il nodo sul mio computer, se hai bisogno di installare bitcoin-core, fai riferimento a <a class="markup--anchor markup--p-anchor" href="https://youtu.be/dyFDDH0IOnU" target="_blank" rel="noopener noreferrer" data-href="https://youtu.be/dyFDDH0IOnU">questo video</a>.</p>
<p class="graf graf--p">Prima di avviare Bitcoin-core, specifico di voler utilizzare la <strong class="markup--strong markup--p-strong">regtest.
</strong>Mi sposto nella cartella di default del mac e creo o modifico il file di configurazione.
Se voi non avete la cartella di default Bitcoin, potete crearla, il percorso predefinito del mac è:</p>

<pre class="graf graf--pre">$ cd $HOME/Library/Application\ Support/Bitcoin</pre>
<p class="graf graf--p">Per gli altri sistemi operativi, fare rifermineto <a class="markup--anchor markup--p-anchor" href="https://en.bitcoin.it/wiki/Data_directory" target="_blank" rel="noopener noreferrer" data-href="https://en.bitcoin.it/wiki/Data_directory">alla wiki di Bitcoin</a>.</p>
<p class="graf graf--p">Di seguito è riportata la configurazione del mio nodo:</p>

<pre class="graf graf--pre">regtest=1</pre>
<pre class="graf graf--pre">daemon=1</pre>
<pre class="graf graf--pre">txindex=1</pre>
<pre class="graf graf--pre"># Options only for mainnet</pre>
<pre class="graf graf--pre">[main]</pre>
<pre class="graf graf--pre"># Options only for testnet</pre>
<pre class="graf graf--pre">[test]</pre>
<pre class="graf graf--pre"># Options only for regtest</pre>
<pre class="graf graf--pre">[regtest]</pre>
<p class="graf graf--p">Eliminiamo la cartella regtest, se esiste, così da partire da una blockchain vuota. Avviamo quindi Bitcoin-core versione grafica.
Io per farlo digito:</p>

<pre class="graf graf--pre">$ bitcoin-qt</pre>
<p class="graf graf--p">Dato che ho spostato l’eseguibile nel mio file $PATH. Se non sai come fare, guarda <a class="markup--anchor markup--p-anchor" href="https://youtu.be/keeEdwPigZs" target="_blank" rel="noopener noreferrer" data-href="https://youtu.be/keeEdwPigZs">questo video</a></p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*Ew9VRJsUSi0OMBrkjdhoUw.png" data-image-id="1*Ew9VRJsUSi0OMBrkjdhoUw.png" data-width="1816" data-height="959" />
<figcaption class="imageCaption">Bitcoin Core</figcaption></figure>
<p class="graf graf--p">La regtest è vuota, quindi la blockchain contiene un solo blocco, il <strong class="markup--strong markup--p-strong">genesis block</strong>.
Otteniamo le sue informazioni, così da prendere confidenza con la GUI. Selezionando Window -&gt; console, si aprirà una nuova finestra nella quale abbiamo la possibilità di eseguire dei comandi.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*75XsDPoLery9oj6ug-DfEw.png" data-image-id="1*75XsDPoLery9oj6ug-DfEw.png" data-width="418" data-height="490" />

<figcaption class="imageCaption">Bitcoin Core – Window Console</figcaption></figure>
<p class="graf graf--p">Digitando <strong class="markup--strong markup--p-strong">help</strong> abbiamo tutta la lista del comandi.
Utilizzando <strong class="markup--strong markup--p-strong">getblockhash 0</strong> abbiamo la possibilità di ottenere l’hash del blocco genesi, e con il comando <strong class="markup--strong markup--p-strong">getblock 0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206</strong> possiamo analizzarlo.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*mk5EaHjWlJ-3HYLOfglMgg.png" data-image-id="1*mk5EaHjWlJ-3HYLOfglMgg.png" data-width="744" data-height="424" />

<figcaption class="imageCaption">Bitcoin-Core — Genesis Block</figcaption></figure>
<p class="graf graf--p">Tutto molto simile alla versione bash ovviamente. L’unica differenza degna di nota è che si omette il comando <strong class="markup--strong markup--p-strong">bitcoin-cli</strong>.
Avviamo un secondo nodo, questa volta da terminale. Per prima cosa creo un’altra cartella sempre nel percorso di default, che chiamerò <strong class="markup--strong markup--p-strong">regtest-cli</strong>.</p>

<pre class="graf graf--pre">$ mkdir regtest-cli</pre>
<p class="graf graf--p">Questa cartella ospiterà la blockchain e tutti i dati del <strong class="markup--strong markup--p-strong">secondo nodo</strong>.
Per avviarlo abbiamo bisogno di creare un’altro file di configurazione nel quale dichiariamo la <strong class="markup--strong markup--p-strong">datadir</strong>, le <strong class="markup--strong markup--p-strong">porte </strong>differenti, e aggiungeremo l’ip e la porta del nodo con l’interfaccia grafica.</p>
<p class="graf graf--p">Creo quindi un file con il nome bitcoin.conf_2 con questa configurazione:</p>

<pre class="graf graf--pre">regtest=1</pre>
<pre class="graf graf--pre">datadir=/Users/barno/Documents/Bitcoin-in-action-book/Bitcoin/regtest-cli</pre>
<pre class="graf graf--pre"># Options only for mainnet</pre>
<pre class="graf graf--pre">[main]</pre>
<pre class="graf graf--pre"># Options only for testnet</pre>
<pre class="graf graf--pre">[test]</pre>
<pre class="graf graf--pre"># Options only for regtest</pre>
<pre class="graf graf--pre">[regtest]</pre>
<pre class="graf graf--pre">daemon=1</pre>
<pre class="graf graf--pre">rpcport=28443</pre>
<pre class="graf graf--pre">port=28444</pre>
<pre class="graf graf--pre">addnode=localhost:18444</pre>
<blockquote class="graf graf--blockquote graf--hasDropCapModel">Le porte di default della regtest sono 18444 e 18443 che al momento sono occupate dalla versione grafica.</blockquote>
<p class="graf graf--p">Avviamo il demone bash</p>

<pre class="graf graf--pre">$ bitcoind --conf=bitcoin.conf_2</pre>
<p class="graf graf--p">Appena avviamo, vediamo che nell’interfaccia grafica si ha un nodo collegato.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*0DPzLULK8dYnx1cDYME7kg.png" data-image-id="1*0DPzLULK8dYnx1cDYME7kg.png" data-width="999" data-height="573" />

<figcaption class="imageCaption">Bitcoin-core GUI con un nodo collegato</figcaption></figure>
<p class="graf graf--p">Siamo noi!</p>
<p class="graf graf--p">Verifichiamo a quanti nodi siamo connessi con il demone da riga di comando, che da questo momento chiameremo <strong class="markup--strong markup--p-strong">nodo2</strong>.</p>

<section class="section section--body">
<div class="section-divider">

<hr class="section-divider" />

</div>
<div class="section-content">
<div class="section-inner sectionLayout--insetColumn">
<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong>bitcoin-cli —-conf=bitcoin.conf_2 getconnectioncount</pre>
<pre class="graf graf--pre">1</pre>
<p class="graf graf--p">Siamo connessi a un nodo, alla GUI.</p>
<p class="graf graf--p">Possiamo ottenere più informazioni del nodo aggiunto con <strong class="markup--strong markup--p-strong">addnode</strong> con il comando <strong class="markup--strong markup--p-strong">getaddednodeinfo</strong>.</p>

<pre class="graf graf--pre">$ bitcoin-cli --conf=bitcoin.conf_2 getaddednodeinfo</pre>
<pre class="graf graf--pre">[</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"addednode": "localhost:18444",</pre>
<pre class="graf graf--pre">"connected": true,</pre>
<pre class="graf graf--pre">"addresses": [</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"address": "[::1]:18444",</pre>
<pre class="graf graf--pre">"connected": "outbound"</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">]</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">]</pre>
<p class="graf graf--p">Ma come funziona il bootstrap di un nodo Bitcoin? Nella modalità mainnet i nodi si collegano ad altri nodi con questa logica:</p>

<ul class="postList">
 	<li class="graf graf--li">Address database (peers.dat)</li>
 	<li class="graf graf--li">User-specified (-addnode and -connect)</li>
 	<li class="graf graf--li">DNS seeding</li>
 	<li class="graf graf--li">Hard-coded seeds</li>
 	<li class="graf graf--li">From other peers (“getaddr” and “addr” messages)</li>
</ul>
<p class="graf graf--p">Quindi prendono gli indirizzi dei nodi dal file peers.dat, successivamente verificano se ci sono dei nodi specificati dall’utente, proprio come abbiamo fatto noi, e, se i peers falliscono, si connettono a dei <a class="markup--anchor markup--p-anchor" href="https://github.com/bitcoin/bitcoin/blob/1e17114917f29da114cb90f52579ddb911a1a856/src/chainparams.cpp#L121" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin/bitcoin/blob/1e17114917f29da114cb90f52579ddb911a1a856/src/chainparams.cpp#L121">DNS</a> e a dei seeds <a class="markup--anchor markup--p-anchor" href="https://github.com/bitcoin/bitcoin/blob/d4159984c360001d9469fd54512bf0da4b02c4fd/src/chainparamsseeds.h" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin/bitcoin/blob/d4159984c360001d9469fd54512bf0da4b02c4fd/src/chainparamsseeds.h">hardcodati nel codice</a>.</p>
<p class="graf graf--p">Miniamo 211 blocchi dal nodo2.</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong>bitcoin-cli --conf=bitcoin.conf_2 generatetoaddress 211 $(bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "" "bech32") &gt;&gt; /dev/null</pre>
<p class="graf graf--p">Per sapere quanti blocchi contiene la blockchain possiamo utilizzare la chiamata getblockcount</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong> bitcoin-cli --conf=bitcoin.conf_2 getblockcount</pre>
<pre class="graf graf--pre">211</pre>
<p class="graf graf--p">Il risultato che otteniamo è 211. Come posso verificare che la GUI sia <em class="markup--em markup--p-em">syncata</em>?</p>
<p class="graf graf--p">Utilizzando Window-&gt;information troviamo una schermata che ci comunica i blocchi, che anche in questo caso risultano essere 211.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*GnPUqKWsanXVEt3ylPhy6w.png" data-image-id="1*GnPUqKWsanXVEt3ylPhy6w.png" data-width="1175" data-height="691" />

<figcaption class="imageCaption">Bitcoin-core Syncata</figcaption></figure>
<p class="graf graf--p">Torniamo nel nodo2 e creiamo una transazione. Per prima cosa verifico il saldo con la chiamata getwalletinfo.</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong> bitcoin-cli --conf=bitcoin.conf_2 getwalletinfo</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"walletname": "",</pre>
<pre class="graf graf--pre">"walletversion": 169900,</pre>
<pre class="graf graf--pre">"balance": 5550.00000000,</pre>
<pre class="graf graf--pre">"unconfirmed_balance": 0.00000000,</pre>
<pre class="graf graf--pre">"immature_balance": 3450.00000000,</pre>
<pre class="graf graf--pre">"txcount": 211,</pre>
<pre class="graf graf--pre">"keypoololdest": 1606752619,</pre>
<pre class="graf graf--pre">"keypoolsize": 999,</pre>
<pre class="graf graf--pre">"keypoolsize_hd_internal": 1000,</pre>
<pre class="graf graf--pre">"paytxfee": 0.00000000,</pre>
<pre class="graf graf--pre">"hdseedid": "50aacc53d11feb46bf8a159d1fb4fdb0ecc18e06",</pre>
<pre class="graf graf--pre">"private_keys_enabled": true,</pre>
<pre class="graf graf--pre">"avoid_reuse": false,</pre>
<pre class="graf graf--pre">"scanning": false</pre>
<pre class="graf graf--pre">}</pre>
<p class="graf graf--p">La chiamata restituisce anche i bitcoin <em class="markup--em markup--p-em">non maturi</em>, ovvero quelli che non hanno ancora passato la <a class="markup--anchor markup--p-anchor" href="https://github.com/bitcoin/bitcoin/blob/78dae8caccd82cfbfd76557f1fb7d7557c7b5edb/src/consensus/consensus.h#L19" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin/bitcoin/blob/78dae8caccd82cfbfd76557f1fb7d7557c7b5edb/src/consensus/consensus.h#L19">coinbase_maturity, ovvero 101 conferme</a>. Per avere il balance confermato, possiamo utilizzare la chiamata <strong class="markup--strong markup--p-strong">getbalance</strong>.</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong>bitcoin-cli --conf=bitcoin.conf_2 getbalance</pre>
<pre class="graf graf--pre">5550.00000000</pre>
<p class="graf graf--p">Inviamo 1 bitcoin all’address del nodo GUI, per prima cosa ottengo un nuovo address.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*3vxv5fXtQaybWuDRCzMsSA.png" data-image-id="1*3vxv5fXtQaybWuDRCzMsSA.png" data-width="1069" data-height="684" />

<figcaption class="imageCaption">Ottengo l’address dal nodo GUI</figcaption></figure>
<p class="graf graf--p">Seleziono <strong class="markup--strong markup--p-strong">receive</strong> e clicco create a <em class="markup--em markup--p-em">new receive address</em>. Il software mi restituisce un address SegWit nativo.
Quale è stato il comando che ha eseguito? È stato <strong class="markup--strong markup--p-strong">getnewaddres</strong>. Replichiamolo nel nodo2.</p>

<pre class="graf graf--pre">$ bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "" "bech32"</pre>
<pre class="graf graf--pre">bcrt1qg887l3jc0q3wmn9ldwtamn5cqhz63gyw4vy84g</pre>
<p class="graf graf--p">Ed ecco ottenuto l’address anche con il nodo2, che ovviamente è diverso dal nodo GUI. Inviamo quindi 1 bitcoin dal nodo2 al nodo GUI, utilizzando il metodo <strong class="markup--strong markup--p-strong">sendtoaddress</strong>, il quale ha il compito di aggregare per noi le UTXO fino ad arrivare all’importo desiderato impostando automaticamente le fees.</p>

<pre class="graf graf--pre">$ bitcoin-cli --conf=bitcoin.conf_2 sendtoaddress bcrt1qfak36m9lmm3uup9s4v2rkd0yeld7vgz9q6fvld 1</pre>
<pre class="graf graf--pre">dde7dc0f4dca1c83fc86ac64a1c5522ecfeedb8f9c64bc013bf4cffce52cf4b7</pre>
<p class="graf graf--p">La transazione è stata inviata, quindi adesso si trova nella <strong class="markup--strong markup--p-strong">mempool</strong>. Nella GUI, nella sezione transaction, possiamo verificare tutte le informazioni della transazione.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*YukiMmh7Er5mhYxkCypJig.png" data-image-id="1*YukiMmh7Er5mhYxkCypJig.png" data-width="1062" data-height="681" />

<figcaption class="imageCaption">Bitcoin Core — Mempool</figcaption></figure>
<p class="graf graf--p">Come è possibile ottenere le stesse informazioni dal nodo2? Utilizzando la chiamata <strong class="markup--strong markup--p-strong">getrawtransaction</strong> specificando una risultato più verboso, utilizzando la <strong class="markup--strong markup--p-strong">txid</strong> ottenuta dalla chiamata sendtoaddress.</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong>bitcoin-cli --conf=bitcoin.conf_2 getrawtransaction dde7dc0f4dca1c83fc86ac64a1c5522ecfeedb8f9c64bc013bf4cffce52cf4b7 2</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"txid": "dde7dc0f4dca1c83fc86ac64a1c5522ecfeedb8f9c64bc013bf4cffce52cf4b7",</pre>
<pre class="graf graf--pre">"hash": "cd43d5f44c108b6ccad6649929bfd5c616d22082310a7dff4c5998d1b2052be7",</pre>
<pre class="graf graf--pre">"version": 2,</pre>
<pre class="graf graf--pre">"size": 222,</pre>
<pre class="graf graf--pre">"vsize": 141,</pre>
<pre class="graf graf--pre">"weight": 561,</pre>
<pre class="graf graf--pre">"locktime": 211,</pre>
<pre class="graf graf--pre">"vin": [</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"txid": "fb75baa7271a6c0c30002ba8587df3370aed4192c6ecd25a65a2f3ec36802033",</pre>
<pre class="graf graf--pre">"vout": 0,</pre>
<pre class="graf graf--pre">"scriptSig": {</pre>
<pre class="graf graf--pre">"asm": "",</pre>
<pre class="graf graf--pre">"hex": ""</pre>
<pre class="graf graf--pre">},</pre>
<pre class="graf graf--pre">"txinwitness": [</pre>
<pre class="graf graf--pre">"304402200e6705b7ddb830422aee5b300a02b34bb46330698e0cd462220c190b0526e6e70220620f13fcbd17de115517a047e5b8c5c5b88b39aba4873af79af2dffc0cdaec7101",</pre>
<pre class="graf graf--pre">"039434ddae8e96297683ff1117935682bfea0d4b7725ee037c3aa323cb04711a53"</pre>
<pre class="graf graf--pre">],</pre>
<pre class="graf graf--pre">"sequence": 4294967294</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">],</pre>
<pre class="graf graf--pre">"vout": [</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"value": 1.00000000,</pre>
<pre class="graf graf--pre">"n": 0,</pre>
<pre class="graf graf--pre">"scriptPubKey": {</pre>
<pre class="graf graf--pre">"asm": "0 4f6d1d6cbfdee3ce04b0ab143b35e4cfdbe62045",</pre>
<pre class="graf graf--pre">"hex": "00144f6d1d6cbfdee3ce04b0ab143b35e4cfdbe62045",</pre>
<pre class="graf graf--pre">"reqSigs": 1,</pre>
<pre class="graf graf--pre">"type": "witness_v0_keyhash",</pre>
<pre class="graf graf--pre">"addresses": [</pre>
<pre class="graf graf--pre">"bcrt1qfak36m9lmm3uup9s4v2rkd0yeld7vgz9q6fvld"</pre>
<pre class="graf graf--pre">]</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">},</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"value": 48.99997180,</pre>
<pre class="graf graf--pre">"n": 1,</pre>
<pre class="graf graf--pre">"scriptPubKey": {</pre>
<pre class="graf graf--pre">"asm": "0 8e54cf6eaefcd27c9297ed512ec3e6e0901287b1",</pre>
<pre class="graf graf--pre">"hex": "00148e54cf6eaefcd27c9297ed512ec3e6e0901287b1",</pre>
<pre class="graf graf--pre">"reqSigs": 1,</pre>
<pre class="graf graf--pre">"type": "witness_v0_keyhash",</pre>
<pre class="graf graf--pre">"addresses": [</pre>
<pre class="graf graf--pre">"bcrt1q3e2v7m4wlnf8ey5ha4gjaslxuzgp9pa3mce9ja"</pre>
<pre class="graf graf--pre">]</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">],</pre>
<pre class="graf graf--pre">"hex": "0200000000010133208036ecf3a2655ad2ecc69241ed0a37f37d58a82b00300c6c1a27a7ba75fb0000000000feffffff0200e1f505000000001600144f6d1d6cbfdee3ce04b0ab143b35e4cfdbe62045fc051024010000001600148e54cf6eaefcd27c9297ed512ec3e6e0901287b10247304402200e6705b7ddb830422aee5b300a02b34bb46330698e0cd462220c190b0526e6e70220620f13fcbd17de115517a047e5b8c5c5b88b39aba4873af79af2dffc0cdaec710121039434ddae8e96297683ff1117935682bfea0d4b7725ee037c3aa323cb04711a53d3000000"</pre>
<pre class="graf graf--pre">}</pre>
<p class="graf graf--p">Questa chiamata restituisce molte più informazioni, nella GUI sono riportate solo quelle di interesse. Che cosa ci resta da fare? Minare dei blocchi! Utilizziamo la GUI per questo. Prima otteniamo un altro indirizzo.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*xvTcHcEfZMABcWVX43qkYA.png" data-image-id="1*xvTcHcEfZMABcWVX43qkYA.png" data-width="1069" data-height="686" />

<figcaption class="imageCaption">Bitcoin Core — Indirizzo Miner</figcaption></figure>
<p class="graf graf--p">Questo indirizzo sarà il nostro miner. <strong class="markup--strong markup--p-strong">bcrt1qcad9r6cn037p3una2fum7v5jwgc2zgm8ssw7un</strong></p>
<p class="graf graf--p">Utilizziamo ancora la console della GUI. Miniamo 10 blocchi con il comando <strong class="markup--strong markup--p-strong">generatetoaddress</strong>.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*YlB_EouKjkXK1RzQk7bv9g.png" data-image-id="1*YlB_EouKjkXK1RzQk7bv9g.png" data-width="1115" data-height="193" /></figure>
<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*_ckpT1CBlNeKuWpZRZPtQg.png" data-image-id="1*_ckpT1CBlNeKuWpZRZPtQg.png" data-width="1113" data-height="590" />

<figcaption class="imageCaption">Bitcoin Core — 10 blocchi minati</figcaption></figure>
<p class="graf graf--p">Abbiamo minato 10 blocchi! Adesso mi aspetto di vedere il la transazione fatta dal nodo2 confermata!</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*LpdkvHi-vt1q04oOVy0ENQ.png" data-image-id="1*LpdkvHi-vt1q04oOVy0ENQ.png" data-width="1139" data-height="818" />

<figcaption class="imageCaption">Bitcoin Core — Transazione Confermata</figcaption></figure>
<p class="graf graf--p">Esatto! la prima transazione è stata minata e ha 10 conferme. Nella schermata vediamo altri blocchi minati con dei reward. Nel primo blocco vediamo un reward un pò più <em class="markup--em markup--p-em">corposo</em>, perchè? Perchè è il blocco che contiene la nostra transazione. Ricorda che il <strong class="markup--strong markup--p-strong">reward</strong> del miner è composta, dal reward impostato dal protocollo che cambia ogni 210.000 blocchi e dalle fees.</p>
<p class="graf graf--p">Perchè qui non abbiamo 50 bitcoin di reward? In regtest l’halving non avviene ogni 210.000 blocchi. Per saperne di più guarda <a class="markup--anchor markup--p-anchor" href="https://youtu.be/nFrN-jROnMI" target="_blank" rel="noopener noreferrer" data-href="https://youtu.be/nFrN-jROnMI">questo video</a>.</p>
<p class="graf graf--p">Facciamo anche l’operazione inversa, inviamo 0.5 bitcoin dalla GUI al nodo2.</p>
<p class="graf graf--p">Otteniamo un address dal nodo2, aggiungiamo anche una label. Io aggiungerò “barno”.</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong>bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "barno" "bech32"</pre>
<pre class="graf graf--pre">bcrt1qtc00wzrcae86rvyacanwd5l9t6fek4h8a6vna4</pre>
<p class="graf graf--p">Spostiamoci nella tab <em class="markup--em markup--p-em">send</em> e inseriamo i valori desiderati.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*fNd2Lpu9XlI0SvJMI6yWuA.png" data-image-id="1*fNd2Lpu9XlI0SvJMI6yWuA.png" data-width="1260" data-height="793" />

<figcaption class="imageCaption">Bitcoin Core — Transazione</figcaption></figure>
<p class="graf graf--p">Ci viene proposto un popup per confermare la transazione</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*KyAcWa8ynO0qOF658GZvNQ.png" data-image-id="1*KyAcWa8ynO0qOF658GZvNQ.png" data-width="964" data-height="622" />

<figcaption class="imageCaption">Bitcoin Core — Conferma</figcaption></figure>
<p class="graf graf--p">Confermiamo.</p>
<p class="graf graf--p">Dove sarà adesso la transazione? Di nuovo nella <strong class="markup--strong markup--p-strong">mempool</strong>!
Dato che sappiamo che è prensente una sola transazione, possiamo utilizzare <strong class="markup--strong markup--p-strong">getrawmempool</strong> dal nodo2.</p>

<pre class="graf graf--pre">bitcoin-cli --conf=bitcoin.conf_2 getrawmempool</pre>
<pre class="graf graf--pre">[</pre>
<pre class="graf graf--pre">"20f2b335d8775d1237523b1f6583ea809716f74e82773c5ad285cbb66a5b3e91"</pre>
<pre class="graf graf--pre">]</pre>
<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*72uwDX-QBJDen84eBFM3iA.png" data-image-id="1*72uwDX-QBJDen84eBFM3iA.png" data-width="1126" data-height="435" />

<figcaption class="imageCaption">Bitcoin Core GUI – Mempool</figcaption></figure>
<p class="graf graf--p">Troviamo infatti corrispondenza con la GUI.</p>
<p class="graf graf--p">Adesso possiamo aspettarci dei bitcoin non confermati con nell’address del nodo2. Abbiamo la verifica utilizzando il metodo <strong class="markup--strong markup--p-strong">listreceivedbyaddress</strong> passando come parametro 0, il quale rappresenta le conferme.</p>

<pre class="graf graf--pre">$ bitcoin-cli --conf=bitcoin.conf_2 listreceivedbyaddress 0</pre>
<pre class="graf graf--pre">[</pre>
<pre class="graf graf--pre">{</pre>
<pre class="graf graf--pre">"address": "bcrt1qtc00wzrcae86rvyacanwd5l9t6fek4h8a6vna4",</pre>
<pre class="graf graf--pre">"amount": 0.50000000,</pre>
<pre class="graf graf--pre">"confirmations": 0,</pre>
<pre class="graf graf--pre">"label": "barno",</pre>
<pre class="graf graf--pre">"txids": [</pre>
<pre class="graf graf--pre">"20f2b335d8775d1237523b1f6583ea809716f74e82773c5ad285cbb66a5b3e91"</pre>
<pre class="graf graf--pre">]</pre>
<pre class="graf graf--pre">}</pre>
<pre class="graf graf--pre">]</pre>
<p class="graf graf--p">Non ci resta che minare! Mineremo utilizzando il nodo2.</p>

<pre class="graf graf--pre"><strong class="markup--strong markup--pre-strong">$ </strong>bitcoin-cli --conf=bitcoin.conf_2 generatetoaddress 11 $(bitcoin-cli --conf=bitcoin.conf_2 getnewaddress "" "bech32") &gt;&gt; /dev/null</pre>
<p class="graf graf--p">Facendo nuovamente doppio click sulla transazione possiamo leggere che la transazione è stata minata e confermata!</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*xWYCAZ6wlbqOm1ENPrhNAQ.png" data-image-id="1*xWYCAZ6wlbqOm1ENPrhNAQ.png" data-width="1121" data-height="333" />

<figcaption class="imageCaption">Bitcoin core – Transazione minata e confermata</figcaption></figure>
<p class="graf graf--p">Verifichiamo l’homepage della GUI.</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*2qprT9XRLKsaJ3dffMuauA.png" data-image-id="1*2qprT9XRLKsaJ3dffMuauA.png" data-width="1139" data-height="657" />

<figcaption class="imageCaption">Bitcoin Core GUI — Homepage</figcaption></figure>
<p class="graf graf--p">Abbiamo un saldo disponibile di 0.49 bitcoin e un 250 bitcoin + fees immaturi. A questo punto sappiamo perchè!</p>
<p class="graf graf--p">Per concludere:
La GUI facilita alcune operazioni ma ne nasconde altre, la riga di comando è sicuramente meno user friendly ma è molto più consigliata in quanto su ogni sistema che andrete a lavorare non vi sentirete spaesati!</p>
<p class="graf graf--p">Ciao!</p>

<figure class="graf graf--figure"><img class="graf-image" src="https://cdn-images-1.medium.com/max/1600/1*mFeOGVPcT3_CeHYzgoV2Dg.jpeg" data-image-id="1*mFeOGVPcT3_CeHYzgoV2Dg.jpeg" data-width="1600" data-height="900" />

<figcaption class="imageCaption">📕 <a class="markup--anchor markup--figure-anchor" href="https://amzn.to/3pJcXj1" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3pJcXj1">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></figcaption></figure>
</div>
</div>
</section>
<section class="section section--body">
<div class="section-divider">

<hr class="section-divider" />

</div>
<div class="section-content">
<div class="section-inner sectionLayout--insetColumn"></div>
</div>
</section>
<p class="graf graf--p"> — — –</p>
<p class="graf graf--p">🎥 <a class="markup--anchor markup--p-anchor" href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">Bitcoin in Action (YouTube)</a></p>
<p class="graf graf--p">—</p>
<p class="graf graf--p">🐙 GitHub:<a class="markup--anchor markup--p-anchor" href="https://bit.ly/2Lj3yeY" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/2Lj3yeY"> https://bit.ly/2Lj3yeY</a></p>
<p class="graf graf--p"> — –</p>
<p class="graf graf--p">📕 <a class="markup--anchor markup--p-anchor" href="https://amzn.to/3pJcXj1" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3pJcXj1">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></p>
<p class="graf graf--p">📕 <a class="markup--anchor markup--p-anchor" href="https://bit.ly/38RtF9x" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/38RtF9x">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a></p>
<p class="graf graf--p"> — –</p>
<p class="graf graf--p">📒 <a class="markup--anchor markup--p-anchor" href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📒 <a class="markup--anchor markup--p-anchor" href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a>
📒 <a class="markup--anchor markup--p-anchor" href="https://amzn.to/2Ym4gz6" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ym4gz6">Book Bitcoin from theory to practice (Amazon)</a></p>
<p class="graf graf--p">📒 <a class="markup--anchor markup--p-anchor" href="https://bit.ly/3ijAyC4" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3ijAyC4">Book Bitcoin from theory to practice (accept bitcoin)</a>
—
🎥 <a class="markup--anchor markup--p-anchor" href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a></p>
<p class="graf graf--p">—
📙 <a class="markup--anchor markup--p-anchor" href="https://amzn.to/3ckIkJj" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3ckIkJj">Tascabile Bitcoin 199 domande (Amazon)</a>
📙 <a class="markup--anchor markup--p-anchor" href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a></p>
<p class="graf graf--p">📙 <a class="markup--anchor markup--p-anchor" href="https://amzn.to/3fB4Kbs" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3fB4Kbs">Pocket Book Bitcoin 199 questions (Amazon)</a>
📙 <a class="markup--anchor markup--p-anchor" href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a class="markup--anchor markup--p-anchor" href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a class="markup--anchor markup--p-anchor" href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (accept bitcoin)</a>
—
► ITA: <a class="markup--anchor markup--p-anchor" href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a> , <a class="markup--anchor markup--p-anchor" href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a class="markup--anchor markup--p-anchor" href="https://bitcoin-in-action.medium.com/" target="_blank" rel="noopener noreferrer" data-href="https://bitcoin-in-action.medium.com/">Medium</a>, <a class="markup--anchor markup--p-anchor" href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a class="markup--anchor markup--p-anchor" href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a class="markup--anchor markup--p-anchor" href="https://github.com/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a></p>
<p class="graf graf--p">► ENG: <a class="markup--anchor markup--p-anchor" href="https://twitter.com/btc_in_action" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/btc_in_action">Twitter</a> , <a class="markup--anchor markup--p-anchor" href="https://www.facebook.com/bitcoininaction/" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/bitcoininaction/">Facebook</a>, <a class="markup--anchor markup--p-anchor" href="https://medium.com/@bitcoin_in_action" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoin_in_action">Medium</a>, <a class="markup--anchor markup--p-anchor" href="https://www.instagram.com/bitcoin_in_action/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/bitcoin_in_action/">Instagram</a>, <a class="markup--anchor markup--p-anchor" href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a class="markup--anchor markup--p-anchor" href="https://github.com/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a></p>
<p class="graf graf--p">Television isn’t a good idea (Radio Stations)
Email isn’t a good idea (Post offices)
Amazon isn’t a good idea (Retail stores)
Bitcoin isn’t a good idea (Central banks)</p>
<p class="graf graf--p">In <strong class="markup--strong markup--p-strong">crypto</strong> we trust</p>