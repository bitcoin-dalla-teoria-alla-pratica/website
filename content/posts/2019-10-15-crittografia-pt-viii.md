---
title: "Crittografia Pt VIII"
date: 2019-10-15T10:00:00+01:00
slug: "crittografia-pt-viii"
draft: false
author: "Alessio Barnini"
description: "RSA — Ron Rivest, Adi Shamir, Leonard Adlemen."
tags:
  - "Bitcoin"
  - "Chiave Privata"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

## RSA — Ron Rivest, Adi Shamir, Leonard Adlemen

Siamo arrivati alla rivoluzione vera e propria della crittografia: la crittografia a chiave pubblica, detta anche crittografia **asimmetrica**. Che cosa la rende così importante? La possibilità di condividere la chiave pubblica senza aver bisogno di un canale sicuro, a differenza della crittografia simmetrica.

Nella crittografia asimmetrica abbiamo due chiavi distinte ma legate matematicamente: la **chiave privata** e la **chiave pubblica**. Viene risolto anche il problema dell'**autenticazione** del mittente e dell'integrità del messaggio trasmesso, grazie alla **firma digitale**.

Tutto nacque nel **1975** dagli studi di [Whitfield Diffie](https://it.wikipedia.org/wiki/Whitfield_Diffie) e [Martin Hellman](https://it.wikipedia.org/wiki/Martin_Hellman). Il loro obiettivo era usare la crittografia senza dover trasferire la chiave su un canale sicuro: veniva scambiata in chiaro una porzione della chiave che, combinata matematicamente con una parte privata, derivava la chiave desiderata.

In questo modo, se qualcuno intercettasse la chiave durante lo scambio, non rappresenterebbe alcun pericolo — a differenza della crittografia simmetrica, dove l'intercettazione della chiave espone tutto il messaggio. Questo meccanismo prende il nome di [**Diffie-Hellman**](https://it.wikipedia.org/wiki/Scambio_di_chiavi_Diffie-Hellman) ed è ancora utilizzato oggi, ma non risolve il problema dell'**autenticazione** né consente la **cifratura dei messaggi**.

Arriviamo quindi alla crittografia asimmetrica sviluppata da [**Rivest**](https://it.wikipedia.org/wiki/Ronald_Rivest), [**Shamir**](https://it.wikipedia.org/wiki/Adi_Shamir) e [**Adleman**](https://it.wikipedia.org/wiki/Leonard_Adleman) — da cui l'acronimo **RSA**.

La rivoluzione sta nella coppia di chiavi: diverse ma legate matematicamente grazie alle proprietà dei numeri primi. Dalla chiave privata è possibile derivare la chiave pubblica, ma la chiave pubblica **non fornisce alcuna informazione** per risalire alla chiave privata.

Per questo la chiave pubblica può essere distribuita liberamente. Questa scoperta ha inaugurato l'era dell'autenticazione e della firma digitale — l'algoritmo RSA è utilizzato, tra gli altri, nel protocollo SSL da Visa e Mastercard.

---

## Come viene utilizzata per nascondere il messaggio

![codificare il messaggio con la chiave pubblica](/img/posts/crittografia-pt-viii-1.webp)
*Cifrare il messaggio con la chiave pubblica del destinatario.*

Ipotizziamo che Bob voglia mandare ad Alice un messaggio cifrato. Ha bisogno solo della chiave pubblica di Alice, trasferibile senza canale sicuro. Bob **cifra** il messaggio **con la chiave pubblica di Alice** e glielo invia. Una volta cifrato, il messaggio non è decifrabile con la stessa chiave pubblica: Alice deve usare la sua **chiave privata**.

> Chiave pubblica → cifra il messaggio
> Chiave privata → decifra il messaggio

---

## Cosa succede se cifriamo con la chiave privata e decifriamo con la pubblica?

Dato che la chiave privata è **segreta**, solo il suo possessore può produrre una certa cifratura. Questo non garantisce la **segretezza** del messaggio — la chiave pubblica è distribuita liberamente — ma **autentica il mittente**: siamo certi che il messaggio provenga esattamente da quella persona.

![Autenticazione ottenuta con la chiave privata del mittente](/img/posts/crittografia-pt-viii-2.webp)
*Autenticazione con la chiave privata del mittente.*

Il flusso è:

- Bob cifra il messaggio con la sua **chiave privata**
- Invia il messaggio ad Alice
- Alice decifra il messaggio con la **chiave pubblica di Bob**

> Chiave privata → cifra (autenticazione)
> Chiave pubblica → decifra (verifica)

---

## Come ottenere autenticazione e segretezza insieme

Per aggiungere anche la segretezza, si cifra il messaggio anche con la chiave pubblica del destinatario.

![Autenticazione e segretezza del messaggio](/img/posts/crittografia-pt-viii-3.webp)
*Autenticazione e segretezza combinate.*

Il flusso completo:

- Bob cifra il messaggio con la sua **chiave privata** → ottiene l'autenticazione
- Bob cifra il risultato con la **chiave pubblica di Alice** → ottiene la segretezza
- Alice decifra con la sua **chiave privata**
- Alice verifica con la **chiave pubblica di Bob**
- Alice legge il messaggio in chiaro

---

## Che cosa è la firma digitale?

La firma digitale è una forma di autenticazione. A differenza dei casi precedenti, non opera direttamente sul messaggio ma su un suo **riassunto**, detto **digest** o **hash del messaggio**.

Un algoritmo di hash produce un output di dimensione fissa da un input di qualsiasi dimensione. Bitcoin usa spesso **SHA256**: qualunque sia l'input, l'output è sempre **256 bit** (64 caratteri esadecimali). La firma digitale è quindi il digest cifrato con la chiave privata.

![Firma digitale](/img/posts/crittografia-pt-viii-4.webp)
*Schema della firma digitale.*

Il flusso:

- Bob applica SHA256 al messaggio in chiaro → ottiene il **digest**
- Cifra il digest con la sua **chiave privata** → ottiene la **firma digitale**
- Invia ad Alice: messaggio in chiaro, firma e chiave pubblica
- Alice applica la **chiave pubblica di Bob** sulla firma → ottiene il digest originale
- Alice applica SHA256 al messaggio ricevuto → ottiene il digest del messaggio
- Alice **confronta i due digest**: se coincidono, la firma è valida e il messaggio non è stato alterato

Questo è esattamente il meccanismo con cui Bitcoin identifica il legittimo possessore di fondi: solo chi possiede la chiave privata può produrre una firma valida. Il protocollo verifica la firma confrontando i digest.

Nei primi capitoli del libro [**Bitcoin dalla teoria alla pratica**](https://www.amazon.it/Bitcoin-Dalla-teoria-alla-pratica/dp/B07SNNNL2P/) mettiamo in pratica la crittografia asimmetrica con esempi concreti e reali.

---

## Cosa risolve la firma digitale

- **Integrità**: garantisce che il messaggio non sia stato alterato durante la trasmissione. Se Peter intercetta e modifica il messaggio, il digest non corrisponderà più.
- **Autenticità**: Alice è certa che il messaggio provenga da Bob e non da qualcuno che si spaccia per lui.
- **Non ripudio**: il mittente non può disconoscere un messaggio che ha firmato con la propria chiave privata.

---

Bitcoin non utilizza RSA, bensì la crittografia a [**curve ellittiche**](https://it.wikipedia.org/wiki/Crittografia_ellittica): stesse proprietà, ma più veloce in esecuzione. Dalla scitala alla crittografia asimmetrica — ne abbiamo fatta di strada.
