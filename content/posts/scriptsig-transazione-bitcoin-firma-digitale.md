---
title: "Che cosa è lo scriptSig?"
date: 2020-07-15T13:41:49+01:00
draft: false


tags:
  - "UTXO"
  - "Crittografia"
---




<section><section><section><section><section>
<section>
Ciao,
Abbiamo ricevuto una domanda da parte di Luca, che ci chiede.
<blockquote>In alcuni video avete parlato di scriptSig, che cosa è?</blockquote>
Bene Luca, lo <strong>scriptSig</strong> è parte della transazione di Bitcoin.
Puoi immaginare la transazione <strong>non SegWit</strong> cosi strutturata.
<figure><img alt="Che cosa è lo scriptSig?" src="https://cdn-images-1.medium.com/max/800/1*SyzHAwvw2nTMrL7W3IYG6w.png" data-image-id="1*SyzHAwvw2nTMrL7W3IYG6w.png" data-width="2232" data-height="1453" /><figcaption>Immagine estratta dal <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">videocorso</a> e dal libro<a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av"> Bitcoin dalla teoria alla pratica</a></figcaption></figure>
<ul>
 	<li>La versione della transazione</li>
 	<li>Il numero di input</li>
 	<li>L’input</li>
 	<li>Il numero di output</li>
 	<li>l’output</li>
 	<li>e il locktime</li>
