---
title: "Address Bitcoin"
date: 2020-12-22T18:16:07+01:00
draft: false


tags:
  - "Script"
  - "Crittografia"
---




<h4>Che cosa è lo stack?</h4>

<p><img src="https://miro.medium.com/max/1280/0*DQgE6OUhAceAOw2Y" alt="Image for post" /></p>
<p id="1520" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Ciao,</p>
<p id="3ec2" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">abbiamo avuto l’idea di creare una nuova playlist per parlare degli address Bitcoin. Spesso sentiamo nomi come Pay to hash public key, oppure Pay to script hash, o ancora bech32.</p>
<p id="f539" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Sono argomenti un pò impegnativi , per questo motivo utilizzeremo una lavagna per creare dei disegni per comprendere meglio l’argomento. Per andare nel dettaglio e capire meglio Bitcoin, io e Alessandro abbiamo scritto 3 libri, <a class="bq jr" href="http://bit.ly/2ADHUN1" rel="noopener nofollow">Bitcoin dalla teoria alla pratica</a>, <a class="bq jr" href="https://bit.ly/38RtF9x" rel="noopener nofollow">Bitcoin in Action</a> e <a class="bq jr" href="https://bit.ly/3cmz07W" rel="noopener nofollow">Bitcoin 199 domande</a>. Oltre a questo facciamo corsi live e offline che trovate su <a class="bq jr" href="http://bitcoininaction.com/" rel="noopener nofollow">bitcoininaction.com</a> in collaborazione con agli amici di <a class="bq jr" href="https://www.bitcoinpeople.it/" rel="noopener nofollow">Bitcoin People.</a></p>
<p id="562e" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Pa<span id="rmm">r</span>tiamo parlando dicendo che non esistono address, ma esistono solo script. Gli address sono il risultato di funzioni crittografiche applicate sulla chiave pubblica.</p>
<p id="2f34" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Utilizzeremo come primo script, l’”address” <strong class="av js">P2PK</strong>.<br />Pensiamo per un attimo al significato di Pay to Public Key. Che cosa ci vuole comunicare? In italiano potremmo tradurla con <em class="jt">pagare a una chiave pubblica</em>. Ed effettivamente è proprio quello che succede, quando si effettua una transazione, essa viene sbloccata confrontando la firma digitale su una chiave pubblica.</p>
<p>Questo non dovrebbe sorprendere, perchè come abbiamo visto nei primi video, <a class="bq jr" href="https://youtu.be/RU7LHPP4Lvk" rel="noopener nofollow">forse proprio il primo video del canale</a>, la firma digitale si valida utilizzando la chiave pubblica derivata dalla chiave privata che ha generato quella firma.</p>
<p id="8866" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Dobbiamo fare un passo indietro prima di parlare della generazione dell’address, dobbiamo chiarire i concetti di <strong class="av js">Stack</strong> e di validazione.</p>
<p id="5d77" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Lo stack è una sequenza di dati, inseriti uno sopra l’altro.<br />Nel caso di Bitcoin si parla di stack <strong class="av js">LIFO</strong>, Last Input First output, quindi il primo elemento che entra è anche il primo ad uscire. Un ulteriore particolarità è che lo stack è <a class="bq jr" href="https://en.wikipedia.org/wiki/Reverse_Polish_notation" rel="noopener nofollow"><strong class="av js">Reverse Polish</strong></a>, ovvero gli operatori seguono l’operandi.</p>
<p>Senza andare troppo nel dettaglio, vediamo un esempio.</p>
<p id="13e4" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">L’operazione che vogliamo fare è una somma 2 + 2, quindi secondo l’annotazione polacca prima mettiamo 22 e poi l’operazione somma, OP_ADD.</p>
<p><iframe src="https://www.youtube.com/embed/gJgavv8wIYs" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe></p>
<p><img src="https://miro.medium.com/max/1646/1*FSsyaz5zQak6TJQFRbeWpg.png" alt="Image for post" /></p>
<p class="graf graf--p"><img src="https://miro.medium.com/max/1548/1*4tcl_pEcUI2CZ1WRgZOSHQ.png" alt="Image for post" /></p>
<p id="bff4" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Viene inserito il primo elemento nello stack. quando un elemento viene inserito nello stack si chiama operazione di push.</p>
<figure class="ju jv jw jx jy hu ey ez paragraph-image">
<div class="ih ii ah ij w ik" tabindex="0" role="button">
<div class="ey ez ki">
<div class="ip s ah iq">
<div class="kj is s">
<div class="ed il fc er eo im w dw in io"><img src="https://miro.medium.com/max/1530/1*97pDz5H7frrGRkbrD4cojw.png" alt="Image for post" /></div>
</div>
</div>
</div>
</div>
</figure>
<p id="1fcd" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Successivamente viene inserito il secondo operatore</p>
<p id="e2d6" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Ed infine viene inserito l’operando che ha il compito di prendere i primi due elementi in top, quindi in cima allo stack, applicare la funzione della somma, e inserire il risultato nello stack.</p>
<p>Quindi l’operazione che farà saranno. POP di 2, POP di 2, PUSH di 4.</p>
<p data-selectable-paragraph=""><img src="https://miro.medium.com/max/1572/1*IZ9jSG3dCNKUFHgfM-9neA.png" alt="Image for post" /></p>
<article>
<div>
<section class="dd fh fi cy fj">
<div class="n p">
<div class="aj ak al am an fk ap w">
<p id="9c84" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Questo è un primo passo per capire come vengono validate le transazioni.</p>
<p id="d367" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Se volete approfondire questo argomento iscrivetevi al canale e visitate il nostro sito <a class="bq jr" href="http://corsobitcoin.com/" rel="noopener nofollow">corsobitcoin.com</a>, dove trovate i nostri libri e i nostri contatti.</p>
<p id="4bac" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Ciao alla prossima</p>
</div>
</div>
</section>
<section class="dd fh fi cy fj">
<div class="n p">
<div class="aj ak al am an fk ap w">
<p id="9b12" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">— — –</p>
<p id="bd12" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">🎥 <a class="bq jr" href="https://www.youtube.com/BitcoinInAction" rel="noopener nofollow">Bitcoin in Action (YouTube)</a></p>
<p id="5c99" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">—</p>
<p id="2b2d" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">🐙 GitHub:<a class="bq jr" href="https://bit.ly/2Lj3yeY" rel="noopener nofollow"> https://bit.ly/2Lj3yeY</a></p>
<p id="5e34" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">— –</p>
<p id="3da5" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">📕 <a class="bq jr" href="https://amzn.to/3pJcXj1" rel="noopener nofollow">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></p>
<p id="c6ee" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">📕 <a class="bq jr" href="https://bit.ly/38RtF9x" rel="noopener nofollow">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a></p>
<p id="033a" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">— –</p>
<p id="8d9a" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">📒 <a class="bq jr" href="https://amzn.to/2MOj1av" rel="noopener nofollow">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br />📒 <a class="bq jr" href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" rel="noopener nofollow">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a><br />📒 <a class="bq jr" href="https://amzn.to/2Ym4gz6" rel="noopener nofollow">Book Bitcoin from theory to practice (Amazon)</a></p>
<p id="4f4f" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">📒 <a class="bq jr" href="https://bit.ly/3ijAyC4" rel="noopener nofollow">Book Bitcoin from theory to practice (accept bitcoin)</a><br />—<br />🎥 <a class="bq jr" href="https://bit.ly/3cUJDyZ" rel="noopener nofollow">Video Corso Bitcoin dalla teoria alla pratica</a></p>
<p id="e640" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">—<br />📙 <a class="bq jr" href="https://amzn.to/3ckIkJj" rel="noopener nofollow">Tascabile Bitcoin 199 domande (Amazon)</a><br />📙 <a class="bq jr" href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" rel="noopener nofollow">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a></p>
<p id="7e16" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">📙 <a class="bq jr" href="https://amzn.to/3fB4Kbs" rel="noopener nofollow">Pocket Book Bitcoin 199 questions (Amazon)</a><br />📙 <a class="bq jr" href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" rel="noopener nofollow">Pocket </a><a class="bq jr" href="https://www.amazon.it/dp/1078155585" rel="noopener nofollow">Book </a><a class="bq jr" href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" rel="noopener nofollow">Bitcoin 199 questions (accept bitcoin)</a><br />—<br />► ITA: <a class="bq jr" href="https://twitter.com/satoshiwantsyou" rel="noopener nofollow">Twitter</a> , <a class="bq jr" href="https://www.facebook.com/satoshiwantsyou" rel="noopener nofollow">Facebook</a>, <a class="bq jr" href="https://bitcoin-in-action.medium.com/" rel="noopener">Medium</a>, <a class="bq jr" href="https://www.instagram.com/satoshiwantsyou/" rel="noopener nofollow">Instagram</a>, <a class="bq jr" href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" rel="noopener nofollow">Youtube</a>, <a class="bq jr" href="https://github.com/bitcoin-dalla-teoria-alla-pratica" rel="noopener nofollow">GitHub</a></p>
<p id="e657" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">► ENG: <a class="bq jr" href="https://twitter.com/btc_in_action" rel="noopener nofollow">Twitter</a> , <a class="bq jr" href="https://www.facebook.com/bitcoininaction/" rel="noopener nofollow">Facebook</a>, <a class="bq jr" href="https://medium.com/@bitcoin_in_action" rel="noopener">Medium</a>, <a class="bq jr" href="https://www.instagram.com/bitcoin_in_action/" rel="noopener nofollow">Instagram</a>, <a class="bq jr" href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" rel="noopener nofollow">Youtube</a>, <a class="bq jr" href="https://github.com/bitcoin-dalla-teoria-alla-pratica" rel="noopener nofollow">GitHub</a></p>
<p id="8a6d" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">Television isn’t a good idea (Radio Stations)<br />Email isn’t a good idea (Post offices)<br />Amazon isn’t a good idea (Retail stores)<br />Bitcoin isn’t a good idea (Central banks)</p>
<p id="6321" class="iw ix fm av b gj iy iz ja gm jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq dd ef" data-selectable-paragraph="">In <strong class="av js">crypto</strong> we trust</p>
</div>
</div>
</section>
</div>
</article>