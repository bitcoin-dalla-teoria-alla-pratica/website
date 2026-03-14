---
title: "Come è costruita una transazione Multisignature P2SH?"
date: 2023-12-05T17:44:41+01:00
draft: false


tags:
  - "Script"
  - "Crittografia"
---




<p>Ciao,</p>

<p>Nel nostro precedente articolo, abbiamo esaminato il processo di creazione del redeem script di un indirizzo P2SH 2-3. In questa lettura, approfondiremo come lo stack viene risolto per garantire la validità della transazione.</p>

<p>Come già discusso in precedenza, nello scriptPubKey (la UTXO), troviamo l'hash del redeem script insieme alle operazioni <strong>OP_HASH160</strong> e <strong>OP_EQUAL</strong>. Questo processo è progettato per ottimizzare le operazioni computazionali, evitando la verifica dell'hash del redeem script quando non è strettamente necessario.</p>

<p>La struttura dello scriptPubKey sarà quindi: </p>

<pre class="wp-block-code"><code>OP_HASH160 redeem script hash OP_EQUAL.</code></pre>

<p>Per quanto riguarda la parte relativa all'input, ossia lo scriptSig, conterrà le condizioni necessarie per rendere la transazione valida. Nel nostro caso, uno script 2-3 richiede almeno due firme. Il redeem script sarà formato da </p>

<pre class="wp-block-code"><code>2 PB PB PB 3 OP_CHECKMULTISIG.</code></pre>

<p>Lo scriptSig sarà strutturato come segue: Signature Signature 2 PB PB PB 3 OP_CHECKMULTISIG, con PB che identifica le chiavi pubbliche coinvolte.</p>

<p>Per affrontare un bug associato all'operation code OP_CHECKMULTISIG, aggiungeremo un elemento innocuo da estrarre dallo stack: OP_0. Lo scriptSig finale avrà quindi la forma: </p>

<pre class="wp-block-code"><code>OP_0 Signature Signature 2 PB PB PB 3 OP_CHECKMULTISIG.</code></pre>

<figure class="wp-block-image size-full"><img src="https://www.corsobitcoin.com/wp-content/uploads/2023/12/image.png" alt="P2SH " class="wp-image-13741"/></figure>

<p>Per ulteriori dettagli sul bug e sulle dinamiche coinvolte, puoi fare riferimento alla <a href="http://documentazione script">documentazione</a> script di Bitcoin.</p>

<p><em>Compares the first signature against each public key until it finds an ECDSA match. Starting with the subsequent public key, it compares the second signature against each remaining public key until it finds an ECDSA match. The process is repeated until all signatures have been checked or not enough public keys remain to produce a successful result. All signatures need to match a public key. Because public keys are not checked again if they fail any signature comparison, signatures must be placed in the scriptSig using the same order as their corresponding public keys were placed in the scriptPubKey or redeemScript. If all signatures are valid, 1 is returned, 0 otherwise. Due to a bug, one extra unused value is removed from the stack.</em></p>

<p>Nei prossimi articoli esploreremo il processo di validazione di una transazione multisignature. Resta sintonizzato!</p>

<p>Ciao!</p>
