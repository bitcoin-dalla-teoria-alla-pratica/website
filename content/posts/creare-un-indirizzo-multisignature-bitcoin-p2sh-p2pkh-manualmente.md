---
title: "Creazione di un Indirizzo Multisignature P2SH-P2PKH Bitcoin: Guida Dettagliata"
date: 2024-01-11T20:49:37+01:00
draft: false

tags:
  - "Script"
  - "Crittografia"
---

<p>In Bitcoin in Azione, ci appassiona svelare i meccanismi sottostanti di Bitcoin. In questa esplorazione, ci immergeremo profondamente nel protocollo, conducendo personalmente la creazione di un indirizzo multifirma P2SH-P2PKH. Perché dedicare tempo a questa attività? Semplice: il nostro obiettivo è acquisire una comprensione completa del funzionamento interno di Bitcoin. È vero, potremmo facilmente generare un indirizzo simile usando Bitcoin Core (tuttavia, riserveremo questo argomento per un futuro articolo, concentrandoci su una configurazione multisig SegWit). Vi rammentiamo che tutto il codice menzionato nei nostri libri, video e articoli è liberamente accessibile su GitHub: <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/">https://github.com/bitcoin-dalla-teoria-alla-pratica/</a>. In questo esempio, optiamo per l'utilizzo di chiavi pubbliche compressi. Iniziamo generando tre chiavi private attraverso la shell, implementando un ciclo di 3 iterazioni.</p>

```bash
for i in 1 2 3
do

  printf  "\n \e[31m ######### Create private key and public key ${i}  #########\e[0m\n\n"

  #private key
  openssl ecparam -genkey -name secp256k1 -rand /dev/urandom -out private_key_$i.pem

  #private key bitcoin
  openssl ec -in private_key_$i.pem -outform DER|tail -c +8|head -c 32 |xxd -p -c 32 > btc_priv_$i.key

  #uncompressed private key
  printf "\n \n 🗝 Uncompressed private key WIF $i \n"
  C=`printf $VERSION_PREFIX_PB$(<btc_priv_$i.key) | xxd -r -p | base58 -c`
  printf $C"\n"
  printf $C > uncompressed_private_key_WIF_$i.txt

  #Compressed private key
  printf "\n \n 🗝 Compressed private key WIF $i \n"
  C=`printf $VERSION_PREFIX_PB$(<btc_priv_$i.key)"01" | xxd -r -p | base58 -c`
  printf $C"\n"
  printf $C > compressed_private_key_WIF_$i.txt

  #Uncompressed public key
  openssl ec -in private_key_$i.pem -pubout -outform DER|tail -c 65|xxd -p -c 65 > btc_pub_$i.key
  printf "\n \n 🔑 Uncompressed public key  $i \n"
  cat btc_pub_$i.key > uncompressed_public_key_$i.txt
  cat uncompressed_public_key_$i.txt

  #Compressed Address legacy
  printf "\n \n 🔑 Compressed Address legacy ${i}\n"
  ADDR_SHA=`printf $(cat uncompressed_public_key_$i.txt) | xxd -r -p | openssl sha256| sed 's/^.* //'`
  ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed 's/^.* //'`
  # echo $ADDR_RIPEMD160
  ADDR=`printf $VERSION_PREFIX_ADDRESS$ADDR_RIPEMD160 | xxd -p -r | base58 -c`
  echo $ADDR > uncompressed_btc_address_$i.txt
  echo $ADDR

  #Check the last byte.
  U=`cat btc_pub_$i.key | cut -c 129-131`
  U=`echo "$U" | tr '[:lower:]' '[:upper:]'`
  U=`echo "ibase=16; $U" | bc`

  if [ $(($U%2)) -eq 0 ];
  then
  #key even
      PREF=02
  else
  #key odd
      PREF=03
  fi

  #Compressed public key
  printf "\n \n 🔑 Compressed public key ${i}\n"
  cat btc_pub_$i.key | tr -d " \t\n\r"  | tail -c $((64*2)) | sed 's/.\{64\}/& /g'| awk '{print $1}'| sed -e 's/^/'$PREF/ > compressed_public_key_$i.txt
  cat compressed_public_key_$i.txt

