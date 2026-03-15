---
title: "Come è costruito un address P2SH?"
date: 2021-04-26T17:59:40+01:00
draft: false


tags:
  - "Script"
  - "Crittografia"
---




<p><a href="https://www.youtube.com/BitcoinInAction" rel="noreferrer noopener" target="_blank">Video completo sul nostro canale YouTube – Bitcoin in&nbsp;Action!</a></p>

<p></p>

<figure class="wp-block-gallery columns-1 is-cropped"><ul class="blocks-gallery-grid"><li class="blocks-gallery-item"><figure><img src="/img/come--costruito-un-address-p2sh-1.jpg" alt="Come è costruito un address P2SH?" data-id="13632" data-full-url="https://www.corsobitcoin.com/wp-content/uploads/2021/04/maxresdefault-1.jpg" data-link="https://www.corsobitcoin.com/?attachment_id=13632" class="wp-image-13632"/></figure></li></ul></figure>

<p>Entriamo nel vivo dell’address <strong>Pay to script Hash</strong>. Come dicevamo nel precedente <a href="https://youtu.be/Aa1pTzC67Io" rel="noreferrer noopener" target="_blank">video</a>, l’utente andrà a pagare ad un <strong>hash</strong> di uno script.</p>

<p>Collegandoci agli address affrontati precedentemente, abbiamo potuto capire che le condizioni necessarie per sbloccare la transazione sono dichiarate all’interno dello <strong>scriptPubKey</strong>, che storicamente prende il nome anche di locking script.</p>

<p>In un address <strong>Pay To Script Hash</strong>, è possibile inserire qualsiasi tipo di <strong>script</strong>, anche custom. Con lo script custom sarà l’utente a prendersi la responsabilità di scrivere un <em>giusto</em> script. Con questo che cosa voglio dire? Non è obbligatorio inserire la firma digitale all’interno di uno script, è possible inserire anche una semplice uguaglianza.</p>

<p>Facciamo un esempio.<br>Immaginiamo che nello <strong>scriptPubKey</strong> sia presente uno script del genere OP_1 OP_EQUAL. Vi sembra sicuro? È vero che, come vedremo successivamente, lo script in chiaro si vede solo se il proprietario dell’address ha effettuato almeno una transazione, perchè come il nome dello script stesso ci suggerisce, nello scriptPubKey troveremo l’hash.</p>

<p>Ma è anche vero che dopo la prima transazione, chiunque è in grado di inserire un OP_1 per soddisfare l’uguaglianza, proprio perchè questa condizione (OP_1 OP_EQUAL) sarà visibile nello scriptSig.</p>

<p>Ecco perchè si usano le firme digitali che risolvono dei problemi fondamentali, quali:</p>

<ul><li><strong>Integrità</strong>: Il messaggio non deve essere alterato durante la trasmissione. Bob manda un messaggio a Alice con scritto W i bitcoin.<br>Peter lo intercetta cambiandolo con W gli ether.<br>Alice deve essere in grado di accorgersi di tale cambiamento.</li><li><strong>Autenticità</strong>: Alice deve essere sicura che il messaggio che ha ricevuto sia stato inviato da Bob, e non da Peter che si è spacciato per Bob.</li><li><strong>Non ripudio</strong>: Il mittente non potrà disconoscere il messaggio che ha firmato.</li></ul>

<p>Quindi abbiamo capito che è compito dell’utente gestire uno script custom, in più, se si utilizza uno script custom dovremo <strong>firmare manualmente la transazione</strong>, come spiegato nel libro <a href="https://bit.ly/38RtF9x" rel="noreferrer noopener" target="_blank">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</a>.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2021/04/book-mockup2.jpg" alt="Come è costruito un address P2SH?" class="wp-image-13633"/><figcaption><a href="https://bit.ly/38RtF9x" target="_blank" rel="noreferrer noopener"><a href="https://bit.ly/38RtF9x">Bitcoin In Action – SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a> </a></figcaption></figure>

<p>Vediamo invece come è costruito un address <strong>P2SH-P2PK</strong>, ovvero un address che racchiude lo script <strong>P2PK</strong>. Facendo riferimento all’esempio di prima, nello scriptPubKey ci saranno le condizioni che abbiamo trovato nel <a href="https://youtu.be/iVWMaGO3m48" rel="noreferrer noopener" target="_blank">video P2PK</a>, ovvero: Public Key OP_CHECKSIG. Questo è conosciuto anche come <strong>redeem script</strong>.</p>

<p>Ma quando viene dichiarato? Durante la generazione dell’address, subito dopo aver ottenuto la chiave pubblica compressa, (<a href="https://www.youtube.com/playlist?list=PLpPLK7SGHncZVl_ZQkqyXGMDGWEx7U_et" rel="noreferrer noopener" target="_blank">se non ti ricordi di che cosa sto parlando guarda i video precedenti</a>), viene costruito il redeem script.</p>

