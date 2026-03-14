---
title: "Come si utilizza un nodo Bitcoin?"
date: 2020-05-27T08:59:58+01:00
draft: false


tags:
  - "Nodo & Network"
  - "Crittografia"
---




<section>
<section>
<hr />
Ciao,
Abbiamo ricevuto un pò domande dai lettori del nostro libro —<a href="https://amzn.to/2Ldym0F" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ldym0F"> Bitcoin dalla teoria alla pratica</a> — e dagli studenti del nostro <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">video-corso</a>, dove ci chiedevano come avere a disposizione un nodo Bitcoin. Abbiamo quindi deciso di risponderli tramite il nostro canale.
Durante l’installazione utilizzeremo la verifica delle chiavi GPG così da essere sicuri di aver scaricato il pacchetto voluto. Personalmente utilizzo Mac Os, quindi la cartella destinata alla blockchain è di default è all’interno di Application Support.
Windows e Linux utilizzano un‘altro percorso, consultabile <a href="https://en.bitcoin.it/wiki/Data_directory" target="_blank" rel="noopener noreferrer" data-href="https://en.bitcoin.it/wiki/Data_directory">https://en.bitcoin.it/wiki/Data_directory</a>.
<blockquote>In Action</blockquote>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dyFDDH0IOnU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Per prima cosa dobbiamo scaricare il software Bitcoin core. Personalmente non amo l’interfaccia grafica, quindi scarichiamo direttamente il bin dall’indirizzo <a href="https://bitcoincore.org/bin/" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/bin/">https://bitcoincore.org/bin/</a>.
Copio il link e utilizzo wget per scaricare il pacchetto.
<pre>$ wget <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.1/bitcoin-0.19.1-osx64.tar.gz" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/bin/bitcoin-core-0.19.1/bitcoin-0.19.1-osx64.tar.gz">https://bitcoincore.org/bin/bitcoin-core-0.19.1/bitcoin-0.19.1-osx64.tar.gz</a></pre>
Utilizzo wget perchè il vostro nodo potrebbe essere su un raspberry senza interfaccia grafica.
Scarico anche le relative firme per verificare l’integrità del pacchetto.
<pre>$ wget <a href="https://bitcoincore.org/bin/bitcoin-core-0.19.1/SHA256SUMS.asc" target="_blank" rel="noopener noreferrer" data-href="https://bitcoincore.org/bin/bitcoin-core-0.19.1/SHA256SUMS.asc">https://bitcoincore.org/bin/bitcoin-core-0.19.1/SHA256SUMS.asc</a>
$ wget <a href="https://bitcoin.org/laanwj-releases.asc" target="_blank" rel="noopener noreferrer" data-href="https://bitcoin.org/laanwj-releases.asc">https://bitcoin.org/laanwj-releases.asc</a></pre>
Verifichiamo l’integrità del pacchetto
<pre>$ sha256sum — check SHA256SUMS.asc — ignore-missing</pre>
Con il comando <strong>shasum </strong>verifichiamo l’integrità e l’autenticità del file controllando il suo <strong>checksum</strong> creato con l’algoritmo SHA.
Controlliamo anche le chiavi.
<pre>$ gpg — import ./laanwj-releases.asc
$ gpg — refresh-keys
$ gpg — verify SHA256SUMS.asc</pre>
<pre>gpg: Good signature from “Wladimir J. van der Laan …”</pre>
<pre>Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964</pre>
Il controllo della firma è andato a buon fine e sappiamo di aver scaricato il file voluto.
Per i più curiosi <a href="https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-June/009045.html" target="_blank" rel="noopener noreferrer" data-href="https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-June/009045.html">questo</a> è il messaggio in mailing list “bitcoin dev” dove si comunicava quale sarebbe stata la fingerprint della chiave PGP utilizzata per le successive release dalla versione 0.11.0rc3.
Possiamo finalmente installarlo.
<pre>$ tar -xvf bitcoin-0.19.1-osx64.tar.gz</pre>
Decomprimiamo l’archivio e spostiamo i file bin all’interno di /usr/local/bin cosi da renderlo globale.
<pre>$ mv bitcoin-0.19.1/bin/* /usr/local/bin</pre>
Se utilizzate un raspberry, il comando potrebbe è quello riportato qui sotto
<pre>$ sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-0.19.1/bin/*</pre>
<strong>/usr/local/bin</strong> deve far parte del $PATH. Il Path nei sistemi UNIX comunica in quali cartelle cercare dei file eseguibili
Per verificare che tutto sia andato a buon fine, possiamo eseguire il comando
<pre>$ bitcoind --version</pre>
Se adesso lanciamo il demone, ovvero bitcoind, inizierà la sincronizzazione con la mainnet, e la datadir sarà posizionata all’interno Application support, proprio perchè io sto usando macOS
<pre>$ cd /Users/$USER/Library/Application Support/Bitcoin</pre>
Se il vostro obiettivo è fare delle prove con il protocollo, vi consiglio di utilizzare la regtest.
Per far questo o passate come opzione -regtest al demone, o più comodamente create un file bitcoin.conf all’interno della cartella di default.
<pre>regtest=1
txindex=1</pre>
regtest=1 indica che di default voglio usare la regtest senza doverla specificare.
txindex=1 che voglio che tutte le transazione siano indicizzate.
Per avere una lista completa delle opzioni è possibile utilizzare
<pre>$ bitcoind --help</pre>
possiamo nuovamente accendere il demone.
Verifichiamo l’ambiente con la chiamata
<pre>$ bitcoin-cli getblockchaininfo</pre>
<pre>{</pre>
<pre>“chain”: “regtest”,</pre>
<pre>…
}</pre>
Abbiamo tutto a disposizione per utilizzare il nostro nodo.
Abbiamo visto come ottenere un nodo bitcoin e come interagirci per iniziare a prendere confidenza con il protocollo.
In descrizione trovate il nostro link a <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action">Github</a> e un articolo scritto da noi sul nostro sito per installarlo su un raspberry.
Ciao alla prossima
</section><section>
<hr />
🎥 <a href="https://www.youtube.com/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction">Canale youtube — Bitcoin in Action</a>
—
📖 <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a>
—
📖 <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a>
📖 <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a>
—
🎥 <a href="https://bit.ly/3cUJDyZ" target="_blank" rel="noopener noreferrer" data-href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica</a>
—
I nostri social:
► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a> , <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a href="https://www.linkedin.com/company/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/satoshiwantsyou">Linkedin</a>, <a href="https://medium.com/@satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou/">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a>
Television isn’t a good idea (Radio Stations)
Email isn’t a good idea (Post offices)
Amazon isn’t a good idea (Retail stores)
Bitcoin isn’t a good idea (Central banks)
In <strong>crypto</strong> we trust
</section>
</section><section>
</section><p>🎥 <a href="https://www.youtube.com/BitcoinInAction">Canale youtube — Bitcoin in Action</a></p><p>— </p><p>📖 <a href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br />📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a><br /> — <br />📖 <a href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a><br />📖 <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a></p><p>📖 <a href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a><br />📖 <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a><br /> — <br />🎥 <a href="https://bit.ly/3cUJDyZ">Video Corso Bitcoin dalla teoria alla pratica </a></p><p> — </p><p>I nostri social:<br />► <a href="https://twitter.com/satoshiwantsyou">Twitter</a> , <a href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a href="https://www.linkedin.com/company/satoshiwantsyou">Linkedin</a>, <a href="https://medium.com/@satoshiwantsyou/">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a></p><p>Television isn’t a good idea (Radio Stations)<br /> Email isn’t a good idea (Post offices)<br /> Amazon isn’t a good idea (Retail stores)<br /> Bitcoin isn’t a good idea (Central banks)</p><p>In <b>crypto</b> we trust</p>