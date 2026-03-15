---
title: "La storia di Bitcoin"
date: 2019-03-09T10:00:00+01:00
slug: "la-storia-di-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Da dove inizia la rivoluzione Bitcoin ?"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Crittografia"
  - "Cypherpunk"
  - "Firma Digitale"
  - "Hash"  
  - "Merkle Tree"
categories:
  - "Bitcoin"
---

---

### La storia di Bitcoin

Quest’anno (2019) abbiamo festeggiato 10 anni di Bitcoin, ovvero dal suo primo blocco creato da** Satoshi Nakamoto**.

Nella** coinbase** si può leggere il titolo del Times del 3 Gennaio 2009

```bash
echo 04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73 | xxd -r -p
```

*The Times 03/Jan/2009 Chancellor on brink of second bailout for banks*

Ma prima di quella data storica che cosa è successo?

![40 anni di ricerca](/img/posts/la-storia-di-bitcoin-1.webp)
*40 anni di ricerca*

Ho trovato in rete questa bellissima immagine che ripercorre dal 1973 al 2009 le tappe fondamentali del protocollo Bitcoin.

Abbiamo elementi come il** Merkle Tree**, nel 1980l Merkle tree elemento fondamentale per l’indicizzazione delle transazioniermette ai nodi SPV di fare delle ricerche senza scaricare l’intera blockchain, ed è anche elemento fondamentale per il PoW.

1985** Elliptic Curve** Cryptography, la crittografia utilizzata da Bitcoin per firmare le transazioni.

Ma più che tecnologie mi vorrei soffermare sulle persone e su quei progetti che hanno fatto diventare Bitcoin quello che è adesso.

Tutti conosciamo** Satoshi Nakamoto** come il creatore di Bitcoin, ma nessuno sa la sua vera identità.

Molti sostengono che non sia una persona soltanto, ma bensì, un gruppo di persone ad aver creato Bitcoin, e forse è l’ipotesi più plausibile.

Ma andiamo per gradi:

Alla fine degli anni 80 nacque un movimento, Cypherpunks.

