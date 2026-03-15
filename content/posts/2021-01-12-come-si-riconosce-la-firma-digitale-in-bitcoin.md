---
title: "Come si riconosce la firma digitale in Bitcoin?"
date: 2021-01-12T10:00:00+01:00
slug: "come-si-riconosce-la-firma-digitale-in-bitcoin"
draft: false
author: "Alessio Barnini"
description: "Nel video precedente, abbiamo analizzato con la pratica come la transazione viene P2PK viene validata."
cover: "/img/posts/come-si-riconosce-la-firma-digitale-in-bitcoin-4.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### Come si riconosce la firma digitale in Bitcoin?

![https://youtu.be/kussfH_U6Ow](/img/posts/come-si-riconosce-la-firma-digitale-in-bitcoin-4.webp)
*https://youtu.be/kussfH_U6Ow*

Nel [video precedente](https://youtu.be/SMDeoY9x3HY), abbiamo analizzato con la pratica come la transazione viene **P2PK** viene validata.

Ci si potrebbe domandare: Come riesce il software a sapere cosa inserire all’interno dello stack?

Come spiegato nei [precedenti video](https://www.youtube.com/BitcoinInAction), Bitcoin utilizza script, linguaggio di programmazione necessario per validare lo stack.

Prima di analizzare come lo stack riesce a capire cosa inserire al suo interno, è necessario spiegare alcune informazioni di base.

---

Il **bit** è l’acronimo di **binary digit**, ed è un’unità di misura informatica.

0 spento  
1 acceso

Il **byte** è formato da 8 bit (2⁸).

Il **nibble** invece è formato da 4 bit.

---

Analizziamo anche i sistemi di numerazione. **Base2**, sistema di numerazione binaria, base della potenza è due. Simboli a disposizione sono 0 e 1.

```bash
10 = (1*2¹+0*2⁰) = (1*2+0*1) = 2
```


Ed ecco come il simbolo 10 corrisponde a **2** in **base10**. **Base10**, sistema di numerazione decimale, ha come base della potenza è 10, ed è quello che utilizziamo noi umani. 
I simboli a disposizione sono da 0–9.  
Prendendo come riferimento l’esempio precedente, vediamo come è interpretiamo il numero 5201.

```bash
5201=(5*10³+2*10²+0*10¹+1*10⁰) = 5000+200+0+1 = 5201.
```


Piu semplicemente, ogni elemento viene moltiplicata per la sua posizione, per questo si chiama anche sistema di [numerazione posizionale](https://it.wikipedia.org/wiki/Sistema_di_numerazione_posizionale).

![](/img/posts/come-si-riconosce-la-firma-digitale-in-bitcoin-2.webp)

```bash
5*1000 + 2*100 + 0*10 + 1*1 = 5201
```


Ogni unità viene moltiplicata per la sua posizione, ottenendo così:

```bash
5*1000 + 2*100 + 0*10 + 1*1 = 5201
```


Il sistema esadecimale, o **base16** o **hex**, è formato da 16 simboli

```bash
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, A, B, C, D, E, F.
```


> Ogni carattere esadecimale corrisponde a un **nibble**, per questo motivo è possibile rappresentare 1 byte con due caratteri esadecimali.

Ad esempio il numero 52 corrisponde a 0x34

![il numero 52 corrisponde a 34 in esadecimale.](/img/posts/come-si-riconosce-la-firma-digitale-in-bitcoin-3.webp)
*il numero 52 corrisponde a 34 in esadecimale.*

Il numero 52 in base due è rappresentato da 0011 0100, in totale 1 byte, 8 bit. 
Dato che un carattere esadecimale può essere rappresentato da un nibble, possiamo dividerlo a “meta”, 4 bit e 4 bit

```bash
0011 = (0*2³)+(0*2²)+(1*2¹)+(1*2⁰) = 0+0+2+1 = 30100 = (0*2³)+(1*2²)+(0*2¹)+(0*2⁰) = 0+4+0+0 = 4
```


Potete utilizzare il comando obase, per ottenere numeri in esadecimale

```bash
$ echo "obase=16;52" | bc34
```


---

Arriviamo quindi al momento di analizzare la transazione dell’[articolo precedente](https://bitcoin-in-action.medium.com/transazione-p2pk-bitcoin-e9bc4dc7870d):

```bash
$ bitcoin-cli getrawtransaction f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16 2 | jq

...

"scriptSig": {"asm": "304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d09[ALL]","hex": "47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901"},
```


Analizziamo il primo dello scriptSig, ovvero l’esadecimale 47.

47 non è mappato su nessuna [Operation code](https://duckduckgo.com/?q=bitcoin+script&ia=web), ma ci indica quanti elementi prendere successivamente.

Ricorda che sono caratteri esadecimali, quindi per sapere il numero in base10 dobbiamo convertire 47 in base10.

quindi:

```bash
(4*16¹) + (7*16⁰) = 71
```


Sappiamo che un byte può essere rappresentato da 2 caratteri esadecimali, quindi:

```bash
71*2 = 144
```


Quindi saranno 144 i caratteri esadecimali da prendere in considerazione. 
Ed ecco come 47 ci indicati inserire 144 esadecimali nello stack (quelli in italico)

```bash
47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901
```


I quali rappresentano la firma digitale.  
Successivamente si inserisce lo **scriptPubKey**, della UTXO ([0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9](https://btc.bitaps.com/0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9)) di riferimento. 
Lo scriptPubKey viene interpretato nel medesimo modo.

```bash
"vout": [

{

"value": 50,

"n": 0,

"scriptPubKey": {

"asm": "0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3 OP_CHECKSIG",

"hex": "410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac",

"type": "pubkey"

}

}

],
```


Il primo byte che troviamo è **41**, il quale ricade nel range delle costanti di Bitcoin script e ci indica quanti caratteri esadecimali prendere successivamente.

```bash
410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac
```


41 in base10 corrisponde a 65. Sappiamo che 1 byte può essere rappresentato da 2 caratteri esadecimale:

```bash
65*2 = 130
```


Dobbiamo inserire 130 caratteri esadecimali all’interno dello stack, i quali corrispondono alla chiave pubblica **NON** compressa.

Il byte successivo è rappresentato da **ac**. Attenzione l’esadecimale **0xac** è tappato sull’operato code **OP_CHECKSIG**.

Quindi viene inserito nello stack.

Successivamente, come abbiamo affrontato nel [precedente video](https://youtu.be/SMDeoY9x3HY), lo stack viene validato.

![Estratto dell’articolohttps://bitcoin-in-action.medium.com/transazione-p2pk-bitcoin-e9bc4dc7870d](/img/posts/come-si-riconosce-la-firma-digitale-in-bitcoin-4.webp)
*Estratto dell’articolohttps://bitcoin-in-action.medium.com/transazione-p2pk-bitcoin-e9bc4dc7870d*

![I nostri libri disponibili su corsobitcoin.com](/img/posts/come-si-riconosce-la-firma-digitale-in-bitcoin-5.webp)
*I nostri libri disponibili su corsobitcoin.com*
