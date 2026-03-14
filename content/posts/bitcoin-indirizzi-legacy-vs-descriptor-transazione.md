---
title: "Bitcoin in Evoluzione: Differenze Chiave tra Indirizzi Legacy e Descriptor - Un'Analisi Pratica"
date: 2023-12-26T18:14:48+01:00
draft: false


tags:
  - "UTXO"
  - "Crittografia"
---




<p>In questo articolo, approfondiremo in modo pratico le divergenze introdotte dall'implementazione dell'aggiornamento descriptor a partire da Bitcoin Core 0.17.0 nel 2018. Se questa tematica ti è nuova, ti suggerisco di consultare <a href="https://medium.com/@bitcoin-in-action/wallet-bitcoin-differenze-tra-wallet-legacy-vs-wallet-descriptor-513b0faa4dd4">questo articolo</a> per una migliore comprensione.</p>

<p>Come consuetudine, gli esempi qui presentati possono essere replicati agevolmente tramite il nostro ambiente docker e il repository associato.</p>

<p>Con l'introduzione del descriptor, la procedura di utilizzo di <code>dumpprivkey</code> e la successiva firma delle transazioni raw mediante il comando <code>signrawtransactionwithkey</code> è stata abbandonata. Invece, il nodo si occupa della firma della transazione, facendo uso del comando <code>signrawtransactionwithwallet</code>.</p>

<p>In questo esempio, eseguiremo due transazioni: una utilizzando un address descriptor a un indirizzo legacy e successivamente dall'indirizzo legacy al descriptor. Per gestire entrambi i casi, creeremo due portafogli distinti e avvieremo il nodo con la direttiva <code>-deprecatedrpc=create_bdb</code> per poter utilizzare i comandi legacy.</p>

<p>È importante notare che questo esempio si basa sul nodo Bitcoin versione 26.</p>

<p><strong>Riproduzione dell'Esempio:</strong><br>Per replicare l'esperimento, segui questi passaggi:</p>

<ol><li>Clona il nostro repository.</li>
</ol>

<pre class="wp-block-syntaxhighlighter-code">   docker exec -it bitcoin-in-action-youtube zsh</pre>

<ol start="2"><li>Entra nel container e spostati nella cartella "Video 13 - P2PKH legacy vs P2PKH descriptor".</li>
</ol>

<pre class="wp-block-syntaxhighlighter-code">   ./main.sh</pre>

<p><strong>In Action!</strong><br>I nostri esempi sono sempre basati sulla regtest, sia in questo contesto che nei nostri libri "<a href="https://bit.ly/38RtF9x">Bitcoin In Action — SegWit, Bitcoin Script e Smart Contracts</a>" e "<a href="https://www.corsobitcoin.com/prodotti/libro-bitcoin-dalla-teoria-alla-pratica/">Libro Bitcoin dalla teoria alla pratica</a>".</p>

<p><em>Per ulteriori approfondimenti e per immergerti nel mondo di Bitcoin, visita il nostro <a href="https://linktr.ee/satoshiwantsyou">linktree</a>.</em></p>

<p>Dopo aver avviato Docker Compose con il comando <code>docker-compose up</code>, entra nel container mediante:</p>

<pre class="wp-block-syntaxhighlighter-code">docker exec -it bitcoin-in-action-youtube bash</pre>

<p>Per prima cosa, arresta e pulisci completamente la regtest eseguendo il seguente comando:</p>

<pre class="wp-block-syntaxhighlighter-code">bitcoin-cli stop &amp;&amp; sleep 5 &amp;&amp; rm -Rf $HOME/.bitcoin/regtest &amp;&amp; bitcoind -deprecatedrpc=create_bdb &amp;&amp; sleep 5</pre>

<p>L'avvio con <code>bitcoind -deprecatedrpc=create_bdb</code> è necessario per abilitare l'uso dei comandi legacy.</p>

<p>Successivamente, crea due portafogli: uno legacy e uno descriptor, generando due indirizzi.</p>

<p>Iniziamo effettuando la transazione dal Descriptor al Legacy:</p>

<pre class="wp-block-syntaxhighlighter-code">bitcoin-cli -named createwallet wallet_name="biaDescriptor"
bitcoin-cli -named createwallet wallet_name="biaLegacy" descriptors="false"

ADDR_DESC=`bitcoin-cli -rpcwallet="biaDescriptor" getnewaddress "" "legacy"`
ADDR_LEGACY=`bitcoin-cli -rpcwallet="biaLegacy" getnewaddress "" "legacy"`</pre>

<p>Da notare che il termine "legacy" si riferisce agli indirizzi legacy e non ai portafogli legacy. Gli indirizzi legacy iniziano con 1 nella mainnet e con m/n nella testnet/regtest.</p>

<p>Successivamente, miniamo 101 blocchi per ottenere un reward da spendere:</p>

<pre class="wp-block-syntaxhighlighter-code">bitcoin-cli generatetoaddress 101 $ADDR_DESC >> /dev/null</pre>

<p>Recuperiamo le UTXO dall'indirizzo associato al portafoglio descriptor:</p>

<pre class="wp-block-syntaxhighlighter-code">UTXO=`bitcoin-cli -rpcwallet="biaDescriptor" listunspent 1 101 '["'$ADDR_DESC'"]'`</pre>

