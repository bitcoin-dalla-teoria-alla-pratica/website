---
title: "Validazione di una transazione P2SH-P2PK: il processo di verifica."
date: 2023-12-06T17:58:23+01:00
draft: false

tags:
  - "Script"
  - "Crittografia"
---

<p>Salve, nell'articolo precedente abbiamo esaminato il processo di transazione utilizzando il P2SH-P2PK. In questo nuovo articolo, ci concentreremo sulla procedura di validazione. Come nelle discussioni precedenti, esploreremo lo stack utilizzando la libreria btcdeb e faremo riferimento al codice del libro "Bitcoin In Action - SegWit, Bitcoin Script e Smart Contracts", disponibile sul nostro GitHub. La logica adottata in questo libro prevede di passare uno specifico parametro di debug allo script (DEBUG=1) per invocare la libreria btcdeb. Ora, procediamo con l'analisi pratica.</p>

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<a href="https://www.youtube.com/watch?v=RBPLKq0sZTg&amp;list=PLpPLK7SGHncZVl_ZQkqyXGMDGWEx7U_et&amp;index=16" target="_blank">https://www.youtube.com/watch?v=RBPLKq0sZTg&amp;list=PLpPLK7SGHncZVl_ZQkqyXGMDGWEx7U_et&amp;index=16</a>
</div></figure>

<p>Come nei casi precedenti, inizieremo con una blockchain a zero blocchi. Mineremo successivamente 101 blocchi per ottenere la ricompensa, trasferendola successivamente a un nuovo indirizzo. Se desideri seguire passo dopo passo questi procedimenti, ti consiglio di leggere l'articolo precedente.</p>

<p>Il nostro compito è avviare il file sh con il comando:</p>

```bash
$ ./main.sh debug=1
```

<p>Il codice è disponibile nel nostro repository e nel libro "Bitcoin In Action - SegWit, Bitcoin Script e Smart Contracts".</p>

<p>Lo script si interromperà prima dell'invio della transazione in broadcast, consentendoci di verificare la sua validità. Analogamente ai casi P2PK e P2PKH, lo stack inizia vuoto, con i primi elementi inseriti nello scriptSig.</p>

<figure class="wp-block-image"><img src="https://www.corsobitcoin.com/wp-content/uploads/2023/12/image.jpeg" alt="Validazione di una transazione P2SH-P2PK: il processo di verifica." class="wp-image-13747"/></figure>

<p>Cosa troveremo nello scriptSig? Come discusso nell'articolo precedente, troveremo la firma digitale e il redeem script in chiaro. La composizione degli elementi nello scriptSig varierà a seconda dello script utilizzato.</p>

<figure class="wp-block-image"><img src="https://www.corsobitcoin.com/wp-content/uploads/2023/12/image-1.png" alt="Validazione di una transazione P2SH-P2PK: il processo di verifica." class="wp-image-13746"/></figure>

<p>Nella foto allegata, vediamo la firma digitale e il redeem script inseriti nello stack. Successivamente, procediamo inserendo gli elementi dello scriptPubKey, utilizzando l'operazione OP_HASH160 che applica SHA256 e RIPEMD160. Il risultato viene inserito nello stack.</p>

<p>Come viene ottenuto il redeem script Hash? Applicando SHA256 e RIPEMD160, la stessa operazione utilizzata per l'HASH160. Il redeem script hash viene poi pushato nello scriptPubKey.</p>

<figure class="wp-block-image"><img src="https://www.corsobitcoin.com/wp-content/uploads/2023/12/image-2.png" alt="Validazione di una transazione P2SH-P2PK: il processo di verifica." class="wp-image-13748"/></figure>

<p>L'operazione successiva, OP_EQUAL, verifica se i primi due elementi nello stack sono uguali. In caso affermativo, inserisce 1; in caso contrario, invalida la transazione. Questo controllo è necessario per garantire la retrocompatibilità del P2SH con i miner non aggiornati.</p>

<figure class="wp-block-image"><img src="https://www.corsobitcoin.com/wp-content/uploads/2023/12/image-4.png" alt="Validazione di una transazione P2SH-P2PK: il processo di verifica." class="wp-image-13750"/></figure>

<p>Se tutto procede correttamente, vedremo uno 01, risultato di OP_EQUAL, che viene rimosso dallo stack (pop) per eseguire il redeem script e il successivo controllo OP_CHECKSIG, simile a un normale P2PK come discusso in precedenza.</p>

<figure class="wp-block-image"><img src="https://www.corsobitcoin.com/wp-content/uploads/2023/12/image-3.png" alt="Validazione di una transazione P2SH-P2PK: il processo di verifica." class="wp-image-13749"/></figure>

