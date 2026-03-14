---
title: "Bitcoin Blockchain fork"
date: 2019-03-21T12:39:57+01:00
draft: false


tags:
  - "Nodo & Network"
  - "Mining & Blockchain"
---




<h4>Forse vi potrà sorprendere che la blockchain Bitcoin subisce dei fork molto frequentemente.<br></h4>
<p>Per proseguire dobbiamo chiarire anche la differenza tra Nodo e Miner</p>
<hr/>
<p><strong>I Full node&nbsp;</strong>come sappiano hanno l’intera blockchain scaricata.</p>
<p>Stanno in ascolto su altri nodi e verificano che una transazione sia valida confrontandola proprio con la blockchain che hanno. Per essere più precisi con LevelDb Chainstate</p>
<p>Se tale transazione viene verificata viene passata ad un altro nodo, e aggiorna la propria&nbsp;<strong>mempool</strong>, dove sono “ospitate” tutte le transazioni&nbsp;<strong>unconfirmed</strong>. Una transazione è&nbsp;<strong>unconfirmed&nbsp;</strong>quando non è ancora inclusa nel blocco, di fatto non fa ancora parte della blockchain</p>
<hr/>
<p><strong>I miners</strong>&nbsp;stanno in ascolto sulle nuove transazioni, prendendo le transazioni da includere nel blocco dalla&nbsp;<strong>mempool</strong></p>
<p>Il loro compito è creare blocchi di transazioni valide e risolvere il PoW dietro ricompensa BTC. Una volta risolto mandano il blocco in broadcast, cioè nella rete</p>
<hr/>
<blockquote><p>Per adesso possiamo dire che i Miners a differenza dei fullnode creano&nbsp;blocchi.</p></blockquote>
<p>Come sappiamo la blockchain è un sistema decentralizzato e come dicevamo i nodi hanno al suo interno la replica esatta della blockchain.</p>
<p>Essendo un sistema decentralizzato può essere che il nodo A abbia ricevuto il&nbsp;<strong>tip</strong>, ovvero il blocco più in alto, il più nuovo, mentre il nodo B non abbia ancora ricevuto lo stesso blocco, proprio perchè essendo una rete decentralizzata,&nbsp;<strong>le informazioni si propagano come dei cerchi nell’acqua e quindi non simultaneamente</strong>.</p>
<p>Il miner per creare il blocco deve risolvere il&nbsp;<strong>Proof Of Work.</strong>(PoW)</p>
<figure><img src="https://cdn-images-1.medium.com/max/800/1*WcOEWrYoZFhTQj7nWz3d_g.gif" alt="Bitcoin Blockchain fork"/><figcaption><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Slide del corso “</a><strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Bitcoin dalla teoria alla pratica — corso completo</a></strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">”</a></figcaption></figure>
<p>Bene il miner con i capelli verdi è Alessio, il miner con i capelli neri è Marco.</p>
<p>Immaginiamo che per risolvere il PoW i miners devono risolvere l’addizione 1+1.</p>
<p>Alessio e Marco trovano la soluzione al problema 1+1 contemporaneamente, risolvendo di fatto il PoW in maniera corretta e creando cosi il blocco da mandare in broadcast</p>
<p>Il nodo Paolo riceve il blocco di Alessio e verifica che sia corretto, una volta verificato lo inoltra ai nodi vicini</p>
<p>Il nodo di Michela invece riceve per primo il blocco di Marco e verifica che sia corretto, una volta verificato lo inoltra ai nodi vicini</p>
<p>Se Michela adesso ricevesse il blocco di Alessio&nbsp;<strong>non potrà considerarlo valido&nbsp;</strong>in quanto il padre di Alessio è lo stesso padre di Marco, ovvero il blocco celeste, e invece il nodo Michela sta tentando di aggiungerlo come figlio del blocco di Marco, cioè il blocco rosso.</p>
<figure><img src="https://cdn-images-1.medium.com/max/800/1*29ayutDqaiTWRfJaaO3-IA.jpeg" alt="Bitcoin Blockchain fork"/></figure>
<p>Entrambi i blocchi, verdi e rossi sono validi al momento, entrambi hanno il&nbsp;<strong>previousBlockhash</strong>&nbsp;il valore hash del blocco celeste, quindi hanno lo stesso padre.</p>
<p>E adesso che succede?</p>
<p>I miners stanno continuando a lavorare sul prossimo blocco</p>
<p>Un nuovo blocco è stato trovato, e ha come&nbsp;<strong>previousblockhash</strong>, l’hash del blocco verde, cioè il blocco minato da Alessio</p>
<p>Il blocco quindi viene mandato in broadcast e i nodi vengono aggiornati, tranne quelli con il blocco rosso, proprio perchè il&nbsp;<strong>previousblockhash</strong>&nbsp;del blocco viola (il nuovo blocco scoperto)non “combacia” con l’hash del blocco rosso.</p>
<p>A questo punto i miners vedono che c’è un ramo più lungo rispetto all’altro</p>
<p>Quindi abbandonano il ramo con il blocco rosso e cominciano a minare il ramo con il blocco viola appena aggiunto</p>
<p>Anche i fullnode si mettono dalla parte della blockchain più lunga.</p>
<p>Il blocco rosso, sarà considerato&nbsp;<strong>orfano</strong>&nbsp;e le sue transazioni re-inserite nella&nbsp;<strong>mempool</strong>&nbsp;e ricontrollate.</p>
<p>Da notare che solitamente il fork avviene con un massimo di un blocco, proprio come l’esempio che abbiamo visto.</p>
<p>Quindi possiamo affermare che il ramo più lungo vince, diventando la main chain. Se vogliamo essere ancora più corretti vince il ramo dove è stata accumulata più&nbsp;<strong>Proof of Work</strong><br></p>
<p><br></p>
<p><br></p>
