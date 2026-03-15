---
title: "Bitcoin In Action — Come replicare gli esempi"
date: 2020-11-25T10:00:00+01:00
slug: "bitcoin-in-action-come-replicare-gli-esempi"
draft: false
author: "Alessio Barnini"
description: "Ciao, come sapete abbiamo rilasciato il nostro terzo libro — Bitcoin in Action, SegWit, Bitcoin script & smart contracts."
cover: "https://cdn-images-1.medium.com/max/1200/1*HKex9kyVdls9X3ItKtxVug.png"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "SegWit"
categories:
  - "Bitcoin"
---

---

### **Bitcoin In Action — Come replicare gli esempi** Ciao, come sapete abbiamo rilasciato il nostro terzo libro —[**Bitcoin in Action**,* SegWit, Bitcoin script & smart contracts*](https://amzn.to/3pJcXj1).

![Bitcoin In Action — SegWit, Bitcoin Script & Smart Contracts](https://cdn-images-1.medium.com/max/1200/1*HKex9kyVdls9X3ItKtxVug.png)
*Bitcoin In Action — SegWit, Bitcoin Script & Smart Contracts*

Come per il libro precedente — [Bitcoin dalla teoria alla pratica](https://amzn.to/2MOj1av) — abbiamo deciso di spiegare tutta la teoria utilizzando la pratica, così da facilitare l’utente alla comprensione della teoria stessa.

Questo video ha proprio questo obiettivo, preparare il nostro computer per seguire senza fatica il libro e replicare gli esempi.

Ecco quello che dobbiamo fare:

- Clonare il [repository](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book)
- Installare Bitcoin core
- Inserire nel $PATH il percorso delle utility del libro
- Installare [JQ](https://stedolan.github.io/jq/)
- Avere Python 3

Vediamo come!

> In Action

Al momento sto utilizzando un Mac, ma i passaggi sono molto simili anche per gli altri sistemi operativi.

Per prima cosa mi collego al repository [GitHub](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book) del libro ([https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book))

Apro quindi il terminale e mi posiziono nel percorso dove voglio clonare repository, nel mio caso in Documenti, e clono il repository sul mio computer.

```bash
$ git clone https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book.git
```

Mi sposto dentro la cartella appena clonata

```bash
$ cd Bitcoin-in-action-book/Capitolo\ 0
```

E installo Bitcoin-core.

Ovviamente se avete già un Bitcoin core installato potete utilizzare quello, oppure se volete installare ex-novo prestate attenzione alle vostre chiavi private.  
La versione che abbiamo utilizzato durante la realizzazione del libro è la 0.19.0.1.

Avvio quindi il file main.sh

```bash
$ sh main.sh
```

lo script scaricherà la versione di riferimento, effettuerà il controllo della firma [PGP](https://medium.com/@satoshiwantsyou/verifica-signature-bitcoin-core-pgp-628bee490767), e ci chiederà se spostare gli elementi appena scaricati in /usr/local/bin, percorso che solitamente fa parte del $PATH in modo tale da rendere il demone globale.

Ci viene quindi chiesta la password del nostro computer.

Una volta inserita, il software viene installato.

Potrebbe essere necessario installare PGP per il controllo delle chiavi.

Se non sai che cosa è PGP cerca il nostro articolo sul nostro sito [corsobitcoin.com](http://corsobitcoin.com) o il [nostro blog su Medium](https://medium.com/@satoshiwantsyou/verifica-signature-bitcoin-core-pgp-628bee490767).

Per verificare che tutto sia andato a buon fine, possiamo digitare:

```bash
$ bitcoind
```

In questo momento Bitcoin sta scaricando la mainnet. Fermiamo il demone con Ctrl-c.

Il secondo passaggio, non obbligatorio ma molto consigliato, è quello di creare un collegamento simbolico con la cartella datadir di Bitcoin e la directory appena creata.

Nel sistema operativo Mac Os, la cartella di default è salvata all’interno di Application Support, per gli altri sistemi operativi, fare riferimento a questo [link](https://en.bitcoin.it/wiki/Data_directory)

Questo è il comando che vado a effettuare:

```bash
$ ln -s $HOME/Library/Application\ Support/Bitcoin $HOME/Documents/Bitcoin-in-action-book
```

La sintassi per creare un collegamento simbolico è il seguente.

```bash
ln -s /path/to/original /path/to/link
```

$HOME invece è una variabile globale nei sistemi UNIX.

Per essere certi che tutto sia corretto, possiamo spostarci nella root del nostro progetto e digitare

```bash
$ ls -l
```

![Collegamento Simbolico con la Datadir di Bitcoin](https://cdn-images-1.medium.com/max/1200/1*9jRlhIJxuOXY4b5P-_MIkw.png)
*Collegamento Simbolico con la Datadir di Bitcoin*

L’ultimo passaggio è inserire nel $PATH la cartella Utility, la quale contiene delle utility appunto, necessarie per evitare di scrivere più e più volte lo stesso snippet di codice durante la pratica

Prima di tutto che cosa è il $PATH?

È una variabile d’ambiente che contiene tutti i percorsi dove la bash può cercare per trovare dei file eseguibili.

Lo abbiamo appena utilizzato per spostarci Bitcoin core, così da evitare di scrivere il percorso assoluto al momento dell’avvio.

Se noi eseguiamo

```bash
$ echo $PATH
```

Troviamo appunto tutte le cartelle dove la shell andrà a cercare per trovare l’eseguibile voluto.

Nei sistemi Mac Os, potete aggiungere il percorso assoluto nel file /etc/paths

```bash
sudo vim /etc/paths
```

Personalmente utilizzo zsh e lo aggiungo nel profilo di riferimento.

In rete troverete moltissimi tutorial per aggiungere un percorso al vostro $PATH.

Per prima cosa apro il file profile di zsh

```bash
$ vim ~/.zshrc
```

Se non utilizzate zsh, il file che dovete cercare è molto probabilmente .bash_profile, l’operazione è la medesima.

Aggiungiamo il nuovo elemento che vogliamo che sia presente nella variabile globale $PATH

```bash
export PATH="$HOME/Documents/Bitcoin-in-action-book/Utility:$PATH"
```

Salviamo il file e ricarichiamo la configurazione con il comando

```bash
$ source ~/.zshrc
```

oppure aprite una nuova finestra del terminale

Per essere sicuri che tutto sia andato a buon fine, possiamo verificare che il percorso faccia parte del $PATH

```bash
$ echo $PATH

/Users/barno/Documents/Bitcoin-in-action-book/Utility:/usr/local/sbin:/usr/local/opt/openssl@1.1/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/barno/.fzf/bin
```

Il percorso aggiunto deve far parte della variabile globale $PATH.

Come posso aver prova che tutto sia andato a buon fine?

Prova a eseguire questo comando:

```bash
$ sh hello.sh

Ciao barno! Divertiti con Bitcoin in Action
```

Ricevi questo messaggio? Bene allora tutto è andato a buon fine!

Altro elemento indispensabile [JQ](https://stedolan.github.io/jq/).  
Lo abbiamo utilizzato anche nel libro precedente, JQ è un Json Processor.

Per l’installazione fare riferimento al sito ufficiale [https://stedolan.github.io/jq/](https://stedolan.github.io/jq/).

Come spiegato nel video precedente, il libro non utilizza la mainnet o la testnet per replicare gli esempi, ma utilizza la regtest.

Dobbiamo quindi creare il file di configurazione per comunicare a Bitcoin core che vogliamo utilizzare tale ambiente.

Come spiegato nel libro Bitcoin dalla teoria alla pratica, possiamo utilizzare o i parametri da riga di comando quando avviamo il demone, oppure utilizzare un [file di configurazione](https://medium.com/@satoshiwantsyou/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353).

Noi preferiamo quest’ultima soluzione.

Creiamo quindi il file bitcoin.conf nella cartella Bitcoin all’interno del nostro progetto. Ecco perchè è comodo creare un collegamento simbolico

```bash
$ vi bitcoin.conf
```

ed inseriamo i seguenti valori

```bash
regtest=1

daemon=1

txindex=1

# Options only for mainnet

[main]

# Options only for testnet

[test]

# Options only for regtest

[regtest]
```

è tutto pronto per provare l’esempio del primo capitolo.

Spostiamoci quindi nel capitolo di riferimento, in questo caso Capitolo 1.

e avviamo il file tx_mall.sh

```bash
$ sh tx_mall.sh
```

Ops, otteniamo un pò di errori!

```bash
Make sure the bitcoind server is running and that you are connecting to the correct RPC port.

error: Could not connect to the server 127.0.0.1:18443
```

Semplice, il demone non è avviato!

Basterà quindi digitare

```bash
$ bitcoind
```

Bene, avviamo di nuovo l’esempio!

![Snapshot dell’esempio replicato.](https://cdn-images-1.medium.com/max/1200/1*yQaqUeCS35EthvSqs2Uj4w.png)
*Snapshot dell’esempio replicato.*

Benissimo l’esempio è stato replicato, i dettagli ovviamente sono descritti nel libro.

Se non avete clonato il repository nella cartella Documenti, potreste ricevere un errore.

Per replicarlo modifico il percorso del file, in tx_mall.sh, aggiungendo una S al mio percorso, così da ottenere l’errore

```bash
Error: Directory /Users/barno/Documents/Bitcoin-in-action-book/Bitcoins does not exist. Set $ABSOLUTE_PATH in tx_mall.sh before continue
```

Che cosa fare in questi casi?

O si clona il progetto in Documents, o prima di avviare l’esempio si modifica il percorso di $ABSOLUTE_PATH.

Tutto qui? NO!

è possibile debuggare lo script! Grazie a questo bellissimo [progetto](https://github.com/bitcoin-core/btcdeb) ([https://github.com/bitcoin-core/btcdeb](https://github.com/bitcoin-core/btcdeb)) è possibile verificare come una transazione viene validata.

Dopo aver seguito le istruzione descritte nel loro [repository](https://github.com/bitcoin-core/btcdeb), possiamo nuovamente avviare l’esempio passando come parametro debug.

```bash
$ sh tx_mall.sh debug
```

![Stack ottenuto con il parametro debug](https://cdn-images-1.medium.com/max/1200/1*DoNy93ODlmML1yxiwHTeog.png)
*Stack ottenuto con il parametro debug*

Non è obbligatorio aver installato [btcdeb](https://github.com/bitcoin-core/btcdeb), ma lo consigliamo, nonostante nel libro siano comunque riportati tutti gli stack. 
  
Complimenti, avete organizzato il vostro computer.

Per qualsiasi informazione, segnalazione e miglioria, fate riferimento al nostro repository GitHub [https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book](https://github.com/bitcoin-dalla-teoria-alla-pratica/Bitcoin-in-action-book), dove oltre alla possibilità di segnalare errori del libro, troverete le immagini ad alta risoluzione e le mappe mentali di ogni capitolo.

Il libro è disponibile su Amazon in formato cartaceo e digitale, e sul nostro sito [corsobitcoin.com](http://corsobitcoin.com) dove è possibile acquistare i nostri libri con bitcoin.

Ciao!
