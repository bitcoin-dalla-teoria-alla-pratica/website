---
title: "La transazione Bitcoin P2SH-P2PK"
date: 2021-06-01T10:14:58+01:00
draft: false


tags:
  - "Script"
  - "SegWit"
---




<h5><a href="https://youtu.be/wMvFm2GJtcI" target="_blank" rel="noreferrer noopener">Video disponibile sul canale YouTube Bitcoin in Action</a></h5>

<p>Negli articoli precedenti abbiamo analizzato come è costruito un&nbsp;<a href="https://bitcoin-in-action.medium.com/come-creare-un-address-p2sh-p2pk-bitcoin-2ed875f9fd7e">address P2SH-P2PK</a>, e in questa introduzione andremo invece ad analizzare come è costruita la transazione</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2021/06/Bitcoin-P2SH-–-Bitcoin-in-Action-1024x768.jpeg" alt="Bitcoin P2SH – Bitcoin in Action" class="wp-image-13643"/><figcaption><a href="https://youtu.be/wMvFm2GJtcI" target="_blank" rel="noreferrer noopener">Frame del video Bitcoin in Action —&nbsp;<strong>Come è formata una transazione P2SH-P2PK</strong></a></figcaption></figure>

<p id="ea0f">Nell’immagine della lavagna è riportata una simil transazione, ovvero come poi verrà eseguito lo script.</p>

<p id="8cd1">Nello&nbsp;<strong>scriptSig</strong>, ovvero la parte dell’input della transazione, troviamo le condizioni necessarie per soddisfare lo&nbsp;<strong>scriptPubKey</strong>&nbsp;della&nbsp;<strong>UTXO</strong>&nbsp;di riferimento.</p>

<p id="dc53">Avendo preso come riferimento un&nbsp;<strong><a href="https://youtu.be/wMvFm2GJtcI" target="_blank" rel="noreferrer noopener">P2SH–P2PK</a></strong>&nbsp;nello scriptSig è presente la firma digitale e il redeem script in chiaro.<br>Esatto, il redeem script, è posizionato nello&nbsp;<strong>scriptSig</strong>, gli stessi elementi che sono stati utilizzati per&nbsp;<a href="https://bitcoin-in-action.medium.com/come-creare-un-address-p2sh-p2pk-bitcoin-2ed875f9fd7e">creare l’address</a>&nbsp;negli articoli precedenti.</p>

<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://youtu.be/wMvFm2GJtcI
</div><figcaption><a href="https://youtu.be/wMvFm2GJtcI" target="_blank" rel="noreferrer noopener">Come è formata una transazione Bitcoin P2SH-P2PK</a></figcaption></figure>

<p id="2384">All'interno scriptPubKey è invece presente l’operation code OP_HASH160 il redeem script hash e l’operation code OP_EQUAL.</p>

<p id="b42e">Lo script sarà sempre così? Lo scriptPubKey avrà sempre questa forma OP_HASH160 Redeem Script Hash OP_EQUAL.</p>

<p id="6fac">La parte che andrà a cambiare sarà lo&nbsp;<strong>scriptSig</strong>, in base allo script utilizzato. Ad esempio, per lo script&nbsp;<strong>P2PKH</strong>, nello scriptSig troveremo la firma digitale e la chiave pubblica, esattamente come una normale&nbsp;<a href="https://bitcoin-in-action.medium.com/transazione-p2pkh-nel-bitcoin-in-action-playground-c9df028d4930">P2PKH</a>.</p>

<p id="3328">Come vedremo nei video successivi la transazione sarà validata in questo modo:</p>

<p id="4127">— –SCRIPTSIG</p>

<p id="b758">– PUSH della firma digitale</p>

<p id="ab74">– PUSH del redeem script</p>

<p id="7cb4">— –SCRIPTPUBKEY</p>

<p id="76b4">– HASH160 sul redeem script</p>

<p id="125a">– PUSH del redeem script HASH</p>

<p id="a01f">– OP_EQUAL il quale confronta i due digest on top, ovvero il redeem script</p>

<p id="bfe1">Se tutto va a buon fine il redeem script viene&nbsp;<em>deserializzato</em>&nbsp;e viene validata la transazione.</p>

<p id="0c44">La transazione validata step by step è spiegata nel libro&nbsp;<a href="https://bit.ly/38RtF9x">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</a>.</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2021/06/Bitcoin-Italiano-in-action-Segwit.jpg" alt="Bitcoin-Italiano-in-action-Segwit" class="wp-image-13648"/><figcaption><a href="https://bit.ly/38RtF9x" target="_blank" rel="noreferrer noopener">Bitcoin in Action - SegWit, Bitcoin Script &amp; Smart Contracts</a></figcaption></figure>

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
