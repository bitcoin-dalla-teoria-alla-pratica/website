---
title: "Pretty Good Privacy"
date: 2020-01-13T08:21:05+01:00
draft: false


tags:
  - "Crittografia"
---




<h4>PGP/GPG come verificare i pacchetti Bitcoin e Electrum.</h4><section>
<hr>
<p>Ma ti pare che capita a me?<br>Ecco il primo pensiero che ci viene in mente quando scarichiamo un software.<br>È molto interessante come nella prima pagina di <strong>Electrum</strong> ci sia questo messaggio:</p>
<blockquote>
<p>Warning: Electrum versions older than 3.3.4 are susceptible to <a href="https://github.com/spesmilo/electrum/issues/4968" target="_blank" rel="noopener noreferrer" data-href="https://github.com/spesmilo/electrum/issues/4968">phishing</a>. Do not download Electrum from another source than electrum.org,<strong> and learn to verify GPG signatures</strong>.</p>
</blockquote>
<figure><img src="https://cdn-images-1.medium.com/max/800/0*O0l-9eGBSVdJVL99.jpg" data-image-id="0*O0l-9eGBSVdJVL99.jpg" data-width="850" data-height="400"><p></p>
<figcaption>Don’t trust,&nbsp;verify!</figcaption>
</figure>
<p>Q: Che cosa significa PGP?<br>R: Pretty good privacy, scritto da <a href="https://it.wikipedia.org/wiki/Phil_Zimmermann" target="_blank" rel="noopener noreferrer" data-href="https://it.wikipedia.org/wiki/Phil_Zimmermann">Phil Zimmermann</a> e ora fa parte della PGP Corporation. È un software di crittografia.</p>
<p>Q: Che cosa significa GPG?<br>R: Gnu Privacy Guard, è un aggiornamento di PGP.&nbsp;</p>
<p>Q: Come posso essere sicuro di aver scaricato esattamente il pacchetto corretto?<br>R: Verificando la firma digitale di quel pacchetto.</p>
<p>Q: Con cosa si verifica la firma digitale?<br>R: Con la chiave pubblica del firmatario.</p>
<p>Q: Come posso recuperare la chiave pubblica del firmatario?<br>R: Puoi recuperare la chiave pubblica dal sito di riferimento o utilizzando dei <strong>keyserver</strong> inserendo il suo <strong>fingerprint</strong>.</p>
<p>Ok sono pronto a scaricare e a verificare il pacchetto Bitcoin!</p>
<p>Prima di tutto è necessario installare <a href="https://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/" target="_blank" rel="noopener noreferrer" data-href="https://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/">GPG</a>.<br>Una volta installato potete verificare la versione in uso.</p>
<pre>$ gpg --version
gpg (GnuPG/MacGPG2) 2.2.17</pre>
<p>Andiamo quindi a scaricare l’ultimo pacchetto di <a href="https://bitcoin.org/en/version-history" target="_blank" rel="noopener noreferrer" data-href="https://bitcoin.org/en/version-history">Bitcoin Core</a> dal sito ufficiale<br><a href="https://bitcoin.org/en/version-history" target="_blank" rel="noopener noreferrer" data-href="https://bitcoin.org/en/version-history">https://bitcoin.org/en/version-history</a>. Ad oggi è lo 0.19.0.1.</p>
<p>Dato che io sto utilizzando un Mac, scaricherò la versione osx64 <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/">https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/</a> e le relative firme <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc">https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc</a></p>
<p>Se non disponiamo dell’interfaccia grafica, possiamo utilizzare il comando wget.</p>
<pre>$ wget <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-osx64.tar.gz" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-osx64.tar.gz">https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-osx64.tar.gz</a>
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc</pre>
<p id="1010" data-selectable-paragraph="">Per prima cosa verifichiamo che il checksum ottenuto con l’algoritmo SHA256 sul pacchetto&nbsp;<em>tar</em>&nbsp;appena scaricato sia fedele a quello che troviamo all’interno di SHA256SUM.ASC, così da essere sicuri di aver scaricato il pacchetto desiderato.</p>
<pre>$ sha256sum --check SHA256SUMS.asc --ignore-missing</pre>
<p id="8e5f" data-selectable-paragraph="">risultato:</p>
<pre>bitcoin-0.19.0.1-osx64.tar.gz: OK<br>sha256sum: WARNING: 20 lines are improperly formatted</pre>
<p id="8215" data-selectable-paragraph=""><em>NB: tutti i file e i comandi sono eseguiti all’interno della stessa cartella.</em></p>
<p id="6ca7" data-selectable-paragraph="">Adesso dobbiamo verificare che il pacchetto provenga esattamente dal mittente voluto.<br>Dobbiamo quindi utilizzare la chiave pubblica che verifica la firma.<br><br></p>
</section>
<section>
<hr>
<blockquote>
<p><a href="https://medium.com/@bitcoindallateoriallapratica/firma-digitale-bitcoin-ecdsa-ecc-blockchain-guida-blockchain-b7278ac4bad1?source=your_stories_page---------------------------" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoindallateoriallapratica/firma-digitale-bitcoin-ecdsa-ecc-blockchain-guida-blockchain-b7278ac4bad1?source=your_stories_page---------------------------"><em>Se hai bisogno di una rinfrescata sulla crittografia, guarda qui</em></a><em> 👀</em></p>
</blockquote>
</section>
<section>
<hr>
<p>Possiamo ottenere il fingerprint della relativa chiave pubblica a questo indirizzo https://bitcoin.org/en/full-node#osx-daemon.</p>
<p>Il fingerprint è:<br><code>01EA 5486 DE18 A882 D4C2  6845 90C8 019E 36C2 E964</code></p>
<p>Non ci resta che scaricarla e verificare l’integrità del pacchetto.<br>Per prima cosa verifichiamo se abbiamo già quella chiave, elencando tutte le chiavi nel nostro computer, con il comando:</p>
<pre>$ gpg --list-keys</pre>
<p>o per essere più precisi:</p>
<pre>$ gpg --fingerprint "01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964"</pre>
<p>Se non abbiamo nessun risultato, dobbiamo importarla.<br>Per farlo ci sono diversi metodi.</p>
<p><strong>Metodo 1:<br></strong>Interrogare il keyserver tramite fingerprint.</p>
<pre>$ gpg --keyserver hkps://keyserver.ubuntu.com --receive-keys “01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964”</pre>
<p><strong>Metodo 2:<br></strong>Scaricare la chiave pubblica dal sito Bitcoin e importarla.</p>
<pre>$ wget <a href="https://bitcoin.org/laanwj-releases.asc" target="_blank" rel="noopener nofollow noreferrer" data-href="https://bitcoin.org/laanwj-releases.asc">https://bitcoin.org/laanwj-releases.asc</a><br>$ gpg --import <a href="https://bitcoin.org/laanwj-releases.asc" target="_blank" rel="noopener nofollow noreferrer" data-href="https://bitcoin.org/laanwj-releases.asc">laanwj-releases.asc</a></pre>
<p><strong>Metodo 3:<br></strong>A questo link <a href="https://bitcoincore.org/en/download/" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/en/download/">https://bitcoincore.org/en/download/</a> è possibile trovare l’id chiavi <strong>01EA5486DE18A882D4C2684590C8019E36C2E964</strong></p>
<pre>$ gpg --keyserver keys.gnupg.net --search-key 01EA5486DE18A882D4C2684590C8019E36C2E964</pre>
<p>È possibile anche cercarla da <a href="https://keyserver.ubuntu.com/" target="_blank" rel="noopener noreferrer" data-href="https://keyserver.ubuntu.com/">https://keyserver.ubuntu.com/</a> inserendo <strong>0x01EA5486DE18A882D4C2684590C8019E36C2E964.</strong></p>
<p>Dopo aver scelto uno dei metodi, possiamo verificare se è stata importata utilizzando i comandi sopra riportatati, list-keys o fingerprint.</p>
<pre>$ gpg --fingerprint "01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964"</pre>
<pre>pub rsa4096 2015–06–24 [SC] [expires: 2022–02–10]
01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964
uid [ unknown] Wladimir J. van der Laan (Bitcoin Core binary release signing key) &lt;laanwj@gmail.com&gt;</pre>
<p>Possiamo finalmente <strong>verificare di aver scaricato il pacchetto corretto.</strong></p>
<pre>$ gpg --verify SHA256SUMS.asc</pre>
<pre>gpg: Signature made Sun Nov 24 10:14:42 2019 CET<br>gpg:                using RSA key 90C8019E36C2E964<br><b>gpg: Good signature from "Wladimir J. van der Laan (Bitcoin Core <br>binary release signing key) &lt;laanwj@gmail.com&gt;" [unknown]
</b>gpg: WARNING: This key is not certified with a trusted signature!
gpg:There is no indication that the signature belongs to the owner.
Primary key fingerprint: 01EA 5486 DE18 A882 D4C2  6845 90C8 019E 36C2 E964</pre>
<p>La verifica è andata a buon fine.<br>Per verificare Electrum il procedimento è molto simile.<br>Tutto è spiegato nel link <a href="https://electrum.org/#download" target="_blank" rel="noopener noreferrer" data-href="https://electrum.org/#download">https://electrum.org/#download</a>.<br>Ecco tutti i passaggi.</p>
<pre>$ wget <a href="https://raw.githubusercontent.com/spesmilo/electrum/master/pubkeys/ThomasV.as" target="_blank" rel="noopener noreferrer" data-href="https://raw.githubusercontent.com/spesmilo/electrum/master/pubkeys/ThomasV.as">https://raw.githubusercontent.com/spesmilo/electrum/master/pubkeys/ThomasV.as</a>c<br>$ gpg --import ThomasV.asc<br>$ wget <a href="https://download.electrum.org/3.3.8/electrum-3.3.8.dmg" target="_blank" rel="noopener noreferrer" data-href="https://download.electrum.org/3.3.8/electrum-3.3.8.dmg">https://download.electrum.org/3.3.8/electrum-3.3.8.dmg</a><br>$ wget <a href="https://download.electrum.org/3.3.8/electrum-3.3.8.dmg.asc" target="_blank" rel="noopener noreferrer" data-href="https://download.electrum.org/3.3.8/electrum-3.3.8.dmg.asc">https://download.electrum.org/3.3.8/electrum-3.3.8.dmg.asc</a><br>$ gpg --verify electrum-3.3.8.dmg.asc</pre>
<pre>gpg: assuming signed data in 'electrum-3.3.8.dmg'
gpg: Signature made Thu Jul 11 16:26:15 2019 CEST
gpg:                using RSA key 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6
gpg: <b>Good signature from "Thomas Voegtlin (https://electrum.org) &lt;thomasv@electrum.org&gt;" [unknown]
</b>gpg:                 aka "ThomasV &lt;thomasv1@gmx.de&gt;" [unknown]
gpg:                 aka "Thomas Voegtlin &lt;thomasv1@gmx.de&gt;" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.</pre>
<pre>Primary key fingerprint: 6694 D8DE 7BE8 EE56 31BE  D950 2BD5 824B 7F94 70E6</pre>
<p>Sai chi è figo?<br>Keybase.</p>
<p><a href="https://keybase.io/barno" target="_blank" rel="noopener noreferrer" data-href="https://keybase.io/barno">https://keybase.io/barno</a></p>
<h3><strong>Don’t trust,&nbsp;Verify.</strong></h3>
</section>
<section>
<hr>
<p>► <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a><br> — <br>&nbsp;► <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a><br>&nbsp;► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a></p>
<p>► <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a><br>&nbsp;► <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a><br> — <br>&nbsp;► <a href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13" target="_blank" rel="noopener noreferrer" data-href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13">Video corso disponibile su Udemy</a></p>
<p>I nostri social:<br>&nbsp;► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a>&nbsp;, <a href="https://www.facebook.com/bitcoin.corso.completo/" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/bitcoin.corso.completo/">Facebook</a>, <a href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica">Linkedin</a>, <a href="https://medium.com/@bitcoindallateoriallapratica" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoindallateoriallapratica">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a></p>
<p>Television isn’t a good idea (Radio Stations)<br>&nbsp;Email isn’t a good idea (Post offices)<br>&nbsp;Amazon isn’t a good idea (Retail stores)<br>&nbsp;Bitcoin isn’t a good idea (Central banks)</p>
<p>In <strong>crypto</strong> we trust</p>
</section>