---
title: "Crittografia Pt II"
date: 2019-09-02T10:00:00+01:00
slug: "crittografia-pt-ii"
draft: false
author: "Alessio Barnini"
description: "L’arte del nascondere"
images: ["https://cdn-images-1.medium.com/max/1200/0*-0Pz_T4ItiEkI9mH.png"]
tags:
  - "Bitcoin"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Crittografia Pt II

#### L’arte del nascondere

Dopo aver analizzato la [prima parte della crittografia](https://medium.com/@bitcoindallateoriallapratica/come-nasce-la-crittografia-fino-al-bitcoin-parte-prima-68756d6715a9), andiamo più in profondità.

> Lo scopo della **crittografia** non è quello di nascondere il messaggio, MA di **nascondere il suo significato**!

Aumentiamo il nostro vocabolario con nuovi termini:

--- **Crittoanalisi**: Tecnica con cui si riesce a interpretare un messaggio senza conoscere la chiave. (dal greco kryptós, “nascosto”, e analýein, “scomporre”). **Chiave**: Influenza il processo di cifratura. È una parola stabilita tra il mittente e il destinatario. Su di essa si basa la segretezza.

---

Altro esempio degno di nota è il cifrario di [Giulio Cesare](https://it.wikipedia.org/wiki/Gaio_Giulio_Cesare).

Era un metodo veramente semplice, si trattava di traslare le lettere di 3 posti in avanti.

Quindi la A diventava la D, la B diventava la E, la Z diventava la C, proprio perchè “riniziare” l’alfabeto.

![Cifrario di cesare](https://cdn-images-1.medium.com/max/1200/0*vAbWArNqQ0dQS4PR.jpg)
*Cifrario di cesare*

Quindi il mio diminutivo **BARNO** si tramutava in **EDUQR**.

Un pò come il farfallino, ve lo ricordate? 
COFO MEFE STAFA IFI?

Altro cifrario particolare fu quello di [Polibio](https://it.wikipedia.org/wiki/Scacchiera_di_Polibio).

Particolare perchè venne pensato per fare una sorta di telegrafo ottico.

Spieghiamo prima la sua tecnica.

Si crea una matrice 5x5 e in ogni casella si inserisce una lettera.

Spesso la I e la J sono nella stessa casella.

![Cifrario di Polibio.](https://cdn-images-1.medium.com/max/1200/1*JNNNrYRbfQSncVbE7BndeQ.png)
*Cifrario di Polibio.*

Cosi per scrivere BARNO si prendono le coordinate della riga e della colonna e si ottiene il risultato 12 11 42 33 34. 
E perchè un telegrafo ottico? Il messaggero era dotato di 5 torce per mano e alzava il giusto numero di torce in base al messaggio da comunicare. 
Nell’esempio BITCOIN (forse a quei tempi c’erano i sesterzi?), il messaggero si sarebbe comportato in questo modo:

- B: 1 torcia a sinistra, 2 torce a destra.
- I: 2 torce a sinistra, 4 torce a destra.
- T: 4 torce a sinistra, 4 torce a destra.
- C: 1 torcia a sinistra, 3 torce a destra.
- O: 3 torce a sinistra, 4 torce a destra.
- I: 2 torce a sinistra, 4 torce a destra.
- N: 3 torce a sinistra, 3 torce a destra.

---

Ed ecco gli arabi che oltre ad inventare diverse tecniche di crittografia inventarono anche la [**crittoanalisi**](https://it.wikipedia.org/wiki/Crittoanalisi), cioè interpretare il messaggio senza conoscere la chiave.  
La chiave, nell’esempio del cifrario di Giulio Cesare, è 3 posizioni avanti dell’alfabeto.  
Qui anche l’ **Italia** si fa avanti, con [**Giovanni Soro**](https://it.wikipedia.org/wiki/Giovanni_Soro), il primo importante decrittatore Europeo, e con l’architetto [**Leon Battista Alberti**](https://it.wikipedia.org/wiki/Leon_Battista_Alberti) che proponeva le cifrature **polialfabetiche**, ovvero utilizzare non uno ma **più alfabeti** con l’obiettivo di offuscare maggiormente il messaggio. 
La crittografia **monoalfabetica** non era così forte, infatti una crittoanalisi di un messaggio di [Maria Stuarda](https://it.wikipedia.org/wiki/Maria_Stuarda) fu decodificato.

Il testo conteneva una cospirazione per assassinare [Elisabetta I](https://it.wikipedia.org/wiki/Elisabetta_I_d%27Inghilterra).

Che cosa si intende con più alfabeti? 
Lo scopriremo nella prossima puntata!

---

![Cifrario di Giulio Cesare](https://cdn-images-1.medium.com/max/1200/0*-0Pz_T4ItiEkI9mH.png)
*Cifrario di Giulio Cesare*
