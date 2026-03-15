---
title: "Bitcoin in Action"
date: 2020-11-17T10:00:00+01:00
slug: "bitcoin-in-action"
draft: false
author: "Alessio Barnini"
description: "Segwit, Bitcoin script & smart contracts"
cover: "/img/posts/bitcoin-in-action-7.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

### Bitcoin in Action

#### *Segwit, Bitcoin script & smart contracts*

Ciao!  
Dopo [Bitcoin dalla teoria alla pratica](https://amzn.to/2MOj1av) e [Bitcoin 199 Domande](https://amzn.to/3ckIkJj), abbiamo completato la nostra terza fatica – [**Bitcoin in Action** * SegWit, Bitcoin script & Smart Contracts*](https://amzn.to/3pJcXj1).

![Bitcoin In Action — SegWit, Bitcoin Script & Smart Contracts](/img/posts/bitcoin-in-action-7.webp)
*Bitcoin In Action — SegWit, Bitcoin Script & Smart Contracts*

Per seguire questo nuovo testo è indispensabile il primo libro, [Bitcoin dalla teoria alla pratica](https://amzn.to/2MOj1av), proprio perchè non saranno spiegati concetti già affrontati precedentemente, come ad esempio il mining, quindi la [proof of work](https://medium.com/@satoshiwantsyou/che-cosa-e-la-proof-of-work-e-il-mining-bitcoin-8401c0d3c149), il problema dei generai bizantini o la blockchain, quindi hard fork e soft fork, ma abbiamo deciso di andare giù nella buca del Bianconiglio 🐰.

L’obiettivo del libro è quello di spiegare, sempre utilizzando la **pratica**, gli aggiornamenti più corposi del protocollo Bitcoin, analizzando prima le problematiche.

Infatti il primo capitolo è dedicato alla [transaction malleability](https://youtu.be/uFnRcQzjr74), la quale viene risolta con l’aggiornamento SegWit.  
  
L’argomento SegWit è affrontato nel dettaglio con più di 100 pagine, su un totale di 440 circa.

Spiegheremo gli address, o per meglio dire gli script, non affrontati nel precedente libro, quali:

- P2MS - Pay to Multisig
- P2SH - Pay to script hash
- P2SH che effettua il Wrap di P2PK
- P2SH che effettua il Wrap di P2PKH
- P2SH Multisig
- P2SH Custom Script

Quando andremo nel dettaglio di SegWit, utilizzeremo script quali:

- P2WPKH
- P2WSH
- P2WSH che effettua il Wrap di P2PKH
- P2WSH Multisg

E anche gli script/address non nativi come:

- P2SH - P2WPKH
- P2SH - P2WSH

Una sezione completamente dedicata ai **timelocks**, dove è necessario prendere confidenza con **Bitcoin Script** e lo **stack**.

Arriveremo infine a creare degli smart contracts in grado di sbloccare dei fondi solo se determinate condizioni sono verificate, utilizzando delle operation code come **OP_IF**, **OP_ELSE** o per meglio dire le operation code del flow control.

Un libro molto corposo che porta due novità fondamentali rispetto al precedente.

La prima sono le **mappe mentali**, strumento che uso quotidianamente e che serviranno a fine capitolo per avere un quadro completo di quanto affrontato.

![Mappe mentali disponibili nel repository GitHub](/img/posts/bitcoin-in-action-2.webp)
*Mappe mentali disponibili nel repository GitHub*

La seconda è la **pratica**.

Come per il libro precedente spieghiamo ogni argomento tramite la pratica utilizzando esclusivamente riga di comando e qualche funzione python. **Non amiamo utilizzare librerie esterne che fanno il lavoro per noi**.

Sappiamo però che scrivere codice per replicare l’esempio può essere complicato, per questo motivo abbiamo deciso di creare un [repository](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book) che ospita tutti gli esempi del libro.

Come fare a replicarli quindi?

Semplice, si clonerà il repository, si seguiranno le istruzioni descritte nel libro, o nel video tutorial che trovate nel nostro [canale YouTube](https://www.youtube.com/BitcoinInAction), e con l’avvio di un semplice file, replicherete tutto l’esempio.

![Come replicare gli esempi del libro con un semplice file sh](/img/posts/bitcoin-in-action-3.webp)
*Come replicare gli esempi del libro con un semplice file sh*

Spenderai dei bitcoin per replicare l’esempio?

Sì, e sarai anche miner! 🚀

Infatti utilizzeremo sempre l’ambiente di **regtest**, in modo tale da poter replicare gli esempi immediatamente!

Il libro è disponibile su [Amazon](https://amzn.to/3pJcXj1) e su [corsobitcoin.com](prodotti/bitcoin-in-action/) con la possibilità di acquistarlo tramite bitcoin. 
  
 Ciao!
