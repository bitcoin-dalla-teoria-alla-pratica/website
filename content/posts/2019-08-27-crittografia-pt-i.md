---
title: "Crittografia Pt I"
date: 2019-08-27T10:00:00+01:00
slug: "crittografia-pt-i"
draft: false
author: "Alessio Barnini"
description: "L’arte del nascondere"
cover: "https://cdn-images-1.medium.com/max/1200/1*IKLt0hEEbWr0RbuNG_klMA.gif"
tags:
  - "Bitcoin"
  - "Crittografia"
  - "Storia"
categories:
  - "Bitcoin"
---

---

### Crittografia Pt I

#### L’arte del nascondere

Durante la creazione del [video corso](https://tinyurl.com/yxe8b8cs) e del libro [Bitcoin dalla teoria alla pratica](https://www.amazon.it/Bitcoin-Dalla-teoria-alla-pratica/dp/B07SNNNL2P/) ci siamo imbattuti in una parte fondamentale del protocollo, la crittografia. 
Ma quali sono state le tappe fondamentali che la storia ha percorso per arrivare a scoprire la crittografia asimmetrica utilizzata in Bitcoin?

La prima volta che ho avuto a che fare con la **cifratura** e la **decifratura** è stato da piccolo, a mia insaputa, durante il caricamento di [Monkey Island](https://www.youtube.com/watch?v=GGCzZdmZgIw), o ancora durante il gioco [Indiana Jones and the Fate of Atlantis](https://youtu.be/LZZXJ3zCRDQ?t=9585).

![Guarda, dietro di te!!! una scimmia a tre teste!!!](https://cdn-images-1.medium.com/max/1200/1*IKLt0hEEbWr0RbuNG_klMA.gif)
*Guarda, dietro di te!!! una scimmia a tre teste!!!*

Entrambi ricordano la tecnica utilizzata da [Enea il tattico](https://it.wikipedia.org/wiki/Enea_Tattico) che utilizzava un sistema meccanico di dischi forati.

Ma andiamo per ordine, dando delle definizioni ai termini base.  
*Il vocabolario delle parole chiave aumenterà strada facendo.*

--- **Messaggio in chiaro**: testo che non ha subito cifrature, interpretabile da chiunque. **Cifrare**: Trasformare un messaggio in chiaro in un messaggio 
incomprensibile. **Crittato**: Messaggio a cui è stato applicato la cifratura. **Cifrario**: È il metodo di cifratura. **Decifratura**: L’operazione inversa di cifrare, convertire un messaggio cifrato in chiaro.

---

È una storia affascinante che descriveremo a *puntate.*

L’obiettivo principale che la **crittografia** vuole raggiungere è **nascondere il messaggio** a chi non deve leggerlo, e dare la possibilità al destinatario di **decifrarlo**, e quindi di leggere il messaggio in chiaro e di comprenderlo.

Le prime tecniche però si basavano sull’ **offuscare** il messaggio cioè di coprirlo. Questa tecnica prende il nome di [steganografia](https://it.wikipedia.org/wiki/Steganografia).

> Dal greco: 
> Steganòs = coperto 
> gràphein = scrivere

Le prime tecniche utilizzate nell’antica Cina sono quelle utilizzate oggi dagli spacciatori internazionali.

Gli **ovuli**.

Infatti il messaggio veniva scritto su una seta molto fine e poi coperta di cera.

Il messaggero, dopo aver inghiottito l’ovulo, si recava dal destinatario per consegnarlo (💩).

Altra tecnica utilizzata nell’antica Persia da **Erodoto** era quella di scrivere sulle **teste rasate** degli schiavi e aspettare che i capelli fossero ricresciuti per occultare il messaggio.

A quel punto lo schiavo partiva verso il destinatario, che a sua volta doveva rasare i capelli al messaggero per scoprire il messaggio.

Tali tecniche soffrivano di un problema molto grande, se i nemici fermavano i messaggeri e scovavano il messaggio potevano interpretarlo senza problemi. 
Ecco che da qui è nata la necessità della **crittografia**. Il suo scopo non è quello di nascondere il messaggio, MA di **nascondere il suo significato**!

> Dal greco: 
> Kryptòs = nascondere 
> gràphein = scrivere

Riporto le tecniche che mi hanno maggiormente emozionato.

![Scitala utilizzata nell’antica Grecia](https://cdn-images-1.medium.com/max/1200/0*xcPT_qg2p2DSfqTq.jpg)
*Scitala utilizzata nell’antica Grecia*

La tecnica della **scitala**, utilizzati dai magistrati di Sparta.

Che cosa è la scitala? La scitala è un bastone rotondo, lungo e liscio.

Il mittente e il destinatario avevo due scitale identiche, per dimensioni e diametro.

Il mittente avvolgeva un nastro di cuoio intorno al bastone facendo attenzione che questo non lasciasse nessuno spazio tra i lembi.

Una volta che il bastone era completamente ricoperto dal cuoio, veniva scritto il messaggio sopra di esso seguendo la lunghezza della scitala.

A lavoro finito il cuoio veniva srotolato e consegnato al messaggero che aveva il compito di portarlo al destinatario.

In questo modo anche se veniva intercettato da un nemico, quest’ultimo non era in grado di decifrare il messaggio in quanto non aveva la scitala adatta per mettere nel giusto ordine le lettere.

Solo il destinatario con la scitala identica al mittente poteva decifrarlo. 
Possiamo paragonarla alla crittografia **simmetrica** dei giorni nostri. Geniale.

![Cifrario di Enea il tattico.](https://cdn-images-1.medium.com/max/1200/1*syXHjOKKVlgFx5sRJcgTIA.png)
*Cifrario di Enea il tattico.*

Altra tecnica menzionata all’inizio di questo articolo è quella utilizzata da **Enea il tattico**.

Consisteva in un disco con 24 fori, ciascuno dei quali era assegnato una lettera disposte in ordine alfabetico.

Un filo partiva dal centro e “bucava” i buchi per scrivere il messaggio.

Il destinatario doveva sciogliere la matassa prodotta dal filo per decifrare il messaggio che a quel punto era scritto al contrario.

Sicuramente una crittografia meno potente della scitala ma comunque degna di nota.
