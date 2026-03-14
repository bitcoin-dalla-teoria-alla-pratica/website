---
title: "Transazioni in regtest"
date: 2020-02-03T09:14:42+01:00
draft: false


tags:
  - "Nodo & Network"
  - "Crittografia"
---




<h4>Come posso creare una transazioni tra due nodi?</h4><section>
<hr>
<p><a href="https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353">Nel tutorial precedente</a> abbiamo visto come sia possibile far comunicare due nodi sullo stesso computer e come si sincronizzano quando dei blocchi vengono minati.&nbsp;</p>
<p>Q: Quindi possiamo fare anche una transazione e vedere che essa sia propagata e capire tutti i passaggi che subisce prima che faccia parte della blockchain?<br>R: Si.</p>
<figure>
Se volete avere un ambiente “pulito” potete cancellare le cartelle regtest dei rispettivi nodi, così da avere zero blocchi minati e nessun reward assegnato.
</figure>
<p>Inseriamo in entrambi i nodi l’opzione txindex=1 in modo tale da avere tutta l’indicizzazione delle transazioni.</p>
<blockquote>
<p>-txindex<br>Maintain a full transaction index, used by the getrawtransaction rpc<br>call (default: 0)</p>
</blockquote>
<pre>$ vim bitcoin_nodo2.conf</pre>
<figure><a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/"><img src="https://cdn-images-1.medium.com/max/1600/1*rRinDepzLOWMv7d0lbjScw.png" data-image-id="1*rRinDepzLOWMv7d0lbjScw.png" data-width="479" data-height="292"></a></figure>
<p>stessa operazione per il nodo di default il cui percorso (default) nel mio computer è:</p>
<pre>/Users/barno/Library/Application Support/Bitcoin/bitcoin.conf</pre>
<p>Avviamo di nuovo entrambi i nodi.<br>Se avete cancellato la cartella regtest (come me), dovete seguire i passaggi del <a href="https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353">tutorial precedente</a> così da avere a disposizione 50 bitcoin su un’indirizzo.<br><em>Già 50 bitcoin, nessun halving era ancora stato fatto.</em></p>
<p>Ottengo quindi 3 indirizzi, 2 dal nodo di default (bizantino) e 1 dal nodo2.</p>
<pre>$ ADDR=`bitcoin-cli getnewaddress bizantino`<br>$ ADDR_RESTO=`bitcoin-cli getnewaddress bizantino_resto`<br>$ ADDR_DEST=`bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getnewaddress destinatario`</pre>
<p>Dal nome delle variabili d’ambiente scelte si capisce il loro scopo.<br>Mino 101 blocchi per ottenere 50 bitcoin con l’indirizzo $ADDR.<br>Perché proprio 101? Per ottenere un reward spendibile e soddisfare la <strong>COINBASE_MATURITY</strong>.</p>
<pre>$ bitcoin-cli generatetoaddress 101 $ADDR</pre>
<p>Adesso entrambi i nodi devono avere 101 blocchi, se così non fosse torna al <a href="https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoindallateoriallapratica/utilizzare-i-file-di-configurazione-bitcoin-d93c6f9ac353">tutorial precedente</a>.</p>
<p>Con il comando <strong>listunpsent</strong> otteniamo tutte le UTXO disponibili.</p>
<pre>$ bitcoin-cli listunspent</pre>
<pre>[{<br>"txid": "75b91cf262c98bdd57b0c3f2ec1a2597cceadc0cc2ef0a103e1a0013d81e332f","vout": 0,<br>"address": "2MvXFfHyxr1U4icdyw1nWM3FZdraXMsfMAq",<br>"label": "bizantino",<br>"redeemScript": "00147700ead177801037c5ec0ad20d1cf7637fe55fde",<br>"scriptPubKey": "a91423f06dcefe3a139e930f059e99b47e9bf908c17f87",<br>"amount": 50.00000000,<br>"confirmations": 101,<br>"spendable": true,<br>"solvable": true,<br>"desc": "sh(wpkh([87aac41a/0'/0'/0']03d5f548512ed8f90773e531440fd4ce1843ee5ddf1097b7731a4464803df468c4))#qksqangj",<br>"safe": true<br>}]</pre>
<p>Quello che interessa a noi per fare la transazione è la <strong>txid</strong> e il <strong>vout</strong>, per questo le salviamo in due variabili d’ambiente.</p>
<pre>$ TXID=75b91cf262c98bdd57b0c3f2ec1a2597cceadc0cc2ef0a103e1a0013d81e332f</pre>
<pre>$ VOUT=0</pre>
<p>Siamo pronti a creare la transazione utilizzando il comando <strong>createrawtransaction</strong>. Sposteremo 1 bitcoin verso il destinatario, e 48.998 bitcoin verso l’indirizzo di resto. Una bella mancia per il miner!<br>Il risultato che otteniamo, la transaction data, la salviamo dentro la variabile d’ambiente TX_DATA.&nbsp;</p>
<pre>$ TX_DATA=`bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_RESTO'":48.998},{"'$ADDR_DEST'":1}]'`</pre>
<p>Per vedere il contenuto della variabile d’ambiente,&nbsp;</p>
<pre>$ echo $TX_DATA</pre>
<p>NB: Nel libro <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/"><strong>Bitcoin dalla teoria alla pratica</strong></a> e nel <a href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13" target="_blank" rel="noopener noreferrer" data-href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13"><strong>video-corso</strong></a> viene analizzato byte per byte la <strong>transaction data.</strong></p>
<p>Quello che dobbiamo fare adesso è firmare la transazione con la chiave privata di $ADDR che posso ottenere con il comando <strong>dumpprivkey.</strong></p>
<pre>$ PK=`bitcoin-cli dumpprivkey $ADDR`</pre>
<p>Attenzione, non deriviamo la chiave privata dalla chiave pubblica ($ADDR) ma la otteniamo da una serie di indirizzi già pronti per il nostro wallet.&nbsp;<br>Per maggiori informazioni guarda il comando dumpwallet.</p>
<p>Bene, firmiamo la transazione.</p>
<pre>$ bitcoin-cli signrawtransactionwithkey $TX_DATA '["'$PK'"]'
{
"hex": "020000000001012f331ed813001a3e100aefc20cdceacc97251aecf2c3b057dd8bc962f21cb97500000000171600147700ead177801037c5ec0ad20d1cf7637fe55fdeffffffff02808cf1230100000017a91489734e8089e307b4ac82eab729519abb2674cb168700e1f5050000000017a9143166112f2219dfd7bdfbabab70bef4ecab850a4587024730440220439be864b4520e29360341b429e9f16da89c5c44e98205025fb3b496e8b296990220638894c61364c3acca31b8acb80314b356713de0f8d11cfa03985bb8ae8c91cb012103d5f548512ed8f90773e531440fd4ce1843ee5ddf1097b7731a4464803df468c400000000",
"complete": true
}</pre>
<p>Per comodità salviamo dentro la variabile d’ambiente TX_DATA_SIGNED il valore di hex.<br>Inviamo la transazione.</p>
<pre>$ bitcoin-cli sendrawtransaction $TX_DATA_SIGNED
d24f8de59e839ee3956f27b44ce8ed980405725acde903e5494450934f9a4db2</pre>
<p>Quello che otteniamo è la TXID.<br>Che cosa succede adesso? La transazione è stata inviata ma non è ancora stata minata, quindi dove si trova?<br>Nella mempool!<br>Dobbiamo essere in grado di verificare la sua presenza in entrambi i nodi.</p>
<figure><em><a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/"><img src="https://cdn-images-1.medium.com/max/1600/1*EdeMc64B2AWgAXx2ODJNsw.png" data-image-id="1*EdeMc64B2AWgAXx2ODJNsw.png" data-width="612" data-height="842" data-is-featured="true"></a></em>
</figure>
<pre>$ bitcoin-cli getrawmempool
[
"d24f8de59e839ee3956f27b44ce8ed980405725acde903e5494450934f9a4db2"
]</pre>
<pre>$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getrawmempool
[
"d24f8de59e839ee3956f27b44ce8ed980405725acde903e5494450934f9a4db2"
]</pre>
<p>Esatto, entrambi i nodi hanno a disposizione la transazione ed entrambi potrebbero minarla. Per verificare il candidate block il comando è <strong>getblocktemplate.</strong></p>
<pre>$ bitcoin-cli getblocktemplate '{"rules": ["segwit"]}'</pre>
<p>Quindi la transazione è <strong>verificata</strong> ma <strong>non confermata</strong>.<br>Possiamo trovare conferma dell’asserzione appena fatta con il comando <strong>getwalletinfo </strong>sul nodo2.</p>
<pre>$  bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getwalletinfo
{
...
"balance": 0.00000000,
"unconfirmed_balance": 1.00000000,
"immature_balance": 0.00000000,
"txcount": 1,
...
}</pre>
<p>Possiamo leggere <strong>“unconfirmed_balance”: </strong>1&nbsp;!<br>Bene, miniamo facendo 6 blocchi così da rendere la transazione sicura.&nbsp;</p>
<pre>$ bitcoin-cli generatetoaddress 6 $ADDR</pre>
<p>Bene, la mempool è vuota e il destinatario ha a disposizione 1 bitcoin!</p>
<pre>$ bitcoin-cli -conf=$PWD/bitcoin_nodo2.conf getwalletinfo<br> ...<br>"balance": 1.00000000,<br>...</pre>
<p>Possiamo verificare le operazioni sui log dei demoni, oppure utilizzando tail sul file di log.</p>
<pre>$ tail -F regtest/debug.log</pre>
<p>Ci provo?</p>
<pre>$ bitcoin-cli sendrawtransaction $TX_DATA_SIGNED
error code: -27
error message:
Transaction already in block chain</pre>
<p>Il double spending non è andato a buon fine.</p>
</section>
<section>
<hr>
<p>Con questo piccolo tutorial è possibile iniziare a studiare il protocollo Bitcoin e a seguire il libro <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/"><strong>Bitcoin dalla teoria alla pratica</strong></a> o se preferisci il <a href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13" target="_blank" rel="noopener noreferrer" data-href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13"><strong>video-corso</strong></a><strong>.</strong></p>
<hr>
</section>
<section>
<p>► <a href="https://amzn.to/2MOj1av" target="_blank" rel="noopener noreferrer" data-href="https://amzn.to/2MOj1av">Libro Bitcoin dalla teoria alla pratica (Amazon)</a><br>► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica (sito ufficiale con pagamento in bitcoin)</a><br> — <br>► <a href="https://www.amazon.it/dp/1098612639" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1098612639">Tascabile Bitcoin 199 domande (Amazon)</a><br>► <a href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/libro-bitcoin-199-domande">Tascabile Bitcoin 199 domande (sito ufficiale con pagamento in bitcoin)</a></p>
<p>► <a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Pocket Book Bitcoin 199 questions (Amazon)</a><br>► <a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Pocket </a><a href="https://www.amazon.it/dp/1078155585" target="_blank" rel="noopener noreferrer" data-href="https://www.amazon.it/dp/1078155585">Book </a><a href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/" target="_blank" rel="noopener noreferrer" data-href="https://www.corsobitcoin.com/prodotto/book-bitcoin-199-questions/">Bitcoin 199 questions (official website — accept bitcoin)</a><br> — <br>► <a href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13" target="_blank" rel="noopener noreferrer" data-href="https://www.udemy.com/course/bitcoin-blockchain-corso-completo-teoria-pratica-esempi-tutorial/?referralCode=AAC8EB895142D8301C13">Video corso disponibile su Udemy</a></p>
<p>I nostri social:<br>► <a href="https://twitter.com/satoshiwantsyou" target="_blank" rel="noopener noreferrer" data-href="https://twitter.com/satoshiwantsyou">Twitter</a>&nbsp;, <a href="https://www.facebook.com/bitcoin.corso.completo/" target="_blank" rel="noopener noreferrer" data-href="https://www.facebook.com/bitcoin.corso.completo/">Facebook</a>, <a href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica" target="_blank" rel="noopener noreferrer" data-href="https://www.linkedin.com/company/bitcoin-dalla-teoria-alla-pratica">Linkedin</a>, <a href="https://medium.com/@bitcoindallateoriallapratica" target="_blank" rel="noopener noreferrer" data-href="https://medium.com/@bitcoindallateoriallapratica">Medium</a>, <a href="https://www.instagram.com/satoshiwantsyou/" target="_blank" rel="noopener noreferrer" data-href="https://www.instagram.com/satoshiwantsyou/">Instagram</a>, <a href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA" target="_blank" rel="noopener noreferrer" data-href="https://www.youtube.com/channel/UCPsuu94QAXZ0fDYN0Zlo-RA">Youtube</a>, <a href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi" target="_blank" rel="noopener noreferrer" data-href="https://github.com/bitcoin-dalla-teoria-alla-pratica/errata-corrige-e-sorgente-esempi">GitHub</a></p>
<p>Television isn’t a good idea (Radio Stations)<br>Email isn’t a good idea (Post offices)<br>Amazon isn’t a good idea (Retail stores)<br>Bitcoin isn’t a good idea (Central banks)</p>
<p>In <strong>crypto</strong> we trust</p>
</section>