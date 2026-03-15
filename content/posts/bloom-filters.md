---
title: "Bloom Filters"
date: 2019-03-29T10:00:00+01:00
slug: "bloom-filters"
draft: false
author: "Alessio Barnini"
description: "Personalmente sono rimasto molto affascinato da questa struttura dati probabilistica creata da Burton Howard Bloom nel 1970."
cover: "https://cdn-images-1.medium.com/max/1200/0*9B009Yc2BZJGb3h8"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Hash"
categories:
  - "Bitcoin"
---

---

### Che cosa sono i bloom filters ?

Personalmente sono rimasto molto affascinato da questa **struttura dati probabilistica** creata da [Burton Howard Bloom](https://en.wikipedia.org/wiki/Bloom_filter) nel 1970.

Tale struttura viene utilizzata per verificare se un elemento appartiene ad un insieme.

I bloom filters si potrebbero riassumere così:

> Forse si, sicuramente no.

Vediamo perchè.

I risultati che può restituire sono i **falsi positivi**, quindi i forse si, è possibile che l’elemento che stai cercando sia dentro l’insieme, ma **non i falsi negativi,**quindi i sicuramente no, sicuramente quello che stai cercando **non è** dentro l’insieme.

Questa struttura dati permette una ricerca molto rapida e salvaguarda la memoria

Perché Bitcoin usa bloom filters oltre ai motivi di velocità e memoria?

Per la **Privacy.**

Infatti i bloom filters sono usati per filtrare le transazioni ed i blocchi che un nodo **SPV**(*simplified payment verification*) riceve dai suoi peers, selezionando solo gli elementi di interesse, senza però **rivelare** a quale sia realmente interessato.

Come fa a fare questo?

Invia una lista di indirizzi, di hash delle transazioni di qualsiasi UTXO controllati dal suo wallet.

Il full node manderà **solo** i risultati che matchano con il bloom filters.

Il nodo SPV, quindi, **non richiede esattamente l’informazione voluta**, ma la *maschera* nei bloom filters, in modo tale da non rivelare esattamente cosa sta cercando, proprio per motivi di privacy.

Il full node manda “I forse sì, quello che cerchi potrebbe essere dentro questo insieme”,e non manda i “sicuramente no”.

Quindi abbiamo già dei risultati più leggeri.

E’ proprio dentro questa risposta che i full node mandano ai nodi SPV il **merkleblock message** che contiene il **merkle path** di ogni transazione richiesta, oltre al classico block header.

Ultimo passaggio, il nodo SPV scarta i falsi positivi, quindi i “forse si”, e aggiorna il wallet balance di riferimento.

Con un esempio pratico sarà più chiaro capire come funzionano i bloom filters.

Cercando di semplificare possiamo dire che il bloom filters si presenta così, ovvero con un array di zeri

![Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”](https://cdn-images-1.medium.com/max/1200/0*9B009Yc2BZJGb3h8)
*Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”*

L’obiettivo è quello di verificare se alcune parole fanno parte dell’insieme. 
Per funzionare ha bisogno di almeno due funzioni di hash.

Il loro risultato deve essere compreso tra 1 e N, dove N è la lunghezza dell’array, in questo caso 8.

Aggiungiamo il primo pattern, cioè la prima parola. 
Ad esempio inseriamo la parola **bitcoin**.

bitcoin è quindi l’input dalle funzioni hash che restituiscono 3 e 5 come output

Le posizioni (in realtà i bit dell’array) vengono mappati a questo risultato e convertiti da 0 a 1.

Quindi nella posizione 3 abbiamo 1 nella posizione 5 abbiamo 1. 
Stesso procedimento per un altra parola, ad esempio blockchain.

Le funzioni hash restituiscono come risultato, ad esempio, 2 e 8, e le posizioni corrispondenti dell’array da 0 diventano 1.

Definito l’insieme, che in questo caso è formato da **bitcoin** e **blockchain**, vediamo come la struttura dati probabilistica **bloom filters**, lavora per comunicarci i “**forse si**” o “**sicuramente no**”.

Arriva la prima parola da verificare, ad esempio, **Banca**. 
Le funzioni di hash restituiscono come risultato, 1 e 2. 
Nella posizione 1 dell’array abbiamo il valore 0 e nella posizione 2 abbiamo un valore 1

Dato che c’è uno 0 e un 1, questo va nei **sicuramente no**. 
Per essere ammesso nei forse sì, entrambi questi valori devono essere 1.

Arriva la parola Satoshi. 
Le funzioni di hash restituiscono come risultato, 8 e 5.

Nell’array le posizioni 8 e 5 hanno il valore 1, quindi va nei forse si. 
E così via.

Lo scenario ottenuto è quello riportato qui sotto.

![Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”](https://cdn-images-1.medium.com/max/1200/1*_DAG5yPd8pwQzL0ijmnaXg.gif)
*Slide del corso “Bitcoin dalla teoria alla pratica — corso completo”*

Ricorda che, non c’è sicuramente si, ma *solo*, sicuramente no.