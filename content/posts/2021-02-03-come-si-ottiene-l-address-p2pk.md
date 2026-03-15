---
title: "Come si ottiene l’address P2PK?"
date: 2021-02-03T10:00:00+01:00
slug: "come-si-ottiene-l-address-p2pk"
draft: false
author: "Alessio Barnini"
description: "O per meglio dire la chiave privata e la chiave pubblica?"
cover: "/img/posts/come-si-ottiene-l-address-p2pk-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

#### O per meglio dire la chiave privata e la chiave pubblica?

In questo ultimo articolo affronteremo con la teoria come si ottiene la chiave privata e come si deriva la chiave pubblica.

![Video disponibile nel canale Bitcoin in Action](/img/posts/come-si-ottiene-l-address-p2pk-1.webp)
*Video disponibile nel canale Bitcoin in Action*

Come già spiegato nei [precedenti articoli](/posts/come-si-riconosce-la-firma-digitale-in-bitcoin/), per lo script **P2PK**, non esiste un **address specifico**.

È molto importante comprendere come il protocollo Bitcoin si è evoluto per arrivare ad ottenere gli address che utilizziamo oggi.

> **Il tutto parte dalla chiave privata**.![SPOILER P2PKH! 👀 — La parte iniziale è identica al P2PK](/img/posts/come-si-ottiene-l-address-p2pk-2.webp)
*SPOILER P2PKH! 👀 — La parte iniziale è identica al P2PK*

La chiave privata è una sequenza di byte ottenuti applicando l’algoritmo [**secp256k1**](https://en.bitcoin.it/wiki/Secp256k1), i valori che otteniamo devono *ricadere* all’interno del range di tale algoritmo.

L’algoritmo secp256k1 è parte della crittografia delle curve ellittiche, spesso la troviamo l’acronimo **ECC**: **Elliptic Curve Cryptography**.

Troviamo anche l’acronimo **ECDSA** che ci indica Elliptic **Curve Digital Signature Algorithm**.

> **ECC**: **Elliptic Curve Cryptography 
> ECDSA:Curve Digital Signature Algorithm **La chiave privata deve rispettare le direttive **DER**, [**Distinguished Encoding Rules**](https://en.wikipedia.org/wiki/X.690#DER_encoding). Brevemente, la chiave viene interpretata come un coding binario e non contiene plain text come le chiavi **PEM**, come ad esempio — — -BEGIN EC PRIVATE KEY — — -

```bash
-----BEGIN EC PRIVATE KEY-----

xxxxx

-----END EC PRIVATE KEY-----
```


Sulla chiave viene aggiunto [un prefisso](https://en.bitcoin.it/wiki/List_of_address_prefixes) per identificare se la chiave privata è destinata all’ambiente di **main** o per l’ambiente di **test**.

Da qui si ottiene la chiave privata in formato **WIF**, acronimo di **Wallet Import Format**.

Se vogliamo importare una chiave privata nel nostro wallet utilizzeremo la chiave privata **WIF** con il comando **importprivkey**.

```bash
$ bitcoin-cli help importprivkey
```


Quando firmiamo la transazione utilizziamo la chiave privata **PEM**, come mostrato nel libro [Bitcoin In Action – SegWit, Bitcoin Script & Smart Contracts](prodotti/bitcoin-in-action/)

![Bitcoin In Action — SegWit, Bitcoin Script & Smart Contracts](/img/posts/come-si-ottiene-l-address-p2pk-3.webp)
*Bitcoin In Action — SegWit, Bitcoin Script & Smart Contracts*

Applicando un byte ( **01** ), in coda alla chiave, si ottiene la chiave privata **WIF** **compressa**, altrimenti si ha la chiave WIF non compressa.  
Ad oggi si utilizza prevalentemente la chiave privata compressa.

Dalla chiave privata si deriva la chiave pubblica, compressa e non compressa.  
La chiave pubblica non compressa è quella che abbiamo analizzato negli articoli [**precedenti dedicati al P2PK**](/posts/come-si-valida-una-transazione-p2pk/), la riconosciamo perchè inizia sempre con il byte **04** ed è lunga **130** caratteri esadecimali

La chiave pubblica compressa si ottiene applicando un **version prefix**, verificando l’ultimo byte e applicando la funzione crittografica **RIPEMD160**.

> Nel [video corso](https://bitcoininaction.com/) e nei [nostri libri](https://www.amazon.it/Alessio-Barnini/e/B07SLZYLC4?ref=sr_ntt_srch_lnk_1&qid=1612347522&sr=8-1) andiamo con la pratica a generare **manualmente** tutti gli indirizzi.

Perchè è stata preferita la chiave pubblica compressa nel corso degli anni? 
Le **fees** si pagano in base a quanto è *pesante* la transazione in termini di bytes, o per meglio dire sulla **vsize** dopo l’introduzione di SegWit.

Come ormai sappiamo, la chiave privata **non deve essere assolutamente condivisa**, perchè è in grado di generare quella firma digitale comprovabile dalla corrispondete chiave pubblica, che ovviamente è stata possibile derivare solo ed esclusivamente da quella chiave privata.

Se ti stai chiedendo perchè è importante la firma,[guarda gli articoli precedenti](/posts/bitcoin-in-action-perch-cos-importante-la-chiave-privata/).
