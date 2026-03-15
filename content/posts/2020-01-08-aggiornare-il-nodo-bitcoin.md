---
title: "Aggiornare il nodo Bitcoin"
date: 2020-01-08T10:00:00+01:00
slug: "aggiornare-il-nodo-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Versione 0.19.0.1"
cover: "/img/posts/aggiornare-il-nodo-bitcoin-1.webp"
tags:
  - "Bitcoin"
  - "Halving"
  - "Hash"
categories:
  - "Bitcoin"
---

---

### Aggiornare il nodo Bitcoin

#### Versione 0.19.0.1

Siamo all’inizio dell’Hanno 2020 (la H sta per Halving 😉) e tra i buoni propositi c’è sempre quello di fare un pò di pulizia, di aggiornare i software e di incrementare le nostre capacità.

Se avete seguito il nostro [tutorial per avere un nodo Raspberry](https://medium.com/@bitcoindallateoriallapratica/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f) e non avete ancora aggiornato il vostro nodo, avrete la versione 0.18.0 di Bitcoin Core.

A novembre 2019 è stato rilasciato l’aggiornamento [0.19.0.1](https://bitcoin.org/en/release/v0.19.0.1), che introduce dei miglioramenti a livello di performance, delle nuove chiamate RPC e rende deprecate delle altre.  
Tutti i changelogs sono presenti anche sul [repository ufficiale Github](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.19.0.1.md).

Ecco come abbiamo aggiornato il nostro Raspberry.

Per prima cosa ci colleghiamo in ssh.

```bash
$ ssh pi@192.168.1.221
```


dove **192.168.1.221** è il vostro IP locale, che potrebbe essere diverso dal nostro.

Ci spostiamo nella cartella download dell’utente pi.

```bash
$ cd /home/pi/download
```


e scarichiamo il nuovo Bitcoin core con il comando [wget](https://it.wikipedia.org/wiki/Wget)

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz
```


Scarichiamo anche le relative firme per verificare l’integrità del pacchetto.

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc$ wget https://bitcoin.org/laanwj-releases.asc
```


Effettuiamo la verifica come mostrato nel [tutorial iniziale del Raspberry](https://medium.com/@bitcoindallateoriallapratica/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f).

```bash
$ sha256sum --check SHA256SUMS.asc --ignore-missing

bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz: OKsha256sum: WARNING: 20 lines are improperly formatted
```


L’importante è che ci sia un bell’ **OK**!

Controlliamo anche le chiavi.

```python
$ gpg --import./laanwj-releases.asc$ gpg --refresh-keys$ gpg --verify SHA256SUMS.asc
```


risultato:

```sql
gpg: Good signature from “Wladimir J. van der Laan …”Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964
```


Benissimo, abbiamo scaricato quello che vogliamo. 
Non ci resta che decomprimere il pacchetto e spostarlo nella cartella bin, cosi da poter interagire globalmente, in quanto **/usr/local/bin** fa parte del [**$PATH**](http://www.linfo.org/path_env_var.html)

> PATH is an *environmental variable* in [Linux](http://www.linfo.org/linuxdef.html) and other [Unix-like](http://www.linfo.org/unix-like.html) [operating systems](http://www.linfo.org/operating_system.html) that tells the [*shell*](http://www.linfo.org/shell.html) which [directories](http://www.linfo.org/directory.html) to search for [*executable files*](http://www.linfo.org/executable.html)

```bash
$ echo $PATH

/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
```


quindi decomprimiamo e spostiamo il tutto.

```bash
$ tar -xvf bitcoin-0.19.0.1-arm-linux-gnueabihf.tar.gz$ sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-0.19.0.1/bin/*
```


Per verificare che tutto sia andato a buon fine, possiamo ottenere la versione di bitcoind con il comando

```bash
$ bitcoind -version

Bitcoin Core version v0.19.0.1
```


Siamo pronti a verificare le nuove chiamate RPC! 
Spostiamoci nell’utente bitcoin.

```bash
$ sudo su bitcoin
```


Per prima cosa stoppiamo il demone attualmente in esecuzione.

```bash
$ bitcoin-cli stop
```


Aspettiamo qualche secondo, dato che abbiamo impostato un [servizio](https://medium.com/@bitcoindallateoriallapratica/tutorial-fullnode-raspberry-bitcoin-blockchain-9c8de546657f) che rimette in esecuzione il demone se questo per qualche motivo dovesse interrompersi.

Proviamo quindi a lanciare un nuovo comando, ad esempio

```bash
$ bitcoin-cli getbalances
```


devo ottenere un risultato.

Ricordiamoci che con il comando

```bash
$ bitcoin-cli help
```


Possiamo ottenere tutti i comandi a nostra disposizione. 
Utilizziamo nuovamente l’utente **pi**, per pulire la cartella download.

```bash
$ exit$ rm -Rf /home/pi/download/*
```


Semplice no?

![Nodo Bitcoin dalla teoria alla pratica](/img/posts/aggiornare-il-nodo-bitcoin-1.webp)
*Nodo Bitcoin dalla teoria alla pratica*
