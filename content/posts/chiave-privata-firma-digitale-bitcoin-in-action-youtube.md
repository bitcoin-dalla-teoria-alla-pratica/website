---
title: " Perché è così importante la chiave privata?"
date: 2020-05-17T21:20:09+01:00
draft: false

tags:
  - "Crittografia"
---

<section>
<section>Benvenuto nel canale youtube <a href="https://www.youtube.com/BitcoinInAction?sub_confirmation=1" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/BitcoinInAction?sub_confirmation=1"><strong>Bitcoin in Action</strong></a>, io sono <a href="https://www.linkedin.com/in/alessiobarnini/" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/in/alessiobarnini/">Alessio</a>, ma per tutti Barno.

Insieme ad <a href="https://twitter.com/creepsound" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/creepsound">Alessandro</a> abbiamo pubblicato il <a href="http://bit.ly/38gGmYr" target="_blank" rel="noopener noreferrer" data-href="http://bit.ly/38gGmYr">video corso</a> sulla piattaforma Udemy, il libro <a href="https://amzn.to/2Ldym0F" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2Ldym0F">Bitcoin dalla teoria alla pratica</a> e il tascabile <a href="https://amzn.to/3ckIkJj" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/3ckIkJj">Bitcoin 199 domande</a>.

Questo canale ha come obiettivo rispondere a domande che spesso riceviamo dagli amici, che leggiamo su internet, e perchè no, alle vostre lasciate nei commenti.

Oggi rispondo a <strong>Paolo</strong>, mio carissimo amico, che mi domanda:

La chiave privata è molto importante quando parliamo di Bitcoin e non solo. Ma di che cosa si tratta? Che cosa è una firma digitale?

Partiamo dicendo che Bitcoin utilizza la crittografia <strong>asimmetrica</strong>, dove abbiamo due chiavi, una privata e l’altra pubblica. Sono legate matematicamente grazie a particolari proprietà dei numeri primi.

Dalla chiave privata si può <strong>derivare</strong> la chiave pubblica ma non si può fare il contrario. Si chiama crittografica asimmetrica proprio per la presenza delle due chiave, altrimenti parliamo di crittografia <strong>simmetrica</strong>.

La firma digitale si ottiene applicando una funzione crittografica utilizzando la chiave privata sul hash del messaggio.

La firma si può verificare grazie all’utilizzo della chiave pubblica corrispondente.

La firma risolve tre fondamentali concetti,
<ul>
 	<li>Non ripudio: cioè chi ha firmato non potrà disconoscerlo</li>
 	<li>Integrità: se il messaggio viene manomesso ce ne accorgiamo</li>
 	<li>Autenticità: Il destinatario deve essere sicuro di aver ricevuto il messaggio dal mittente desiderato.</li>
</ul>
In Bitcoin la firma digitale viene utilizzata nella verifica delle transazioni, tramite <strong>OP_CODE</strong> come <strong>OP_CHECKSIG</strong> e derivate.

Passiamo alla pratica utilizzando l’algoritmo delle curve ellittiche utilizzato in bitcoin.

<iframe src="https://www.youtube.com/embed/RU7LHPP4Lvk" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

</section>
<section>
</section>
<section>

<hr>

Abbiamo quindi visto quanto è importante custodire la chiave privata, perchè ci autentica verso qualcuno o verso un’intera rete. La parte pratica che avete visto è possibile scaricarla dal nostro repository <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action">Github</a>, l’indirizzo lo trovate nella descrizione del video.

Non mi resta che salutarvi, di mettermi un like se il video vi è piaciuto e di iscrivervi a canale attivando la campanella per essere avvisati dei prossimi video.

Ciao!

</section>
<section>

<hr>

🎥 <a href="https://www.youtube.com/c/BitcoinInAction" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/c/BitcoinInAction">Canale youtube — Bitcoin in Action</a>

—

📖 <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a>
—
📖 <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a>

📖 <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a>
📖 <a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a>
—
🎥 <a href="http://bit.ly/38gGmYr" target="_blank" rel="noopener noreferrer" data-href="http://bit.ly/38gGmYr">Video corso disponibile su Udemy</a>

► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a>&nbsp;, <a href="https://www.facebook.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/satoshiwantsyou">Facebook</a>, <a href="https://www.linkedin.com/company/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/satoshiwantsyou">Linkedin</a>, <a href="https://medium.com/@satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@satoshiwantsyou/">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a>

</section>
</section>
<section>
</section>