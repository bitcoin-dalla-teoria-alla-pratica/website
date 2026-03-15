---
title: "Che cosa è lo scriptSig?"
date: 2020-07-15T10:00:00+01:00
slug: "che-cosa-lo-scriptsig"
draft: false
author: "Alessio Barnini"
description: "Video disponibile nel nostro canale Bitcoin in Action!"
cover: "/img/posts/che-cosa-lo-scriptsig-2.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

#### [Video disponibile nel nostro canale Bitcoin in Action!](https://www.youtube.com/BitcoinInAction)

![Che cosa è lo scriptSig?](/img/posts/che-cosa-lo-scriptsig-2.webp)
*Che cosa è lo scriptSig?*

Ciao,

Abbiamo ricevuto una domanda da parte di Luca, che ci chiede.

> In alcuni video avete parlato di scriptSig, che cosa è?

Bene Luca, lo **scriptSig** è parte della transazione di Bitcoin. 
Puoi immaginare la transazione **non SegWit** cosi strutturata.

![Immagine estratta dalvideocorsoe dal libroBitcoin dalla teoria alla pratica](/img/posts/che-cosa-lo-scriptsig-2.webp)
*Immagine estratta dalvideocorsoe dal libroBitcoin dalla teoria alla pratica*

- La versione della transazione
- Il numero di input
- L’input
- Il numero di output
- l’output
- e il locktime

Dove si posiziona lo **scriptSig**?  
Lo scriptSig è all’interno di ogni singolo input, e contiene gli elementi che andranno a soddisfare la UTXO di riferimento.

Attenzione, nelle transazioni Segwit native lo **scriptSig è vuoto**, risolvendo così la **transaction malleability e la scalabilità della rete Bitcoin**.

Per questo esempio utilizzeremo una transazione **legacy**, una **P2PKH** e analizzeremo nel dettaglio ogni singolo byte, vediamo come.

> In Action

Prendiamo una semplice transazione dalla blockchain [mainnet](https://btc.bitaps.com/c2297c9fefdd058e2ce5477868bcbf88bd4f860fbb552399053e3666687809bd).

```bash
$ bitcoin-cli getrawtransaction c2297c9fefdd058e2ce5477868bcbf88bd4f860fbb552399053e3666687809bd 2
```

La transazione contiene un input e due output. La nostra attenzione in questo momento ricade sull’input, all’interno dell’array vin

```bash
“vin”: [

{

“txid”: “d44cbca5911e53322e14fe0617f078dd1f162a7dcb97f83690eac285ed7ebe80”,

“vout”: 1,

“scriptSig”: {

“asm”: “3044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7[ALL] 04794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732”,

“hex”: “473044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7014104794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732”

},

“sequence”: 4294967295

}

],
```

Analizziamo quindi il suo hex, ovvero l’esadecimale. Questo è lo scriptSig e lo salviamo nella variabile d’ambiente SCRIPTSIG.

```bash
SCRIPTSIG=473044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7014104794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732
```

Dato che stiamo analizzando una transazione P2PKH, all’interno dello scriptSig ci aspettiamo la firma digitale e la chiave pubblica.

Dobbiamo conoscere leggermente il linguaggio script, ma per questo esempio vi basterà sapere che esistono delle costanti che ci indicano quanti caratteri esadecimali prendere successivamente.

Ad esempio 47, ricade esattamente nel range delle costanti.

```bash
$ echo $SCRIPTSIG | cut -c 1–2
```

Grazie al metodo cut riesco a prendere la porzione di byte di interesse

47 in base2 è 71, i quali rappresentano i byte.

Sappiamo che un byte può essere rappresentato da 2 caratteri esadecimali, 71*2 = 142.

Questo significa che dobbiamo considerare i 142 caratteri successivi all’esadecimale 47.

Ecco il calcolo da base 16 a base 2, e la moltiplicazione per due per conoscere i caratteri esadecimali da prendere in considerazione

```bash
$ expr `echo “ibase=16; $(printf 47)” | bc` “*” 2
```

Ed ecco la porzione di esadecimali che rappresentano la firma digitale.

```bash
$ echo $SCRIPTSIG | cut -c 3–142

3044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7

$ printf 3044022059515b358d938d04c812177a2eefba52a4427b9e807c28538148e04edf042f3b022057e00e46acec7708b3087bfaadf25001ff449759b063aa9f39f5eb6606ceeef7 | wc -c
```

Contando gli esadecimali estratti grazie al metodo wc notiamo che sono 140 e non 142, perchè?

Perchè il prossimo byte è il flag che indica come è stata firmata la transazione, solitamente SIGHASH_ALL rappresentato da 01

```bash
$ echo $SCRIPTSIG | cut -c 143–144

01
```

il prossimo byte cade nuovamente nel range delle costante di Bitcoin script

```bash
$ echo $SCRIPTSIG | cut -c 145–14641
```

e ci indica quanti esadecimali prendere in considerazione successivamente.

Ripeto l’operazione descritta poco fa

```bash
$ expr `echo “ibase=16; $(printf 41)” | bc` “*” 2

130
```

estraggo quindi la porzione di esadecimali indicata

```bash
$ echo $SCRIPTSIG | cut -c 147–277

04794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732
```

I seguenti byte sono la chiave pubblica necessaria per verificare la firma e per soddisfare la UTXO di riferimento.

Come?

Vediamo la UTXO grazie al metodo getrawtransaction

```bash
$ bitcoin-cli getrawtransaction d44cbca5911e53322e14fe0617f078dd1f162a7dcb97f83690eac285ed7ebe80 2
```

Alla seconda posizione dell’array troviamo la UTXO da sbloccare, questo lo sappiamo dal valore vout contenuto in vin.

Che cosa è quel valore dopo HASH160, ba716926b9313ca3bcf2791cf96a0f5f89472261?

È il digest della nostra chiave pubblica dopo aver applicato le funzioni crittografiche sha256 e ripemd160.

```bash
$ printf $(echo 04794dffa10783c305d72c44acc36003760a53c03a1e5529747a5ef7eef7c87c6c19ba26c7eee03ab6da9115d11bce3a46dd21aede86af19c3ee19eeb7f8d92732 | xxd -r -p | openssl sha256| sed ‘s/^.* //’) |xxd -r -p | openssl ripemd160 | sed ‘s/^.* //’
```

Lo script non confronterà solo l’hash della chiave pubblica ma anche la firma stessa.

Diciamo che la domanda che il protocollo Bitcoin si pone è:

- L’hash (HASH160) della chiave pubblica dello scriptSig è uguale all’hash della chiave pubblica contenuta nello **scriptPubKey** della UTXO?
- La firma può essere verificata con la chiave pubblica presente nello scriptSig?

Nel libro [**Bitcoin dalla teoria alla pratica**](https://amzn.to/2MOj1av) e nel [video corso](/prodotti/videocorso-teoria-pratica), analizziamo byte per byte la transazione P2PKH andando nel dettaglio della firma e studiando la convenzione DER

Bene abbiamo chiarito che cosa è lo scriptSig e dove si trova.

Spero che il video vi sia piaciuto, ciao e alla prossima