</ul>
Dove si posiziona lo <strong>scriptSig</strong>?
Lo scriptSig è all’interno di ogni singolo input, e contiene gli elementi che andranno a soddisfare la UTXO di riferimento. Attenzione, nelle transazioni Segwit native lo <strong>scriptSig è vuoto</strong>, risolvendo così la <strong>transaction malleability e la scalabilità della rete Bitcoin</strong>.
Per questo esempio utilizzeremo una transazione <strong>legacy</strong>, una <strong>P2PKH</strong> e analizzeremo nel dettaglio ogni singolo byte, vediamo come.
<blockquote>In Action</blockquote>
<iframe src="https://www.youtube.com/embed/IPpSCOy3yHg" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<figure>
Prendiamo una semplice transazione dalla blockchain <a style="background-color: var(--mdc-theme-surface,#fff);" href="https://btc.bitaps.com/c2297c9fefdd058e2ce5477868bcbf88bd4f860fbb552399053e3666687809bd" target="_blank" rel="noopener noreferrer" data-href="https://btc.bitaps.com/c2297c9fefdd058e2ce5477868bcbf88bd4f860fbb552399053e3666687809bd">mainnet</a>.
</figure>
<pre><strong>$</strong> bitcoin-cli getrawtransaction c2297c9fefdd058e2ce5477868bcbf88bd4f860fbb552399053e3666687809bd 2</pre>
La transazione contiene un input e due output. La nostra attenzione in questo momento ricade sull’input, all’interno dell’array vin
<pre>“vin”: [</pre>
<pre>{</pre>
<pre>“txid”: “d44cbca5911e53322e14fe0617f078dd1f162a7dcb97f83690eac285ed7ebe80”,</pre>
<pre>“vout”: 1,</pre>
<pre>“scriptSig”: {</pre>
<pre>“asm”: “3044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7[ALL] 04794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732”,</pre>
<pre>“hex”: “473044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7014104794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732”</pre>
<pre>},</pre>
<pre>“sequence”: 4294967295</pre>
<pre>}</pre>
<pre>],</pre>
Analizziamo quindi il suo hex, ovvero l’esadecimale. Questo è lo scriptSig e lo salviamo nella variabile d’ambiente SCRIPTSIG.
<pre>SCRIPTSIG=473044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7014104794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732</pre>
Dato che stiamo analizzando una transazione P2PKH, all’interno dello scriptSig ci aspettiamo la firma digitale e la chiave pubblica. Dobbiamo conoscere leggermente il linguaggio script, ma per questo esempio vi basterà sapere che esistono delle costanti che ci indicano quanti caratteri esadecimali prendere successivamente.
Ad esempio 47, ricade esattamente nel range delle costanti.
<pre>$ echo $SCRIPTSIG | cut -c 1–2</pre>
Grazie al metodo cut riesco a prendere la porzione di byte di interesse
47 in base2 è 71, i quali rappresentano i byte.
Sappiamo che un byte può essere rappresentato da 2 caratteri esadecimali, 71*2 = 142.
Questo significa che dobbiamo considerare i 142 caratteri successivi all’esadecimale 47.
Ecco il calcolo da base 16 a base 2, e la moltiplicazione per due per conoscere i caratteri esadecimali da prendere in considerazione
<pre>$ expr `echo “ibase=16; $(printf 47)” | bc` “*” 2</pre>
Ed ecco la porzione di esadecimali che rappresentano la firma digitale.
<pre>$ echo $SCRIPTSIG | cut -c 3–142</pre>
<pre>3044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7</pre>
<pre>$ printf 3044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7 | wc -c</pre>
Contando gli esadecimali estratti grazie al metodo wc notiamo che sono 140 e non 142, perchè?
Perchè il prossimo byte è il flag che indica come è stata firmata la transazione, solitamente SIGHASH_ALL rappresentato da 01
<pre>$ echo $SCRIPTSIG | cut -c 143–144</pre>
<pre>01</pre>
il prossimo byte cade nuovamente nel range delle costante di Bitcoin script
<pre>$ echo $SCRIPTSIG | cut -c 145–146
41</pre>
e ci indica quanti esadecimali prendere in considerazione successivamente.
Ripeto l’operazione descritta poco fa
<pre>$ expr `echo “ibase=16; $(printf 41)” | bc` “*” 2</pre>
<pre>130</pre>
estraggo quindi la porzione di esadecimali indicata
<pre>$ echo $SCRIPTSIG | cut -c 147–277</pre>
<pre>04794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732</pre>
I seguenti byte sono la chiave pubblica necessaria per verificare la firma e per soddisfare la UTXO di riferimento.
Come?
Vediamo la UTXO grazie al metodo getrawtransaction
<pre>$ bitcoin-cli getrawtransaction d44cbca5911e53322e14fe0617f078dd1f162a7dcb97f83690eac285ed7ebe80 2</pre>
Alla seconda posizione dell’array troviamo la UTXO da sbloccare, questo lo sappiamo dal valore vout contenuto in vin.
Che cosa è quel valore dopo HASH160, ba716926b9313ca3bcf2791cf96a0f5f89472261?
È il digest della nostra chiave pubblica dopo aver applicato le funzioni crittografiche sha256 e ripemd160.
<pre>$ printf $(echo 04794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732 | xxd -r -p | openssl sha256| sed ‘s/^.* //’) |xxd -r -p | openssl ripemd160 | sed ‘s/^.* //’</pre>
Lo script non confronterà solo l’hash della chiave pubblica ma anche la firma stessa.
Diciamo che la domanda che il protocollo Bitcoin si pone è:
<ul>
 	<li>L’hash (HASH160) della chiave pubblica dello scriptSig è uguale all’hash della chiave pubblica contenuta nello <strong>scriptPubKey</strong> della UTXO?</li>
 	<li>La firma può essere verificata con la chiave pubblica presente nello scriptSig?</li>
</ul>
Nel libro <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av"><strong>Bitcoin dalla teoria alla pratica</strong></a> e nel <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">video corso</a>, analizziamo byte per byte la transazione P2PKH andando nel dettaglio della firma e studiando la convenzione DER
Bene abbiamo chiarito che cosa è lo scriptSig e dove si trova.
Spero che il video vi sia piaciuto, ciao e alla prossima
— —
🎥 <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">Bitcoin in Action</a>
—
🐙 GitHub:<a href="https://bit.ly/2Lj3yeY" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/2Lj3yeY"> https://bit.ly/2Lj3yeY</a>
—
📖 <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a>
📖 <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📖 <a href="https://amzn.to/2Ym4gz6" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ym4gz6">Book Bitcoin from theory to practice</a>
—
📖 <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a>
📖 <a href="https://amzn.to/3fB4Kbs" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3fB4Kbs">Pocket Book Bitcoin 199 questions (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Bitcoin 199 questions (accept bitcoin)</a>
—
🎥 <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a>
—
► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a> , <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a href="https://www.linkedin.com/company/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/satoshiwantsyou">Linkedin</a>, <a href="https://medium.com/@satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou/">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a>
Television isn’t a good idea (Radio Stations)
Email isn’t a good idea (Post offices)
Amazon isn’t a good idea (Retail stores)
Bitcoin isn’t a good idea (Central banks)
In <strong>crypto</strong> we trust
</section>
</section>
<section>
</section>
</section></section></section></section><section></section>