<p>Il processo potrebbe sembrare intricato, ma con la conoscenza degli script come P2PK e P2PKH, diventa più lineare.</p>

<p>Ciao!</p>

<p id="1ecf">🐳&nbsp;<a href="https://app.gitbook.com/@corsobitcoin/s/bitcoin-in-action-playground" rel="noreferrer noopener" target="_blank">Playground Bitcoin in Action</a></p>

<p id="3d46">🎥&nbsp;<a href="https://www.youtube.com/BitcoinInAction" rel="noreferrer noopener" target="_blank">Bitcoin in Action (YouTube)</a></p>

<p id="3832">🐙 GitHub:<a href="https://bit.ly/2Lj3yeY" rel="noreferrer noopener" target="_blank">&nbsp;https://bit.ly/2Lj3yeY</a></p>

<p id="478b">📕&nbsp;<a href="https://amzn.to/3pJcXj1" rel="noreferrer noopener" target="_blank">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (Amazon)</a></p>

<p id="31ee">📕&nbsp;<a href="https://bit.ly/38RtF9x" rel="noreferrer noopener" target="_blank">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts (pagamento in bitcoin)</a></p>

<p id="8f81">📒&nbsp;<a href="https://amzn.to/2MOj1av" rel="noreferrer noopener" target="_blank">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>📒&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/" rel="noreferrer noopener" target="_blank">Libro Bitcoin dalla teoria alla pratica (pagamento in bitcoin)</a><br>📒&nbsp;<a href="https://amzn.to/2Ym4gz6" rel="noreferrer noopener" target="_blank">Book Bitcoin from theory to practice (Amazon)</a></p>

<p id="da90">📒&nbsp;<a href="https://bit.ly/3ijAyC4" rel="noreferrer noopener" target="_blank">Book Bitcoin from theory to practice (accept bitcoin)</a><br>—<br>🎥&nbsp;<a href="https://bit.ly/3cUJDyZ" rel="noreferrer noopener" target="_blank">Video Corso Bitcoin dalla teoria alla pratica</a></p>

<p id="e408">—<br>📙&nbsp;<a href="https://amzn.to/3ckIkJj" rel="noreferrer noopener" target="_blank">Tascabile Bitcoin 199 domande (Amazon)</a><br>📙&nbsp;<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-199-domande" rel="noreferrer noopener" target="_blank">Tascabile Bitcoin 199 domande (pagamento in bitcoin)</a></p>

<p id="e740">📙&nbsp;<a href="https://amzn.to/3fB4Kbs" rel="noreferrer noopener" target="_blank">Pocket Book Bitcoin 199 questions (Amazon)</a><br>📙&nbsp;<a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" rel="noreferrer noopener" target="_blank">Pocket&nbsp;</a><a href="https://www.amazon.it/dp/1078155585" rel="noreferrer noopener" target="_blank">Book&nbsp;</a><a href="https://www.corsobitcoin.com/prodotti/book-bitcoin-199-questions/" rel="noreferrer noopener" target="_blank">Bitcoin 199 questions (accept bitcoin)</a><br>—<br>► ITA:&nbsp;<a href="https://twitter.com/satoshiwantsyou" rel="noreferrer noopener" target="_blank">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/satoshiwantsyou" rel="noreferrer noopener" target="_blank">Facebook</a>,&nbsp;<a href="https://bitcoin-in-action.medium.com/">Medium</a>,&nbsp;<a href="https://www.instagram.com/satoshiwantsyou/" rel="noreferrer noopener" target="_blank">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" rel="noreferrer noopener" target="_blank">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica" rel="noreferrer noopener" target="_blank">GitHub</a></p>

<p id="dc1e">► ENG:&nbsp;<a href="https://twitter.com/btc_in_action" rel="noreferrer noopener" target="_blank">Twitter</a>&nbsp;,&nbsp;<a href="https://www.facebook.com/bitcoininaction/" rel="noreferrer noopener" target="_blank">Facebook</a>,&nbsp;<a href="https://medium.com/@bitcoin_in_action">Medium</a>,&nbsp;<a href="https://www.instagram.com/bitcoin_in_action/" rel="noreferrer noopener" target="_blank">Instagram</a>,&nbsp;<a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" rel="noreferrer noopener" target="_blank">Youtube</a>,&nbsp;<a href="https://github.com/bitcoin-dalla-teoria-alla-pratica" rel="noreferrer noopener" target="_blank">GitHub</a></p>

<p id="34d8">In&nbsp;<strong>crypto</strong>&nbsp;we trust</p>
