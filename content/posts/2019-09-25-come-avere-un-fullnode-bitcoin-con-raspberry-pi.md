---
title: "Come avere un Fullnode Bitcoin con Raspberry Pi"
date: 2019-09-25T10:00:00+01:00
slug: "come-avere-un-fullnode-bitcoin-con-raspberry-pi"
draft: false
author: "Alessio Barnini"
description: "Un lampone decentralizzato"
images: ["https://cdn-images-1.medium.com/max/1200/1*zd6R6cKGNZFDOJjB2TEFGg.png"]
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Blockchain"
categories:
  - "Bitcoin"
---

---

#### Un lampone decentralizzato

Nel libro [Bitcoin dalla teoria alla pratica](https://www.amazon.it/Bitcoin-Dalla-teoria-alla-pratica/dp/B07SNNNL2P/) viene utilizzato un fullnode concesso gentilmente da [Growbit](https://log.growbit.xyz/tagged/blockchain), ma non è pubblico.

Diamo come alternativa [chainquery](https://chainquery.com/) per fare determinate operazioni ma non è sufficiente a coprire tutti gli esempi che sono riportati.

Abbiamo quindi deciso di scrivere una guida per costruire e interagire con un proprio nodo Raspberry.

Ovviamente il nodo può *vivere* anche nel vostro computer che solitamente usate, ma dovrebbe stare sempre connessi per essere up-to-date con la blockchain e dedicare un pò di spazio per il salvataggio della blockchain.  
Oggi 2 Agosto 2018 la testnet *pesa circa 25 *gigabytes.

![](https://cdn-images-1.medium.com/max/1200/1*yeB6nWHogv4zjyYi8vUvsw.png)

A questo [indirizzo](https://bitinfocharts.com/) potete trovare informazioni interessanti per la mainnet, e a oggi sono all’incirca 270 gigabytes.

#### **Componenti** I componenti che ho usato non sono miei, quindi non ho nessun interesse a pubblicizzarli. Elenco semplicemente il mio setup.

- [Raspberry Pi 3 B+](https://www.amazon.it/Raspberry-Modello-Piastra-base-verde/dp/B07BFH96M3/ref=sr_1_7?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=Raspberry+Pi+b%2B&qid=1564738413&s=gateway&sr=8-7)
- [MicroSd 16 gigabytes](https://www.amazon.it/Kingston-SDCS-16GB-Velocit%C3%A0-Adattatore/dp/B079H6PDCK/ref=asc_df_B079H6PDCK/?tag=googshopit-21&linkCode=df0&hvadid=85509081743&hvpos=1o2&hvnetw=g&hvrand=5967796253327298423&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1008664&hvtargid=pla-429048381826&psc=1)
- [Custodia, alimentatore, ventole, dissipatore](https://www.amazon.it/gp/product/B07CB7P1RD/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)(kit)
- [Hard disk esterno USB 3.0](https://www.amazon.it/gp/product/B00CRZ2PRM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (anche se il Raspberry in questione ha le porte USB 2.0)
- [Cavo ethernet categoria 8](https://www.amazon.it/gp/product/B07G8XY9SZ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (un cavo categoria 5 può arrivare a una velocità di 1 gigabit per secondo)

Invito chiunque a indicare un setup migliore del mio se è necessario :)

![Setup finale: Raspberry + case + alimentatore + HDD +tappetino](https://cdn-images-1.medium.com/max/1200/1*DoX5T6trmF1hmUZRDj1hDg.png)
*Setup finale: Raspberry + case + alimentatore + HDD +tappetino*

Benissimo appena costruito il nostro dispositivo scarichiamo il software necessario.

#### Scaricare Raspberry Lite Image

Dal [sito](https://www.raspberrypi.org/software/operating-systems/) ufficiale scarica l’immagine lite. 
Come vedete nel sito abbiamo lo SHA256 dello zip, che nel mio caso è

```bash
9e5cf24ce483bb96e7736ea75ca422e3560e7b455eee63dd28f66fa1825db70e
```

Quindi abbiamo la possibilità di verificare di aver scaricato il giusto archivio.

```bash
echo "9e5cf24ce483bb96e7736ea75ca422e3560e7b455eee63dd28f66fa1825db70e 2019–07–10-raspbian-buster-lite.zip" | shasum -a 256 -c -
```

NB: dovete essere nella stessa cartella dello zip appena scaricato, e tra lo SHA256 e il nome dello Zip ci devono essere due spazi

> Con il comando **shasum** verifichiamo l’integrità e l’autenticità del file controllando il suo **checksum** creato con l’algoritmo SHA.

Se ottenete questo risultato:

```bash
2019–07–10-raspbian-buster-lite.zip: OK
```

![](https://cdn-images-1.medium.com/max/1200/1*NpMKM_xdZBVabSLec-DAYg.png)

la prova è andata a buon fine.

#### Formattare SD card (facoltativo)

Questo passaggio potrebbe essere facoltativo, ma per sicurezza io l’ho eseguito ugualmente. Dopo aver inserito la SD card, ho lanciato questo comando per individuarla.

```bash
diskutil list
```

nel mio caso era disk2, ho eseguito quindi questo comando:

```bash
sudo dd if=/dev/urandom of=/dev/disk2s2 bs=1000000
```

> NB: questo comando non da output, quindi attendete fiduciosi :). Nei sistemi OSX con Ctrl+T possiamo sbirciare un pò…

Sui dispositivi mac potrebbe essere necessario lanciare questo comando prima e formattare.

```bash
$ sudo diskutil umountDisk /dev/disk2Unmount of all volumes on disk2 was successful
```

#### Copiare l’immagine nella SD card

Bene è il momento di fare sul serio, spostiamo l’immagine nell’SD card.

Smontiamo SD card

```bash
diskutil unmountDisk /dev/disk2
```

copiamo quindi l’immagine al suo interno

```bash
sudo dd bs=1m if=2019–07–10-raspbian-buster-lite.img of=/dev/disk2
```

> NB: questo comando non da output, quindi attendete fiduciosi² :). Nei sistemi OSX con Ctrl+T possiamo sbirciare un pò…

Quando l’immagine è stata copiata, abilitiamo ssh.  
Come dimostra la [guida](https://www.raspberrypi.org/documentation/remote-access/ssh/?source=post_page---------------------------) di Raspberry, ci sono diversi modalità per accedere con il comando **ssh**.

Uno di questi, il più semplice, è posizionare nel percorso dell’SD card **/Volumes/boot/** un file ssh senza estensione

```bash
touch /Volumes/boot/ssh
```

> SSH, **secure shell**, è un protocollo che permette di creare un canale sicuro tra due entità, cioè tra il client e il server (in questo caso Raspberry). Le comunicazioni sono crittate lato client e decrittate lato server automaticamente, così da poter trasferire le informazioni in modo sicuro. SSH risolve l’autenticazione, encryption (quindi cifrare messaggi) e l’integrità del messaggio testo.

Se abbiamo formattato la nostra SD card abbiamo due partizioni, una più piccola chiamata boot e una rootfs (almeno nel mio caso), il file deve essere posizionato nella partizione più piccola, ovvero in boot.  
Per verificare quanto spazio abbiamo a disposizione possiamo utilizzare il comando df.

```bash
df -h
```

risultato:

```bash
Filesystem Size Used Avail Capacity iused ifree …..

/dev/disk2s2 1.8Gi 1.0Gi 776Mi 58% 42164 75196 36% /Volumes/rootfs/dev/disk2s1 252Mi 40Mi 212Mi 16% 0 0 100% /Volumes/boot
```

posizionando il file ssh, quando il Raspberry si avvia, vede che c’e il file, lo cancella e abilita ssh.

Possiamo smontare il disco:

```bash
diskutil unmountDisk /dev/disk2
```

Siamo pronti a inserire l’SD card nel Raspberry!

#### Trovare il Raspberry nella rete

Dopo aver inserito l’SD card, acceso il Raspberry (davvero?) e collegato con il cavo ethernet, dobbiamo trovare il suo IP. 
Possiamo collegarci al router e trovarlo dall’interfaccia grafica del router stesso, oppure possiamo usare il comando

```bash
arp -a
```

che restituisce tutti gli indirizzi dei dispositivi connessi.  
Sappiamo che per [convenzione](https://udger.com/resources/mac-address-vendor-detail?name=raspberry_pi_foundation) l’indirzzo [MAC](https://it.wikipedia.org/wiki/Indirizzo_MAC) del Raspberry inizia con b8:27:eb, quindi possiamo usare grep per filtrare il risultato.

```bash
arp -a | grep 'b8:27:eb'? (192.168.1.221) at b8:27:eb:84:7b:a0 on en0 ifscope [ethernet]
```

> Il MAC address (media access control) , chiamato anche physical address, individua con certezza l’interfaccia di rete. Ogni dispositivo ne ha una ed è univoca.

Nel mio caso l’ip designato per il Raspberry è 192.168.1.221 
Dato che abbiamo abilitato ssh (vedi sopra) posso collegarmi con:

```bash
ssh pi@192.168.1.221
```

inserendo la password di default **raspberry**. 
Per motivi di sicurezza è consigliato modificare la password ssh, dato che per tutto il mondo è raspberry :) 
Con il comando:

```bash
passwd
```

è possibile cambiare la password per l’utente **pi**. Cambiamo anche la password per l’utente **root**.

```bash
sudo passwd root
```

Io per comodità ho messo le stesse password. 
Creiamo anche l’utente bitcoin che sarà l’utente designato alle operazioni sul nodo, in modo tale da creare anche una nuova home che, più avanti, linkeremo all’hard disk esterno.

```bash
sudo adduser bitcoin
```

#### Usare la chiave pubblica per loggarsi nel Raspberry

È molto comodo, oltre che sicuro, loggarsi con la chiave pubblica invece che con la password. 
Creiamo quindi la coppia di chiave privata e pubblica. 
Non sai se le hai già? Con questo comando verifichi le chiavi in tuo possesso.

```bash
ls -la ~/.ssh/*.pub
```

Se non la hai, puoi creare la tua chiave nel formato [Ed25519](https://en.wikipedia.org/wiki/EdDSA).

> Il formato Ed25519 è stato introdotto con OpenSSH versione 6.5. Utilizza la curva ellittica ([https://en.wikipedia.org/wiki/Twisted_Edwards_curve](https://en.wikipedia.org/wiki/Twisted_Edwards_curve)) per derivare le chiavi ed è stata pensata per essere più veloce rispetto allo schema esistente della *classica *firma digitale. Per maggiori [informazioni](https://en.wikipedia.org/wiki/EdDSA).

Per creare una nuova chiave:

```bash
ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519 -C "email@email.com"
``` **~/.ssh/id_ed25519** rappresenta la nostra private key, “la nostra identità digitale” **~/.ssh/id_ed25519.pub** rappresenta la nostra public key che dovremo mettere sul Raspberry per essere **autenticati**. > HINT: è buona norma mettere una password alla chiave privata. Cosi facendo ogni volta che ci autentichiamo, dobbiamo inserirla in modo da decrittare la chiave privata e loggarsi su Raspberry.  
> Come possiamo evitare di scrivere la password della chiave privata? 
> Lanciando **ssh-add**, il quale aggiunge la password a **ssh-agent**.  
> Per non dover scrivere ogni volta la password possiamo lanciare questo comando: **ssh-add -K ~/.ssh/id_ed25519** > Se invece vuoi cambiare la password della chiave privata: **ssh-keygen -p -f id_ed25519** Copiamo la chiave appena creata nel nostro raspberry 
*ricordate che il vostro ip potrebbe essere differente*

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub pi@192.168.1.221
```

una volta copiata la chiave nel Raspberry, ci colleghiamo con ssh e togliamo la password. 
Nel Raspberry è necessario fare questa procedura:

```bash
ssh pi@192.168.1.221sudo nano /etc/ssh/sshd_config
```

cercate PasswordAuthentication, e settarla a no.

> HINT: vuoi loggarti direttamente con l’utente bitcoin?  
> Con **ssh bitcoin@192.168.1.221** puoi già loggarti inserendo la password, se invece vuoi loggarti con la chiave pubblica, fai la stessa operazione descritta sopra. Ogni utente ha le proprie chiavi, infatti vengono copiate nell home dell’utente /home/ **bitcoin/**.ssh.  
> La cartella **.ssh** viene creata dal comando ssh-copy-id. 
> Se invece non potete creare la cartella .ssh nell’utente bitcoin, potete copiarla con il comando sudo con l’utente pi, e dopo cambiare l’owner  
> sudo chown -R bitcoin:bitcoin /home/bitcoin/.ssh **Note su SSH** (facoltativo)

La prima volta che ci autentichiamo con SSH, riceveremo questo messaggio:

```bash
The authenticity of host ‘192.168.1.221 (192.168.1.221)’ can’t be established.ECDSA key fingerprint is SHA256:XXXXXXXXXXXXXXX.Are you sure you want to continue connecting (yes/no)?
```

Il fingerprint è l’impronta digitale del Raspberry. Lo potete trovare qui:

```bash
pi@raspberrypi:/etc/ssh $ ssh-keygen -lf ssh_host_ecdsa_key.pub256 SHA256:IPYYELcHtVEmIVdZDswU4sgr991ZiPZOPyW9knKx4aY root@raspberrypi (ECDSA)
```

Quindi ci sta informando che ci stiamo collegando a tale dispositivo. 
Scegliendo **yes**, l’indirizzo locale del Raspberry verrà aggiunto sul client nel file known_hosts (/Users/barno/.ssh).  
Analizzando tale file vedrete che ci sarà l’IP del Raspberry e la sua chiave pubblica, come questa:

```bash
192.168.1.221 ecdsa-sha2-nistp256 chiave XXXX
```

La chiave è la chiave pubblica del Raspberry che trovate in

```bash
pi@raspberrypi:/etc/ssh $ cat /etc/ssh/ssh_host_ecdsa_key.pub
```

Mentre la chiave pubblica (creata e spostata in precedenza) del vostro client usata per l’autenticazione è salvata in:

```bash
pi@raspberrypi: $cat ~/.ssh/authorized_keys
```

Quindi se volete aggiungere un’altro utente, potete inserire la public key all’interno di quel file.

#### Router: IP Fisso, porte e IP pubblico

Se ogni volta che voglio accedere al Raspberry ha un indirizzo diverso diventa molto noioso se non controproducente.

Quindi, stabiliamo un IP fisso locale per il nostro nodo configurandolo dal router. 
Nel mio caso ho associato l’IP statico 192.168.1.221. 
Un ulteriore passaggio fondamentale è aprire le opportune porte. 
In questo caso apro sia la mainnet che la testnet e la porta 22 per SSH.

![Configurazioni Porte.](https://cdn-images-1.medium.com/max/1200/1*fME80jLpzjRpcMERLLbFmQ.png)
*Configurazioni Porte.*

Le porta **8333** (mainnet) e la porta **18333** (testnet) dobbiamo aprirle se vogliamo essere raggiunti dagli altri nodi. 
La porta **8332** (mainnet) e la porta **18332** (testnet) che non sono state aperte permetterebbero di fare delle richieste RPC dall’esterno. 
La porta **5100** è mappata sulla porta **22** del vostro router. Per collegarsi dall’esterno dobbiamo riferirsi alla porta 5100 (o una scelta da voi nel range di 1024–65535).

> HINT: per verificare se le porte sono aperte correttamente potete utilizzare telnet IP_PUBBLICO PORTA e vedere se risponde. 
> Oppure potete utilizzare nmap (per installarlo su mac => brew install nmap) e inserire il vostro IP pubblico per verificare le porte aperte. (nmap — open IP PUB)

Potrebbe essere interessante collegarsi dall’esterno al nostro nodo.  
Se non siete in possesso di un ip pubblico dovete contattare il vostro [ISP](https://it.wikipedia.org/wiki/Internet_service_provider).

#### GUI? no grazie.

Non vogliamo la GUI, quindi settiamo la RAM dedicata al minimo. 
Dal vostro nodo digitate

```bash
sudo raspi-config
```

E vi troverete davanti a una schermata come questa

![](https://cdn-images-1.medium.com/max/1200/1*3EVVvlIpcgCOi3A4krOWYA.png)

Come vedete ci sono un pò di opzioni.  
Selezioniamo la voce 3 -> B1 -> B1.  
Di fatto diciamo di volere la console come boot. 
Poi possiamo scegliere locale e time-zone alla voce **4**. Ed infine spostandosi sulla voce **7** Advanced Options, e successivamente su A3 Memory split, settiamo la RAM a 16. 
Buona cosa anche tenere il Raspberry aggiornato, quindi anche la voce numero 8 Update. 
Fatto tutto, andate su finish. 
Il Raspberry si riavvierà, appena torna raggiungibile possiamo fare gli aggiornamento dei pacchetti

```bash
sudo apt updatesudo apt -y upgrade
```

Riavviamo di nuovo il nostro Raspberry.

```bash
sudo shutdown -r now
```

#### Configurare l’hard disk esterno

Colleghiamo l’hard disk al nostro Raspberry e digitiamo il comando

```bash
sudo lsblk -o UUID,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,MODEL
```

cosi da individuarlo, nel mio caso è sda.

![](https://cdn-images-1.medium.com/max/1200/0*YQeZkMhZ1L11RWbF)

Bene, siamo pronti a formattarlo! 
Attenzione questa operazione elimina tutti i file dal proprio hard disk, quindi siate certi che non contenga le chiavi private di Satoshi!

```bash
sudo mkfs.ext4 /dev/sda -L LN
```

dove **LN** è la label dell’hard disk.

Per essere sicuri che tutto sia andato a buon fine possiamo richiamare il comando

```bash
sudo lsblk -o UUID,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,MODEL
```

e dobbiamo leggere LN nella colonna LABEL del nostro hard disk. 
Dato che il Raspberry lavorerà sempre con il nostro hard disk, montiamolo in automatico. 
Prima di tutto creiamo la cartella hdd.

```bash
sudo mkdir /mnt/hdd
```

Poi individuiamo l’UUID dell’hard disk con il comando:

```bash
sudo blkid | grep /dev/sda
```

e una volta preso nota, apriamo il file necessario

```bash
sudo nano /etc/fstab
```

e aggiungiamo

```bash
UUID=XXXXXX /mnt/hdd ext4 defaults 0 0
```

dove XXXXX è l’UUID recuperato precedentemente.

e infine montiamo tutto!

```bash
sudo mount -a
```

In questo modo ogni volta che si riavvia il Raspberry l’HDD sarà già montato e pronto. Se riavviamo il Raspberry senza avere l’HDD collegato, potrebbe creare problemi.

Dato che abbiamo creato l’utente bitcoin che sarà l’addetto a interfacciarsi con il nodo, diamo i privilegi di scrittura alla cartella (ricorsivamente) appena creata

```bash
sudo chown -R bitcoin:bitcoin /mnt/hdd
```

In questo modo l’utente **pi** può **solo** leggere (a meno che non si usi sudo) e l’utente bitcoin leggere e scrivere.

Il percorso di default dove viene salvata la blockchain è **~/.bitcoin/** e questa non è dentro l’hdd esterno.  
Per risolvere questo *problema* abbiamo due soluzioni. 
O inseriamo datadir=/percorso/che/vogliamo nel file **.conf**, oppure facciamo una link simbolico.  
Per cercare di lasciare più pulito possibile il file **.conf**, opteremo per il link simbolico che punta dentro alla cartella bitcoin nell’HDD. 
Quindi creiamo la cartella con l’utente bitcoin. 
*PS: per cambiare utente: sudo su bitcoin*

```bash
mkdir /mnt/hdd/bitcoin
```

creiamo quindi il link simbolico

```bash
ln -s /mnt/hdd/bitcoin /home/bitcoin/.bitcoin
```

per verificare che tutto sia andato a buon fine potete spostarvi in

```bash
cd /home/bitcoin/
```

e digitare

```bash
ls -al
```

dovreste vedere il collegamento evidenziato da -> **SWAP**! Che cosa è lo swap?  
La definizione di Wikipedia è molto intuitiva:

> Con il termine **swap** si intende, in [informatica](https://it.wikipedia.org/wiki/Informatica), l’estensione della capacità della [memoria volatile](https://it.wikipedia.org/wiki/Memoria_volatile) complessiva del [computer](https://it.wikipedia.org/wiki/Computer), oltre il limite imposto dalla quantità di [RAM](https://it.wikipedia.org/wiki/RAM) installata, attraverso l’utilizzo di uno spazio su un altro supporto fisico di memorizzazione, ad esempio il [disco fisso](https://it.wikipedia.org/wiki/Disco_fisso). L’uso dello swap è una delle tecniche impiegate dal [sistema operativo](https://it.wikipedia.org/wiki/Sistema_operativo) per la gestione della [memoria virtuale](https://it.wikipedia.org/wiki/Memoria_virtuale).

La memoria complessiva del raspberry Pi 3 B+ è di 2 gigabyte, quindi cercheremo di aumentarla virtualmente.

Con l’utente pi digitare:

```bash
sudo dphys-swapfile swapoffsudo dphys-swapfile uninstallsudo nano /etc/dphys-swapfile
```

Quindi alla voce modificare come segue:

```bash
CONF_SWAPFILE=/mnt/hdd/swapfile#CONF_SWAPSIZE=
```

Salvare e creare il file swapfile manualmente

```bash
sudo dd if=/dev/zero of=/mnt/hdd/swapfile count=1000 bs=1MiBsudo chmod 600 /mnt/hdd/swapfilesudo mkswap /mnt/hdd/swapfile
```

Quindi attivare lo swap

```bash
sudo dphys-swapfile setupsudo dphys-swapfile swapon
```

Benissimo a questo punto possiamo installare qualche pacchetto interessante:

```bash
sudo apt install git build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev libminiupnpc-dev libzmq3-dev jq
```

#### **È il momento di installare Bitcoin Core**! Bene è arrivato il momento! 
Loggato come **pi** creiamo la cartella download che ospiterà il software.

```bash
mkdir /home/pi/downloadcd /home/pi/download
```

Verifica l’ultima versione di bitcoin core disponibile: [https://bitcoincore.org/en/download/](https://bitcoincore.org/en/download/) o qui [https://github.com/bitcoin/bitcoin/releases](https://github.com/bitcoin/bitcoin/releases)

Qui invece è possibile vedere i change logs [https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.18.0.md](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.18.0.md)

nel mio caso bitcoin core 0.18.0 e dobbiamo installare la versione **linux arm 32 bit**.

```bash
wget https://bitcoincore.org/bin/bitcoin-core-0.18.0/bitcoin-0.18.0-arm-linux-gnueabihf.tar.gz
```

Scarico anche le relative firme per verificare il pacchetto.

```bash
wget https://bitcoincore.org/bin/bitcoin-core-0.18.0/SHA256SUMS.ascwget https://bitcoin.org/laanwj-releases.asc
```

controllo il pacchetto ignorando i Warning

```bash
sha256sum --check SHA256SUMS.asc --ignore-missing
```

risultato:

```bash
bitcoin-0.18.0-arm-linux-gnueabihf.tar.gz: OKsha256sum: WARNING: 20 lines are improperly formatted
```

L’importante è che ci sia un bell’ **OK**!

Controlliamo anche le chiavi.

```python
gpg --import./laanwj-releases.ascgpg --refresh-keysgpg --verify SHA256SUMS.asc
```

risultato:

```sql
gpg: Good signature from “Wladimir J. van der Laan …”Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964
```

Bene, siamo sicuri di avere quello che vogliamo, possiamo finalmente installarlo. Decomprimiamo l’archivio e spostiamo i file bin all’interno di /usr/local/bin cosi da renderlo globale.

```bash
tar -xvf bitcoin-0.18.0-arm-linux-gnueabihf.tar.gz

sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-0.18.0/bin/*
```

Per verificare che tutto sia andato a buon fine, possiamo digitare:

```bash
bitcoind -version

> Bitcoin Core Daemon version v0.18.0
```

Bene, momento di pulizia, assicuratevi di essere nella cartella /home/pi/download

```bash
rm -Rf *
```

Ottimo, siamo pronti a creare il file .conf che leggerà Bitcoin core. 
Con l’utente bitcoin (sudo su bitcoin) spostarsi in **/mnt/hdd/bitcoin** e digitare

```bash
nano bitcoin.conf
```

e aggiungere:

```bash
# Generated by https://jlopp.github.io/bitcoin-core-config-generator/

# This config should be placed in following path:# ~/.bitcoin/bitcoin.conf

# [core]# Run in the background as a daemon and accept commands.daemon=1# Set database cache size in megabytes; machines sync faster with a larger cache. Recommend setting as high as possible based upon machine’s available RAM.dbcache=100# Keep at most <n> unconnectable transactions in memory.maxorphantx=10# Keep the transaction memory pool below <n> megabytes.maxmempool=50# Maintain a full transaction index, used by the getrawtransaction rpc call.txindex=1

# Maintain at most N connections to peers.maxconnections=40# Tries to keep outbound traffic under the given target (in MiB per 24h), 0 = no limit.maxuploadtarget=5000

# Run this node on the Bitcoin Test Network.testnet=1

# Accept command line and JSON-RPC commands.server=1

# Options only for mainnet[main]

# Options only for testnet[test]

# Options only for regtest[regtest]
```

Per creare la configurazione ho usato comodo servizio [*https://jlopp.github.io/bitcoin-core-config-generator/*](https://jlopp.github.io/bitcoin-core-config-generator/) .  
Per sapere tutti i parametri ci basterà comunque digitare **bitcoind -h**. 
Per avere una demo di configurazione possiamo visitare il GitHub ufficiale di Bitcoin [https://github.com/bitcoin/bitcoin/blob/master/share/examples/bitcoin.conf](https://github.com/bitcoin/bitcoin/blob/master/share/examples/bitcoin.conf)

Il file contiene testnet=1, quindi scaricheremo la blockchain testnet.

Gli esempi riportati nel [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica), utilizzando la testnet e poi per fare degli esperimenti direi che è meglio non perdere btc.

Siamo pronti a partire! 🚀 
Digitiamo

```bash
bitcoind
```

e il nodo inizia a scaricare la blockchain.  
Per vedere i log possiamo usare tail.

```bash
tail -f /home/bitcoin/.bitcoin/testnet3/debug.log
```

e per avere delle informazioni più dettagliate

```bash
bitcoin-cli getblockchaininfo | jq
```

Vuoi conoscere tutti i comandi possibili?

```bash
bitcoin-cli help
```

Vuoi sapere che significato hanno i valori ottenuti con la chiamata getblockchaininfo?

```bash
bitcoin-cli help getblockchaininfo
```

Vuoi stoppare il nodo?

```bash
bitcoin-cli stop
```

HINT:

Dato che con Raspberry abbiamo delle limitazione del numero peers e altri parametri, un metodo per sincronizzare la blockchain più velocemente è quello di scaricare il core sul proprio computer, collegare l’hard disk esterno che stiamo utilizzando sul Raspberry e lanciare il demone facendo scaricare la blockchain all’interno dell’unità esterna. il file bitcoin.conf lo potete generare da qui [*https://jlopp.github.io/bitcoin-core-config-generator*](https://jlopp.github.io/bitcoin-core-config-generator/)*.*

Come fare a far scaricare la blockchain nell’hard disk esterno? 
Dopo aver scaricato bitcoin core, come mostrato poco sopra, mi sposto nella cartella bin

```bash
/Users/barno/Documents/btc/bitcoin-0.18.0/bin
```

e lancio il comando

```bash
./bitcoind -datadir=/Volumes/LN/bitcoin
```

dove /Volumes/LN/bitcoin è la cartella del disco esterno.

Per leggere i log vale quanto spiegato sopra, ovviamente cambiando il path.

```bash
tail -f /Volumes/LN/bitcoin/testnet3/debug.log
```

check blockchain

```bash
/Users/barno/Documents/btc/bitcoin-0.18.0/bin/bitcoin-cli getblockchaininfo
```

*Ho inserito i percorsi assoluti per far capire dove sono posizionato.*

#### Utilizzare il nodo Raspberry dal proprio client (opzionale)

Potremmo avere la necessità di fare delle chiamate al nostro nodo da **non** dentro il Raspberry. 
Se siamo nella rete locale possiamo fare un tunnel ssh facendo il forward della porta 18333 locale sulla porta 18333 del Raspberry. 
In questo modo è come se dicessimo: *Ehi, tutte le chiamate che faccio sul mio localhost (client) sulla porta 18333 inoltrale in questo tunnel*.  
Dall’altro lato del tunnel è presente il Raspberry. 
Colleghiamoci al Raspberry con questo comando ssh:

```bash
ssh -L 18332:127.0.0.1:18332 pi@192.168.1.221
```

Sul nostro client, spostiamoci in bitcoin core, nel mio caso il percorso è quello riportato poco sopra

```bash
/Users/barno/Documents/btc/bitcoin-0.18.0/bin/bitcoin-cli
```

Facciamo una chiamata per interrogare il nodo

```bash
./bitcoin-cli getblockchaininfo | jq
```

riceviamo però questo errore:

```bash
error: Could not connect to the server 127.0.0.1:8332

Make sure the bitcoind server is running and that you are connecting to the correct RPC port.
```

ok, dobbiamo essere autenticati. 
Per fare questo ci sono tre modi,

- username e password come parametri dalla chiamata.
- rpcauth
- copiare il cookie dal Bitcoin core del Raspberry nel nostro client. **Soluzione 1 (username e password)** In Raspberry con l’utente bitcoin stoppiamo il nodo Bitcoin

```bash
bitcoin-cli stop
```

Adesso editiamo il .conf

```bash
vi /mnt/hdd/bitcoin/bitcoin.conf
```

e aggiungiamo

```bash
[test]rpcuser=barnorpcpassword=barnopass
```

e riavviamo il nodo con il comando bitcoind (se avete implementato la soluzione che avvia il nodo in automatico, potrebbe essersi già riavviato).

Adesso dal nostro client possiamo fare la nostra chiamata, passando anche rpcport nelle opzioni.

```bash
./bitcoin-cli -rpcuser=barno -rpcpassword=barnopass -testnet=1 getblockchaininfo | jq
``` **Soluzione 2 rpcauth** A differenza della prima soluzione, non scriveremo in chiaro la username e la password nel file di .conf ma utilizzeremo questo [script](https://raw.githubusercontent.com/bitcoin/bitcoin/master/share/rpcauth/rpcauth.py) in python per aggiungere il salt e offuscare la nostra password. 
Una volta scaricato lo script python lanciatelo passando username e password che volete utilizzare

```bash
./rpcauth.py barno barnopassString to be appended to bitcoin.conf:rpcauth=barno:bf92263dcf78afbf74c69af146a5f5df$ec8d07c7952ad57b616f3af7898074c286f0b5151f6aeaf840248c0945405801Your password:barnopass
```

Come si capisce dall’output, dobbiamo aggiungere la stringa rpcauth nel nostro file .conf 
Stoppiamo il nodo e inseriamo la riga suggerita.

```bash
[test]rpcauth=barno:bf92263dcf78afbf74c69af146a58074c286f0b5151f6aeaf840248c0945405801
```

e riavviamo il nodo con il comando bitcoind (se avete implementato la soluzione che avvia il nodo in automatico, potrebbe essersi già riavviato).

Adesso dal nostro client possiamo fare la nostra chiamata, passando anche rpcport nelle opzioni.

```bash
./bitcoin-cli -rpcuser=barno -rpcpassword=barnopass -testnet=1 getblockchaininfo | jq
```

Il vantaggio di questa procedura è che la username e la password sono *hashati* con HMAC-SHA-256, e possiamo creare più utenti, aggiungendo un altro rpcauth in bitcoin.conf. **Soluzione 3 cookie** il file .cookie è la via più comoda cosi da evitare di non dover mettere username e password se siamo interessati ad un utente solo.

Si trova all’interno della datadir, che nel nostro caso avendo scaricato la blockchain di test, è all’interno di testnet3.

![](https://cdn-images-1.medium.com/max/1200/1*lNnWz6pFisaShfIAiJA58Q.png)

Anche nel client deve essere dentro la cartella testnet3, oppure possiamo specificare un percorso. 
Usando il comando [scp](https://en.wikipedia.org/wiki/Secure_copy), copiamo il cookie dal Raspberry al nostro client. 
Il [percorso di default](https://en.bitcoin.it/wiki/Data_directory) sul Mac per la datadir è **~/Library/Application Support/Bitcoin**, su Linux è **~/.bitcoin/** Il comando da eseguire dal client per copiare il .cookie è:

```bash
scp bitcoin@192.168.1.221:/mnt/hdd/bitcoin/testnet3/.cookie /Users/barno/Library/Application\ Support/Bitcoin/testnet3
```

Adesso abbiamo a disposizione il .cookie che ci autentica più velocemente senza inserire username e password. 
Dal client possiamo quindi eseguire il nostro comando RPC.

```bash
./bitcoin-cli -testnet=1 getblockchaininfo | jq
```

Se vogliamo posizionare il .cookie in un altro percorso dobbiamo passare l’opzione -rpccookiefile.

#### Avviare il demone bitcoind in automatico

Creiamo un servizio in modo tale che se il demone bitcoind dovesse crashare, oppure per qualsiasi motivo si dovesse spengere il Raspberry, al suo riavvio siamo in grado di sincronizzare la blockchain senza eseguire nessun comando manuale. 
Con l’utente pi, creiamo il servizio

```bash
sudo nano /etc/systemd/system/bitcoind.service
```

E scriviamo:

```bash
[Unit]

Description=Bitcoin daemon

After=network.target

[Service]

ExecStartPre=/bin/sh -c 'sleep 30'

ExecStart=/usr/local/bin/bitcoind -daemon -conf=/home/bitcoin/.bitcoin/bitcoin.conf -pid=/home/bitcoin/.bitcoin/bitcoind.pid

PIDFile=/home/bitcoin/.bitcoin/bitcoind.pid

User=bitcoin

Group=bitcoin

Type=forking

KillMode=process

Restart=always

TimeoutSec=120

RestartSec=30

[Install]

WantedBy=multi-user.target
```

Salviamo e abilitiamo il servizio

```bash
sudo systemctl enable bitcoind.service
```

Riavviamo il Raspberry

```bash
sudo shutdown -r now
```

Adesso al vostro login dovreste avere già il nodo attivo!

Comandi utili per i servizi **enable** ```bash
sudo systemctl enable bitcoind.service
``` **restart** ```bash
sudo systemctl restart bitcoind.service
``` **start** ```bash
sudo systemctl start bitcoind.service
``` **stop** ```bash
sudo systemctl stop bitcoind.service
``` **status** ```bash
sudo systemctl status bitcoind.service
```

### **Sicurezza** #### ufw

Bene cerchiamo di mettere in sicurezza il nostro Raspberry. 
Utilizzeremo ufw (firewall) come suggerito anche dalla guida Raspberry [https://www.raspberrypi.org/documentation/configuration/security.md](https://www.raspberrypi.org/documentation/configuration/security.md).

Installiamolo con

```bash
sudo apt install ufw
```

ufw blocca le connessioni in entrata e lascia libere quelle in uscita. 
Ecco la configurazione che ho usato io.

ATTENZIONE siate sicuri dell’indirizzi ip Interno ed esterno, altrimenti vi chiudete fuori!

```sql
sudo suufw default deny incomingufw default allow outgoingufw allow from 192.168.1.0/24 to any port 22 comment 'allow SSH from local LAN'

ufw allow ssh
```

```sql
ufw allow proto udp from 192.168.1.0/24 port 1900 to any comment 'allow local LAN SSDP for UPnP discovery'ufw allow 9735 comment 'allow Lightning'ufw allow 8333 comment 'allow Bitcoin mainnet'ufw allow 18333 comment 'allow Bitcoin testnet'ufw enablesystemctl enable ufwufw statusexit
```

e per verificare le regole attive

```bash
sudo ufw status verbose
```

Le configurazioni sono salvate in:

```bash
/etc/ufw/
```

> HINT: avete inserito una regola per errore? 
> con il comando **sudo ufw status numbered** potete individuare l’indice della regola errata e con il comando **sudo** **ufw delete [numero]** potete cancellarla. 
> [Clicca qui](https://www.howtoforge.com/tutorial/ufw-uncomplicated-firewall-on-ubuntu-15-04/) per maggiori informazioni sui comandi ufw.

#### fail2ban

[https://www.raspberrypi.org/documentation/configuration/security.md](https://www.raspberrypi.org/documentation/configuration/security.md)

Altro tool consigliato dalla guida Raspberry, che analizza il log per verificare delle attività sospette, ad esempio attacchi di tipo bruteforce.

```bash
sudo apt-get install fail2ban
```

Bene adesso avete tutto a disposizione per tenere attivo il vostro nodo.

Potete tranquillamente fare esperimenti, oppure seguire senza problemi il [libro Bitcoin dalla teoria alla pratica](prodotti/bitcoin-dalla-teoria-alla-pratica) :)

![Il mio nodo in funzione.](https://cdn-images-1.medium.com/max/1200/1*zd6R6cKGNZFDOJjB2TEFGg.png)
*Il mio nodo in funzione.*

Ogni **suggerimento** o modifica è sempre benvenuta. 
Le fonti che ho utilizzato per questo articolo sono: 
- [https://medium.com/@meeDamian/bitcoin-full-node-on-rbp3-revised-88bb7c8ef1d1](https://medium.com/@meeDamian/bitcoin-full-node-on-rbp3-revised-88bb7c8ef1d1) 
- [https://stadicus.github.io/RaspiBolt/](https://stadicus.github.io/RaspiBolt/)