done
```

<p><strong>Generazione delle Chiavi: Un Viaggio nell'Universo Crittografico<br></strong>Il frammento di codice presentato in precedenza ha con successo prodotto tre chiavi private e le corrispondenti chiavi pubbliche. Se nutrite curiosità su come si formano le chiavi private e come derivano le chiavi pubbliche, vi invitiamo a esplorare l'articolo completo e a immergervi nel nostro libro "Bitcoin dalla Teoria alla Pratica".<br>Ora, ci addentriamo nella fase successiva del nostro viaggio: la creazione del redeem script.</p>

```bash
SCRIPT="5221"$(cat compressed_public_key_1.txt)"21"$(cat compressed_public_key_2.txt)"21"$(cat compressed_public_key_3.txt)"53AE"
```

<p>Il redeem script assume un ruolo cruciale, definendo le condizioni necessarie per lo sblocco dell'UTXO. Esaminiamo più da vicino il suo contenuto e il suo significato nel contesto di Bitcoin.</p>

<p>Analisi Approfondita del Redeem Script: Un'Esplorazione Dettagliata</p>

<p>Consultando la documentazione ufficiale di Bitcoin Script disponibile su https://en.bitcoin.it/wiki/Script, possiamo comprendere appieno il contenuto del nostro script.</p>

<p>Il redeem script che abbiamo generato è composto dai seguenti elementi:</p>

<ul><li>52: Rappresenta l'OP_CODE OP_2, indicando l'inizio di una sequenza coinvolgente due elementi nello stack.</li>

<li>21: Indica il numero di byte successivamente inseriti nello stack. Convertendo 0x21 in decimale otteniamo 33, equivalente a 66 caratteri esadecimali. Questo rappresenta la nostra chiave pubblica compressa.</li>
</ul>

```bash
cat compressed_public_key_1.txt | wc -m
```

<p>Output: 66</p>

<ul><li>53: Rappresenta l'OP_CODE OP_3, introdotto per inserire una sequenza di tre elementi nello stack.</li>

<li>AE: Rappresenta l'OP_CODE OP_CHECKMULTISIG, indicando che il redeem script ora include l'operazione di verifica multisignature.</li>
</ul>

<p>Per comodità, salviamo questo script per ulteriori analisi e riferimenti.</p>

```bash
printf $SCRIPT > redeem_script.txt
```

<p>Questo ci fornisce una base solida per esplorare ulteriormente la complessità del redeem script nel contesto delle transazioni Bitcoin.</p>

<p>Codice Hashing del Redeem Script: Utilizzo di SHA256 e RIPEMD160</p>

<p>Nella fase successiva del nostro itinerario, procederemo all'applicazione degli hash SHA256 e RIPEMD160 al redeem script precedentemente creato. Questa fase riveste importanza cruciale nel processo di generazione di un indirizzo Bitcoin P2SH-P2PKH.</p>

<figure class="wp-block-image size-full"><img src="/img/image.png" alt="Creazione di un Indirizzo Multisignature P2SH-P2PKH Bitcoin: Guida Dettagliata" class="wp-image-13768"/></figure>

```bash
ADDR_SHA=`printf $SCRIPT | xxd -r -p | openssl sha256| sed 's/^.* //'`
    ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed 's/^.* //'`
    printf $ADDR_RIPEMD160 > scriptPubKey.txt
    printf "\n \n\e[46m ---------- scriptPubKey --------- \e[49m\n"
    printf $ADDR_RIPEMD160

    #ADDRESS
    printf "\n \n\e[46m ---------- 🔑 ADDRESS P2SH️ --------- \e[49m\n"
    ADDR=`printf $VERSION_PREFIX_ADDRESS$ADDR_RIPEMD160 | xxd -p -r | base58 -c`
    echo $ADDR > address_P2SH.txt
    echo $ADDR
```

