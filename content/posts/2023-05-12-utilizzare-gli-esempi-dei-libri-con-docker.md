---
title: "Utilizzare gli esempi dei libri con Docker"
date: 2023-05-12T10:00:00+01:00
slug: "utilizzare-gli-esempi-dei-libri-con-docker"
draft: false
author: "Alessio Barnini"
description: "Ciao a tutti,
abbiamo pensato di creare un repository per facilitare gli esempi che troviamo nei due nostri libri, Bicoin dalla teoria alla…"
cover: "https://cdn-images-1.medium.com/max/1200/1*1hBErngCdIgVlHtojL1r4w.png"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Nodi"
categories:
  - "Bitcoin"
---

---

### Utilizzare gli esempi dei libri con Docker

Ciao a tutti, 
abbiamo pensato di creare un **repository per facilitare** gli esempi che troviamo nei due nostri libri, [Bicoin dalla teoria alla pratica](https://amzn.to/2MOj1av) e [Bitcoin in Action](https://amzn.to/3pJcXj1).

Per questo andremo ad utilizzare Docker!

![Il nostro Repositoryhttps://github.com/bitcoin-dalla-teoria-alla-pratica/Docker-bitcoin](https://cdn-images-1.medium.com/max/1200/1*1hBErngCdIgVlHtojL1r4w.png)
*Il nostro Repositoryhttps://github.com/bitcoin-dalla-teoria-alla-pratica/Docker-bitcoin*

#### Che cosa è Docker?

> Docker è una piattaforma open source per la creazione, distribuzione e gestione di applicazioni in container. I container Docker sono degli ambienti virtuali isolati che includono tutto il necessario per eseguire un’applicazione, tra cui il codice, le librerie e le dipendenze.

Abbiamo quindi creato un’immagine docker che contiene **tutto quello necessario**, dall’installazione del nodo (ad oggi versione 24.0) la verifica dell’integrità del pacchetto e il nostro caro debugger [btcdeb](https://github.com/bitcoin-core/btcdeb)!

A [questo indirizzo](https://github.com/bitcoin-dalla-teoria-alla-pratica/Docker-bitcoin) è possibile verificare come è stata creata l’immagine che andremo ad utilizzare e le istruzioni necessarie per interagire con gli esempi del libro.

---

In Action!

Per prima cosa sarà necessario installare [Docker](https://www.docker.com/) nel proprio computer.

Successivamente cloniamo i repository necessari.

```bash
git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/Docker-bitcoin.git --depth 1cd Docker-bitcoin
```

Cloniamo quindi gli esempi dei libri.

```bash
git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi.git --depth 1 &&git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book.git --depth 1
```

A questo punto non ci resta che avviare docker con

```bash
docker-compose up
```

> Il comando `docker-compose up` viene utilizzato per avviare i container specificati in un file di configurazione `docker-compose.yml`.

Appena avviato il container leggeremo tutti i log, assicurarsi che il nodo stia utilizzando la rete regtest! Come? se vedere che sta scaricando dei blocchi dalla rete significa che qualcosa è andato storto!

Apriamo quindi un altro terminale, e digitiamo

```bash
docker ps
```

Il quale restituisce tutti i container che sono in esecuzione. Questo è di vitale importanza, perchè dobbiamo “entrare” all’interno del container ed eseguire l’esempi del libro.

Questo è il risultato che ottengo utilizzando `docker ps`

```bash
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMESf693d16b1961 docker-bitcoin-bitcoin-in-action "/entrypoint.sh" 2 hours ago Up 2 hours 0.0.0.0:18443-18444->18443-18444/tcp docker-bitcoin-bitcoin-in-action-1
```

Entro quindi dentro il container

```bash
docker exec -it docker-bitcoin-bitcoin-in-action-1 zsh
```

Immaginiamo di voler eseguire l’esempio del Capitolo 3.

```bash
cd Bitcoin-in-action-bookcd Capitolo\ 3cd P2SH\ -\ P2PK./main.sh
```

Se vogliamo eseguire l’esempio utilizzando il debug, niente di più facile, sarà necessario passare il parametro DEBUG=1

```bash
./main.sh DEBUG
```

e btcdeb sarà attivato!

---

![](https://cdn-images-1.medium.com/max/1200/0*cDXJsJpPljxYbQAo.jpeg)



