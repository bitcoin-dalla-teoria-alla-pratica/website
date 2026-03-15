---
title: "Il titolo de 'The Times' nella blockchain Bitcoin."
date: 2019-05-06T21:31:56+01:00
draft: false


tags:
  - "Crittografia"
  - "UTXO"
---




<p>Abbiamo spesso sentito che un titolo del celebre giornale “The Times” è inserito dentro la blockchain <strong>Bitcoin</strong>.</p>
<p>Ma esattamente dove è inserito? <br />Come è stato possibile?</p>
<p>È una storia romantica se vogliamo, infatti <strong>Satoshi Nakamoto</strong>, il creatore di <strong>Bitcoin,</strong> ha lasciato un messaggio nel blocco genesi della blockchain Bitcoin.</p>
<p>Il blocco genesi è il primo blocco della blockchain, ed è <em>hardcodato</em> cioè inserito manualmente. </p>
<p>All’interno della <strong>coinbase </strong>possiamo leggere la famosa frase.</p>
<!-- HTML generated using hilite.me -->

```bash
04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```

<p>Tale frase ha un duplice significato, testimoniare la data del primo blocco, e la nascita di un nuovo sistema monetario indipendente.</p>
<p>Ma che cosa c’è scritto in questo esadecimale? <br />Come è possibile recuperarlo ed interpretarlo?</p>
<!-- HTML generated using hilite.me -->

```bash
bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 2
```

<p>Analizzando l’output ottenuto, possiamo leggere <strong>coinbase</strong>, seguito dal suo valore in esadecimale.</p>
<!-- HTML generated using hilite.me -->

```bash
{
  "hash": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
  "confirmations": 574888,
  "strippedsize": 285,
  "size": 285,
  "weight": 1140,
  "height": 0,
  "version": 1,
  "versionHex": "00000001",
  "merkleroot": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
  "tx": [
    {
      "txid": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
      "hash": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
      "version": 1,
      "size": 204,
      "vsize": 204,
      "weight": 816,
      "locktime": 0,
      "vin": [
        {
          "coinbase": "04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73",
          "sequence": 4294967295
        }
      ],
      "vout": [
        {
          "value": 50.00000000,
          "n": 0,
          "scriptPubKey": {
            "asm": "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f OP_CHECKSIG",
            "hex": "4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac",
            "reqSigs": 1,
            "type": "pubkey",
            "addresses": [
              "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
            ]
          }
        }
      ],
      "hex": "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"
    }
  ],
  "time": 1231006505,
  "mediantime": 1231006505,
  "nonce": 2083236893,
  "bits": "1d00ffff",
  "difficulty": 1,
  "chainwork": "0000000000000000000000000000000000000000000000000000000100010001",
  "nTx": 1,
  "nextblockhash": "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"
}
```

<p>Adesso possiamo convertire l’esadecimale in ASCII.</p>
<!-- HTML generated using hilite.me -->

```bash
echo 04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73 | xxd -r -p
```

<p>Ottenendo così il titolo de “The Times” del 3 gennaio 2009.</p>
<figure><img src="https://www.corsobitcoin.com/wp-content/uploads/2019/05/satoshi-nakamoto-the-times-bitcoin-corso-italiano-791x1024.jpg" alt="Il titolo de 'The Times' nella blockchain Bitcoin." width="396" height="512" /></figure>
