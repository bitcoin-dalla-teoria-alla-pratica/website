---
title: "Come si utilizza un nodo
Bitcoin?"
date: 2020-06-03T10:00:00+01:00
slug: "come-si-utilizza-un-nodo-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Seguici sul canale youtube — Bitcoin in Action"
cover: "/img/posts/come-si-utilizza-un-nodo-bitcoin-1.webp"
tags:
  - "Bitcoin"
  - "Blockchain"
  - "Hash"
categories:
  - "Bitcoin"
---

---

### Come si utilizza un nodo 
Bitcoin?

#### Seguici sul canale youtube — [Bitcoin in Action](https://www.youtube.com/BitcoinInAction)

![](/img/posts/come-si-utilizza-un-nodo-bitcoin-1.webp)

Ciao,

Abbiamo ricevuto un pò domande dai lettori del nostro libro —[Bitcoin dalla teoria alla pratica](https://amzn.to/2Ldym0F) — e dagli studenti del nostro [video-corso](/prodotti/videocorso-teoria-pratica), dove ci chiedevano come avere a disposizione un nodo Bitcoin.

Abbiamo quindi deciso di risponderli tramite il nostro canale.

Durante l’installazione utilizzeremo la verifica delle chiavi GPG così da essere sicuri di aver scaricato il pacchetto voluto.

Personalmente utilizzo Mac Os, quindi la cartella destinata alla blockchain è di default è all’interno di Application Support.

Windows e Linux utilizzano un‘altro percorso, consultabile [https://en.bitcoin.it/wiki/Data_directory](https://en.bitcoin.it/wiki/Data_directory).

> In Action

Per prima cosa dobbiamo scaricare il software Bitcoin core.

Personalmente non amo l’interfaccia grafica, quindi scarichiamo direttamente il bin dall’indirizzo [https://bitcoincore.org/bin/](https://bitcoincore.org/bin/).

Copio il link e utilizzo wget per scaricare il pacchetto.

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.1/bitcoin-0.19.1-osx64.tar.gz
```

Utilizzo wget perchè il vostro nodo potrebbe essere su un raspberry senza interfaccia grafica.

Scarico anche le relative firme per verificare l’integrità del pacchetto.

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.1/SHA256SUMS.asc$ wget https://bitcoin.org/laanwj-releases.asc
```

Verifichiamo l’integrità del pacchetto

```bash
$ sha256sum — check SHA256SUMS.asc — ignore-missing
```

Con il comando **shasum** verifichiamo l’integrità e l’autenticità del file controllando il suo **checksum** creato con l’algoritmo SHA.

Controlliamo anche le chiavi.

```python
$ gpg — import./laanwj-releases.asc$ gpg — refresh-keys$ gpg — verify SHA256SUMS.asc
```

```sql
gpg: Good signature from “Wladimir J. van der Laan …”

Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964
```

Il controllo della firma è andato a buon fine e sappiamo di aver scaricato il file voluto.

Per i più curiosi [questo](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-June/009045.html) è il messaggio in mailing list “bitcoin dev” dove si comunicava quale sarebbe stata la fingerprint della chiave PGP utilizzata per le successive release dalla versione 0.11.0rc3.

Possiamo finalmente installarlo.

```bash
$ tar -xvf bitcoin-0.19.1-osx64.tar.gz
```

Decomprimiamo l’archivio e spostiamo i file bin all’interno di /usr/local/bin cosi da renderlo globale.

```bash
$ mv bitcoin-0.19.1/bin/* /usr/local/bin
```

Se utilizzate un raspberry, il comando potrebbe è quello riportato qui sotto

```bash
$ sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-0.19.1/bin/*
``` **/usr/local/bin** deve far parte del $PATH. Il Path nei sistemi UNIX comunica in quali cartelle cercare dei file eseguibili

Per verificare che tutto sia andato a buon fine, possiamo eseguire il comando

```bash
$ bitcoind --version
```

Se adesso lanciamo il demone, ovvero bitcoind, inizierà la sincronizzazione con la mainnet, e la datadir sarà posizionata all’interno Application support, proprio perchè io sto usando macOS

```bash
$ cd /Users/$USER/Library/Application\ Support/Bitcoin
```

Se il vostro obiettivo è fare delle prove con il protocollo, vi consiglio di utilizzare la regtest.

Per far questo o passate come opzione -regtest al demone, o più comodamente create un file bitcoin.conf all’interno della cartella di default.

```bash
regtest=1txindex=1
```

regtest=1 indica che di default voglio usare la regtest senza doverla specificare.  
txindex=1 che voglio che tutte le transazione siano indicizzate.

Per avere una lista completa delle opzioni è possibile utilizzare

```bash
$ bitcoind --help
```

possiamo nuovamente accendere il demone.

Verifichiamo l’ambiente con la chiamata

```bash
$ bitcoin-cli getblockchaininfo

{

“chain”: “regtest”,

…}
```

Abbiamo tutto a disposizione per utilizzare il nostro nodo.

Abbiamo visto come ottenere un nodo bitcoin e come interagirci per iniziare a prendere confidenza con il protocollo.

In descrizione trovate il nostro link a [Github](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-Action) e un articolo scritto da noi sul nostro sito per installarlo su un raspberry.

Ciao alla prossima
