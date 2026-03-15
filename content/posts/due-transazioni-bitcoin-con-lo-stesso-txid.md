---
title: "Due transazioni con lo stesso txid"
date: 2019-04-29T11:00:19+01:00
draft: false


tags:
  - "Crittografia"
  - "UTXO"
---




<figure>
										<img width="300" height="300" src="http://www.corsobitcoin.com/wp-content/uploads/2019/04/s-l300.jpg" alt="Bitcoin dalla teoria alla pratica - two bad Master of the universe" srcset="https://i2.wp.com/www.corsobitcoin.com/wp-content/uploads/2019/04/s-l300.jpg?w=300 300w, https://i2.wp.com/www.corsobitcoin.com/wp-content/uploads/2019/04/s-l300.jpg?resize=150%2C150 150w" sizes="(max-width: 300px) 100vw, 300px" />											<figcaption>Two bad - master of the universe</figcaption>
										</figure>
		<p>Un pò di tempo fa il protocollo <strong>Bitcoin</strong> fece nascere due transazioni con lo stesso identificativo. <br />Cercando la transazione con id <strong>e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468</strong>:</p>
<p><!-- HTML generated using hilite.me --></p>

```bash
bitcoin-cli getrawtransaction 
e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468 
true
```

<p><br />Risultato:<br /><!-- HTML generated using hilite.me --></p>

```bash
...
{
  "txid": 
"e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468
",
... altre informazioni ...
  "blockhash": 
"00000000000743f190a18c5577a3c2d2a1f610ae9601ac046a38084ccb7cd72"
,
  "confirmations": 481756,
  "time": 1289781379,
  "blocktime": 1289781379
}
...
```

<p><br />Otteniamo l’hash del blocco che contiene la transazione.<br />Analizziamo un altro blocco.<br /><!-- HTML generated using hilite.me --></p>

```bash
bitcoin-cli getblock 
00000000000271a2dc26e7667f8419f2e15416dc6955e5a6c6cdf3f2574dd08e
```

<p><br />Risultato:</p>
<p><!-- HTML generated using hilite.me --></p>

```bash
{
 "hash": "00000000000271a2dc26e7667f8419f2e15416dc6955e5a6c6cdf3f2574dd08e",
...
 "tx": [
 "e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468"
 ],
 ...
}
```

<p>Come è possibile che una transazione sia inclusa dentro a due blocchi? Siamo davanti al tanto temuto <strong>double spending</strong>? <br />No.<br />Partiamo dicendo che il protocollo Bitcoin non vieta la possibilità di creare due transazioni con lo stesso <strong>txid</strong>, ma sicuramente non porta benefici.</p>
<ul>
<li>Il primo indizio è che la transazione che stiamo esaminando è una <strong>coinbase</strong></li>
<li>Il secondo indizio è che è stato lo stesso miner a risolvere entrambi i blocchi.</li>
<li>Il terzo indizio è che entrambi i reward erano di 50 bitcoin.</li>
</ul>
<p>Come si forma la transaction id? <br />Applicando la funzione crittografica <strong>SHA256</strong> per due volte sulla transaction data e girando l’ordine dei bytes in<strong> little-endian</strong>. La transaction data è formata da: </p>
<ul>
<li>La version della transazione</li>
<li>Numero di input</li>
<li>Input (scriptsig)</li>
<li>Numero di output</li>
<li>Output (scriptPubKey)</li>
<li>Locktime</li>
</ul>
<p>La transaction data della txid che stiamo esaminando è la seguente:</p>
<p><!-- HTML generated using hilite.me --></p>

```bash
01000000010000000000000000000000000000000000000000000000000000000
000000000ffffffff060456720e1b00ffffffff0100f2052a0100000043410412
4b212f5416598a92ccec88819105179dcb2550d571842601492718273fe0f2179
a9695096bff94cd99dcccdea7cd9bd943bfca8fea649cac963411979a33e9ac00
000000
```

<p><br />Facendo il doppio SHA256 e girando l’ordine dei bytes in little endian, otteniamo la txid incriminata.</p>
<p><!-- HTML generated using hilite.me --></p>

```bash
printf `printf 01000000010000000000000000000000000000000000000000000000000000000
000000000ffffffff060456720e1b00ffffffff0100f2052a0100000043410412
4b212f5416598a92ccec88819105179dcb2550d571842601492718273fe0f2179
a9695096bff94cd99dcccdea7cd9bd943bfca8fea649cac963411979a33e9ac00
000000 | xxd -r -p | sha256sum -b | xxd -r -p | sha256sum -b` | 
tac -rs ..
```

<p>risultato:<br /><strong>e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468</strong></p>
<p>Esatto, le due transazioni hanno lo stesso identico transaction data, ecco perchè hanno lo stesso <strong>txid</strong>!<br />Per evitare questo problema è stato introdotto il <a href="https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki" target="_blank" rel="noreferrer noopener">BIP-34</a>, che obbliga ad inserire l’altezza del blocco all’interno dello scriptSig, risolvendo così il problema.</p><p></p>
<figure><img src="https://www.corsobitcoin.com/wp-content/uploads/2019/04/Screenshot-2019-04-28-at-20.39.25-1024x763.png" alt="Due transazioni con lo stesso txid" />
<p> </p>
<figcaption><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Slide del corso "</a><strong><a href="https://www.udemy.com/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?couponCode=WP_WORDPRESS" target="_blank" rel="noreferrer noopener" aria-label=" (si apre in una nuova scheda)">Bitcoin dalla teoria alla pratica — corso completo"</a></strong></figcaption>
</figure>
<p></p>
<p></p>