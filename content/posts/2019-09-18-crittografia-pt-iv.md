---
title: "Crittografia Pt IV"
date: 2019-09-18T10:00:00+01:00
slug: "crittografia-pt-iv"
draft: false
author: "Alessio Barnini"
description: "L’arte del nascondere —  Guerra fredda e Che Guevara"
cover: "/img/posts/crittografia-pt-iv-1.webp"
tags:
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Crittografia Pt IV

#### L’arte del nascondere — Guerra fredda e Che Guevara

Ancora non è stato spiegato [nei passati articoli](https://medium.com/@bitcoindallateoriallapratica/https-medium-com-bitcoindallateoriallapratica-come-nasce-la-crittografia-parte-terza-monoalfabetico-b3bd155367b8), ma come si può facilmente immaginare, la crittografia è stata materia di studio per scopi bellici. 
Era infatti molto importante comunicare con l’alleato senza far capire al nemico il proprio piano d’azione. 
A partire dal 1700 ogni potenza europea aveva la sua **camera nera**, un centro per la **decifratura** dei messaggi in codice.  
Questo portò velocemente a sviluppare nuovi sistemi **polialfabetici** e mandare in pensione quelli **monoalfabetici**.

Nel 1917 [**Gilbert Vernam**](https://it.wikipedia.org/wiki/Gilbert_Vernam) allora impiegato alla AT&T inventò un sistema di cifratura da utilizzare con il telegrafo.

![Il telegrafo permette la trasmissione di dati a distanza](/img/posts/crittografia-pt-iv-2.webp)
*Il telegrafo permette la trasmissione di dati a distanza*

Il cifrario di **Vernam** consisteva nel sostituire le lettere con dei numeri che venivano a loro volta *sommati* con una chiave lunga quanto il messaggio da codificare.

La chiave era OTP, **One time pad**, usa e getta.

Il sistema Vernam fu etichettato come sistema di **cifratura perfetto** il che vuol dire che non si può ottenere il testo in chiaro avvalendosi della crittoanalisi, ma serve la chiave di cifratura per decifrare il messaggio.

![Il telefono rosso](/img/posts/crittografia-pt-iv-3.webp)
*Il telefono rosso*

Fu utilizzato durante la guerra fredda con l’utilizzo del [telefono rosso](https://it.wikipedia.org/wiki/Linea_rossa), la linea che collegava Washington e Mosca.

Questa linea di comunicazione doveva evitare il rischio di una **guerra atomica**.

![Ernesto Che Guevara](/img/posts/crittografia-pt-iv-1.webp)
*Ernesto Che Guevara*

Anche [Che Guevara](https://it.wikipedia.org/wiki/Che_Guevara) e [Fidel Castro](https://it.wikipedia.org/wiki/Fidel_Castro) utilizzavano il sistema Vernam per le loro comunicazioni.

Infatti fu ritrovato un codice Vernam nella tasca di Ernesto Che Guevara quando fu catturato e giustiziato dall’esercito boliviano.

---

Ma come funziona il cifrario di **Vernam**?  
Come detto poco sopra abbiamo bisogno di una chiave usa e getta lunga quanto il messaggio che vogliamo codificare e le lettere vengono convertite in numeri, i quali vengono sommati per ottenere la lettera codificata, fino ad ottenere il messaggio crittato.  
Facciamo un esempio con la parola BARNO.

Prendiamo l’alfabeto e numeriamolo. Prendiamo anche una chiave random **APWQM**. Ovviamente il mittente e il destinatario dovevano conoscere la chiave.  
Qui abbiamo il problema delle distribuzioni delle chiavi che si presenta nella [crittografia simmetrica](https://it.wikipedia.org/wiki/Crittografia_simmetrica), che vedremo più avanti.

![scusate l’immagine un pò artigianale :)](/img/posts/crittografia-pt-iv-4.webp)
*scusate l’immagine un pò artigianale :)* **Testo chiaro ….**. `B A R N O` **Chiave………....**. `A P W Q M` **Testo crittato ….**. `B P N D A`

La prima lettera del testo in chiaro è la **B** che ha come valore numerico 1. 
La prima lettera della chiave è **A** che ha come valore numerico 0. 
1+0=1 che corrisponde alla lettera **B**.

La seconda lettera del testo in chiaro è la **A** che ha come valore numerico 0. 
La seconda lettera della chiave è **P** che ha come valore numerico 15. 
0+15=15 che corrisponde alla lettera **P**.

La terza lettera del testo in chiaro è la **R** che ha come valore numerico 17. 
La terza lettera della chiave è **W** che ha come valore numerico 22. 
17+22=39 che corrisponde alla lettera **N**.  
(ripartiamo dall’inizio se otteniamo un numero maggiore della lunghezza dell’alfabeto).

La quarta lettera del testo in chiaro è la **N** che ha come valore numerico 13. 
La quarta lettera della chiave è **Q** che ha come valore numerico 16. 
13+16=29 che corrisponde alla lettera **D**.

La quinta lettera del testo in chiaro è la **O** che ha come valore numerico 14. 
La quinta lettera della chiave è **M** che ha come valore numerico 12. 
14+12=26 che corrisponde alla lettera **A**.

Il risultato è `B P N D A`.

Per decifrarlo, dobbiamo compiere l’operazione inversa. **Testo crittato ….**. `B P N D A` **Chiave………….**. `A P W Q M`

La prima lettera del testo crittato è **B** che ha come valore numerico 1. 
La prima lettera della chiave è **A** che ha come valore numerico 0. 
1–0= 1 che corrisponde alla lettera **B** La seconda lettera del testo crittato è **P** che ha come valore numerico 15. 
La seconda lettera della chiave è **P** che ha come valore numerico 15. 
15–15= 0 che corrisponde alla lettera **A** La terza lettera del testo crittato è **N** che ha come valore numerico 13. 
La terza lettera della chiave è **W** che ha come valore numerico 22. 
13–22=-9 che corrisponde alla lettera **R** (percorriamo l’alfabeto al contrario).

La quarta lettera del testo crittato è **D** che ha come valore numerico 3. 
La quarta lettera della chiave è **Q** che ha come valore numerico 16. 
16–3=-13 che corrisponde alla lettera **N**.

La quinta lettera del testo crittato è **A** che ha come valore numerico 0. 
La quinta lettera della chiave è **M** che ha come valore numerico 12. 
0–12=-12 che corrisponde alla lettera **O**.

Il risultato è `B A R N O`. **Incredibile**. ---

![Alcuni appunti presi durante lo studio](/img/posts/crittografia-pt-iv-5.webp)
*Alcuni appunti presi durante lo studio*
