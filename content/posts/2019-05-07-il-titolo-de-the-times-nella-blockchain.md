---
title: "Il titolo de “The Times” nella blockchain."
date: 2019-05-07T10:00:00+01:00
slug: "il-titolo-de-the-times-nella-blockchain"
draft: false
author: "Alessio Barnini"
description: "Abbiamo spesso sentito che un titolo del celebre giornale “The Times” è inserito dentro la blockchain Bitcoin."
cover: "/img/posts/il-titolo-de-the-times-nella-blockchain-1.jpg"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Hash"
categories:
  - "Bitcoin"
---

---

### Il titolo de “The Times” nella blockchain Bitcoin.

Abbiamo spesso sentito che un titolo del celebre giornale “The Times” è inserito dentro la blockchain **Bitcoin**.

Ma esattamente dove è inserito?  
Come è stato possibile?

È una storia romantica se vogliamo, infatti **Satoshi Nakamoto**, il creatore di **Bitcoin**, ha lasciato un messaggio nel blocco genesi della blockchain Bitcoin.

Il blocco genesi è il primo blocco della blockchain, ed è *hardcodato* cioè inserito manualmente.

All’interno della **coinbase** possiamo leggere la famosa frase.

> 04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73

Tale frase ha un duplice significato, testimoniare la data del primo blocco, e la nascita di un nuovo sistema monetario indipendente.

Ma che cosa c’è scritto in questo esadecimale?  
Come è possibile recuperarlo ed interpretarlo? 
Utilizzando il comando **RPC** getblock e l’hash del blocco genesi, richiedendo un risultato più verboso aggiungendo 2 in fondo.

Analizzando l’output ottenuto, possiamo leggere **coinbase**, seguito dal suo valore in esadecimale.

Adesso possiamo convertire l’esadecimale in ASCII.

Ottenendo così il titolo de “The Times” del 3 gennaio 2009.

![Il Titolo De The Times Nella Blockchain](/img/posts/il-titolo-de-the-times-nella-blockchain-1.jpg)
