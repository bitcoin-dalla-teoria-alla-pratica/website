---
title: "Introduzione a P2SH"
date: 2021-03-26T21:36:27+01:00
draft: false

tags:
  - "Script"
  - "Crittografia"
---

<h2 id="6583">Pay to Public Key</h2>

<figure class="wp-block-gallery columns-1 is-cropped"><ul class="blocks-gallery-grid"><li class="blocks-gallery-item"><figure><img src="/img/introduzione-a-p2sh-1.jpg" alt="Introduzione a P2SH" data-id="13623" data-full-url="https://www.corsobitcoin.com/wp-content/uploads/2021/03/maxresdefault.jpg" data-link="https://www.corsobitcoin.com/?attachment_id=13623" class="wp-image-13623"/></figure></li></ul></figure>

<p id="a0cc">Lo&nbsp;<strong>P2PKH&nbsp;</strong>si presenta così:</p>

<ul><li>lo&nbsp;<strong>scriptSig</strong>&nbsp;è formato da: Signature, Public key compressa.</li><li>lo&nbsp;<strong>scriptPubKey</strong>&nbsp;è formato dalle operation code OP_DUP OP_HASH PBH OP_EQUALVERIFY OP_CHECKSIG dove PBH rappresenta l’hash della chiave pubblica compressa.</li></ul>

<p id="ea35">Lo&nbsp;<strong>P2SH</strong>&nbsp;è invece formato in questo modo:</p>

<ul><li>Lo scriptSig è formato da signatures {serialized script}</li><li>Lo scriptPubKey è formato da OP_HASH160 [20-byte-hash-value] OP_EQUAL</li></ul>

<figure class="wp-block-image"><img src="https://miro.medium.com/max/1239/1*p7w35Sdwp8xs4j0BgI3Y9Q.png" alt="Introduzione a P2SH"/></figure>

<p id="0804">Che cosa sono il serialized Script e 20-byte hash?</p>

<p id="95b8">Premettendo che, in questi articoli andremo ad analizzare solo template riconosciuti da bitcoin-core, non andremo quindi a creare script custom, i quali invece sono affrontati nel libro&nbsp;<a href="https://bit.ly/38RtF9x">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</a>.</p>

<p id="c7d6">Il serialised script, viene descritto nel&nbsp;<a href="http://bit.ly/3blePHt">Il BIP0016</a>, Bitcoin Improve Proposal (2013), e rappresenta lo script da eseguire al fine di ottenere una transazione valida. Questo è conosciuto anche come&nbsp;<strong>redeem script</strong>.</p>

<p id="3505">Il suo hash è ottenuto dall’op_code HASH160, ovvero il digest della funzione crittografica SHA256 e RIPEMD160, è posizionato nello scriptPubKey.</p>

<p id="15fa">Che cosa può contenere il redeem script? Può contenere qualsiasi cosa, come scritto in precedenza, anche script custom.<br>Ci sono dei template&nbsp;<em>standard,&nbsp;</em>che vengono riconosciuti da Bitcoin core al momento della firma, tra questi troviamo i vari Wrap di P2PK, P2PKH, Multisig e SegWit (non nativo).</p>

<p id="e0e3">La cosa interessante da sottolineare è che, quando andiamo a pagare a un address P2SH, se questo non ha mai fatto nessuna transazione, non sapremo mai che condizioni sono necessarie per sbloccare il suo UTXO, proprio perchè nel suo ScriptPubKey troviamo l’hash del redeem script.</p>

<p id="1a27">Solo al momento di una sua spesa, potremo andare ad analizzare il suo redeem script, nel suo scriptSig di riferimento, proprio perchè&nbsp;<em>in chiaro.</em></p>

<p id="69b5">Nel prossimo articolo andremo nel dettaglio della costruzione dell’address P2SH Wrap P2PK.</p>

<p id="c3d2">Ciao!</p>

<p id="3acd">🐳&nbsp;<a href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground">Playground Bitcoin in Action</a></p>

<p id="6e67">🎥&nbsp;<a href="https://www.youtube.com/BitcoinInAction">Bitcoin in Action (YouTube)</a></p>

<p id="5780">🐙 GitHub:<a href="https://bit.ly/2Lj3yeY">&nbsp;https://bit.ly/2Lj3yeY</a></p>

<p id="1c89">📕&nbsp;<a href="https://amzn.to/3pJcXj1">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></p>

<p id="f459">📕&nbsp;<a href="https://bit.ly/38RtF9x">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a></p>

<p id="5d58">📒&nbsp;<a href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>📒&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a><br>📒&nbsp;<a href="https://amzn.to/2Ym4gz6">Book Bitcoin from theory to practice (Amazon)</a></p>

<p id="4dc1">📒&nbsp;<a href="https://bit.ly/3ijAyC4">Book Bitcoin from theory to practice (accept bitcoin)</a><br>—<br>🎥&nbsp;<a href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a></p>

<p id="2c1d">—<br>📙&nbsp;<a href="https://amzn.to/3ckIkJj">Tascabile Bitcoin 199 domande (Amazon)</a><br>📙&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a></p>

<p id="a02b">📙&nbsp;<a href="https://amzn.to/3fB4Kbs">Pocket Book Bitcoin 199 questions (Amazon)</a><br>📙&nbsp;<a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Pocket&nbsp;</a><a href="https://www.amazon.it/dp/1078155585">Book&nbsp;</a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Bitcoin 199 questions (accept bitcoin)</a><br>—<br>► ITA:&nbsp;<a href="https://twitter.com/satoshiwantsyou">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/satoshiwantsyou">Facebook</a>,&nbsp;<a href="https://bitcoin-in-action.medium.com/">Medium</a>,&nbsp;<a href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a></p>

<p id="ac8c">► ENG:&nbsp;<a href="https://twitter.com/btc_in_action">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/bitcoininaction/">Facebook</a>,&nbsp;<a href="https://medium.com/@bitcoin_in_action">Medium</a>,&nbsp;<a href="https://www.instagram.com/bitcoin_in_action/">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a></p>

<p id="ed2a">In&nbsp;<strong>crypto</strong>&nbsp;we trust</p>
