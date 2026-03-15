---
title: "Satoshi è morto, lunga vita a Satoshi! We are all Satoshi!"
date: 2020-05-27T10:00:00+01:00
slug: "satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi"
draft: false
author: "Alessio Barnini"
description: "Scopri il video sul nostro canale youtube Bitcoin in action"
cover: "/img/posts/satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi-4.webp"
tags:
  - "BIP"
  - "Bitcoin"
  - "Bitcoin Script"
categories:
  - "Bitcoin"
---

Il 24 Maggio 2020, non il 25 come molte testate hanno riportato, è stato pubblicato un messaggio anonimo su [Debian Pastezone](https://web.archive.org/web/20200525113513/https://paste.debian.net/1148565).

![](/img/posts/satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi-4.webp)

La traduzione in italiano del messaggio è: “Craig Steven Wright è un bugiardo e un truffatore.

Non ha le chiavi usate per firmare questo messaggio.

Lightning Network è un risultato significativo.

Tuttavia dobbiamo continuare a lavorare per migliorare la capacità on-chain.

Sfortunatamente la soluzione non è solo cambiare una costante nel codice o permettere a partecipanti possenti di spingerne fuori altri.

Siamo tutti Satoshi”

Per un neofita questo messaggio risulterà criptico, proviamo a sintetizzarlo punto per punto.

### Craig Steven Wright (CSW) è un bugiardo e un truffatore.

Craig Steven Wright è una persona enigmatica della scena Bitcoin.

Più volte pubblicamente ha tentato di dimostrare, senza successo, di essere Satoshi Nakamoto o almeno di possedere le chiavi private attribuite a Satoshi.

Il contesto è alquanto articolato e la storia si prolunga per anni quindi non possiamo offrirvi una sintesi giornalistica/sensazionalistica.

Vi consigliamo di leggere il capitolo dedicato alla questione all’interno del libro “[La vita segreta](https://amzn.to/2XuRq08)”.

![Capitolo “L’affaire Satoshi” a p.121](/img/posts/satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi-5.webp)
*Capitolo “L’affaire Satoshi” a p.121*

### Non ha le chiavi usate per firmare questo messaggio.
**Perché sono importanti le chiavi usate per firmare questo messaggio**? 

Sono importanti perchè risultano essere le stesse chiavi per le quali CSW ha dichiarato, in [sede legale](https://www.courtlistener.com/recap/gov.uscourts.flsd.521536/gov.uscourts.flsd.521536.268.19.pdf%20/) tramite l’allegato [EXHIBIT 7](https://www.courtlistener.com/recap/gov.uscourts.flsd.521536/gov.uscourts.flsd.521536.512.7.pdf), di possederne le corrispettive chiavi private. Le UTXO associate a queste chiavi, secondo CSW, risultano essere parte di un accordo, chiamato “Tulip Trust” fra CSW e Dave Kleiman. Dave è un altro early-adopter di Bitcoin sul quale vi consigliamo di [documentarvi](https://en.wikipedia.org/wiki/Dave_Kleiman#Alleged_Bitcoin_involvement).

### Lightning Network è un risultato significativo. Tuttavia dobbiamo continuare a lavorare per migliorare la capacità on-chain. Sfortunatamente la soluzione non è solo cambiare una costante nel codice o permettere a partecipanti possenti di spingerne fuori altri.

Questa parte contiene 3 messaggi distinti.

Il primo: “LN è un ottimo progetto ma non dobbiamo scordarci di continuare ad aumentare la quantità di tx/secondo che Bitcoin è in grado di processare.”

Il secondo: “per aumentare la capacità non bisogna aumentare ciecamente la dimensione dei blocchi”

Il terzo: “non vogliamo riporre tutto il potere in pochi miners”.

Sintetizzando estremamente, chi è dietro a questo messaggio dice “LN è la via, Bitcoin Cash (ovvero il fork di Bitcoin che per aumentare le tx/secondo ha alzato la costante riguardante la dimensione dei blocchi) non è la soluzione, non siamo a favore della centralizzazione del mining”

Quindi :) chi scrive probabilmente non è:

— promotore di Bitcoin Cash e dell’approccio “big blockers”

— Non e’ a favore di raggruppamenti di big miners

Quindi quindi chi rimane escluso?

Rimangono esclusi early bitcoiners forti promotori di SegWit, LN ed in contrasto con l’approccio “big blockers”.  
Per diritto di cronaca dobbiamo dire che alcuni supporter di spicco orbitano attorno [Blockstream](https://blockstream.com/).

### Siamo tutti Satoshi

Si riferisce al contenuto di una mail, purtroppo senza firma PGP, inviata da Satoshi nel 2015 che riportava “[I am not Craig Wright.

We are all Satoshi.](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-December/011936.html)”

![“I am not Craig Wright. We are all Satoshi.”](/img/posts/satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi-6.webp)
*“I am not Craig Wright. We are all Satoshi.”*

> **Adesso basta filosofia vogliamo vedere con la pratica se realmente** 1. Gli indirizzi in questione sono quelli citati da CSW in sede legale
2. Le firme associate ad ogni indirizzo sono vere

---

#### In Action

Iniziamo confrontando il PDF “[EXHIBIT 7](https://www.courtlistener.com/recap/gov.uscourts.flsd.521536/gov.uscourts.flsd.521536.512.7.pdf)” depositato in sede legale e l’elenco su Debian Pastezone.

Cerchiamo il primo indirizzo nel file PDF trovando corrispondenza.

![](/img/posts/satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi-5.webp)

Come possiamo verificare la firma fornita nel Debian Pastezone e l’indirizzo? Nel primo [video del canale Bitcoin in Action](https://www.youtube.com/watch?v=RU7LHPP4Lvk) è stata spiegata proprio la firma digitale, per verificarla è necessario, la chiave pubblica, il messaggio e la firma digitale.

Solo il possessore di una determinata chiave privata può generare una determinata firma che può essere comprovata con la corrispondente chiave pubblica.

In bitcoin-cli esiste il metodo [**verifymessage**](https://bitcoin-rpc.github.io/en/doc/0.17.99/rpc/util/verifymessage/) per ottenere la verifica che stiamo cercando.

Per conoscere i suoi parametri è possibile utilizzare **help**.

Per verificare le firme è necessario utilizzare la blockchain mainnet.

Per prima cosa salviamo il messaggio nella variabile d’ambiente MSG così da utilizzarla più facilmente

```bash
$ MSG="Craig Steven Wright is a liar and a fraud. He doesn’t have the keys used to sign this message.
The Lightning Network is a significant achievement. However, we need to continue work on improving on-chain capacity.
Unfortunately, the solution is not to just change a constant in the code or to allow powerful participants to force out others.
We are all Satoshi"
```
per assicurarci che tutto sia andato a buon fine, eseguiamo il comando echo

```bash
echo $MSG
```


Siamo pronti a verificare il messaggio, inserendo come primo parametro l’indirizzo, che non è altro che la chiave pubblica, la firma generata dalla chiave privata corrispondente, e il messaggio firmato.

Il risultato di questa chiamata restituisce true se il controllo è andato a buon fine, false altrimenti.

```bash
$ bitcoin-cli verifymessage "1FbPLPR1XoufBQRPGd9JBLPbKLaGjbax5m" "G3SsgKMKAOiOaMzKSGqpKo5MFpt0biP9MbO5UkSl7VxRKcv6Uz+3mHsuEJn58lZlRksvazOKAtuMUMolg/hE9WI=" $MSG

true
```


**La verifica è andata a buon fine**. Adesso andrebbero controllate tutte le firme manualmente. Abbiamo invece creato uno script disponibile nel nostro repository [GitHub](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action) che svolge il lavoro in automatico. Inoltre lo script inserisce altre informazioni, quale l’altezza del blocco in cui si trova la transazione stessa.

Il file si chiama, ovviamente, satoshi.sh

eseguiamolo

```bash
sh satoshi.sh
```


**La verifiche sono andate tutte a buon fine**. Bene, in questo appuntamento abbiamo approfondito un pò narrativa della community Bitcoin ed abbiamo provato con mano come sia possibile dichiarare la proprietà delle UTXO e di messaggi associati off-chain.

![https://twitter.com/adam3us/status/1264940026326061057](/img/posts/satoshi-morto-lunga-vita-a-satoshi-we-are-all-satoshi-6.webp)
*https://twitter.com/adam3us/status/1264940026326061057*

Alla prossima!