<p>Quando si gestiscono più portafogli, specifica con <code>-rpcwallet</code> a quale portafoglio ti stai riferendo. Immagazzina la lista degli UTXO nella variabile d'ambiente UTXO.</p>

<p>A questo punto, con Jq, memorizziamo le informazioni necessarie per effettuare la transazione:</p>

<pre class="wp-block-syntaxhighlighter-code">TXID=$(echo $UTXO | jq -r '.[0].txid')
VOUT=$(echo $UTXO | jq -r '.[0].vout')
AMOUNT=$(echo $UTXO | jq -r '.[0].amount-0.009')
TOTAL_UTXO_AMOUNT=$(echo $UTXO | jq -r '.[0].amount')
TXIN=`bitcoin-cli getrawtransaction $TXID`</pre>

<p>Ora che abbiamo i dati necessari, creiamo la transazione utilizzando il nuovo metodo introdotto con l'aggiornamento descriptor:</p>

<pre class="wp-block-syntaxhighlighter-code">TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_LEGACY'":'$AMOUNT'}]')</pre>

<p>Il metodo "signrawtransactionwithwallet" è stato inserito con l'aggiornamento descriptor. Ora firmiamo la transazione:</p>

<pre class="wp-block-syntaxhighlighter-code">TX_SIGNED=$(bitcoin-cli -rpcwallet="biaDescriptor" signrawtransactionwithwallet $TX_DATA | jq -r '.hex')</pre>

<p>In questo caso, non forniamo la chiave privata direttamente; sarà il metodo <code>signrawtransactionwithwallet</code> a occuparsi della firma. Il risultato viene memorizzato in <code>TX_SIGNED</code>.</p>

<p>Infine, inviamo la transazione:</p>

<pre class="wp-block-syntaxhighlighter-code">bitcoin-cli sendrawtransaction $TX_SIGNED</pre>

<p>Ora eseguiamo l'operazione inversa, dal legacy al descriptor. Poiché abbiamo già dei bitcoin spendibili grazie alla transazione appena creata, l'operazione sarà più veloce.</p>

<p>Recuperiamo le informazioni necessarie per creare la transazione:</p>

<pre class="wp-block-syntaxhighlighter-code">UTXO=`bitcoin-cli -rpcwallet="biaLegacy" listunspent 1 101 '["'$ADDR_LEGACY'"]'`
TXID=$(echo $UTXO | jq -r '.[0].txid')
VOUT=$(echo $UTXO | jq -r '.[0].vout')
AMOUNT=$(echo $UTXO | jq -r '.[0].amount-0.009')
TOTAL_UTXO_AMOUNT=$(echo $UTXO | jq -r '.[0].amount')
SCRIPTPUBKEY=$(echo $UTXO | jq -r '.[0].scriptPubKey')
TXIN=`bitcoin-cli getrawtransaction $TXID`</pre>

<p>Usiamo <code>-rpcwallet="biaLegacy"</code> in questo caso. Successivamente, otteniamo la chiave privata con il comando <code>dumpprivkey</code>:</p>

<pre class="wp-block-syntaxhighlighter-code">PK=$(bitcoin-cli -rpcwallet="biaLegacy" dumpprivkey $ADDR_LEGACY)</pre>

<p>Ora siamo pronti a creare la transazione:</p>

<pre class="wp-block-syntaxhighlighter-code">TX_DATA=$(bitcoin-cli createrawtransaction '[{"txid":"'$TXID'","vout":'$VOUT'}]' '[{"'$ADDR_DESC'":'$AMOUNT'}]')</pre>

<p>Firmiamo la transazione con la chiave privata e aggiungiamo lo <code>scriptPubKey</code>:</p>

<pre class="wp-block-syntaxhighlighter-code">TX_SIGNED=$(bitcoin-cli signrawtransactionwithkey $TX_DATA '["'$PK'"]' '[{"txid":"'$TXID'","vout":'$VOUT',"scriptPubKey":"'$SCRIPTPUBKEY'"}]' | jq -r '.hex')</pre>

<p>Infine, inviamo la transazione in broadcast:</p>

<pre class="wp-block-syntaxhighlighter-code">TXSPENT=$(bitcoin-cli sendrawtransaction $TX_SIGNED)</pre>

<p>Le due differenze principali sono:</p>

<ol><li>Non è più possibile ottenere la chiave privata tramite <code>dumpprivkey</code> dal portafoglio descriptor, che è ora la configurazione predefinita in Bitcoin. Tentare di eseguire il dump restituirà un errore:</li>
</ol>

<pre class="wp-block-syntaxhighlighter-code">   bitcoin-cli -rpcwallet="biaDescriptor" dumpprivkey $ADDR_DESC
   error code: -4
   error message:
   Only legacy wallets are supported by this command</pre>

<ol start="2"><li>La seconda differenza riguarda il metodo per firmare la transazione: da <code>signrawtransactionwithkey</code> a <code>signrawtransactionwithwallet</code>.</li>
</ol>

<p>In luce di queste significative differenze tra l'uso di indirizzi legacy e descriptor in Bitcoin, emergono nuove prospettive sulla gestione delle transazioni e sulla sicurezza delle chiavi private. L'evoluzione del protocollo continua a offrire agli utenti nuovi strumenti per interagire in modo sicuro e flessibile.</p>

<p>Per ulteriori dettagli e per approfondire il mondo di Bitcoin, visita il nostro <a href="https://linktr.ee/satoshiwantsyou">linktree</a>.</p>
