---
title: "P2PK, il padre di tutti gli Address Bitcoin"
date: 2021-02-03T11:28:12+01:00
draft: false


tags:
  - "Crittografia"
  - "Script"
---




<figure class="wp-block-image size-large"><img src="/img/p2pk-il-padre-di-tutti-gli-address-bitcoin-1.jpg" alt="P2PK, il padre di tutti gli Address Bitcoin" class="wp-image-13523"/></figure>

<p>In questo ultimo articolo affronteremo con la teoria come si ottiene la chiave privata e come si deriva la chiave pubblica.</p>
<p id="b4dc" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Come già spiegato nei <a class="bq jo" href="https://bitcoin-in-action.medium.com/come-si-riconosce-la-firma-digitale-in-bitcoin-c6fb09a43722" rel="noopener">precedenti articoli</a>, per lo script <strong class="av ju">P2PK</strong>, non esiste un <strong class="av ju">address specifico</strong>. È molto importante comprendere come il protocollo Bitcoin si è evoluto per arrivare ad ottenere gli address che utilizziamo oggi.</p>
<blockquote class="jv jw jx">
<p id="7c4c" class="hx hy jy av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph=""><strong class="av ju">Il tutto parte dalla chiave privata.</strong></p>
</blockquote>
<figure class="ip iq ir is it iu fb fc paragraph-image">
<div class="iv iw ah ix w iy" tabindex="0" role="button">
<div class="fb fc jz">
<div class="jd s ah je">
<div class="ka jg s">
<div class="ec iz ff et eq ja w dv jb jc"> </div>
<img class="qr qs ff et eq ja w c" src="https://miro.medium.com/max/2000/0*bCoJWPyBDlqVK2vG" sizes="700px" srcset="https://miro.medium.com/max/276/0*bCoJWPyBDlqVK2vG 276w, https://miro.medium.com/max/552/0*bCoJWPyBDlqVK2vG 552w, https://miro.medium.com/max/640/0*bCoJWPyBDlqVK2vG 640w, https://miro.medium.com/max/700/0*bCoJWPyBDlqVK2vG 700w" alt="Image for post" width="2000" height="2147" /></div>
</div>
</div>
</div>
<figcaption class="jk jl fd fb fc jm jn av b aw ax ay" data-selectable-paragraph="">SPOILER P2PKH! 👀 — La parte iniziale è identica al P2PK</figcaption>
</figure>
<p id="8bd6" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">La chiave privata è una sequenza di byte ottenuti applicando l’algoritmo <a class="bq jo" href="https://en.bitcoin.it/wiki/Secp256k1" rel="noopener nofollow"><strong class="av ju">secp256k1</strong></a>, i valori che otteniamo devono <em class="jy">ricadere</em> all’interno del range di tale algoritmo.</p>
<p id="00b9" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">L’algoritmo secp256k1 è parte della crittografia delle curve ellittiche, spesso la troviamo l’acronimo <strong class="av ju">ECC</strong>: <strong class="av ju">Elliptic Curve Cryptography</strong>.</p>
<p id="03b9" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Tro<span id="rmm">v</span>iamo anche l’acronimo <strong class="av ju">ECDSA</strong> che ci indica Elliptic <strong class="av ju">Curve Digital Signature Algorithm</strong>.</p>
<blockquote class="jv jw jx">
<p id="cf04" class="hx hy jy av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph=""><strong class="av ju">ECC</strong>: <strong class="av ju">Elliptic Curve Cryptography<br />ECDSA:Curve Digital Signature Algorithm</strong></p>
</blockquote>
<p id="3831" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">La chiave privata deve rispettare le direttive <strong class="av ju">DER</strong>, <a class="bq jo" href="https://en.wikipedia.org/wiki/X.690#DER_encoding" rel="noopener nofollow"><strong class="av ju">Distinguished Encoding Rules</strong></a>. Brevemente, la chiave viene interpretata come un coding binario e non contiene plain text come le chiavi <strong class="av ju">PEM</strong>, come ad esempio —</p>
<pre class="ip iq ir is it kb kc kd"><span id="0548" class="ee ke kf fp kg b dd kh ki s kj" data-selectable-paragraph="">-----BEGIN EC PRIVATE KEY<br />-----</span><span id="6baf" class="ee ke kf fp kg b dd kk kl km kn ko ki s kj" data-selectable-paragraph="">xxxxx</span><span id="415f" class="ee ke kf fp kg b dd kk kl km kn ko ki s kj" data-selectable-paragraph="">---<br />--END EC PRIVATE KEY-----</span></pre>
<p id="ae4a" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Sulla chiave viene aggiunto <a class="bq jo" href="https://en.bitcoin.it/wiki/List_of_address_prefixes" rel="noopener nofollow">un prefisso</a> per identificare se la chiave privata è destinata all’ambiente di <strong class="av ju">main</strong> o per l’ambiente di <strong class="av ju">test</strong>.</p>
<p id="8b4c" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Da qui si ottiene la chiave privata in formato <strong class="av ju">WIF</strong>, acronimo di <strong class="av ju">Wallet Import Format</strong>.</p>
<p id="23f0" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Se vogliamo importare una chiave privata nel nostro wallet utilizzeremo la chiave privata <strong class="av ju">WIF</strong> con il comando <strong class="av ju">importprivkey</strong>.</p>
<pre class="ip iq ir is it kb kc kd"><span id="c904" class="ee ke kf fp kg b dd kh ki s kj" data-selectable-paragraph="">$ bitcoin-cli help importprivkey</span></pre>
<p id="5493" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Quando firmiamo la transazione utilizziamo la chiave privata <strong class="av ju">PEM</strong>, come mostrato nel libro <a class="bq jo" href="https://bit.ly/38RtF9x" rel="noopener nofollow">Bitcoin In Action – SegWit, Bitcoin Script &amp; Smart Contracts</a></p>
<figure class="ip iq ir is it iu fb fc paragraph-image">
<div class="iv iw ah ix w iy" tabindex="0" role="button">
<div class="fb fc io">
<div class="jd s ah je">
<div class="kp jg s">
<div class="ec iz ff et eq ja w dv jb jc"> </div>
<img class="qr qs ff et eq ja w c" src="https://miro.medium.com/max/1280/1*5_3dnFLsXLct77_oX8kfcQ.png" sizes="700px" srcset="https://miro.medium.com/max/276/1*5_3dnFLsXLct77_oX8kfcQ.png 276w, https://miro.medium.com/max/552/1*5_3dnFLsXLct77_oX8kfcQ.png 552w, https://miro.medium.com/max/640/1*5_3dnFLsXLct77_oX8kfcQ.png 640w, https://miro.medium.com/max/700/1*5_3dnFLsXLct77_oX8kfcQ.png 700w" alt="Image for post" width="1280" height="960" /></div>
</div>
</div>
</div>
<figcaption class="jk jl fd fb fc jm jn av b aw ax ay" data-selectable-paragraph=""><a class="bq jo" href="https://bit.ly/38RtF9x" rel="noopener nofollow">Bitcoin In Action — SegWit, Bitcoin Script &amp; Smart Contracts</a></figcaption>
</figure>
<p id="576f" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Applicando un byte (<strong class="av ju">01</strong>), in coda alla chiave, si ottiene la chiave privata <strong class="av ju">WIF</strong> <strong class="av ju">compressa</strong>, altrimenti si ha la chiave WIF non compressa.<br />Ad oggi si utilizza prevalentemente la chiave privata compressa.</p>
<p id="ec3f" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Dalla chiave privata si deriva la chiave pubblica, compressa e non compressa.<br />La chiave pubblica non compressa è quella che abbiamo analizzato negli articoli <a class="bq jo" href="https://bitcoin-in-action.medium.com/come-si-valida-una-transazione-p2pk-92dcafb8dae2" rel="noopener"><strong class="av ju">precedenti dedicati al P2PK</strong></a>, la riconosciamo perchè inizia sempre con il byte <strong class="av ju">04</strong> ed è lunga <strong class="av ju">130</strong> caratteri esadecimali</p>
<p>https://www.youtube.com/embed/NaRh613ME9M</p>
<section class="dc fk fl cx fm">
<div class="n p">
<div class="aj ak al am an fn ap w">
<p id="6535" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">La chiave pubblica compressa si ottiene applicando un <strong class="av ju">version prefix</strong>, verificando l’ultimo byte e applicando la funzione crittografica <strong class="av ju">RIPEMD160</strong>.</p>
<blockquote class="jv jw jx">
<p id="6e92" class="hx hy jy av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Nel <a class="bq jo" href="https://bitcoininaction.com/" rel="noopener nofollow">video corso</a> e nei <a class="bq jo" href="https://www.amazon.it/Alessio-Barnini/e/B07SLZYLC4?ref=sr_ntt_srch_lnk_1&amp;qid=1612347522&amp;sr=8-1" rel="noopener nofollow">nostri libri</a> andiamo con la pratica a generare <strong class="av ju">manualmente</strong> tutti gli indirizzi.</p>
</blockquote>
<p id="892d" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Perchè è stata preferita la chiave pubblica compressa nel corso degli anni?<br />Le <strong class="av ju">fees</strong> si pagano in base a quanto è <em class="jy">pesante</em> la transazione in termini di bytes, o per meglio dire sulla <strong class="av ju">vsize</strong> dopo l’introduzione di SegWit.</p>
<p id="1cf8" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Come ormai sappiamo, la chiave privata <strong class="av ju">non deve essere assolutamente condivisa</strong>, perchè è in grado di generare quella firma digitale comprovabile dalla corrispondete chiave pubblica, che ovviamente è stata possibile derivare solo ed esclusivamente da quella chiave privata.</p>
<p id="e327" class="hx hy fp av b gm jp hz ia gp jq ib ic id jr ie if ig js ih ii ij jt ik il in dc ee" data-selectable-paragraph="">Se ti stai chiedendo perchè è importante la firma,<a class="bq jo" href="https://bitcoin-in-action.medium.com/chiave-privata-firma-digitale-bitcoin-in-action-ef2b470d0227" rel="noopener"> guarda gli articoli precedenti</a>.</p>
</div>
</div>
</section>
<div class="n p cm kr ks kt" role="separator">
<p class="p1">–––––</p>
<p class="p2"><span class="s1">🎥 <a href="https://www.youtube.com/BitcoinInAction"><span class="s2">Bitcoin in Action (YouTube)</span></a></span></p>
<p class="p1">— </p>
<p class="p2"><span class="s1">🐙 GitHub:<a href="https://bit.ly/2Lj3yeY"> https://bit.ly/2Lj3yeY</a></span></p>
<p class="p1">–––</p>
<p class="p2"><span class="s1">📕 <a href="https://amzn.to/3pJcXj1">Bitcoin In Action – SegWit, Bitcoin Script e Smart Contracts (Amazon)</a><span class="Apple-converted-space"> </span></span></p>
<p class="p2"><span class="s1">📕 <a href="https://bit.ly/38RtF9x">Bitcoin In Action – SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a><span class="Apple-converted-space"> </span></span></p>
<p class="p1">–––</p>
<p class="p2"><span class="s1">📒 <a href="https://amzn.to/2MOj1av"><span class="s2">Libro Bitcoin dalla teoria alla pratica (Amazon)</span></a><br />📒 <a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/"><span class="s2">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</span></a><br />📒 <a href="https://amzn.to/2Ym4gz6"><span class="s2">Book Bitcoin from theory to practice (Amazon)</span></a></span></p>
<p class="p2"><span class="s1">📒 <a href="https://bit.ly/3ijAyC4"><span class="s2">Book Bitcoin from theory to practice (accept bitcoin)</span></a><br /> — <br />🎥 <a href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica<span class="s2"><span class="Apple-converted-space"> </span></span></a></span></p>
<p class="p2"><span class="s1"> — <br />📙 <a href="https://amzn.to/3ckIkJj"><span class="s2">Tascabile Bitcoin 199 domande (Amazon)</span></a><br />📙 <a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande"><span class="s2">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</span></a></span></p>
<p class="p2"><span class="s1">📙 <a href="https://amzn.to/3fB4Kbs"><span class="s2">Pocket Book Bitcoin 199 questions (Amazon)</span></a><br />📙 <a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/"><span class="s2">Pocket </span></a><a href="https://www.amazon.it/dp/1078155585"><span class="s2">Book </span></a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/"><span class="s2">Bitcoin 199 questions (accept bitcoin)</span></a><br /> — <br />► ITA: <a href="https://twitter.com/satoshiwantsyou"><span class="s2">Twitter</span></a> , <a href="https://www.facebook.com/satoshiwantsyou"><span class="s2">Facebook</span></a>, <a href="https://bitcoin-in-action.medium.com/"><span class="s2">Medium</span></a>, <a href="https://www.instagram.com/satoshiwantsyou/"><span class="s2">Instagram</span></a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA"><span class="s2">Youtube</span></a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica"><span class="s2">GitHub</span></a></span></p>
<p class="p2"><span class="s1">► ENG: <a href="https://twitter.com/btc_in_action"><span class="s2">Twitter</span></a> , <a href="https://www.facebook.com/bitcoininaction/"><span class="s2">Facebook</span></a>, <a href="https://medium.com/@bitcoin_in_action"><span class="s2">Medium</span></a>, <a href="https://www.instagram.com/bitcoin_in_action/"><span class="s2">Instagram</span></a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA"><span class="s2">Youtube</span></a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica"><span class="s2">GitHub</span></a></span></p>
<p class="p1"><br />Television isn’t a good idea (Radio Stations)<br />Email isn’t a good idea (Post offices)<br />Amazon isn’t a good idea (Retail stores)<br />Bitcoin isn’t a good idea (Central banks)</p>
<p class="p1">In <b>crypto</b> we trust</p>
</div>