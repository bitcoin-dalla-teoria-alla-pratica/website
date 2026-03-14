---
title: "Come aggiornare il nodo Bitcoin"
date: 2020-01-08T10:06:32+01:00
draft: false


tags:
  - "Nodo & Network"
---




<p>Siamo all’inizio dell’Hanno 2020 (la H sta per Halving 😉) e tra i buoni propositi c’è sempre quello di fare un pò di pulizia, di aggiornare i software e di incrementare le nostre capacità.</p>
<p>Se avete seguito il nostro&nbsp;<a href="https://medium.com/@bitcoindallateoriallapratica/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f" target="_blank" rel="noopener noreferrer">tutorial per avere un nodo Raspberry</a>&nbsp;e non avete ancora aggiornato il vostro nodo, avrete la versione 0.18.0 di Bitcoin Core.</p>
<p>A novembre 2019 è stato rilasciato l’aggiornamento&nbsp;<a href="https://bitcoin.org/en/release/v0.19.0.1" target="_blank" rel="noopener nofollow noreferrer">0.19.0.1</a>, che introduce dei miglioramenti a livello di performance, delle nuove chiamate RPC e rende deprecate delle altre.<br>Tutti i changelogs sono presenti anche sul&nbsp;<a href="https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.19.0.1.md" target="_blank" rel="noopener nofollow noreferrer">repository ufficiale Github</a>.</p>
<p>Ecco come abbiamo aggiornato il nostro Raspberry.</p>
<p>Per prima cosa ci colleghiamo in ssh.</p>
<pre><strong>$ </strong>ssh pi@192.168.1.221</pre>
<p>dove&nbsp;<strong>192.168.1.221</strong>&nbsp;è il vostro IP locale, che potrebbe essere diverso dal nostro.</p>
<p>Ci spostiamo nella cartella download dell’utente pi.</p>
<pre><strong>$ </strong>cd /home/pi/download</pre>
<p>e scarichiamo il nuovo Bitcoin core con il comando&nbsp;<a href="https://it.wikipedia.org/wiki/Wget" target="_blank" rel="noopener nofollow noreferrer">wget</a></p>
<pre><strong>$ </strong>wget <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz" target="_blank" rel="noopener nofollow noreferrer">https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz</a></pre>
<p>Scarichiamo anche le relative firme per verificare l’integrità del pacchetto.</p>
<pre><strong>$ </strong>wget <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc" target="_blank" rel="noopener nofollow noreferrer">https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc</a><br><strong>$ </strong>wget <a href="https://bitcoin.org/laanwj-releases.asc" target="_blank" rel="noopener nofollow noreferrer">https://bitcoin.org/laanwj-releases.asc</a></pre>
<p>Effettuiamo la verifica come mostrato nel&nbsp;<a href="https://medium.com/@bitcoindallateoriallapratica/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f" target="_blank" rel="noopener noreferrer">tutorial iniziale del Raspberry</a>.</p>
<pre><strong>$</strong> sha256sum --check SHA256SUMS.asc --ignore-missing
bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz: OK
sha256sum: WARNING: 20 lines are improperly formatted</pre>
<p>L’importante è che ci sia un bell’<strong>OK</strong>!</p>
<p>Controlliamo anche le chiavi.</p>
<pre><strong>$ </strong>gpg --import ./laanwj-releases.asc<br><strong>$ </strong>gpg --refresh-keys<br><strong>$ </strong>gpg --verify SHA256SUMS.asc</pre>
<p>risultato:</p>
<pre>gpg: Good signature from “Wladimir J. van der Laan …”<br>Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964</pre>
<p>Benissimo, abbiamo scaricato quello che vogliamo.<br>Non ci resta che decomprimere il pacchetto e spostarlo nella cartella bin, cosi da poter interagire globalmente, in quanto&nbsp;<strong>/usr/local/bin</strong>&nbsp;fa parte del&nbsp;<a href="http://www.linfo.org/path_env_var.html" target="_blank" rel="noopener nofollow noreferrer"><strong>$PATH</strong></a></p>
<blockquote>
<p>PATH is an&nbsp;<em>environmental variable</em>&nbsp;in&nbsp;<a href="http://www.linfo.org/linuxdef.html" target="_blank" rel="noopener nofollow noreferrer">Linux</a>&nbsp;and other&nbsp;<a href="http://www.linfo.org/unix-like.html" target="_blank" rel="noopener nofollow noreferrer">Unix-like</a>&nbsp;<a href="http://www.linfo.org/operating_system.html" target="_blank" rel="noopener nofollow noreferrer">operating systems</a>&nbsp;that tells the&nbsp;<a href="http://www.linfo.org/shell.html" target="_blank" rel="noopener nofollow noreferrer"><em>shell</em></a>&nbsp;which&nbsp;<a href="http://www.linfo.org/directory.html" target="_blank" rel="noopener nofollow noreferrer">directories</a>&nbsp;to search for&nbsp;<a href="http://www.linfo.org/executable.html" target="_blank" rel="noopener nofollow noreferrer"><em>executable files</em></a></p>
</blockquote>
<pre><strong>$</strong> echo $PATH/usr/local/sbin:<strong>/usr/local/bin</strong>:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games</pre>
<p>quindi decomprimiamo e spostiamo il tutto.</p>
<pre><strong>$ </strong>tar -xvf bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz<br><strong>$ </strong>sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-0.19.0.1/bin/*</pre>
<p>Per verificare che tutto sia andato a buon fine, possiamo ottenere la versione di bitcoind con il comando</p>
<pre><strong>$ </strong>bitcoind -version</pre>
<pre>Bitcoin Core version v0.19.0.1</pre>
<p>Siamo pronti a verificare le nuove chiamate RPC!<br>Spostiamoci nell’utente bitcoin.</p>
<pre><strong>$ </strong>sudo su bitcoin</pre>
<p>Per prima cosa stoppiamo il demone attualmente in esecuzione.</p>
<pre><strong>$ </strong>bitcoin-cli stop</pre>
<p>Aspettiamo qualche secondo, dato che abbiamo impostato un&nbsp;<a href="https://medium.com/@bitcoindallateoriallapratica/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f" target="_blank" rel="noopener noreferrer">servizio</a>&nbsp;che rimette in esecuzione il demone se questo per qualche motivo dovesse interrompersi.</p>
<p>Proviamo quindi a lanciare un nuovo comando, ad esempio</p>
<pre><strong>$ </strong>bitcoin-cli getbalances</pre>
<p>devo ottenere un risultato.</p>
<p>Ricordiamoci che con il comando</p>
<pre>$ bitcoin-cli help</pre>
<p>Possiamo ottenere tutti i comandi a nostra disposizione.<br>Utilizziamo nuovamente l’utente&nbsp;<strong>pi</strong>, per pulire la cartella download.</p>
<pre>$ exit<br>$ rm -Rf /home/pi/download/*</pre>
<p>Semplice no?</p>		
										<img width="1024" height="768" src="http://www.corsobitcoin.com/wp-content/uploads/2020/01/raspberry-nodo-bitcoin-dalla-teoria-alla-pratica.png" alt="raspberry-nodo-bitcoin-dalla-teoria-alla-pratica" srcset="https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2020/01/raspberry-nodo-bitcoin-dalla-teoria-alla-pratica.png?w=1024 1024w, https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2020/01/raspberry-nodo-bitcoin-dalla-teoria-alla-pratica.png?resize=300%2C225 300w, https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2020/01/raspberry-nodo-bitcoin-dalla-teoria-alla-pratica.png?resize=768%2C576 768w, https://i0.wp.com/www.corsobitcoin.com/wp-content/uploads/2020/01/raspberry-nodo-bitcoin-dalla-teoria-alla-pratica.png?resize=600%2C450 600w" sizes="(max-width: 1024px) 100vw, 1024px" />											
		<p>► <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener nofollow noreferrer">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br />► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener nofollow noreferrer">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a><br />—<br />► <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener nofollow noreferrer">Tascabile Bitcoin 199 domande (Amazon)</a><br />► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener nofollow noreferrer">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a></p>► <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener nofollow noreferrer">Pocket Book Bitcoin 199 questions (Amazon)</a><br />► <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener nofollow noreferrer">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener nofollow noreferrer">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener nofollow noreferrer">Bitcoin 199 questions (official website — accept bitcoin)</a><br />—<br />► <a href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13" target="_blank" rel="noopener nofollow noreferrer">Video corso disponibile su Udemy</a><br />I nostri social:<br />► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener nofollow noreferrer">Twitter</a> , <a href="https://www.facebook.com/bitcoin.corso.completo/" target="_blank" rel="noopener nofollow noreferrer">Facebook</a>, <a href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener nofollow noreferrer">Linkedin</a>, <a href="https://medium.com/@bitcoindallateoriallapratica" target="_blank" rel="noopener noreferrer">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener nofollow noreferrer">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener nofollow noreferrer">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener nofollow noreferrer">GitHub</a>