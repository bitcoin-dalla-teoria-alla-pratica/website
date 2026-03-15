---
title: "File di configurazione Bitcoin"
date: 2020-01-27T08:52:46+01:00
draft: false

tags:
  - "Nodo & Network"
---

<section>
<p id="4fd8" style="text-align: left;" data-selectable-paragraph="">Nell’<a href="https://www.corsobitcoin.com/imparare-bitcoin/" target="_blank" rel="noopener noreferrer">articolo precedente</a>&nbsp;abbiamo installato il nodo Bitcoin sul proprio computer e abbiamo passato come parametro -regtest per interagire in locale.</p>
<p id="8d5d" style="text-align: left;" data-selectable-paragraph="">Un parametro non è cosi scomodo da passare ogni volta che vogliamo fare delle chiamate, ma quando il comando da eseguire diventa</p>
<pre>bitcoind -datadir=$PWD/regtest2 -regtest -debug=1 -rpcport=28443 -port=28444 -addnode=localhost:18444</pre>
<p id="0436" style="text-align: left;" data-selectable-paragraph="">non è il massimo.</p>
<figure>
<iframe title="King Of The Hill Eating GIF - Find &amp; Share on GIPHY" src="https://cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fgiphy.com%2Fembed%2F129fSchexp3aPC%2Ftwitter%2Fiframe&amp;url=https%3A%2F%2Fmedia.giphy.com%2Fmedia%2F129fSchexp3aPC%2Fgiphy.gif&amp;image=https%3A%2F%2Fi.giphy.com%2Fmedia%2F129fSchexp3aPC%2Fgiphy.gif&amp;key=a19fcc184b9711e1b4764040d3dc5c07&amp;type=text%2Fhtml&amp;schema=giphy" width="435" height="244" frameborder="0" scrolling="auto" allowfullscreen="allowfullscreen" data-mce-fragment="1"></iframe>
<figcaption></figcaption>
</figure>
<p id="67ea" style="text-align: left;" data-selectable-paragraph="">Fortunatamente possiamo utilizzare un file di configurazione per gestire uno o più nodi sullo stesso computer.</p>
<p id="cdc5" style="text-align: left;" data-selectable-paragraph="">Nel repository ufficiale Bitcoin possiamo trovare un esempio di file di&nbsp;<a href="https://github.com/bitcoin/bitcoin/blob/master/share/examples/bitcoin.conf" target="_blank" rel="noopener nofollow noreferrer">configurazione</a>. Degno di nota anche questo&nbsp;<a href="https://jlopp.github.io/bitcoin-core-config-generator/" target="_blank" rel="noopener nofollow noreferrer">link</a>&nbsp;che ti aiuta a crearlo realtime.</p>
<p id="af38" style="text-align: left;" data-selectable-paragraph="">Di default il nodo Bitcoin effettua una ricerca del file&nbsp;<strong>bitcoin.conf</strong>&nbsp;nella&nbsp;<a href="https://en.bitcoin.it/wiki/Data_directory" target="_blank" rel="noopener nofollow noreferrer">datadir di default</a>. Nel Mac è&nbsp;<strong>~/Library/Application Support/Bitcoin</strong>.</p>
<p id="1361" style="text-align: left;" data-selectable-paragraph="">Così, creando il file&nbsp;<strong>bitcoin.conf</strong>&nbsp;all’interno della cartella di default possiamo impostare il parametro regtest senza doverlo passare come parametro.</p>
<pre>regtest=1
<br># Options only for mainnet[main]
<br># Options only for testnet[test]
<br># Options only for regtest[regtest]</pre>
<p id="7b20" style="text-align: left;" data-selectable-paragraph="">Adesso possiamo utilizzare il client senza passare nessun parametro.</p>
<pre>$ bitcoin-cli getblockcount
0</pre>
<p id="0f66" style="text-align: left;" data-selectable-paragraph="">Otteniamo lo stesso risultato del&nbsp;<a href="https://www.corsobitcoin.com/imparare-bitcoin/" target="_blank" rel="noopener noreferrer">tutorial precedente</a>.</p>
<p id="7e41" style="text-align: left;" data-selectable-paragraph="">Nel prossimo tutorial vedremo come far comunicare due o più nodi sullo stesso computer!</p>
<figure>
<p><img alt="File di configurazione Bitcoin" role="presentation" src="https://miro.medium.com/max/1023/1*GulUDJxcumDlTzZVU_yNww.png" width="1023" height="492"></p>
</figure>
</section>
<hr>
<section>
<p id="b90c" data-selectable-paragraph="">►&nbsp;<a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener nofollow noreferrer">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>►&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener nofollow noreferrer">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a><br>—<br>►&nbsp;<a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener nofollow noreferrer">Tascabile Bitcoin 199 domande (Amazon)</a><br>►&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande" target="_blank" rel="noopener nofollow noreferrer">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a></p>
<p id="8478" data-selectable-paragraph="">►&nbsp;<a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener nofollow noreferrer">Pocket Book Bitcoin 199 questions (Amazon)</a><br>►&nbsp;<a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" target="_blank" rel="noopener nofollow noreferrer">Pocket&nbsp;</a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener nofollow noreferrer">Book&nbsp;</a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" target="_blank" rel="noopener nofollow noreferrer">Bitcoin 199 questions (official website — accept bitcoin)</a><br>—<br>►&nbsp;<a href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13" target="_blank" rel="noopener nofollow noreferrer">Video corso disponibile su Udemy</a></p>
<br>►&nbsp;<a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener nofollow noreferrer">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/bitcoin.corso.completo/" target="_blank" rel="noopener nofollow noreferrer">Facebook</a>,&nbsp;<a href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener nofollow noreferrer">Linkedin</a>,&nbsp;<a href="https://medium.com/@bitcoindallateoriallapratica" target="_blank" rel="noopener noreferrer">Medium</a>,&nbsp;<a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener nofollow noreferrer">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener nofollow noreferrer">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener nofollow noreferrer">GitHub</a></p>

<p id="576c" data-selectable-paragraph="">In&nbsp;<strong>crypto</strong>&nbsp;we trust</p>
</section>