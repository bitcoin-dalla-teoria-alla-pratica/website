---
title: "Che cosa è la Proof of work? Come si mina un blocco?"
date: 2020-06-24T10:00:00+01:00
slug: "che-cosa-la-proof-of-work-come-si-mina-un-blocco"
draft: false
author: "Alessio Barnini"
description: "Video completo su Bitcoin in Action!"
images: ["https://cdn-images-1.medium.com/max/2560/1*Uy45T1_19bYs4zh6DG6quw.png"]
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Che cosa è la Proof of work? Come si mina un blocco?

#### Video completo su [Bitcoin in Action](https://youtu.be/XEMpnRrL6S4)!

![Video completo suBitcoin in Action!](https://cdn-images-1.medium.com/max/2560/1*Uy45T1_19bYs4zh6DG6quw.png)
*Video completo suBitcoin in Action!*

Ciao,

siamo orgogliosi di aver ricevuto la prima domanda da una donna! Infatti Eli ci domanda:

Che cosa è la proof of work? Come si mina un blocco?

La risposta a questa domanda non è banale.

Andando per gradi, la Proof of work, denominata PoW è l’algoritmo di consenso utilizzato in Bitcoin, è necessario per validare i blocchi e mettere in sicurezza la blockchain.

Puoi immaginare la PoW come una competizione tra miners. I miners sono nodi che cercano di risolvere un problema matematico.

Combinando degli elementi del blocco, devono trovare un numero minore di una soglia stabilita dal protocollo Bitcoin.

Per trovarlo vengono effettuate moltissime prove utilizzando l’algoritmo SHA256. [Come spiegato nel video inerente all’algoritmo SHA256](https://youtu.be/oooUGOTfVx0), se l’input della della funzione crittografica è lo stesso, otterremo sempre lo stesso digest.

Ecco perchè si utilizza un parametro random da utilizzare solo una volta durante il calcolo della PoW per cercare di ottenere un digest sotto la soglia.

Questo parametro prende il nome di nonce.

Quando la soluzione viene trovata è presentata alla rete, la quale la verifica e dà il proprio consenso.

Il consenso da parte della rete è sotto forma di accettazione ed inoltro del blocco minato.

In caso di mancato consenso il blocco verra’ scartato e non inoltrato.

Questo procedimento è fatto da ogni nodo, arrivando a un consenso “globale” tramite il consenso emergente, appunto.

Il miner sarà poi premiato per il suo sforzo computazionale nel trovare la risposta al problema.

Tale premio prende il nome di reward, il quale ad oggi è di 6,25 bitcoins a blocco più tutte le fees di ogni transazione che ha inserito nel blocco stesso.

Tale reward si dimezza ogni 210.000 blocchi, all’incirca 4 anni come spiegato nel video relativo [all’halving](https://youtu.be/nFrN-jROnMI).

La soglia di difficoltà viene aggiustata ogni 2016 blocchi, all’incirca 2 settimane.

Vediamo con un esempio come è stato minato un blocco passato.

> In Action

Utilizzeremo il blocco [1773164](https://tbtc.bitaps.com/1773164).

Recuperiamo il suo hash con la chiamata getblockhash, e le sue informazioni con la chiamate getblock.

Utilizzeremo le sottoshell per fare una chiamata unica.

```bash
$ bitcoin-cli getblock $(bitcoin-cli getblockhash 1773164)

{

“hash”: “00000000000000eb74d096b83594d770f23d633e3a8b08813763489fbde7a0ef”,

“confirmations”: 2,

“strippedsize”: 1704,

“size”: 2722,

“weight”: 7834,

“height”: 1773164,

“version”: 545259520,

“versionHex”: “20800000”,

“merkleroot”: “75870dd46a503862af6fcf700be5e02e008db4521d96713bda51607ed05e2a18”,

“tx”: [

“5e68fb0018f65216db1f559437705350934451da086c0bc3e4073c0f2b8df4cc”,

“64b3ceadb693d33be7cdc4233c4607d77d37effcf426c9ce75146bfb269a93dd”,

“8f4ce2cfa530a5f3912d2c75be3b4d018da18037a68c6b2fac0415d09bdd39b3”,

“9d67968905df317779d3c92b7e052fae96020ccbc68d3f77d40bca0f2e50449d”,

“4684cbc6831af10960835cd0c10831a23eb90e736dab9e96229e45828ded2760”,

“6f66bcfab129e6d3a5b18e3e9554d54178b415cb54ecf82e350cc24d63209eff”,

“fc874f84759c9c4944037af4b3be02efd03c6436ebc8b8571519658de1e5580a”,

“6d11edc6b84444206dd97f9924e8ca6b273b0bce9ea58218590a275a64da740a”,

“370151706116ba9ae7bff77d9244a6a3e5401aadb43de221bf3f804386724c4d”,

“5d6c8801705493612138d3addfb0b0b5a49cc5177b5f2cee370d4b765d3e37b2”

],

“time”: 1592919152,

“mediantime”: 1592917919,

“nonce”: 3940145976,

“bits”: “1a01a5f2”,

“difficulty”: 10178811.40698772,

“chainwork”: “000000000000000000000000000000000000000000000160b51965fab057015d”,

“nTx”: 10,

“previousblockhash”: “00000000000001249b9a4e000135acecec2dcd7385eba54639ff962f3883e861”,

“nextblockhash”: “0000000000000171c5c04355788d2531b349b55c6189e2e3719d2b5c82fa2026”

}
```

Come vedete il blocco contiene un pò di informazioni, ma non tutte sono utilizzate per provare a vincere la corsa del Pow.

Il miner ha dovuto trovare un numero minore di quello riportato in bits.

Il **bits** è la rappresentazione compressa del target del candidate block.

Il candidate block è il blocco che il miner utilizza per effettuare le sue prove e vincere il proof of work al fine di inserirlo nella blockchain.

Con il metodo getblocktemplate è possibile recuperare il candidate block attuale.

```bash
$ bitcoin-cli getblocktemplate ‘{“rules”: [“segwit”]}’
```

E per trovare il target attuale è possibile filtrare il risultato con l’aiuto della libreria jq

```bash
$ bitcoin-cli getblocktemplate ‘{“rules”: [“segwit”]}’ | jq -r ‘.target’

00000000000001a5f20000000000000000000000000000000000000000000000
```

In questo momento il miner deve trovare un numero che deve stare sotto all’esadecimale appena estratto.

Noi però, non essendo miner, replicheremo il lavoro che il miner ha fatto sul blocco che abbiamo scelto. I valori che il miner utilizza sono:

- Version hex
- Previousblockhash
- merkleroot
- time
- bits
- nonce

Per comodità utilizziamo delle variabili d’ambiente per salvare il loro valore.

Salviamo nella variabile d’ambiente ver, il versionhex nella sua rappresentazione little endian.

```bash
$ ver=`printf 20800000 | tac -rs..| tr -d ‘\n’`
```

Salviamo nella variabile d’ambiente prev, il previous blockhash nella sua rappresentazione little endian.

```bash
$ prev=`printf 00000000000001249b9a4e000135acecec2dcd7385eba54639ff962f3883e861 | tac -rs.. | tr -d ‘\n’`
```

Salviamo nella variabile d’ambiente mkl, il merkle root hash nella sua rappresentazione little endian.

```bash
$ mkl=`printf 75870dd46a503862af6fcf700be5e02e008db4521d96713bda51607ed05e2a18 | tac -rs.. | tr -d ‘\n’`
```

Salviamo nella variabile d’ambiente time, il time nella sua rappresentazione esadecimale e little endian.

```bash
$ time=`printf ‘%x\n’ 1592919152 | tac -rs.. | tr -d ‘\n’`
```

Salviamo nella variabile d’ambiente bits, il bits nella sua rappresentazione little endian.

```bash
$ bits=`echo 1a01a5f2 | tac -rs.. | tr -d ‘\n’`
```

Salviamo nella variabile d’ambiente nonce, il nonce nella sua rappresentazione esadecimale e little endian.

```bash
$ nonce=`printf ‘%x\n’ 3940145976 | tac -rs.. | tr -d ‘\n’`
```

Otteniamo quindi il digest della concatenazione dei valori che abbiamo salvato nelle variabili d’ambiente, applicando per due volte la funzione crittografica SHA256

```bash
$ printf $ver$prev$mkl$time$bits$nonce | xxd -r -p | sha256sum -b | xxd -r -p | sha256sum -b
```

Otteniamo quindi la sua rappresentazione in little endian

```bash
$ printf efa0e7bd9f48633781088b3a3e633df270d79435b896d074eb00000000000000 | tac -rs..

00000000000000eb74d096b83594d770f23d633e3a8b08813763489fbde7a0ef
```

Il risultato ottenuto è il numero che soddisfava la difficoltà dell’epoca. Come facciamo ad esserne sicuri? Convertiamo in base 10 sia l’hash ottenuto che il bits.

Per ottenere il Bits in base 10 è necessario dividerlo in due parti, rispettivamente coefficiente ed esponente.

Dato il bits:

```bash
1a01a5f2
```

il coefficiente è 0x1a il quale ci comunica la lunghezza dell’esponente.

In questo caso 26 byte, perchè 1a in base 10 è 26.

```bash
$ echo ‘ibase=16; 1A’ | bc

26
```

Il coefficiente è la parte rimanente del bits, ovvero 01a5f2.

Dobbiamo quindi avere una stringa lunga 52 caratteri esadecimali compreso l’esponente.  
 Ricorda che 1byte può essere rappresentato da due caratteri esadecimali.

Otteniamo quindi

```bash
01a5f20000000000000000000000000000000000000000000000
```

Verifichiamo di aver scritto la lunghezza giusta

```bash
$ printf 01a5f20000000000000000000000000000000000000000000000 | wc -c

52
```

Ottimo, convertiamolo in base 10 e salviamolo nella variabile d’ambiente BITS_10

```bash
$ BITS_10=”$(echo “obase=10; ibase=16; -u; $(echo 01a5f20000000000000000000000000000000000000000000000 | tr ‘[:lower:]’ ‘[:upper:]’)” |bc | sed -n 2p)”
```

Esaminiamo il risultato ottenuto

```bash
$ echo $BITS_10

2648593653332025323234430866859553558338063400000453437554688
```

Convertiamo in base 10 anche l’hash ottenuto precedentemente e salviamolo nella variabile d’ambiente TARGET.

```bash
$ TARGET=”$(echo “obase=10; ibase=16; -u; $(echo 00000000000000eb74d096b83594d770f23d633e3a8b08813763489fbde7a0ef | tr ‘[:lower:]’ ‘[:upper:]’)” |bc | sed -n 2p)”
```

Adesso $TARGET deve essere minore di $BITS_10, ovvero della difficoltà imposta dal protocollo in quel momento storico.

```bash
$ echo “$TARGET<$BITS_10”|bc

1
```

Otteniamo come risultato 1, quindi true, il miner ha risolto con successo il problema matematico.

Come fa la rete a replicare il risultato? È molto semplice, sapendo i parametri, in particolar modo il nonce, verifica che il risultato sia corretto.

Se, parametri differenti restituiscono lo stesso risultato, come detto nel video riguardante lo [SHA256](https://youtu.be/oooUGOTfVx0), siamo di fronte ad una collisione.

I più attenti avranno notato che il risultato ottenuto è l’hash del blocco.

```bash
$ test 00000000000000eb74d096b83594d770f23d633e3a8b08813763489fbde7a0ef = $(bitcoin-cli getblockhash 1773164) && echo sono uguali || echo sono diversi
```

Sono uguali!

Il codice utilizzato è disponibile nel nostro repository GitHub.

Con questo video un pò più tecnico abbiamo cercato di dimostrare che cosa un miner esegue per creare un blocco, e mettere in sicurezza la blockchain, ma come potete immaginare è un argomento molto ampio e non è sufficiente un video di pochi minuti per analizzare in maniera dettagliata ogni singola sfumatura.

L’argomento invece è approfondito nel nostro libro e corso, trovate i link nella descrizione del video.

Spero però di aver risposta alla tua domanda!

Ciao alla prossima
