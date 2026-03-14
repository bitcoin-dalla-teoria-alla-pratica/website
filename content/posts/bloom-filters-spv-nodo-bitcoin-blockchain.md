---
title: "Che cosa sono i bloom filters?"
date: 2019-03-29T18:00:11+01:00
draft: false


tags:
  - "Crittografia"
  - "UTXO"
---




<p>Personalmente sono rimasto molto affascinato da questa&nbsp;<strong>struttura dati probabilistica</strong>&nbsp;creata da&nbsp;<a href="https://en.wikipedia.org/wiki/Bloom_filter" rel="noreferrer noopener" target="_blank">Burton Howard Bloom</a>&nbsp;nel 1970.</p>
<p>Tale struttura viene utilizzata per verificare se un elemento appartiene ad un insieme.</p>
<p>I bloom filters si potrebbero riassumere così:</p>
<blockquote style="text-align:center"><p>Forse si, sicuramente no.</p></blockquote>
<p>Vediamo perchè.</p>
<p>I risultati che può restituire sono i&nbsp;<strong>falsi positivi</strong>, quindi i forse si, è possibile che l’elemento che stai cercando sia dentro l’insieme, ma&nbsp;<strong>non i falsi negativi,</strong>quindi i sicuramente no, sicuramente quello che stai cercando&nbsp;<strong>non è</strong>&nbsp;dentro l’insieme.</p>
<p>Questa struttura dati permette una ricerca molto rapida e salvaguarda la memoria</p>
<p>Perché Bitcoin usa bloom filters oltre ai motivi di velocità e memoria?</p>
<p>Per la<strong>&nbsp;Privacy.</strong></p>
<p>Infatti i bloom filters sono usati per filtrare le transazioni ed i blocchi che un nodo&nbsp;<strong>SPV&nbsp;</strong>(<em>simplified payment verification</em>) riceve dai suoi peers, selezionando solo gli elementi di interesse, senza però&nbsp;<strong>rivelare</strong>&nbsp;a quale sia realmente interessato.</p>
<p>Come fa a fare questo?</p>
<p>Invia una lista di indirizzi, di hash delle transazioni di qualsiasi UTXO controllati dal suo wallet.</p>
<p>Il full node manderà&nbsp;<strong>solo</strong>&nbsp;i risultati che matchano con il bloom filters.</p>
<p>Il nodo SPV, quindi,&nbsp;<strong>non richiede esattamente l’informazione voluta</strong>, ma la&nbsp;<em>maschera</em>&nbsp;nei bloom filters, in modo tale da non rivelare esattamente cosa sta cercando, proprio per motivi di privacy.</p>
<p>Il full node manda “I forse sì, quello che cerchi potrebbe essere dentro questo insieme”,e non manda i “sicuramente no”.</p>
<p>Quindi abbiamo già dei risultati più leggeri.</p>
<p>E’ proprio dentro questa risposta che i full node mandano ai nodi SPV il&nbsp;<strong>merkleblock message</strong>&nbsp;che contiene il&nbsp;<strong>merkle path</strong>&nbsp;di ogni transazione richiesta, oltre al classico block header.</p>
<p>Ultimo passaggio, il nodo SPV scarta i falsi positivi, quindi i “forse si”, e aggiorna il wallet balance di riferimento.</p>
<p>Con un esempio pratico sarà più chiaro capire come funzionano i bloom filters.</p>
<p>Cercando di semplificare possiamo dire che il bloom filters si presenta così, ovvero con un array di zeri</p>
<figure><img src="https://cdn-images-1.medium.com/max/800/0*9B009Yc2BZJGb3h8" alt="Che cosa sono i bloom filters?"/><figcaption><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Slide del corso “</a><strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Bitcoin dalla teoria alla pratica — corso completo</a></strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">”</a></figcaption></figure>
<p>L’obiettivo è quello di verificare se alcune parole fanno parte dell’insieme.<br>Per funzionare ha bisogno di almeno due funzioni di hash.</p>
<p>Il loro risultato deve essere compreso tra 1 e N, dove N è la lunghezza dell’array, in questo caso 8.</p>
<p>Aggiungiamo il primo pattern, cioè la prima parola.<br>Ad esempio inseriamo la parola&nbsp;<strong>bitcoin</strong>.</p>
<p>bitcoin è quindi l’input dalle funzioni hash che restituiscono 3 e 5 come output</p>
<p>Le posizioni (in realtà i bit dell’array) vengono mappati a questo risultato e convertiti da 0 a 1.</p>
<p>Quindi nella posizione 3 abbiamo 1 nella posizione 5 abbiamo 1.<br>Stesso procedimento per un altra parola, ad esempio blockchain.</p>
<p>Le funzioni hash restituiscono come risultato, ad esempio, 2 e 8, e le posizioni corrispondenti dell’array da 0 diventano 1.</p>
<p>Definito l’insieme, che in questo caso è formato da&nbsp;<strong>bitcoin</strong>&nbsp;e&nbsp;<strong>blockchain</strong>, vediamo come la struttura dati probabilistica<strong>&nbsp;bloom filters</strong>, lavora per comunicarci i “<strong>forse si</strong>” o “<strong>sicuramente no</strong>”.</p>
<p>Arriva la prima parola da verificare, ad esempio,&nbsp;<strong>Banca</strong>.<br>Le funzioni di hash restituiscono come risultato, 1 e 2.<br>Nella posizione 1 dell’array abbiamo il valore 0 e nella posizione 2 abbiamo un valore 1</p>
<p>Dato che c’è uno 0 e un 1, questo va nei&nbsp;<strong>sicuramente no</strong>.<br>Per essere ammesso nei forse sì, entrambi questi valori devono essere 1.</p>
<p>Arriva la parola Satoshi.<br>Le funzioni di hash restituiscono come risultato, 8 e 5.</p>
<p>Nell’array le posizioni 8 e 5 hanno il valore 1, quindi va nei forse si.<br>E così via.</p>
<p>Lo scenario ottenuto è quello riportato qui sotto.</p>
<figure><img src="https://cdn-images-1.medium.com/max/800/1*_DAG5yPd8pwQzL0ijmnaXg.gif" alt="Che cosa sono i bloom filters?"/><figcaption><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label="Slide del corso “Bitcoin dalla teoria alla pratica — corso completo” (si apre in una nuova scheda)">Slide del corso “</a><strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label="Slide del corso “Bitcoin dalla teoria alla pratica — corso completo” (si apre in una nuova scheda)">Bitcoin dalla teoria alla pratica — corso completo</a></strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label="Slide del corso “Bitcoin dalla teoria alla pratica — corso completo” (si apre in una nuova scheda)">”</a></figcaption></figure>
<p>Ricorda che non c’è sicuramente si ma solo sicuramente no.</p>
