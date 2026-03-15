---
title: "La firma digitale"
date: 2019-12-02T10:00:00+01:00
slug: "la-firma-digitale"
draft: false
author: "Alessio Barnini"
description: "Che cosa è e come si ottiene?"
cover: "/img/posts/la-firma-digitale-1.webp"
tags:
  - "Bitcoin"
  - "Chiave Privata"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### La firma digitale

#### Che cosa è e come si ottiene?

Negli articoli precedenti abbiamo percorso la [storia della crittografia](https://medium.com/@bitcoindallateoriallapratica/crittografia-pt-viii-rsa-firma-digitale-bitcoin-blockchain-4f13445bfff3), capendo la differenza tra stenografia e la crittografia stessa.

> Steganòs = coperto 
> gràphein = scrivere

> Kryptòs = nascondere 
> gràphein = scrivere

La firma digitale come si posiziona nello scenario della crittografia?

Per spiegarla utilizzeremo la **crittografia asimmetrica** la quale permette di avere due chiavi distinte ma legate matematicamente.  
Le due chiavi prendono il nome di, **chiave privata** e **chiave pubblica**.

Come suggerisce il nome, la chiave privata deve rimanere tale, mentre la chiave pubblica può essere distribuita senza problemi.  
La chiave pubblica si deriva dalla chiave privata e **non è possibile** fare l’operazione inversa.

Siamo proprio sicuri che sia impossibile?

In realtà è possibile derivare la chiave privata partendo dalla chiave pubblica, utilizzando un attacco informatico che prende il nome di [brute force](https://en.wikipedia.org/wiki/Brute-force_attack).

Dobbiamo anche dire che è come trovare un atomo nell’universo.  
Per dare un’idea di grandezza stiamo parlando di 1 su 150,000 miliardi miliardi miliardi miliardi miliardi miliardi miliardi miliardi.

![](/img/posts/la-firma-digitale-2.webp)

---

Otteniamo 3 informazioni molto importanti utilizzando firma digitale, per capirle immaginando 3 persone, Alice, Bob e Peter (fantasia eh?). **Integrità**: Il messaggio non deve essere alterato durante la trasmissione.

Bob manda un messaggio a Alice con scritto W i bitcoin. 
Peter lo intercetta cambiandolo con W gli ether. 
Alice deve essere in grado di accorgersi di tale cambiamento. **Autenticità**: Alice deve essere sicura che il messaggio che ha ricevuto sia stato inviato da Bob, e non da Peter che si è *spacciato *per Bob. **Non ripudio**: il mittente non potrà disconoscere il messaggio che ha firmato.

---

Facendo riferimento al titolo dell’articolo, cerchiamo di capire come ottenere la firma digitale utilizzando il terminale.

Creiamo due cartelle Alice e Bob.

All’interno della cartella di Alice, genero la chiave privata utilizzando **ECC** ( **Elliptic Curve Cryptography** ), proprio la curva ellittica utilizzata in **Bitcoin**.

```bash
openssl ecparam -genkey -name secp256k1 -rand /dev/urandom -noout -out private.pem
```


Abbiamo ottenuto **private.pem**, la chiave privata che utilizzeremo per derivare la chiave pubblica, utilizzando il seguente comando.

```bash
openssl ec -in private.pem -pubout -out public.pem
```


Bene, abbiamo ottenuto anche la chiave pubblica (public.pem). 
Creiamo un messaggio da inviare a **Bob** e lo salviamo dentro messaggio_amore.txt.

```bash
echo “Bob ti Amo! By la tua Alice” > messaggio_amore.txt
```


Abbiamo tutto il necessario per creare la firma digitale. **La chiave privata e il messaggio**. 

```bash 
openssl dgst -sha256 -sign private.pem messaggio_amore.txt > signature.bin
```


Abbiamo ottenuto la firma, salvandola nel file **signature.bin (** ECDSA: Elliptic Curve Digital Signature Algorithm). 
Adesso possiamo inviare la firma, il messaggio e la nostra chiave pubblica a Bob, cosi da metterlo in condizione di verificare il messaggio!

```bash
cp./{public.pem,signature.bin,messaggio_amore.txt}../Bob && cd../Bob
```


Bob può verificare se il messaggio d’amore sia stato veramente inviato dalla sua dolce metà, utilizzando la chiave pubblica di Alice, il messaggio e la firma.

```bash
openssl dgst -sha256 -verify public.pem -signature signature.bin messaggio_amore.txt
```


**Verifica confermata**! Bob adesso è sicuro che il mittente sia proprio Alice!  
Perchè? 
Perchè Alice è l’unica che può fornire una firma che sia comprovata dalla sua chiave pubblica!

Non ci credete? Modificate il messaggio e applicate di nuovo la verifica!

---

È necessario conoscere le basi per imparare e capire il protocollo Bitcoin! 
Questo tipo di approccio è stato utilizzato nel nostro [**libro** **Bitcoin dalla teoria alla pratica**](https://www.corsobitcoin.com/) acquistabile su [Amazon](https://www.amazon.it/Bitcoin-Dalla-teoria-alla-pratica/dp/B07SNNNL2P/) e nei corsi [Udemy](https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13).