Che cosa è un movimento [**Cypherpunks**](https://it.wikipedia.org/wiki/Cypherpunk)?

Un movimento** Cypherpunks** è un movimento che si pone come obiettivo quello di aumentare la privacy tramite la crittografia al fine di ottenere un cambiamento socio politico.

Un movimento molto ambizioso.

---

![David Chaum—DigiCash Inc](https://cdn-images-1.medium.com/max/1200/1*eH4HmNQTdMA_k3x3JzMz8A.png)
*David Chaum—DigiCash Inc*

*Security without Identification: Transaction Systems to Make Big Brother Obsolete*, cosi [**David Chaum**](https://en.wikipedia.org/wiki/David_Chaum), pubblicò il suo pensiero.

Chaum nel** 1989** crea una società [**DigiCash Inc**](https://en.wikipedia.org/wiki/DigiCash)a quale aveva come obiettivo quello di portare le sue “monete” nel mondo bancario.

Era una forma di pagamento elettronico anticipato, infatti l’utente doveva prelevare banconote dalla banca ed assegnare chiavi (pubblica e privata) da inviare al destinatarion questo modo sarebbe stato impossibile per le banche e per i governi rintracciare gli utenti , dato che gli utenti erano identificati con una stringa alfanumerica…ricorda qualcosa?

Purtroppo questo soffriva di centralizzazione in quanto la banca doveva rilasciare un nullaosta per utilizzarle, e dopo innumerevoli tentativi di colmare questo gap, la società andò in fallimento.

Ma questo fu l’inizio della** rivoluzione**. 👊

Da qui iniziarono ad entrare dei personaggi molto importanti

---

![Adam Back—Hashcash](/img/posts/la-storia-di-bitcoin-3.webp)
*Adam Back—Hashcash*

Già nel** 1997** si parlava di [**Proof of work**](https://en.bitcoin.it/wiki/Proof_of_work)** (PoW).**

Infatti [**Adam Back**](https://en.wikipedia.org/wiki/Adam_Back) creò [**Hashcash**](https://it.wikipedia.org/wiki/Hashcash), basato appunto sul Proof of work, per limitare lo spam email e attacchi DoS.

Come?

Rendendo la vita difficile agli spammers, il cui obiettivo è quello di mandare una grande quantità di email a basso costo.

Mentre in questo modo il destinatario poteva verificare che il mittente avesse effettivamente fatto il PoW e quindi filtrare più facilmente.

Questo algoritmo suona famigliare ?

---

![Wei Dai—b-money](/img/posts/la-storia-di-bitcoin-4.webp)
*Wei Dai—b-money*

L’anno successivo, 1998, [**Wei Dai**](https://en.bitcoin.it/wiki/Wei_Dai), pubblicò il primo paper dove descriveva la sua idea di** criptovaluta**.

La [**b-money**](https://en.bitcoin.it/wiki/B-money).

Era la prima criptovaluta anonima e distribuita.

Dai sviluppò due protocolli

Il Primo serviva per mantenere un database sincronizzato, dove registrare tutte le informazioni relative al mezzo di scambio, quindi ogni utente aveva questo database, quindi stiamo parlando di decentralizzazione.

Proprio come fanno i full node di Bitcoin che hanno la copia esatta della blockchain nel database [**LevelDb**](https://en.bitcoin.it/wiki/Bitcoin_Core_0.11_%28ch_2%29:_Data_Storage)

Il secondo, serviva per conteggiare l’ammontare di** b-money** posseduti.

---

![Hal Finney—RPoW](/img/posts/la-storia-di-bitcoin-5.webp)
*Hal Finney—RPoW*

Nel 2004, [**Hal Finney**](https://en.wikipedia.org/wiki/Hal_Finney_%28computer_scientist%29), sulla base di** Hashcash**, creo [RPoW](https://cryptome.org/rpow.htm), Reusable Proof of work.

Permetteva lo scambio di token e garantiva che ogni token potesse essere speso solo una volta.

Si chiamava RPoW, perchè oltre al PoW, utilizzava anche una crittografia** RSA** **asimmetrica** per firmare le Transazioni, quindi RPoW.

R di** RSA** e PoW di Proof of work

Questo progetto soffriva però di centralizzazione, in quanto le convalide per il double spending, venivano fatte da un server centralizzato

---

![Nick Szabo](/img/posts/la-storia-di-bitcoin-6.webp)
*Nick Szabo*

Si arriva quindi a [Nick Szabo](https://en.wikipedia.org/wiki/Nick_Szabo), che pubblica** Bit gold.**

Una valuta digitale basata su RPoW.

Bit gold proponeva un sistema decentralizzato, dove gli utenti grazie alla loro coppia di chiavi, firmavano la transazione, ovvero utilizzavano la firma digitale.

Anche se** BitGold** non ha mai visto luce, è da molti considerato il** precursore del Bitcoin**, anche perchè introduceva argomenti come [Byzantine fault-tolerant](https://en.wikipedia.org/wiki/Byzantine_fault) , il timestamping e la risoluzione di puzzle criptografici da parte degli utenti.

A differenza di bitcoin, questa moneta non avrebbe avuto una supply

---

![](https://cdn-images-1.medium.com/max/1200/1*WULseEL7GwZUkuJKkbe4vA.png)

Si arriva quindi al 2008, proprio durante la crisi finanziaria nasce [**Bitcoin**](https://bitcoin.org/bitcoin.pdf).

Sembra infatti che [**Satoshi Nakamoto**](https://it.wikipedia.org/wiki/Satoshi_Nakamoto) abbia riunito tutto il buono fatto dai precedenti personaggi ed abbia creato quello che tutti oggi noi conosciamo come blockchain e Bitcoin.

Ancora oggi non sappiamo la vera identità di Satoshi Nakamoto

La rivoluzione è nata 👊