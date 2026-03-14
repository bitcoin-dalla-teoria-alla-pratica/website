---
title: "Replica gli esempi del Libro Bitcoin in Action con Docker!"
date: 2023-12-04T19:12:27+01:00
draft: false


tags:
  - "Nodo & Network"
  - "Script"
---




<p>Salve a tutti,</p>

<p>abbiamo deciso di istituire un repository dedicato per semplificare l'utilizzo degli esempi presenti nei nostri due libri, "Bitcoin dalla Teoria alla Pratica" e "Bitcoin in Action". A tale scopo, faremo uso di Docker!</p>

<p>Ma cosa è Docker?</p>

<p>Docker è una piattaforma open source che facilita la creazione, distribuzione e gestione di applicazioni all'interno di container. I container Docker sono ambienti virtuali isolati che contengono tutto ciò che serve per eseguire un'applicazione, compreso il codice, le librerie e le dipendenze.</p>

<p>Abbiamo sviluppato un'immagine Docker che racchiude tutti gli elementi necessari, dalla versione attuale del nodo (24.0) alla verifica dell'integrità del pacchetto, fino al nostro fidato debugger btcdeb!</p>

<p>Potete trovare l'immagine creata e le istruzioni dettagliate su come interagire con gli esempi del libro all'indirizzo specificato.</p>

<p>E ora, all'azione!</p>

<p>Il primo passo è installare Docker sul vostro computer.</p>

<p>Successivamente, clonate i repository necessari.</p>

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://youtu.be/jvIynVRo8_8?si=_Kbb9QHQdF34yWck
</div></figure>

<hr class="wp-block-separator has-alpha-channel-opacity"/>

<p>In Action!</p>

<p>Per prima cosa, è necessario installare Docker sul proprio computer.</p>

<p>Successivamente, cloniamo i repository necessari.</p>

<pre class="wp-block-code"><code>git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/Docker-bitcoin.git --depth 1<br>cd Docker-bitcoin</code></pre>

<p>Quindi procediamo con il clonare gli esempi dei libri.</p>

<pre class="wp-block-code"><code>git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi.git --depth 1 &amp;&amp;<br>git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book.git --depth 1</code></pre>

<p>A questo punto, non ci resta che avviare Docker con:</p>

<pre class="wp-block-code"><code>docker-compose up</code></pre>

<p>Il comando <code>docker-compose up</code> viene utilizzato per avviare i container specificati nel file di configurazione <code>docker-compose.yml</code>.</p>

<p>Una volta avviato il container, controlliamo tutti i log per assicurarci che il nodo stia utilizzando la rete <code>regtest</code>. Come? Se vediamo che sta scaricando blocchi dalla rete, significa che qualcosa è andato storto!</p>

<p>Apriamo quindi un altro terminale e digitiamo:</p>

<pre class="wp-block-code"><code>docker ps</code></pre>

<p>Questo comando restituirà tutti i container in esecuzione, il che è di vitale importanza perché dobbiamo "entrare" all'interno del container ed eseguire gli esempi del libro.</p>

<p>Ecco il risultato ottenuto utilizzando <code>docker ps</code>:</p>

<pre class="wp-block-code"><code>CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
f693d16b1961 docker-bitcoin-bitcoin-in-action "/entrypoint.sh" 2 hours ago Up 2 hours 0.0.0.0:18443-18444->18443-18444/tcp docker-bitcoin-bitcoin-in-action-1</code></pre>

<p>Entriamo quindi dentro il container:</p>

<pre class="wp-block-code"><code>docker exec -it docker-bitcoin-bitcoin-in-action-1 zsh</code></pre>

<p>Immaginiamo di voler eseguire l'esempio del Capitolo 3.</p>

<pre class="wp-block-code"><code>cd Bitcoin-in-action-book
cd "Capitolo 3"
cd "P2SH - P2PK"
./main.sh</code></pre>

<p>Se vogliamo eseguire l'esempio utilizzando il debug, sarà sufficiente passare il parametro <code>DEBUG</code></p>

<pre class="wp-block-code"><code>./main.sh DEBUG</code></pre>

<p>E btcdeb sarà attivato!</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2021/01/libri2-1024x698.jpg" alt="Bitcoin dalla teoria alla pratica – Bitcoin in Action" class="wp-image-13512"/></figure>