<p>Il blocco di codice fornito descrive il processo dettagliato per ottenere l'indirizzo Bitcoin P2SH-P2PKH attraverso la generazione di hash e l'applicazione di metodi crittografici. Qui di seguito, troverai una versione alternativa del testo senza apportare modifiche al codice:</p>

<p>Nel seguente estratto di codice:</p>

<ul><li><code>ADDR_SHA</code> contiene l'hash SHA256 del redeem script.</li>

<li><code>ADDR_RIPEMD160</code> contiene l'hash RIPEMD160 dell'hash SHA256.</li>
</ul>

<p>Questi passaggi ci conducono allo scriptPubKey, un elemento essenziale per ottenere l'indirizzo Bitcoin P2SH-P2PKH. Per un'approfondita guida passo dopo passo attraverso questo processo, ti consiglio di consultare l'articolo dettagliato disponibile su https://bitcoin-in-action.medium.com/come-si-ottiene-address-bitcoin-p2sh-f009f28206b7.</p>

<p>Infine, procediamo applicando il "Version Prefix" e il processo di Base58Check per ottenere il nostro indirizzo Bitcoin P2SH-P2PKH. Per le reti regtest e testnet, il "Version Prefix" è 0xC4. L'indirizzo finale, ottenuto applicando il "Version Prefix" e il processo di Base58Check all'hash RIPEMD160, è ora pronto per l'uso sulla rete regtest o testnet.</p>

<p>Concludiamo così il processo manuale di creazione dell'indirizzo Bitcoin P2SH-P2PKH, il quale è ora pronto per essere utilizzato sulla rete regtest o testnet.</p>

<p>È importante notare che il nostro indirizzo presenterà come prefisso il numero 2, una caratteristica distintiva dei P2SH nelle reti regtest/testnet.</p>

```bash
######### P2SH #########

 ---------- Redeem Script ---------
522102bd13132bea99bcd50f93dedc6cab13e0f973a8a5f6aec0150f9e835ce41bcbf42102a95dc9d317e57da0ad149eca4cc85aa2665cbb35ced8ccf41c0aec3d5c0333672102ebf7690e84552c3c01a5f01ecd4a1442fb411b501c29c91b7ff27766c8a494f453AE

 ---------- scriptPubKey ---------
03d9f8e4487229f0bd3f3af5ce4b6301930f18de

 ---------- 🔑 ADDRESS P2SH️ ---------
2Msbb8qRdT5N3YJYc8BDbQ25sMJQUuKUKMW
```

<p>Per chi fosse interessato al codice completo, lo troverà disponibile in questo <a href="https://gist.github.com/bitcoin-in-action/13f21456d3b49bc7f91154307847df50">gist</a> oltre che nel nostro repository su <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica">GitHub</a>.</p>

<p>Per esempi più approfonditi e dettagliati, ti invitiamo a unirti a noi nel nostro libro: 📕 "<a href="https://www.amazon.it/stores/author/B07SLZYLC4/allbooks">Bitcoin In Action - SegWit, Bitcoin Script e Smart Contracts</a>". Troverai ulteriori dettagli, spiegazioni approfondite e esempi pratici per approfondire la tua comprensione di SegWit, Bitcoin Script e Smart Contracts. </p>

<figure class="wp-block-image size-full"><img src="https://www.corsobitcoin.com/wp-content/uploads/2024/01/image-1.png" alt="Creazione di un Indirizzo Multisignature P2SH-P2PKH Bitcoin: Guida Dettagliata" class="wp-image-13769"/></figure>

<hr class="wp-block-separator has-alpha-channel-opacity"/>

<p>📌 <a href="https://linktr.ee/satoshiwantsyou" rel="noreferrer noopener" target="_blank">https://linktr.ee/satoshiwantsyou</a></p>

