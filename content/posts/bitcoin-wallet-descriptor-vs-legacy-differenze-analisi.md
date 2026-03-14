---
title: "Bitcoin Wallet Legacy vs. Wallet Descriptor: Un Confronto Approfondito"
date: 2023-12-21T20:59:19+01:00
draft: false


tags:
  - "Crittografia"
  - "Script"
---




<p>In questo articolo, esploreremo le differenze tra i wallet legacy e i wallet descriptor di Bitcoin. Potrebbe essere sfuggito alla tua attenzione, ma a partire da Bitcoin Core 0.17.0 nel 2018, è stata implementata una funzionalità di rilievo destinata a rendere obsoleti i wallet legacy nel prossimo futuro.</p>

<p><strong>Un Aggiornamento Cruciale, Benché Silenzioso</strong></p>

<p>L'introduzione dei wallet descriptor è stata silenziosa per gli utenti, ma la sua importanza si traduce in una maggiore sicurezza e flessibilità. Questo avanzamento nell'ecosistema Bitcoin è stato dettagliatamente esplorato nell'articolo "Output Script Descriptors" di Ava Chown, uno sviluppatore che fornisce una panoramica completa delle migliorie introdotte.</p>

<p><strong>Descrizione dei Wallet: Legacy vs. Descriptor</strong></p>

<p>La distinzione fondamentale tra i Legacy Wallets e i nuovi Descriptor Wallets risiede nell'approccio allo sviluppo. I Descriptor Wallets sono progettati per supportare il linguaggio Bitcoin Script, mentre i Legacy Wallets hanno una concezione basata sul concetto di chiavi.</p>

<p><strong>Cambiamenti nei Comandi RPC</strong></p>

<p>Con l'avvento dei Descriptor Wallets, sono stati apportati significativi cambiamenti ai comandi RPC. Ad esempio, i comandi "dumpprivkey" e "signrawtransactionwithkey" sono stati sostituiti dal più moderno "signrawtransactionwithwallet". Questa modifica è parte integrante dell'approccio più sicuro adottato dai Descriptor Wallets.</p>

<p><strong>Maggiore Sicurezza con Descriptor Wallets</strong></p>

<p>Una caratteristica distintiva dei Descriptor Wallets è l'assenza di esposizione della chiave privata tramite il comando "dumpprivkey". Questa scelta mira a proteggere gli utenti da possibili errori o compromissioni di sicurezza.</p>

<p>Inoltre, i Descriptor Wallets risolvono un problema critico legato alle chiavi non rinforzate. Precedentemente, un attaccante in possesso dell'extended public key (xpub) e di una chiave privata non rinforzata avrebbe potuto dedurre la chiave privata dell'extended public key, ottenendo così ogni chiave derivabile, sia rinforzata che non rinforzata.</p>

<p>Per ulteriori dettagli su questo argomento, si consiglia la lettura del libro "<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/">Bitcoin dalla Teoria alla Pratica</a>".</p>

<figure class="wp-block-image size-large"><img src="https://www.corsobitcoin.com/wp-content/uploads/2019/06/bitcoin-teoria-pratica-front-1024x1024.png" alt="Esplora le differenze cruciali tra i wallet Bitcoin Descriptor e Legacy. Scopri come l'implementazione del Descriptor Wallet sta ridefinendo la sicurezza e la flessibilità, rendendo obsoleti i wallet legacy nel futuro della gestione delle chiavi." class="wp-image-13439"/></figure>

<p><strong>Il Futuro dei Wallet Bitcoin</strong></p>

<p>L'introduzione dei Descriptor Wallets rappresenta un passo cruciale nella creazione di portafogli più sicuri e flessibili. Con i wallet legacy destinati a essere deprecati nelle versioni future, comprendere e adottare le nuove tecnologie diventa fondamentale per mantenere un ambiente di gestione delle chiavi sicuro ed efficiente.</p>

<p><strong>Links Utili:</strong></p>

<ul><li><a>Documentazione Bitcoin Core su Descriptors</a></li>

<li><a>Discussione su Bitcoin Talk: New HD Wallets vs. Legacy</a></li>
</ul>
