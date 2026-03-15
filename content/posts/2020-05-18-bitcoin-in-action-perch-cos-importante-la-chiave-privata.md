---
title: "Bitcoin in action — Perché è così importante la chiave privata?"
date: 2020-05-18T10:00:00+01:00
slug: "bitcoin-in-action-perch-cos-importante-la-chiave-privata"
draft: false
author: "Alessio Barnini"
description: "Canale youtube Bitcoin in Action"
cover: "https://cdn-images-1.medium.com/max/1200/1*KZ5XKmo-TENn7qA5STH8HA.png"
tags:
  - "Bitcoin"
  - "Chiave Privata"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### Bitcoin in action — Perché è così importante la chiave privata?

#### [Scoprilo su Youtube — Bitcoin in Action](https://www.youtube.com/BitcoinInAction)

![Perché è così importante la chiave privata?](https://cdn-images-1.medium.com/max/1200/1*KZ5XKmo-TENn7qA5STH8HA.png)
*Perché è così importante la chiave privata?*

Benvenuto nel canale youtube [**Bitcoin in Action**](https://www.youtube.com/BitcoinInAction?sub_confirmation=1), io sono [Alessio](https://www.linkedin.com/in/alessiobarnini/), ma per tutti Barno.

Insieme ad [Alessandro](https://twitter.com/creepsound) abbiamo pubblicato il [video corso](http://bit.ly/38gGmYr) sulla piattaforma Udemy, il libro [Bitcoin dalla teoria alla pratica](https://amzn.to/2Ldym0F) e il tascabile [Bitcoin 199 domande](https://amzn.to/3ckIkJj).

Questo canale ha come obiettivo rispondere a domande che spesso riceviamo dagli amici, che leggiamo su internet, e perchè no, alle vostre lasciate nei commenti.

Oggi rispondo a **Paolo**, mio carissimo amico, che mi domanda:

La chiave privata è molto importante quando parliamo di Bitcoin e non solo. Ma di che cosa si tratta? Che cosa è una firma digitale?

Partiamo dicendo che Bitcoin utilizza la crittografia **asimmetrica**, dove abbiamo due chiavi, una privata e l’altra pubblica.

Sono legate matematicamente grazie a particolari proprietà dei numeri primi.

Dalla chiave privata si può **derivare** la chiave pubblica ma non si può fare il contrario.

Si chiama crittografica asimmetrica proprio per la presenza delle due chiave, altrimenti parliamo di crittografia **simmetrica**.

La firma digitale si ottiene applicando una funzione crittografica utilizzando la chiave privata sul hash del messaggio.

La firma si può verificare grazie all’utilizzo della chiave pubblica corrispondente.

La firma risolve tre fondamentali concetti,

- Non ripudio: cioè chi ha firmato non potrà disconoscerlo
- Integrità: se il messaggio viene manomesso ce ne accorgiamo
- Autenticità: Il destinatario deve essere sicuro di aver ricevuto il messaggio dal mittente desiderato.

In Bitcoin la firma digitale viene utilizzata nella verifica delle transazioni, tramite **OP_CODE** come **OP_CHECKSIG** e derivate.

Passiamo alla pratica utilizzando l’algoritmo delle curve ellittiche utilizzato in Bitcoin.

---

---

Abbiamo quindi visto quanto è importante custodire la chiave privata, perchè ci autentica verso qualcuno o verso un’intera rete.

La parte pratica che avete visto è possibile scaricarla dal nostro repository [Github](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action), l’indirizzo lo trovate nella descrizione del video.

Non mi resta che salutarvi, di mettermi un like se il video vi è piaciuto e di iscrivervi a canale attivando la campanella per essere avvisati dei prossimi video.

Ciao!
