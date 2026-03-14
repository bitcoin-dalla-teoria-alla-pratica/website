---
title: "Seed Phrase, come si ottiene?"
date: 2019-04-02T12:37:55+01:00
draft: false


tags:
  - "Crittografia"
---




<p></p>
<p>Vi siete mai domandati come si ottiene il <a href="https://en.bitcoin.it/wiki/Seed_phrase" target="_blank" rel="noreferrer noopener">seed phrase</a>?</p>
<p>Il Seed phrase è una serie di parole, che permettono di generare o rigenerare l’albero delle chiavi, di derivare quindi il wallet deterministico.</p>
<p>Quindi se qualcuno trova il seed phrase, va da se che ha a disposizione tutte le nostre chiave e di conseguenza i nostri bitcoin.</p>
<p><strong>Quindi conservatelo in un posto sicuro !</strong></p>
<p>Il <a href="https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki" target="_blank" rel="noreferrer noopener"><strong>BIP39</strong></a> definisce la creazione del mnemonic code e del seed.</p>
<blockquote>
<p>mnemonic code, <strong>mnemonic phrase, mnemonic recovery phrase, mnemonic seed, </strong>seed phrase. Sono tutti sinonimi :)</p>
</blockquote>
<p>La sequenza di queste parole sono sufficienti per ricreare il <strong>seed,</strong> e da qui ricreare il wallet HD e le chiavi derivate.</p>
<blockquote>
<p>Seed Phrase -&gt; Seed-&gt; Chiavi Master -&gt; Chiavi</p>
</blockquote>
<p>Se si usa lo standard mnemonic, abbiamo a disposizione <a href="https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt" target="_blank" rel="noreferrer noopener">un dizionario di 2048 parole</a>, con <strong>2048¹² </strong>combinazioni.</p>
<p>Tali parole sono selezionate con <strong>cura</strong> per non essere simili tra loro e non sbagliare a scriverle.</p>
<h3 id="791a">Gli steps da seguire</h3>
<p>Partiamo da 128 bits, 32 caratteri esadecimali, che rappresentano l’entropia.</p>
<p>Applichiamo lo SHA256 e appendiamo i primi 4 bits (cioè 1 carattere esadecimale) in fondo all’entropia.</p>
<p><br />Questo rappresenta il <a href="https://it.wikipedia.org/wiki/Checksum" target="_blank" rel="noreferrer noopener"><strong>checksum</strong></a><strong>.</strong></p>
<p><br />Convertiamo il risultato ottenuto in base2.</p>
<p><br />Il risultato binario viene diviso in <strong>12 segmenti da 11 bits ciascuno</strong>, ogni segmento rappresenta una <strong>parola</strong>.</p>
<p>È necessario convertire il valore delle singole <em>caselle</em> in base10, in modo tale da ottenere un numero che si può mappare nel <a href="https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt" target="_blank" rel="noreferrer noopener">dizionario</a>.<br /><br /></p>
<p>Prendiamo i valori corrispondenti dei bits accesi, cioè dove è presente il numero 1, e gli sommiamo.</p>
<p>Il risultato che otteniamo è un numero, che mappato al dizionario inglese dato dalle 2048 parole, da come risultato <strong>accident</strong>.</p>
<figure></figure>
<p></p>		
							<figure>
											<a href="https://tinyurl.com/yy8otosv" data-elementor-open-lightbox="">
							<img width="720" height="540" src="http://www.corsobitcoin.com/wp-content/uploads/2019/04/seed.gif" alt="Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”" />								</a>
											<figcaption>Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”</figcaption>
										</figure>
<p>Partiamo dall’entropia</p>
<p><!-- HTML generated using hilite.me --></p>
<pre style="margin: 0; line-height: 125%;">0168071cf29dbdf232de82fa34acb933
</pre>
<p> </p>
<p>applichiamo quindi lo SHA256 e prendiamo il primo carattere del digest.</p>
<p><!-- HTML generated using hilite.me --></p>
<pre style="margin: 0; line-height: 125%;">printf 0168071cf29dbdf232de82fa34acb933 | xxd -r -p | sha256sum -b | head -c 1
&gt; 3</pre>
<p> </p>
<p>Il <strong>3</strong> è il checksum che dobbiamo appendere all’entropia, e poi convertire in base2.</p>
<p><!-- HTML generated using hilite.me --></p>
<pre style="margin: 0; line-height: 125%;">echo "ibase=16; obase=2; $(echo 0168071cf29dbdf232de82fa34acb9333  | tr '[:lower:]' '[:upper:]') " | bc| tr -d 'n'
&gt; 10110100000000111000111001111001010011101101111011111001000110010110111101000001011111010001101001010110010111001001100110011
</pre>
<p><br />Convertendo il primo risultato in base10</p>
<p><!-- HTML generated using hilite.me --></p>
<pre style="margin: 0; line-height: 125%;">echo "ibase=2; 00000001011" | bc
</pre>
<p><br />Otteniamo il risultato </p>
<p><!-- HTML generated using hilite.me --></p>
<pre style="margin: 0; line-height: 125%;">11
</pre>
<p>Possiamo verificare che parola è mappata all’indice 11 <a href="https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt" target="_blank" rel="noreferrer noopener">https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt.</a><br />La parola che troviamo all’indice 11 è <strong>accident</strong>.</p>
<p><strong>Attenzione</strong>, la lista parte da 1, quindi l’elemento è n+1.</p>
<p>Abbiamo la possibilità di verificare il nostro risultato utilizzando il sito <a href="https://iancoleman.io/bip39/#english" target="_blank" rel="noreferrer noopener">https://iancoleman.io/bip39/</a> ed inserire l’entropia che abbiamo utilizzato</p>
							<figure>
											<a href="https://tinyurl.com/yy8otosv" data-elementor-open-lightbox="">
							<img width="1024" height="779" src="http://www.corsobitcoin.com/wp-content/uploads/2019/04/Screenshot-2019-04-03-at-15.00.44-1024x779.png" alt="Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”" srcset="https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2019/04/Screenshot-2019-04-03-at-15.00.44.png?resize=1024%2C779 1024w, https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2019/04/Screenshot-2019-04-03-at-15.00.44.png?resize=300%2C228 300w, https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2019/04/Screenshot-2019-04-03-at-15.00.44.png?resize=768%2C584 768w" sizes="(max-width: 1024px) 100vw, 1024px" />								</a>
											<figcaption>Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”</figcaption>
										</figure>
			<a href="https://tinyurl.com/yy8otosv"><img src="https://cdn-images-1.medium.com/max/800/0*j-onAjAGFzIje-QT"></a>		
		<p>► <a href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica</a> (Amazon)<br />► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a><br />► <a href="https://tinyurl.com/yxe8b8cs">Video corso disponibile su Udemy</a></p>
<p>I nostri social:</p>
<p>► <a href="https://twitter.com/satoshiwantsyou">Twitter</a> , <a href="https://www.facebook.com/bitcoin.corso.completo/">Facebook</a>, <a href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica">Linkedin</a>, <a href="https://medium.com/@bitcoindallateoriallapratica">Medium</a>, <a href="https://www.instagram.com/BitcoinDallaTeoriaAllaPratica">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a></p>
<p>In <b>crypto</b> we trust</p>