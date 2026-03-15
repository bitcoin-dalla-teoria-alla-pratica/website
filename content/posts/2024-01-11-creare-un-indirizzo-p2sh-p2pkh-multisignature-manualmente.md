---
title: "Creare un Indirizzo P2SH-P2PKH Multisignature manualmente"
date: 2024-01-11T10:00:00+01:00
slug: "creare-un-indirizzo-p2sh-p2pkh-multisignature-manualmente"
draft: false
author: "Alessio Barnini"
description: "In Bitcoin in Action, siamo appassionati di svelare i segreti di Bitcoin. Oggi, ci immergeremo nelle profondità del protocollo, creando…"
images: ["https://cdn-images-1.medium.com/max/1200/0*tTDhT_QA5Euio5Jo.png"]
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Privata"
categories:
  - "Bitcoin"
---

---

In Bitcoin in Action, siamo appassionati di svelare i *segreti* di Bitcoin.

Oggi, ci immergeremo nelle profondità del protocollo, creando manualmente un indirizzo **P2SH-P2PKH multisig**.

Perché ci prendiamo il tempo di farlo? Semplice: vogliamo capire appieno il funzionamento di Bitcoin sotto il cofano.

Naturalmente, è possibile generare un indirizzo simile utilizzando Bitcoin Core (ma tranquilli, approfondiremo questo argomento in un futuro articolo, concentrandoci su un SegWit multisig).

