---
title: "Che cosa contiene il P2SH?"
date: 2021-04-26T10:00:00+01:00
slug: "che-cosa-contiene-il-p2sh"
draft: false
author: "Alessio Barnini"
description: "Video completo sul nostro canale YouTube – Bitcoin in Action!"
cover: "/img/posts/che-cosa-contiene-il-p2sh-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### **Che cosa contiene il P2SH**? #### [Video completo sul nostro canale YouTube – Bitcoin in Action!](https://www.youtube.com/BitcoinInAction)

![P2SH: Come è costruito?](/img/posts/che-cosa-contiene-il-p2sh-1.webp)
*P2SH: Come è costruito?*

Entriamo nel vivo dell’address **Pay to script Hash**. Come dicevamo nel precedente [video](https://youtu.be/Aa1pTzC67Io), l’utente andrà a pagare ad un **hash** di uno script.

Collegandoci agli address affrontati precedentemente, abbiamo potuto capire che le condizioni necessarie per sbloccare la transazione sono dichiarate all’interno dello **scriptPubKey**, che storicamente prende il nome anche di locking script.

In un address **Pay To Script Hash**, è possibile inserire qualsiasi tipo di **script**, anche custom.

Con lo script custom sarà l’utente a prendersi la responsabilità di scrivere un *giusto* script.

Con questo che cosa voglio dire? Non è obbligatorio inserire la firma digitale all’interno di uno script, è possible inserire anche una semplice uguaglianza.

Facciamo un esempio. 
Immaginiamo che nello **scriptPubKey** sia presente uno script del genere OP_1 OP_EQUAL.

Vi sembra sicuro? È vero che, come vedremo successivamente, lo script in chiaro si vede solo se il proprietario dell’address ha effettuato almeno una transazione, perchè come il nome dello script stesso ci suggerisce, nello scriptPubKey troveremo l’hash.

Ma è anche vero che dopo la prima transazione, chiunque è in grado di inserire un OP_1 per soddisfare l’uguaglianza, proprio perchè questa condizione (OP_1 OP_EQUAL) sarà visibile nello scriptSig.

Ecco perchè si usano le firme digitali che risolvono dei problemi fondamentali, quali:

- **Integrità**: Il messaggio non deve essere alterato durante la trasmissione. Bob manda un messaggio a Alice con scritto W i bitcoin. 
Peter lo intercetta cambiandolo con W gli ether. 
Alice deve essere in grado di accorgersi di tale cambiamento.
- **Autenticità**: Alice deve essere sicura che il messaggio che ha ricevuto sia stato inviato da Bob, e non da Peter che si è spacciato per Bob.
- **Non ripudio**: Il mittente non potrà disconoscere il messaggio che ha firmato.

Quindi abbiamo capito che è compito dell’utente gestire uno script custom, in più, se si utilizza uno script custom dovremo **firmare manualmente la transazione**, come spiegato nel libro [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://bit.ly/38RtF9x).

![Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](/img/posts/che-cosa-contiene-il-p2sh-2.webp)
*Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts*

Vediamo invece come è costruito un address **P2SH-P2PK**, ovvero un address che racchiude lo script **P2PK**.

Facendo riferimento all’esempio di prima, nello scriptPubKey ci saranno le condizioni che abbiamo trovato nel [video P2PK](https://youtu.be/iVWMaGO3m48), ovvero: Public Key OP_CHECKSIG.

Questo è conosciuto anche come **redeem script**.

Ma quando viene dichiarato? Durante la generazione dell’address, subito dopo aver ottenuto la chiave pubblica compressa, ([se non ti ricordi di che cosa sto parlando guarda i video precedenti](https://www.youtube.com/playlist?list=PLpPLK7SGHncZVl_ZQkqyXGMDGWEx7U_et)), viene costruito il redeem script. **Redeem script = PB OP_CHECKSIG** Successivamente ci vengono applicate le funzioni crittografiche, **SHA256** e **RIPEMD160**, ottenendo così il **redeem script Hash**.

Al digest ottenuto viene aggiunto l’address prefix e applicato l’encoding base58 comprensivo di checksum.

Piccolo Spoiler:

Vi ricorda niente **SHA256 e RIPEMD160**? Esatto sono le stessa operazioni che si ottengono con l’ **OP_HASH160**, e dopo vedremo perchè!

In questo modo è possibile ottenere un P2SH che wrappa, un P2PK.

> In [informatica](https://it.wikipedia.org/wiki/Informatica), e in particolare in [programmazione](https://it.wikipedia.org/wiki/Programmazione_%28informatica%29), è un modulo software che ne “riveste” un altro.

Come si ottiene un P2SH che Wrappa un P2PKH?

![P2SH — Guarda il video completo sul canale Youtube Bitcoin in Action](/img/posts/che-cosa-contiene-il-p2sh-3.webp)
*P2SH — Guarda il video completo sul canale Youtube Bitcoin in Action*

Il Redeem script sarà composto dallo script del P2PKH: OP_DUP OP_HASH160 <PubKHash> OP_EQUALVERIFY OP_CHECKSIG e successivamente applicate le stesse funzioni crittografiche e di encoding al fine di ottenere l’address.

Nella prossima lezione vedremo con la pratica come analizzare un Address P2SH!

Ciao!


