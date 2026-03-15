---
title: "Pretty Good Privacy"
date: 2020-01-13T10:00:00+01:00
slug: "pretty-good-privacy"
draft: false
author: "Alessio Barnini"
description: "PGP/GPG come verificare i pacchetti Bitcoin e Electrum."
cover: "/img/posts/pretty-good-privacy-1.webp"
tags:
  - "Bitcoin"
  - "Chiave Pubblica"
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Pretty Good Privacy

#### PGP/GPG come verificare i pacchetti Bitcoin e Electrum.

Ma ti pare che capita a me? 
Ecco il primo pensiero che ci viene in mente quando scarichiamo un software. 
È molto interessante come nella prima pagina di **Electrum** ci sia questo messaggio:

> Warning: Electrum versions older than 3.3.4 are susceptible to [phishing](https://github.com/spesmilo/electrum/issues/4968). Do not download Electrum from another source than electrum.org, **and learn to verify GPG signatures**.

![Don’t trust, verify!](/img/posts/pretty-good-privacy-1.webp)
*Don’t trust, verify!*

Q: Che cosa significa PGP? 
R: Pretty good privacy, scritto da [Phil Zimmermann](https://it.wikipedia.org/wiki/Phil_Zimmermann) e ora fa parte della PGP Corporation. È un software di crittografia.

Q: Che cosa significa GPG? 
R: Gnu Privacy Guard, è un aggiornamento di PGP.

Q: Come posso essere sicuro di aver scaricato esattamente il pacchetto corretto? 
R: Verificando la firma digitale di quel pacchetto.

Q: Con cosa si verifica la firma digitale? 
R: Con la chiave pubblica del firmatario.

Q: Come posso recuperare la chiave pubblica del firmatario? 
R: Puoi recuperare la chiave pubblica dal sito di riferimento o utilizzando dei **keyserver** inserendo il suo **fingerprint**.

Ok sono pronto a scaricare e a verificare il pacchetto Bitcoin!

[https://medium.com/@satoshiwantsyou/verifica-signature-bitcoin-core-pgp-628bee490767](https://medium.com/@satoshiwantsyou/verifica-signature-bitcoin-core-pgp-628bee490767)

Prima di tutto è necessario installare [GPG](https://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/). 
Una volta installato potete verificare la versione in uso.

```bash
$ gpg --version

gpg (GnuPG/MacGPG2) 2.2.17
```

Andiamo quindi a scaricare l’ultimo pacchetto di [Bitcoin Core](https://bitcoin.org/en/version-history) dal sito ufficiale 
[https://bitcoin.org/en/version-history](https://bitcoin.org/en/version-history). Ad oggi è lo 0.19.0.1.

Dato che io sto utilizzando un Mac, scaricherò la versione osx64 [https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/](https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/) e le relative firme [https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc](https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc)

Se non disponiamo dell’interfaccia grafica, possiamo utilizzare il comando wget.

```bash
$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/bitcoin-0.19.0.1-osx64.tar.gz

$ wget https://bitcoincore.org/bin/bitcoin-core-0.19.0.1/SHA256SUMS.asc
```

Per prima cosa verifichiamo che il checksum ottenuto con l’algoritmo SHA256 sul pacchetto *tar* appena scaricato sia fedele a quello che troviamo all’interno di SHA256SUM.ASC, così da essere sicuri di aver scaricato il pacchetto desiderato.

```bash
$ sha256sum --check SHA256SUMS.asc --ignore-missing
```

risultato:

```bash
bitcoin-0.19.0.1-osx64.tar.gz: OKsha256sum: WARNING: 20 lines are improperly formatted
```

*NB: tutti i file e i comandi sono eseguiti all’interno della stessa cartella.*

Adesso dobbiamo verificare che il pacchetto provenga esattamente dal mittente voluto. 
Dobbiamo quindi utilizzare la chiave pubblica che verifica la firma.

---

> [*Se hai bisogno di una rinfrescata sulla crittografia, guarda qui*](https://medium.com/@bitcoindallateoriallapratica/firma-digitale-bitcoin-ecdsa-ecc-blockchain-guida-blockchain-b7278ac4bad1?source=your_stories_page---------------------------)* 👀*

---

Possiamo ottenere il fingerprint della relativa chiave pubblica a questo indirizzo https://bitcoin.org/en/full-node#osx-daemon.

Il fingerprint è: 
`01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964`

Non ci resta che scaricarla e verificare l’integrità del pacchetto. 
Per prima cosa verifichiamo se abbiamo già quella chiave, elencando tutte le chiavi nel nostro computer, con il comando:

```bash
$ gpg --list-keys
```

o per essere più precisi:

```bash
$ gpg --fingerprint "01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964"
```

Se non abbiamo nessun risultato, dobbiamo importarla. 
Per farlo ci sono diversi metodi. **Metodo 1**: Interrogare il keyserver tramite fingerprint.

```bash
$ gpg --keyserver hkps://keyserver.ubuntu.com --receive-keys “01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964”
``` **Metodo 2**: Scaricare la chiave pubblica dal sito Bitcoin e importarla.

```python
$ wget https://bitcoin.org/laanwj-releases.asc$ gpg --import laanwj-releases.asc
``` 

**Metodo 3**: A questo link [https://bitcoincore.org/en/download/](https://bitcoincore.org/en/download/) è possibile trovare l’id chiavi **01EA5486DE18A882D4C2684590C8019E36C2E964** 

```bash
$ gpg --keyserver keys.gnupg.net --search-key 01EA5486DE18A882D4C2684590C8019E36C2E964
```

È possibile anche cercarla da [https://keyserver.ubuntu.com/](https://keyserver.ubuntu.com/) inserendo **0x01EA5486DE18A882D4C2684590C8019E36C2E964**. Dopo aver scelto uno dei metodi, possiamo verificare se è stata importata utilizzando i comandi sopra riportatati, list-keys o fingerprint.

```bash
$ gpg --fingerprint "01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964"

pub rsa4096 2015–06–24 [SC] [expires: 2022–02–10]

01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

uid [ unknown] Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>
```

Possiamo finalmente **verificare di aver scaricato il pacchetto corretto**. 

```bash
$ gpg --verify SHA256SUMS.asc
```

```sql
gpg: Signature made Sun Nov 24 10:14:42 2019 CETgpg: using RSA key 90C8019E36C2E964gpg: Good signature from "Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>" [unknown]

gpg: WARNING: This key is not certified with a trusted signature!gpg:There is no indication that the signature belongs to the owner.Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964
```

La verifica è andata a buon fine. 
Per verificare Electrum il procedimento è molto simile. 
Tutto è spiegato nel link [https://electrum.org/#download](https://electrum.org/#download). 
Ecco tutti i passaggi.

```python
$ wget https://raw.githubusercontent.com/spesmilo/electrum/master/pubkeys/ThomasV.asc$ gpg --import ThomasV.asc$ wget https://download.electrum.org/3.3.8/electrum-3.3.8.dmg$ wget https://download.electrum.org/3.3.8/electrum-3.3.8.dmg.asc$ gpg --verify electrum-3.3.8.dmg.asc

gpg: assuming signed data in 'electrum-3.3.8.dmg'

gpg: Signature made Thu Jul 11 16:26:15 2019 CEST

gpg: using RSA key 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6
```

```sql
gpg: Good signature from "Thomas Voegtlin (https://electrum.org) <thomasv@electrum.org>" [unknown]

gpg: aka "ThomasV <thomasv1@gmx.de>" [unknown]

gpg: aka "Thomas Voegtlin <thomasv1@gmx.de>" [unknown]

gpg: WARNING: This key is not certified with a trusted signature!

gpg: There is no indication that the signature belongs to the owner.

Primary key fingerprint: 6694 D8DE 7BE8 EE56 31BE D950 2BD5 824B 7F94 70E6
```

Sai chi è figo? 
Keybase. [https://keybase.io/barno](https://keybase.io/barno)

### **Don’t trust, Verify**.
