---
title: "Creare e Firmare una Transazione Bitcoin Multisig P2SH"
date: 2024-03-22T10:00:00+01:00
slug: "creare-e-firmare-una-transazione-bitcoin-multisig-p2sh"
draft: false
author: "Alessio Barnini"
description: "Nel precedente articolo abbiamo visto come creare un address P2SH Multisig, in questo articolo vedremo come firmarlo"
cover: "/img/posts/creare-e-firmare-una-transazione-bitcoin-multisig-p2sh-1.webp"
tags:
  - "Bitcoin"
  - "Bitcoin Script"
  - "Fee"
categories:
  - "Bitcoin"
---

---

### Creare e Firmare una Transazione Bitcoin Multisig P2SH

Nel precedente articolo abbiamo visto come creare un [address P2SH Multisig](https://bitcoin-in-action.medium.com/creare-un-indirizzo-p2sh-p2pkh-multisignature-manualmente-f946a225a586), in questo articolo vedremo come firmarlo

Come sempre utilizziamo l’ambiente di [Docker](https://github.com/bitcoin-dalla-teoria-alla-pratica/bitcoin-in-action-youtube-docker) che abbiamo a disposizione

> in Action

Utilizzeremo i [wallet descriptor come spiegato in questo articolo](https://bitcoin-in-action.medium.com/wallet-bitcoin-differenze-tra-wallet-legacy-vs-wallet-descriptor-513b0faa4dd4), qiundi avvio la regtest completamente pulita e creo il wallet

```bash
bitcoin-cli stop && sleep 5 && rm -Rf $HOME/.bitcoin/regtest && bitcoind && sleep 5bitcoin-cli -named createwallet wallet_name="bitcoin in action"
```

Successivamente recupero l’address che avevamo creato [nell’articolo precedente](https://bitcoin-in-action.medium.com/creare-un-indirizzo-p2sh-p2pkh-multisignature-manualmente-f946a225a586) e mino 101 blocchi cosi da avere 50 bitcoin a disposizione

```bash
ADDR_MITT=`bitcoin-cli getnewaddress "mittente" "legacy"`#Get P2SH addressADDR_DEST=`cat address_P2SH.txt`#Mint 101 blocks and get reward to spendbitcoin-cli generatetoaddress 101 $ADDR_MITT >> /dev/null
```

Una volta ottenuto il reward, salvo dentro le variabili, le informazioni necessarie per crearela prossima transazione verso l’address multisignature

```bash
TXID=$(bitcoin-cli listunspent 1 101 '["'$ADDR_MITT'"]' | jq -r '.[0].txid')VOUT=$(bitcoin-cli listunspent 1 101 '["'$ADDR_MITT'"]' | jq -r '.[0].vout')AMOUNT=$(bitcoin-cli listunspent 1 101 '["'$ADDR_MITT'"]' | jq -r '.[0].amount-0.001')printf "\n \e[31m######### TX_DATA #########\e[39m \n"TX_DATA=`bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_DEST'":'$AMOUNT'}]'`bitcoin-cli decoderawtransaction $TX_DATA | jq
```

Quello che otteniamo è qualcosa del genere

```bash
 ######### TX_DATA #########{ "txid": "8f5c26dbbadf64aba4e97ed36d90d9b45d1a2f514412b224857414da340e8a4a", "hash": "8f5c26dbbadf64aba4e97ed36d90d9b45d1a2f514412b224857414da340e8a4a", "version": 2, "size": 83, "vsize": 83, "weight": 332, "locktime": 0, "vin": [ { "txid": "22f0ddcbf458da9f43f0ea17dec31f800f2f2d6bba61723f76df649711f57e30", "vout": 0, "scriptSig": { "asm": "", "hex": "" }, "sequence": 4294967293 } ], "vout": [ { "value": 49.999, "n": 0, "scriptPubKey": { "asm": "OP_HASH160 e873186916376b9584872da96679c422b45bad16 OP_EQUAL", "desc": "addr(2NESJdkgbe9bmc7oaAisDXkNPiz16tqo4Xo)#6fndqkt5", "hex": "a914e873186916376b9584872da96679c422b45bad1687", "address": "2NESJdkgbe9bmc7oaAisDXkNPiz16tqo4Xo", "type": "scripthash" } } ]}
```

Come si può vedere nel vout (scriptPubKey) abbiamo

```bash
"asm": "OP_HASH160 e873186916376b9584872da96679c422b45bad16 OP_EQUAL",
```

ovvero lo script P2SH.

Siamo quindi pronti ad inviare la transazione e a minare 6 blocchi

```bash
TX_DATA_SIGNED=$(bitcoin-cli signrawtransactionwithwallet $TX_DATA | jq -r '.hex')TXID=`bitcoin-cli sendrawtransaction $TX_DATA_SIGNED`bitcoin-cli generatetoaddress 6 $ADDR_MITT
```

Adesso abbiamo a disposizione dei bitcoin da spendere dall’address P2SH.

Con questo comando

```bash
bitcoin-cli getrawtransaction $TXID 2 | jq -r
```

possiamo vedere quanti bitcoin ha l’address $ADDR_DEST ipotizzando che sia un address nuovo e che abbia una solo UTXO da utilizzare

```bash
bitcoin-cli getrawtransaction $TXID 2 | jq -r{ "txid": "6575f8a7c21cad84f20a658a48863414133ab29743aef99f70f5446a739b23b0", "hash": "6575f8a7c21cad84f20a658a48863414133ab29743aef99f70f5446a739b23b0", "version": 2, "size": 189, "vsize": 189, "weight": 756, "locktime": 0, "vin": [ { "txid": "22f0ddcbf458da9f43f0ea17dec31f800f2f2d6bba61723f76df649711f57e30", "vout": 0, "scriptSig": { "asm": "30440220540e9f7921c074503a2d422d11a3c7a77c35f60674debc420a425c07b2fe005a022074246df812ba4d644c8e21646f36be3c2ce76c4adab2ac7ab9564262d1f95a31[ALL] 02cbf09f88786b713dce56c1e2b468fb96711f916a37d8085209f29b8d8fe9b006", "hex": "4730440220540e9f7921c074503a2d422d11a3c7a77c35f60674debc420a425c07b2fe005a022074246df812ba4d644c8e21646f36be3c2ce76c4adab2ac7ab9564262d1f95a31012102cbf09f88786b713dce56c1e2b468fb96711f916a37d8085209f29b8d8fe9b006" }, "prevout": { "generated": true, "height": 1, "value": 50, "scriptPubKey": { "asm": "OP_DUP OP_HASH160 9bc88e5752f7afc9ead6d83d7d1ee341985085f9 OP_EQUALVERIFY OP_CHECKSIG", "desc": "addr(muifHfUx7LPiKzdCwGMdAZeJzxUtSmWazJ)#8w5jejp8", "hex": "76a9149bc88e5752f7afc9ead6d83d7d1ee341985085f988ac", "address": "muifHfUx7LPiKzdCwGMdAZeJzxUtSmWazJ", "type": "pubkeyhash" } }, "sequence": 4294967293 } ], "vout": [ { "value": 49.999, "n": 0, "scriptPubKey": { "asm": "OP_HASH160 e873186916376b9584872da96679c422b45bad16 OP_EQUAL", "desc": "addr(2NESJdkgbe9bmc7oaAisDXkNPiz16tqo4Xo)#6fndqkt5", "hex": "a914e873186916376b9584872da96679c422b45bad1687", "address": "2NESJdkgbe9bmc7oaAisDXkNPiz16tqo4Xo", "type": "scripthash" } } ], "fee": 0.001, "hex": "0200000001307ef5119764df763f7261ba6b2d2f0f801fc3de17eaf0439fda58f4cbddf022000000006a4730440220540e9f7921c074503a2d422d11a3c7a77c35f60674debc420a425c07b2fe005a022074246df812ba4d644c8e21646f36be3c2ce76c4adab2ac7ab9564262d1f95a31012102cbf09f88786b713dce56c1e2b468fb96711f916a37d8085209f29b8d8fe9b006fdffffff01606b042a0100000017a914e873186916376b9584872da96679c422b45bad168700000000", "blockhash": "1ae53d3f40eceba92c532cdfb99640636ac2da2a4a66c4424665d786aa05cb00", "confirmations": 6, "time": 1711103449, "blocktime": 1711103449}
```

Possiamo quindi creare l’amount da spostare e recuperare le tre chiavi private relative all’address in questione

```bash
AMOUNT=`bitcoin-cli getrawtransaction $TXID 2 | jq -r '.vout[0].value-0.0001'`VOUT=0PK1=`cat compressed_private_key_WIF_1.txt`PK2=`cat compressed_private_key_WIF_2.txt`PK3=`cat compressed_private_key_WIF_3.txt`
```

Siamo quindi pronti a importare il descriptor, ottenendo prima il suo checksum.

```bash
CHECKSUM=$(bitcoin-cli getdescriptorinfo "sh(multi(2,$PK1,$PK2,$PK3))" | jq -r.checksum)bitcoin-cli importdescriptors '[{ "desc": "sh(multi(2,'$PK1','$PK2','$PK3'))#'$CHECKSUM'", "timestamp": "now", "internal": true }]'
```

Salviamo il Reedem script in una variabile

```bash
REDEEM=`cat redeem_script.txt`
```

e creiamo lo scriptPubKey

```bash
SCRIPTPUBKEY="A914"`cat scriptPubKey.txt`"87"
```

Ricordate che lo scriptPubKey è cosi formato

```bash
# A9 => OP_HASH160# 14 => 20 bytes, 40 caratteri esadecimali da inserire nello stack $(expr `echo "ibase=16; $(printf 14 | tr '[:lower:]' '[:upper:]')" | bc` "*" 2 )# 87 => OP_EQUAL
```

siamo finalmente in grado di creare la transazione

```bash
TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'","redeemScript":"'$REDEEM'"}]' '[{"'$ADDR_MITT'":'$AMOUNT'},{"data":"636f72736f626974636f696e2e636f6d0a"}]')
```

ed infine di firmarla

```bash
TX_SIGNED=$(bitcoin-cli signrawtransactionwithwallet $TX_DATA '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'","redeemScript":"'$REDEEM'"}]' | jq -r '.hex')
```

ottnendo cosi la transazione firmata che potrebbe assomigliare a qualcosa del genere

```bash
bitcoin-cli decoderawtransaction $TX_SIGNED | jq{ "txid": "bb446403925d846ea4b60bcfc384dfc1ce7be7cb1fbb84f2a5b934e5e599bbf0", "hash": "bb446403925d846ea4b60bcfc384dfc1ce7be7cb1fbb84f2a5b934e5e599bbf0", "version": 2, "size": 365, "vsize": 365, "weight": 1460, "locktime": 0, "vin": [ { "txid": "6575f8a7c21cad84f20a658a48863414133ab29743aef99f70f5446a739b23b0", "vout": 0, "scriptSig": { "asm": "0 304402205b7a4971ae3842c94c9da7ecf64fd54b2d4769de02c87e6f7e22dd08a8e5271c022015848e673b28d4b924dd257838aa1d2727bbeaeebb484da30ae1fc4cc0c2923b[ALL] 304402204e66ffdd82cce4b2fef619f26774412a5f0745f7bd415fdfdfd7f5059335506502207309335c016d763a7624fe9155ced18727eb4e44a713d43608a5f2ea3795ba9b[ALL] 5221034b7e5d9998d4d123157019b100f45f284278ff12802c811ac16ba8122dbe1c7921032b7ba8b88703df89dea5c91a46c7d7e6926da3134e7e48da141b5ebcf1200e5d21032aa059f3c1f245802c228221b220395070b1b7ab7f693ac191603657c2654a2753ae", "hex": "0047304402205b7a4971ae3842c94c9da7ecf64fd54b2d4769de02c87e6f7e22dd08a8e5271c022015848e673b28d4b924dd257838aa1d2727bbeaeebb484da30ae1fc4cc0c2923b0147304402204e66ffdd82cce4b2fef619f26774412a5f0745f7bd415fdfdfd7f5059335506502207309335c016d763a7624fe9155ced18727eb4e44a713d43608a5f2ea3795ba9b014c695221034b7e5d9998d4d123157019b100f45f284278ff12802c811ac16ba8122dbe1c7921032b7ba8b88703df89dea5c91a46c7d7e6926da3134e7e48da141b5ebcf1200e5d21032aa059f3c1f245802c228221b220395070b1b7ab7f693ac191603657c2654a2753ae" }, "sequence": 4294967293 } ], "vout": [ { "value": 49.9989, "n": 0, "scriptPubKey": { "asm": "OP_DUP OP_HASH160 9bc88e5752f7afc9ead6d83d7d1ee341985085f9 OP_EQUALVERIFY OP_CHECKSIG", "desc": "addr(muifHfUx7LPiKzdCwGMdAZeJzxUtSmWazJ)#8w5jejp8", "hex": "76a9149bc88e5752f7afc9ead6d83d7d1ee341985085f988ac", "address": "muifHfUx7LPiKzdCwGMdAZeJzxUtSmWazJ", "type": "pubkeyhash" } }, { "value": 0, "n": 1, "scriptPubKey": { "asm": "OP_RETURN 636f72736f626974636f696e2e636f6d0a", "desc": "raw(6a11636f72736f626974636f696e2e636f6d0a)#ewaggvhr", "hex": "6a11636f72736f626974636f696e2e636f6d0a", "type": "nulldata" } } ]}
```

siamo finalmente in grado di inviarla

```bash
bitcoin-cli generatetoaddress 6 $ADDR_MITT
```

Ottenendo gli hash dei 6 blocchi

```bash
bitcoin-cli generatetoaddress 6 $ADDR_MITT[ "441a32ae9511faa4292516cff6809087db820ad2d683f1dcc5516b1fb9071c3f", "7b68f807d854b54af0a954fb31595d395fe999e97591adb3b392cede25fcde5f", "68751ccb18d19e47373244d29a6b33719e8d7619104499651eb2d8897c7228fa", "533db5b216108d277aabe11e69fdda41dbc6b0abf732a69cc6f8fce05c3c358f", "4d2413893a93f522df8ef83057a28c9ef7d7be0fa2735f0281b2fda8c27e2424", "4027a93d0babfbe0cc0a980b3c5e3cceef3f0dead9e0ac6236a8910c7d0b07a6"]
```

Analizziamo adesso grazie a [btcdeb](https://github.com/bitcoin-core/btcdeb) ([https://github.com/bitcoin-core/btcdeb](https://github.com/bitcoin-core/btcdeb)) come avviane la validazione passo passo

```bash
 btcdeb --tx=$TX_SIGNED --txin=$(bitcoin-cli getrawtransaction $TXID)
```

![](/img/posts/creare-e-firmare-una-transazione-bitcoin-multisig-p2sh-1.webp)

con il comando step, possiamo proseguire

![](/img/posts/creare-e-firmare-una-transazione-bitcoin-multisig-p2sh-2.webp)

vengono inserite le due chiavi pubbliche e il redeem script. 
I piu attenti avranno visti 0x come primo elemento dello stack, ecco il motivo:

> CHECKMULTISIG BUG: Esegue un pop in più sullo stack. Viene usato OP_0 come workaround.

![](https://cdn-images-1.medium.com/max/1200/1*7jMv7HpIXZSqBEKqcyhmAA.png)

successivamente viene applicata la funzione OP_HASH160 sul redeem script che successivamente sarà confrontata con OP_EQUAL

![](https://cdn-images-1.medium.com/max/1200/1*n7d4HIW3KL6D9ZbSJM_IDQ.png)

Successivamente saranno inserite nello stack le tre firme.

OP_CHECKMULTISIG ha proprio il compito di confrontarle le firma digitali con le chiavi pubbliche inserite nello stack, per validare la loro autenticità e integrità, in poche parole se sono valide.

![](https://cdn-images-1.medium.com/max/1200/1*LtU_Uypng9cgknD81yU0og.png)

transazione andata a buon fine!

Per esempi più approfonditi, unisciti a noi nel nostro libro:

📕 [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://amzn.to/3pJcXj1)

![](https://cdn-images-1.medium.com/max/1200/0*BW3reOjtXhapBdp5.jpeg)

📕 [Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts](https://amzn.to/3pJcXj1)

📌 [https://linktr.ee/satoshiwantsyou](https://linktr.ee/satoshiwantsyou)

Television isn’t a good idea (Radio Stations) 
Email isn’t a good idea (Post offices) 
Amazon isn’t a good idea (Retail stores) 
Bitcoin isn’t a good idea (Central banks)

In **crypto** we trust