Ricordatevi che tutto il codice che useremo nei nostri libri, nei video e negli articoli, potete trovarlo su GitHub: [https://github.com/bitcoin-dalla-teoria-alla-pratica/](https://github.com/bitcoin-dalla-teoria-alla-pratica/).

Per questo esempio, opteremo per l’utilizzo di chiavi pubbliche compresse. Cominciamo creando tre chiavi private attraverso la bash, attraverso un ciclo di 3 iterazioni.

```bash
for i in 1 2 3do printf "\n \e[31m ######### Create private key and public key ${i} #########\e[0m\n\n" #private key openssl ecparam -genkey -name secp256k1 -rand /dev/urandom -out private_key_$i.pem #private key bitcoin openssl ec -in private_key_$i.pem -outform DER|tail -c +8|head -c 32 |xxd -p -c 32 > btc_priv_$i.key #uncompressed private key printf "\n \n 🗝 Uncompressed private key WIF $i \n" C=`printf $VERSION_PREFIX_PB$(<btc_priv_$i.key) | xxd -r -p | base58 -c` printf $C"\n" printf $C > uncompressed_private_key_WIF_$i.txt #Compressed private key printf "\n \n 🗝 Compressed private key WIF $i \n" C=`printf $VERSION_PREFIX_PB$(<btc_priv_$i.key)"01" | xxd -r -p | base58 -c` printf $C"\n" printf $C > compressed_private_key_WIF_$i.txt #Uncompressed public key openssl ec -in private_key_$i.pem -pubout -outform DER|tail -c 65|xxd -p -c 65 > btc_pub_$i.key printf "\n \n 🔑 Uncompressed public key $i \n" cat btc_pub_$i.key > uncompressed_public_key_$i.txt cat uncompressed_public_key_$i.txt #Compressed Address legacy printf "\n \n 🔑 Compressed Address legacy ${i}\n" ADDR_SHA=`printf $(cat uncompressed_public_key_$i.txt) | xxd -r -p | openssl sha256| sed 's/^.* //'` ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed 's/^.* //'` # echo $ADDR_RIPEMD160 ADDR=`printf $VERSION_PREFIX_ADDRESS$ADDR_RIPEMD160 | xxd -p -r | base58 -c` echo $ADDR > uncompressed_btc_address_$i.txt echo $ADDR #Check the last byte. U=`cat btc_pub_$i.key | cut -c 129-131` U=`echo "$U" | tr '[:lower:]' '[:upper:]'` U=`echo "ibase=16; $U" | bc` if [ $(($U%2)) -eq 0 ]; then #key even PREF=02 else #key odd PREF=03 fi #Compressed public key printf "\n \n 🔑 Compressed public key ${i}\n" cat btc_pub_$i.key | tr -d " \t\n\r" | tail -c $((64*2)) | sed 's/.\{64\}/& /g'| awk '{print $1}'| sed -e 's/^/'$PREF/ > compressed_public_key_$i.txt cat compressed_public_key_$i.txtdone
```

#### **Creazione delle Chiavi: Un Mondo da Esplorare** Il codice mostrato sopra ha generato con successo tre chiavi private e le rispettive chiavi pubbliche. Se siete curiosi di capire come vengono create le chiavi private e come derivano le chiavi pubbliche, non perdetevi l’ [articolo](https://bitcoin-in-action.medium.com/come-si-ottiene-laddress-p2pk-34a47c30bbfe) completo e il nostro libro “[Bitcoin dalla teoria alla pratica](https://amzn.to/2MOj1av)”.

Ora, entriamo nella parte successiva della nostra esplorazione: la creazione del redeem script.

```bash
SCRIPT="5221"$(cat compressed_public_key_1.txt)"21"$(cat compressed_public_key_2.txt)"21"$(cat compressed_public_key_3.txt)"53AE"
```

Il **redeem script** è un componente chiave, rappresentando le condizioni necessarie per sbloccare l’UTXO.

Diamo uno sguardo più approfondito a cosa contiene e quale ruolo svolge nel contesto di Bitcoin.

#### Decodificando il Redeem Script: Un’Analisi Dettagliata

Facendo riferimento alla documentazione ufficiale di Bitcoin Script [https://en.bitcoin.it/wiki/Script](https://en.bitcoin.it/wiki/Script), possiamo capire ciò che contiene il nostro script.

Il redeem script che abbiamo generato è composto dai seguenti elementi:

- `52`: Rappresenta l'OP_CODE `OP_2`. In altre parole, questo indica l'inizio di una sequenza che coinvolgerà due elementi nello stack.
- `21`: Indica quanti byte verranno successivamente inseriti nello stack. Convertendo `0x21` in decimale otteniamo 33. Dato che un byte è rappresentato da due caratteri esadecimali, avremo esattamente 66 caratteri esadecimali. Questo è il punto in cui la nostra chiave pubblica compressa entra in gioco.

```bash
cat compressed_public_key_1.txt | wc -m66
```

- `53`: Rappresenta l'OP_CODE `OP_3`. Ora, stiamo inserendo un'altra sequenza nello stack che coinvolgerà tre elementi.
- `AE`: Rappresenta l'OP_CODE `OP_CHECKMULTISIG`. Questo indica che il redeem script include ora l'operazione di verifica multisignature.

Per comodità, salviamo questo script per ulteriori analisi e riferimenti.

```bash
printf $SCRIPT > redeem_script.txt
```

#### **Redeem Script: Applicazione di SHA256 e RIPEMD160** In una fase successiva del nostro percorso, applicheremo l’hash SHA256 e RIPEMD160 al redeem script che abbiamo creato. Questa è una parte cruciale del processo di creazione di un indirizzo Bitcoin P2SH-P2PKH.

![P2SH — Guarda il video completo sul canale Youtube Bitcoin in Action](https://cdn-images-1.medium.com/max/1200/0*tTDhT_QA5Euio5Jo.png)
*P2SH — Guarda il video completo sul canale Youtube Bitcoin in Action*

```bash
 ADDR_SHA=`printf $SCRIPT | xxd -r -p | openssl sha256| sed 's/^.* //'` ADDR_RIPEMD160=`printf $ADDR_SHA |xxd -r -p | openssl ripemd160 | sed 's/^.* //'` printf $ADDR_RIPEMD160 > scriptPubKey.txt printf "\n \n\e[46m ---------- scriptPubKey --------- \e[49m\n" printf $ADDR_RIPEMD160 #ADDRESS printf "\n \n\e[46m ---------- 🔑 ADDRESS P2SH️ --------- \e[49m\n" ADDR=`printf $VERSION_PREFIX_ADDRESS$ADDR_RIPEMD160 | xxd -p -r | base58 -c` echo $ADDR > address_P2SH.txt echo $ADDR
```

In questo blocco di codice:

- `ADDR_SHA` contiene l'hash SHA256 del redeem script.
- `ADDR_RIPEMD160` contiene l'hash RIPEMD160 dell'hash SHA256.

Questo ci porterà allo **scriptPubKey**, che è essenziale per ottenere l’indirizzo Bitcoin P2SH-P2PKH.

Se vuoi seguire passo dopo passo questo processo, ti suggerisco di dare un’occhiata all’articolo dettagliato su [https://bitcoin-in-action.medium.com/come-si-ottiene-address-bitcoin-p2sh-f009f28206b7](https://bitcoin-in-action.medium.com/come-si-ottiene-address-bitcoin-p2sh-f009f28206b7).

Infine, applicheremo il “Version Prefix” e il processo di Base58Check per ottenere il nostro indirizzo Bitcoin P2SH-P2PKH. Per la regtest e testnet, il “Version Prefix” è 0xC4.

> `ADDR` contiene l'indirizzo Bitcoin P2SH-P2PKH ottenuto applicando il "Version Prefix" e il processo di Base58Check all'hash RIPEMD160.

Concludiamo così la creazione manuale dell’indirizzo Bitcoin P2SH-P2PKH. L’indirizzo è ora pronto per essere utilizzato nella rete regtest o testnet.

> Base58 evita di utilizzare caratteri ambigui come lo 0 (zero) e O.

> 123456789

> ABCDEFGHJKLMNPQRSTUVWXYZ

> abcdefghijkmnopqrstuvwxyz

Da notare che il nostro indirizzo inizierà con il numero 2, una caratteristica specifica dei P2SH nelle reti regtest/testnet.

```bash
######### P2SH ######### ---------- Redeem Script ---------522102bd13132bea99bcd50f93dedc6cab13e0f973a8a5f6aec0150f9e835ce41bcbf42102a95dc9d317e57da0ad149eca4cc85aa2665cbb35ced8ccf41c0aec3d5c0333672102ebf7690e84552c3c01a5f01ecd4a1442fb411b501c29c91b7ff27766c8a494f453AE ---------- scriptPubKey ---------03d9f8e4487229f0bd3f3af5ce4b6301930f18de ---------- 🔑 ADDRESS P2SH️ ---------2Msbb8qRdT5N3YJYc8BDbQ25sMJQUuKUKMW
```

Per chi fosse interessato al codice completo, è disponibile nel in questo gist oltre che nel nostro repository

Per esempi più approfonditi, unisciti a noi nel nostro libro:

📕 [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://amzn.to/3pJcXj1)

![📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://cdn-images-1.medium.com/max/1200/1*imG__98FnJWdFN9KT0cgRQ.jpeg)
*📕Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts*

---

📌 [https://linktr.ee/satoshiwantsyou](https://linktr.ee/satoshiwantsyou)

Television isn’t a good idea (Radio Stations) 
Email isn’t a good idea (Post offices) 
Amazon isn’t a good idea (Retail stores) 
Bitcoin isn’t a good idea (Central banks)

In **crypto** we trust
