---
title: "Crittografia Pt VII"
date: 2019-10-07T10:00:00+01:00
slug: "crittografia-pt-vii"
draft: false
author: "Alessio Barnini"
description: "Hello computer."
tags:
  - "Bitcoin"
  - "Chiave Privata"
  - "Crittografia"
categories:
  - "Bitcoin"
---

### Crittografia Pt VII

#### Hello computer.

I computer iniziano ad entrare nelle case delle persone comuni. Siamo intorno agli anni 70 e il loro prezzo diventa accessibile permettendo l’inizio della diffusione di massa.

> Nel 1977 viene presentato [Apple II](https://en.wikipedia.org/wiki/Apple_II_series)

Così anche la crittografia comincia a mutare e a spostarsi sui computer, anche perchè tutte le forme che [abbiamo affrontato](https://medium.com/@bitcoindallateoriallapratica/crittografia-pt-vi-alan-turing-enigma-guerra-mondiale-apple-bitcoin-dalla-teoria-alla-pratica-85a4464ca5ce) fino ad adesso erano estremamente lente anche se sicure. 
Aumentiamo di nuovo il nostro vocabolario, con delle sigle che iniziano a essere familiari con il periodo attuale in cui viviamo.

--- **DES**: Data Encryption Standard. **3-DES**: Triple Des. **AES**: Advanced Encryption Standard.

---

Uno dei primi algoritmi degni di nota fu [Lucifer](https://it.wikipedia.org/wiki/Lucifer_%28cifrario%29) creato da [Horst Feistel](https://it.wikipedia.org/wiki/Horst_Feistel) e colleghi all’[IBM](https://it.wikipedia.org/wiki/IBM).

L’algoritmo divenne lo Standard ( **DES** ) e successivamente fu venduto alla compagnia Lloyd’s che lo implementò nei primi **Bancomat**, sempre con l’appoggio di IBM.

Qui possiamo già capire come negli anni 70, la crittografia entra a far parte della vita comune e come paradossalmente oggi, nel 2020 ci si sorprenda del fatto che Bitcoin utilizzi la crittografia per la sicurezza.

Per fortuna non utilizza Lucifer, perchè venne crackato grazie all’utilizzo di 70000 computer.

Questo evento portò prima alla nascita del **3-DES** e successivamente di un nuovo standard [**AES**](https://it.wikipedia.org/wiki/Advanced_Encryption_Standard) con la scelta di un nuovo algoritmo di [cifratura a blocchi](https://it.wikipedia.org/wiki/Cifratura_a_blocchi), l’algoritmo di Rijndael.

Tutti i sistemi di cifratura affrontati (DES, 3-DES, AES) fino ad adesso, dalla scitala all’algoritmo di Rijndael avevano un funzionamento **simmetrico**, chiamato anche **cifratura a chiave privata**.![Cifratura simmetrica](/img/posts/crittografia-pt-vii-1.webp)
*Cifratura simmetrica*

Quali sono i suoi problemi noti?

Il problema principale è che la chiave cifrante è anche la chiave che decifra, quindi una possibile intercettazione della chiave porta a poter leggere il messaggio in chiaro a insaputa del mittente e del destinatario. 
Abbiamo un problema di **distribuzione** della chiave su un canale non sicuro.

> Se ci fosse un canale sicuro non sarebbe necessaria la crittografia :)

Come può avvenire quindi lo scambio delle chiavi?  
Preventivamente tra tutti i soggetti della *rete, *sempre che il numero non cambi durante le comunicazioni e se è *comodo *distribuire la chiave.

Se io sono italiano e il mio collega è giapponese la comodità e la sicurezza viene già meno.

Immaginiamo che la chiave di cifratura sia intercettata da un terzo non autorizzato.

Egli potrebbe inviare dei messaggi cifrati spacciandosi per un altro mittente e il destinatario non potrà mai sapere se il mittente è verificato o meno.

Tale problema (che poi sarà risolto con la firma digitale) è chiamato **autenticazione del mittente**.

Rullo di tamburi per il trio [Whitfield Diffie](https://it.wikipedia.org/wiki/Whitfield_Diffie), [Martin Hellman](https://it.wikipedia.org/wiki/Martin_Hellman) e [Ralph Merkle](https://en.wikipedia.org/wiki/Ralph_Merkle).

Sì, proprio lui, il padre del **merkle tree** utilizzato in Bitcoin. 
Questi tre Signori, grazie anche a studi approfonditi da parte di Diffie-Hellman hanno rivoluzionato il mondo, riuscendo a introdurre la crittografia asimmetrica, considerata ancora oggi estremamente sicura, e sì, è quella utilizzata in **Bitcoin**.

Ma per una degna spiegazione abbiamo bisogno di un altro articolo!
