---
title: "Dove posso leggere il famoso titolo de The Times?"
date: 2020-05-13T10:00:00+01:00
slug: "dove-posso-leggere-il-famoso-titolo-de-the-times"
draft: false
author: "Alessio Barnini"
description: "Seguici sul canale youtube — Bitcoin in Action"
images: ["https://cdn-images-1.medium.com/max/1200/1*eMz70QEkdqz4elk9WnzdaA.png"]
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Genesis Block"
categories:
  - "Bitcoin"
---

---

### **Dove posso leggere il famoso titolo de The Times**? #### Seguici su [Bitcoin in Action](https://www.youtube.com/BitcoinInAction?sub_confirmation=1).

Oggi rispondo a una domanda che mi ha fatto Alberto che chiede: *Il primo blocco generato da Bitcoin è collegato a un famoso titolo del giornale * ***The Times** * *, testimoniando anche la data della sua nascita.

La pagina è dentro la blockchain*?

Bene Alberto, il primo blocco di Bitcoin, chiamato **blocco genesi**, è stato generato il 3 Gennaio 2009.

Nello stesso giorno nella prima pagina del Times potevamo leggere “ **Chancellor on brink of second bailout for banks** ”, che in italiano potremmo tradurre come “Il Cancelliere ipotizza un secondo salvataggio per le banche” dato che eravamo in piena crisi finanziaria.

Titolo molto azzeccato per far conoscere al mondo **Bitcoin**. **Sì, il titolo del Times è contenuto dentro la blockchain, ma non l’intera pagina**.

Più precisamente lo possiamo leggere nella coinbase del genesis block, quindi al blocco numero 0.

La tua domanda ha un ottimo timing, perchè proprio ieri, l’11 maggio 2020 in occasione del terzo **halving** c’è stato un messaggio molto simile.

Vediamoli con un esempio.

---

Sappiamo che il messaggio è stato inserito nel blocco genesi, quindi nel primo blocco della blockchain.

Possiamo identificare il blocco o tramite la sua altezza o tramite il suo hash, in questo caso la sua altezza sarà 0, dato che è il primo.

```bash
bitcoin-cli getblockhash 0
```

Quindi utilizziamo la chiamata getblockhash e otteniamo il suo hash.

Adesso che abbiamo il suo hash possiamo ottenere più dettagli con la chiamata **getblock**. ```bash
bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

Nell’array tx vediamo che c’è una sola transazione, cerchiamo di ottenere più informazioni con la chiamata **getrawtransaction**.

```bash
bitcoin-cli getrawtransaction 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b 2
```

Questa chiamata restituisce un errore, essendo una transazione particolare.

Il metodo getblock mi permette di esplorare il blocco ancora più a fondo, per conoscere i parametri che accetta la chiamata è possibile utilizzare **help prima del comando** Utilizziamo quindi nuovamente la chiamata getblock chiedendo un risultato più verboso, aggiungendo il numero 2.

```bash
bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 2
```

Abbiamo la possibilità di leggere l’esadecimale della coinbase, convertiamolo in ASCII usando il comando xxd.

```bash
echo 04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73 | xxd -r -p
```

Il risultato che otteniamo è il titolo del Times con tanto di data.

---

Proprio ieri, 11 maggio 2020 è avvenuto l’halving e la comunità Bitcoin ci ha deliziato con un altro messaggio. Utilizzando un qualsiasi explorer possiamo leggere il messaggio lasciato dal miner. Dove è scritto nella blockchain? Esattamente come il titolo del the times, il messaggio è nella coinbase, cerchiamo di estrarlo

Recuperiamo l’hash del blocco

```bash
bitcoin-cli getblockhash 629999
```

Una volta ottenuto l’hash del blocco, utilizziamo la chiamata getblock 
con l’hash appena ottenuto

```bash
bitcoin-cli getblock 0000000000000000000d656be18bb095db1b23bd797266b0ac3ba720b1962b1e
```

Recuperiamo la prima transazione, che sappiamo essere sempre la coinbase, utilizziamo la chiamata getrawtransaction richiedendo un risultato più verboso

```bash
bitcoin-cli getrawtransaction aed3754889f65dff83504fd0a8b78e1b69fc22c5396c67df23b0e607bf4e0d67 2 |jq
```

identifichiamo quindi la coinbase e convertiamo l’esadecimale in Ascii con il comando usato precedentemente

```bash
$ printf 03ef9c0952f09f909f4e5954696d65732030392f4170722f3230323020576974682024322e335420496e6a656374696f6e2c20466564277320506c616e2046617220457863656564732032303038205265736375652020144d696e6564200500ba5e4800 | xxd -r -p

? R🐟NYTimes 09/Apr/2020 With $2.3T Injection, Fed’s Plan Far Exceeds 2008 Rescue Mined?^H
```

Ecco il messaggio che ogni full node possiede all’interno del proprio hard-disk. È un chiaro riferimento a un sistema economico fallimentare. Si potrebbe tradurre così: Con un’iniezione di 2.3 trilioni di dollari, il piano della FED supera di molto il salvataggio del 2008

---

Abbiamo quindi visto come sia possibile scrivere dei messaggi nella blockchain, anche se non è l’unico modo. Con il passare degli anni ci sono stati degli aggiornamenti che permettono di inserire messaggi in modi differenti. Anche questo esempio è possibile scaricarlo dal nostro repository [**GitHub**](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action).

Abbiamo utilizzato [#IPFS](https://www.youtube.com/results?search_query=%23IPFS) per salvare le due pagine storiche: [https://bit.ly/3fJTYzN](https://bit.ly/3fJTYzN)

Ciao alla prossima

![A destra il titolo storico del The Times — a sinistra Il giornale 10 anni dopo.](https://cdn-images-1.medium.com/max/1200/1*eMz70QEkdqz4elk9WnzdaA.png)
*A destra il titolo storico del The Times — a sinistra Il giornale 10 anni dopo.*