<p><strong>Redeem script = PB OP_CHECKSIG</strong></p>

<p>Successivamente ci vengono applicate le funzioni crittografiche, <strong>SHA256</strong> e <strong>RIPEMD160</strong>, ottenendo così il <strong>redeem script Hash.</strong></p>

<p>Al digest ottenuto viene aggiunto l’address prefix e applicato l’encoding base58 comprensivo di checksum.</p>

<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://www.youtube.com/watch?v=SzlTMdp7txE
</div></figure>

<p>Piccolo Spoiler:</p>

<p>Vi ricorda niente <strong>SHA256 e RIPEMD160</strong>? Esatto sono le stessa operazioni che si ottengono con l’<strong>OP_HASH160</strong>, e dopo vedremo perchè!</p>

<p>In questo modo è possibile ottenere un P2SH che wrappa, un P2PK.</p>

<blockquote class="wp-block-quote"><p>In <a href="https://it.wikipedia.org/wiki/Informatica" rel="noreferrer noopener" target="_blank">informatica</a>, e in particolare in <a href="https://it.wikipedia.org/wiki/Programmazione_%28informatica%29" rel="noreferrer noopener" target="_blank">programmazione</a>, è un modulo software che ne “riveste” un altro.</p></blockquote>

<p>Come si ottiene un P2SH che Wrappa un P2PKH?</p>

<figure class="wp-block-image"><img src="https://cdn-images-1.medium.com/max/800/1*rE5iKriU-nhH4Ukt-PMBCA.png" alt="P2SH — Pay to script hash Bitcoin"/><figcaption><a href="https://youtu.be/SzlTMdp7txE" rel="noreferrer noopener" target="_blank">P2SH — Guarda il video completo sul canale Youtube Bitcoin in&nbsp;Action</a></figcaption></figure>

<p>Il Redeem script sarà composto dallo script del P2PKH: OP_DUP OP_HASH160 &lt;PubKHash&gt; OP_EQUALVERIFY OP_CHECKSIG e successivamente applicate le stesse funzioni crittografiche e di encoding al fine di ottenere l’address.</p>

<p>Nella prossima lezione vedremo con la pratica come analizzare un Address P2SH!</p>

<p>Ciao!</p>

<p id="f08e">— — –</p>

<p id="3acd">🐳&nbsp;<a href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground">Playground Bitcoin in Action</a></p>

<p id="6e67">🎥&nbsp;<a href="https://www.youtube.com/BitcoinInAction">Bitcoin in Action (YouTube)</a></p>

<p id="a79d">—</p>

<p id="5780">🐙 GitHub:<a href="https://bit.ly/2Lj3yeY">&nbsp;https://bit.ly/2Lj3yeY</a></p>

<p id="03a0">— –</p>

<p id="1c89">📕&nbsp;<a href="https://amzn.to/3pJcXj1">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></p>

<p id="f459">📕&nbsp;<a href="https://bit.ly/38RtF9x">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a></p>

<p id="4c21">— –</p>

<p id="5d58">📒&nbsp;<a href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>📒&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a><br>📒&nbsp;<a href="https://amzn.to/2Ym4gz6">Book Bitcoin from theory to practice (Amazon)</a></p>

<p id="4dc1">📒&nbsp;<a href="https://bit.ly/3ijAyC4">Book Bitcoin from theory to practice (accept bitcoin)</a><br>—<br>🎥&nbsp;<a href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a></p>

<p id="2c1d">—<br>📙&nbsp;<a href="https://amzn.to/3ckIkJj">Tascabile Bitcoin 199 domande (Amazon)</a><br>📙&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a></p>

<p id="a02b">📙&nbsp;<a href="https://amzn.to/3fB4Kbs">Pocket Book Bitcoin 199 questions (Amazon)</a><br>📙&nbsp;<a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Pocket&nbsp;</a><a href="https://www.amazon.it/dp/1078155585">Book&nbsp;</a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Bitcoin 199 questions (accept bitcoin)</a><br>—<br>► ITA:&nbsp;<a href="https://twitter.com/satoshiwantsyou">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/satoshiwantsyou">Facebook</a>,&nbsp;<a href="https://bitcoin-in-action.medium.com/">Medium</a>,&nbsp;<a href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a></p>

<p id="ac8c">► ENG:&nbsp;<a href="https://twitter.com/btc_in_action">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/bitcoininaction/">Facebook</a>,&nbsp;<a href="https://medium.com/@bitcoin_in_action">Medium</a>,&nbsp;<a href="https://www.instagram.com/bitcoin_in_action/">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a></p>

<p id="263a">Television isn’t a good idea (Radio Stations)<br>Email isn’t a good idea (Post offices)<br>Amazon isn’t a good idea (Retail stores)<br>Bitcoin isn’t a good idea (Central banks)</p>

<p id="ed2a">In&nbsp;<strong>crypto</strong>&nbsp;we trust</p>
