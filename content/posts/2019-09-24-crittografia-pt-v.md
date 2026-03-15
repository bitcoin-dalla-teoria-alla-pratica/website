---
title: "Crittografia Pt V"
date: 2019-09-24T10:00:00+01:00
slug: "crittografia-pt-v"
draft: false
author: "Alessio Barnini"
description: "L’arte del nascondere. Enigma."
cover: "https://cdn-images-1.medium.com/max/1200/1*oPEthuxSMyNsY6rO6ZrrLQ.png"
tags:
  - "Bitcoin"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Crittografia Pt V

#### L’arte del nascondere. Enigma.

In questo articolo cominceremo a conoscere la macchina [**Enigma**](https://it.wikipedia.org/wiki/Enigma_%28crittografia%29), famosa anche grazie al film [The imitation game](https://it.wikipedia.org/wiki/The_Imitation_Game).

Fu una macchina utilizzata dai tedeschi nella seconda guerra mondiale ed era basata su una serie di cilindri e dischi rotanti.

Ma prima di andare nel dettaglio è doveroso tornare all’inizio dell’800 con [**Thomas Jefferson**](https://it.wikipedia.org/wiki/Thomas_Jefferson), il quale non si fece *mancare niente, *è stato infatti uno degli autori della Dichiarazione d’indipendenza e presidente degli Stati Uniti.

![Wheel cypher di Jefferson](https://cdn-images-1.medium.com/max/1200/0*q8cJsjrWSSq3JMsy.jpg)
*Wheel cypher di Jefferson*

Fu anche il primo a ideare un cifrario **polialfabetico** **meccanico** basato su un cilindro e dischi rotanti dove erano presenti le lettere dell’alfabeto. 
Il suo cifrario chiamato anche *wheel cypher *iniziò ad essere utilizzato dal 1922 fino al 1943.

Come si può vedere dall’immagine il cifrario è basato su un numero arbitrario di dischi sui quali sono scritte le 26 lettere dell’alfabeto in ordine sparso.

I dischi si possono muovere in maniera indipendente. 
Come funzionava? 
Chi cifrava il messaggio formava il testo in chiaro e poi comunicava la **parola cifrata** che si era formata su un’altra colonna e la chiave, formata dall’ordine di come i dischi venivano impilati.  
Facciamo un esempio concreto sfruttando la tabella di [Wikipedia](https://it.wikipedia.org/wiki/Rullo_di_Jefferson).

Questo sistema presuppone che anche il destinatario abbia lo stesso Wheel cypher e gli stessi dischi. 
La parola da comunicare è sempre **BARNO**. I dischi si presentono così:

```bash
1: < ZWAXJGDLUBVIQHKYPNTCRMOSFE < 2: < KPBELNACZDTRXMJQOYHGVSFUWI < 3: < BDMAIZVRNSJUWFHTEQGYXPLOCK < 4: < RPLNDVHGFCUKTEBSXQYIZMJWAO < 5: < IHFRLABEUOTSGJVDKCPMNZQWXY < 6: < AMKGHIWPNYCJBFZDRUSLOQXVET < 7: < GWTHSPYBXIZULVKMRAFDCEONJQ < 8: < NOZUTWDCVRJLXKISEFAPMYGHBQ < 9: < XPLTDSRFHENYVUBMCQWAOIKZGJ < 10: < UDNAJFBOWTGVRSCZQKELMXYIHP <
```

Il compito del mittente è scrivere il messaggio, comunicare la parola cifrata e la chiave, ovvero l’ordine dei dischi.

```bash
7: < B NOZUTWDCVRJ L XKISEFAPMYGHQ < 1: < A XPLTDSRFHEN Y VUBMCQWOIKZGJ < 10:< R AMKGHIWPNYC J BFZDUSLOQXVET < 4: < N RPLDVHGFCUK T EBSXQYIZMJWAO < 2: < O ZWAXJGDLUBV I QHKYPNTCRMSFE < 6: < W AMKGHIPNYCJ B FZDRUSLOQXVET < 5: < K GWTHSPYBXIZ U LVMRAFDCEONJQ < 8: < X NOZUTWDCVRJ L KISEFAPMYGHBQ < 9: < W XPLTDSRFHEN Y VUBMCQAOIKZGJ < 3: < W UDNAJFBOTGV R SCZQKELMXYIHP <
```

Il mittente quindi comunicherà come chiave **7,1,10,4,2,6,5,8,9,3** e come parola cifrata **LYJTIBULYR**.

Il Wheel cypher, in questo caso, ha più dischi del necessario, veniva quindi inserito un padding con lettere random che non formavano nessun significato. 
Il destinatario avrà il compito di mettere i dischi nella giusta sequenza (la chiave) e di formare la parola crittata **LYJTIBULYR** in una delle colonne rimanenti, a quel punto era in grado di leggere il messaggio.

---

![La macchina Enigma](https://cdn-images-1.medium.com/max/1200/1*oPEthuxSMyNsY6rO6ZrrLQ.png)
*La macchina Enigma* **Enigma**, inventata nel 1918 di [Arthur Scherbius](https://it.wikipedia.org/wiki/Arthur_Scherbius), appariva come una macchina da scrivere ed era divisa in tre parti collegate tramite fili elettrici. 
- Una tastiera per scrivere il messaggio in chiaro 
- Un’unità di scambio (rotore) 
- Una parte formata da una serie di lampadine che illuminava la lettera cifrata. 
Il mittente per ottenere il testo cifrato, doveva semplicemente scrivere il testo in chiaro e ricopiare le lettere che si illuminavano grazie a degli impulsi elettrici.

Le lettere si illuminavano grazie ai collegamenti elettrici all’interno del rotore stesso.

![Rotore della macchina Enigma](https://cdn-images-1.medium.com/max/1200/1*QWJRBncDiKzOrvgMCkv7Kg.png)
*Rotore della macchina Enigma*

Una delle parti fondamentali della macchina **Enigma** erano i rotori, che possiamo immaginare come a degli ingranaggi, i quali potevano assumere 26 posizioni (lettere dell’alfabeto) e, ad ogni lettera premuta, il primo rotore faceva un “passo”, ovvero cambiava posizione.

Quando il primo rotore aveva compiuto 26 *passi,* era il secondo rotore che veniva spostato di una posizione.

Grazie a questo meccanismo **Enigma** era una macchina polialfabetica.

Solitamente era dotata di 3 rotori, i quali potevano assumere 26 posizioni ciascuna, fino ad arrivare ad avere un totale di 17576 posizioni ottenendo così 150 milioni di milioni di combinazioni. 
Enigma venne utilizzata durante la seconda guerra mondiale, e per sicurezza i tedeschi decisero di cambiare le chiavi di cifratura ogni giorno, in alcuni casi anche ogni 8 ore.

I soldati tedeschi ricevano insieme alla macchina Enigma anche un cifrario e un manuale di istruzioni.

Proprio grazie a delle fotografie di questi manuali che vendette [Hans Thilo Schmidt](https://en.wikipedia.org/wiki/Hans-Thilo_Schmidt) che Enigma cominciò a essere decodificata. 
Prima di utilizzare Enigma l’operatore doveva impostare la chiave di cifratura dei tre rotori attenendosi alla chiave giornaliera e posizionare gli spinotti frontali per la permutazione delle lettere.

![La chiave di Enigma](https://cdn-images-1.medium.com/max/1200/1*QQmXAVqr3cWYTPvZUKHVBg.png)
*La chiave di Enigma*

L’addetto alla decodifica, riceveva il messaggio crittato in [codice morse](https://it.wikipedia.org/wiki/Codice_Morse).

Una volta decodificato posizionava i rotori e la chiave nella stessa posizione del mittente.

Digitando quindi il codice crittato otteneva il messaggio in chiaro.

Per una dimostrazione consiglio questo video veramente ben fatto.

E pensare che la macchina fu inventata per scopi commerciali. 
Ancora una volta soffriamo della distribuzione delle chiavi, proprio come avviene nella crittografia simmetrica, risolta poi dalla crittografia asimmetrica utilizzata anche in **Bitcoin**.
