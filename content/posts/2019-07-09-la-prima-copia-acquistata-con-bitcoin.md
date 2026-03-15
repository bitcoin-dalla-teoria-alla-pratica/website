---
title: "La prima copia acquistata con bitcoin!"
date: 2019-07-09T10:00:00+01:00
slug: "la-prima-copia-acquistata-con-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Il libro Bitcoin dalla teoria alla pratica acquistato dal nostro sito con bitcoin."
images: ["https://cdn-images-1.medium.com/max/1200/1*-t5t4uBssgmP0vy_5UGBEQ.png"]
tags:
  - "Bitcoin"
  - "Transazioni"
  - "Wallet"
categories:
  - "Bitcoin"
---

---

### La prima copia acquistata con bitcoin!

#### Il [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica) acquistato dal nostro sito con bitcoin.

Ebbene sì, c’è stata la **prima** transazione verso il nostro wallet che gestisce le vendite del [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica) e del tascabile [Bitcoin 199 domande](/prodotti/bitcoin-199-domande/)!  
Un nostro lettore ha deciso di acquistare la propria copia tramite il sito [corsobitcoin.com](https://www.corsobitcoin.com/) e di usare come metodo di pagamento bitcoin!

Siamo molto orgogliosi che il nostro esperimento faccia parte del blocco [583867](https://blockchair.com/bitcoin/block/583867) e che questa txid [4f88f9fbfd390bb5553e5e177684a6c04f7f296b04c57794426a6894b3e2ea3c](http://4f88f9fbfd390bb5553e5e177684a6c04f7f296b04c57794426a6894b3e2ea3c) 
sia collegata al nostro libro! 
La transazione raw è:

```bash
0100000001cf27c205c39400338f196789ae1f14a25cd74716cf3117d148cff253900b64fb560000006a473044022051b08370e993235686aaeac47e746025f3f353c9b23f785920961d41d793148d02201315ad31fc1e153607b608dc24b5312a34e698e8e1c07280e884be06fb5423ab0121038477302e8c4d464005f851412d0c90c713ea7f7b33ead039f7651a32f8c16ff0ffffffff025cb603000000000016001427724d7c520ac6b0b58bac3d1afa7e5d9e051cee60200900000000001976a9148252e9cb9611bd58a2b44c4fbe2c67843a6dc0dd88ac00000000
```

![Esempio delvideo corsoe dellibro Bitcoin dalla teoria alla pratica](https://cdn-images-1.medium.com/max/1200/1*CCCJ5QkbFs7X-5L3hvjtag.png)
*Esempio delvideo corsoe dellibro Bitcoin dalla teoria alla pratica*

Il [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica) spiega come leggere ogni singolo byte della transazione. 
Ad esempio, nella raw transaction dell’acquisto del libro possiamo vedere quanti bitcoin sono stati spostati con alcune operazioni. 
Come?  
Prendiamo la porzione di byte di riferimento:

```bash
5cb6030000000000
```

Le operazioni da fare sono: 
- girare l’ordine dei byte 
- convertire in base 16 
- convertire nell’unità di misura bitcoin, cosi da confrontarla con il [block explorer](https://blockchair.com/bitcoin/transaction/4f88f9fbfd390bb5553e5e177684a6c04f7f296b04c57794426a6894b3e2ea3c) per avere una prova del nostro lavoro. 
Il risultato che dobbiamo ottenere è: 0.00243292 btc.

```bash
printf 5cb6030000000000 | tac -rs..
```

risultato: 
> **000000000003b65c** convertiamo in base16

```bash
echo "ibase=16; $(echo 0000000000061a80 | tr '[:lower:]' '[:upper:]') " | bc
```

risultato: 
> **243292** converto nell’unità di misura bitcoin.

```bash
echo “243292*10^-08” | bc -l
```

risultato: 
>. **00243292000000000000** Il risultato ottenuto corrisponde [all’explorer](https://blockchair.com/bitcoin/transaction/4f88f9fbfd390bb5553e5e177684a6c04f7f296b04c57794426a6894b3e2ea3c)!

La lettura della raw transaction fa parte dei capitoli transazioni del [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica). 
Adesso alla domanda ricorrente “Ragazzi ma che cosa ci compro con bitcoin?” abbiamo un’ottima risposta e con tanto di prova **immutabile** e **permanente**:)

Grazie! 🙏

---

![Immagine del libroBitcoin dalla teoria alla Pratica](https://cdn-images-1.medium.com/max/1200/1*-t5t4uBssgmP0vy_5UGBEQ.png)
*Immagine del libroBitcoin dalla teoria alla Pratica*
