---
title: "Che cosa è la Proof of Work?"
date: 2019-03-18T19:59:15+01:00
draft: false


tags:
  - "Mining & Blockchain"
  - "Crittografia"
---




<h4>Una delle parti fondamentali di Bitcoin è la Proof of Work (PoW).</h4>
<p>In che cosa consiste la PoW&nbsp;?</p>
<p>La proof of work è il processo con il quale il miner inserisce le transazioni all’interno del blocco e riesce ad ottenere un&nbsp;<strong>block header hash</strong>&nbsp;minore della difficoltà (<strong>target</strong>) imposta in quel momento storico dalla rete, aggiudicandosi così un posto nella blockchain.</p>
<figure><img src="https://cdn-images-1.medium.com/max/1600/1*88X3oKZEuIyWa39RMD2Sxw.gif" alt="Che cosa è la Proof of Work?"/><figcaption><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Slide del corso “</a><strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Bitcoin dalla teoria alla pratica — corso completo</a></strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">”</a></figcaption></figure>
<p>La difficoltà viene “<em>tarata</em>” ogni 2016 blocchi, in modo tale che un blocco sia minato in media ogni 10 minuti.</p>
<p>Perchè ogni 10 minuti?</p>
<p><strong>Per evitare fork</strong>&nbsp;troppo frequenti. E per fork non si intende hard fork o soft fork, ma si intende quando due miners forniscono contemporaneamente una PoW valida.</p>
<p>I due blocchi hanno di fatto lo stesso padre, o meglio lo stesso&nbsp;<strong>previous block hash</strong></p>
<p><strong>E per la sicurezza.</strong></p>
<p>Se fosse facile fare i blocchi, ci sarebbe meno sicurezza in quanto dei miners con tanta potenza di calcolo, potrebbero creare dei blocchi in autonomia, fino ad arrivare a fare il famoso attacco del 51%</p>
<p>Che cosa fa esattamente il miner per vincere il PoW ed aggiudicarsi il reward?</p>
<p>Ogni miner crea un&nbsp;<strong>candidate block</strong>&nbsp;con le transazioni prese della&nbsp;<strong>mempool</strong>, e cerca di ottenere un&nbsp;<strong>block header hash</strong>&nbsp;minore del&nbsp;<strong>target</strong>&nbsp;imposto in quel momento storico dalla rete.</p>
<p>Se il miner non riesce ad ottenere l’hash piu basso del target, deve provare nuovamente. Il miner però deve cambiare qualche parametro d’ingresso per ottenere un&nbsp;<strong>digest</strong>&nbsp;differente.</p>
<blockquote style="text-align:center"><p>Digest è il risultato ottenuto da una funzione crittografica<br></p></blockquote>
<p>Diventa di fondamentale importanza il&nbsp;<strong>nonce</strong>, valore all’interno di ogni blocco, in particolar modo nell’<strong>header block</strong>.</p>
<p>Perchè è cosi importante? Perchè se il miner usasse sempre lo stesso input otterrebbe sempre lo stesso output, o meglio, lo stesso digest.</p>
<p>Quindi cambia il valore del nonce per fare una nuova prova e cercare di vincere la&nbsp;<strong>PoW.</strong></p>
<p>Se due input diversi dessero lo stesso output, saremmo davanti ad un problema chiamato&nbsp;<strong>collisione</strong></p>
<blockquote style="text-align:center"><p>In crittografia, una collisione hash è una situazione che avviene quando due diversi input producono lo stesso output tramite una funzione&nbsp;hash.</p></blockquote>
<p>Quali sono i valori che il miner utilizza per fare il&nbsp;<strong>PoW</strong>&nbsp;?</p>
<p>Il miner fa il doppio&nbsp;<strong>SHA256</strong>&nbsp;di tutti gli elementi del block header.</p>
<p>Per essere più precisi:</p>
<ul><li>versionHex</li><li>previousblockhash</li><li>merkleroot</li><li>time</li><li>bits</li><li>nonce</li></ul>
<p>Il risultato che deve ottenere è un hash minore del target (il bits è il target nella sua forma compatta).<br>Se riesce a vince il&nbsp;<strong>PoW</strong>, dopo moltissimi tentativi, il blocco diventa parte della blockchain, e il suo hash è esattamente l’hash che ha fatto vincere il miner.</p>
<p>Prima di essere “ammesso” alla blockchain, il blocco viene verificato ancora, controllando i parametri necessari per essere conforme al protocollo, inclusa la coinbase, transazione che il miner crea per aggiudicarsi il reward.</p>
<p>Per concludere possiamo dire che, per trovare la soluzione al&nbsp;<strong>PoW,</strong>&nbsp;il miner impiega molto tempo, mentre per verificare che l’hash trovato sia sotto la difficoltà imposta ci vuole pochissimo tempo, proprio perchè non abbiamo il problema della collisione.</p>
<p><br></p>
