---
title: "Crittografia Pt VIII"
date: 2019-10-15T10:00:00+01:00
slug: "crittografia-pt-viii"
draft: false
author: "Alessio Barnini"
description: "RSA — Ron Rivest, Adi Shamir, Leonard Adlemen."
tags:
  - "Bitcoin"
  - "Chiave Privata"
  - "Chiave Pubblica"
categories:
  - "Bitcoin"
---

---

### Crittografia Pt VIII

#### RSA — Ron Rivest, Adi Shamir, Leonard Adlemen.

Siamo arrivati alla rivoluzione vera e propria della crittografia, questo articolo parlerà della crittografia a chiave pubblica detta anche crittografia **asimmetrica**. **Che cosa rende così importante la crittografia asimmetrica**? La possibilità di condividere la chiave (pubblica) senza aver bisogno di un canale sicuro a differenza della crittografia simmetrica. 
Proprio così, nella crittografia asimmetrica abbiamo due chiavi distinte ma legate matematicamente.  
Le chiavi prendono il nome di **chiave privata** e la **chiave pubblica**. 
Un’altro problema che viene risolto è l’ **autenticazione** del mittente e dell’integrità del messaggio trasmesso, grazie all’ **autenticazione** e alla **firma digitale**. 
Come si capisce da queste poche righe, siamo di fronte ad una nuova frontiera.

Tutto nacque nel **1975** dagli studi di [Whitfield Diffie](https://it.wikipedia.org/wiki/Whitfield_Diffie) e [Martin Hellman](https://it.wikipedia.org/wiki/Martin_Hellman).

Il loro obiettivo era quello di poter utilizzare la crittografia senza dover trasferire in modo sicuro la chiave, per far questo veniva scambiata in chiaro una porzione della chiave che combinata matematicamente con un’altra non condivisa (privata) derivava la chiave desiderata. 
In questo modo se qualcuno intercetta la chiave durante lo scambio non rappresenta nessun pericolo, a differenza della crittografia simmetrica che se viene intercettata la chiave può essere letto il messaggio in chiaro, oppure può essere addirittura cambiato il messaggio all’insaputa del mittente e del destinatario. 
Questo tipo di scambio di chiavi prende il nome di [**Diffie-Hellman**](https://it.wikipedia.org/wiki/Scambio_di_chiavi_Diffie-Hellman) e viene ancora utilizzato. 
Non risolve però il problema di **autenticazione** e non consente la **cifratura dei messaggi**.

Arriviamo alla crittografia asimmetrica sviluppata da [**R** ivest](https://it.wikipedia.org/wiki/Ronald_Rivest) [**S** hamir](http://Shamir) e [**A** dleman](https://it.wikipedia.org/wiki/Leonard_Adleman) (RSA).

La rivoluzione è data dalla presenza di due chiavi, chiave privata e chiave pubblica, diverse ma legate matematicamente (grazie a particolari proprietà dei numeri primi). 
Dalla chiave privata è possibile derivare la chiave pubblica, ma la chiave pubblica **non fornisce nessuna informazione** per effettuare la derivazione della chiave privata.

Per questo motivo la chiave pubblica ha questo nome, in quanto può essere distribuita pubblicamente. 
Questa scoperta ha inaugurato l’era dell’autenticazione e della firma digitale. 
Pensate che l’algoritmo è utilizzato nel SSL (Secure Socket Layer) da Visa e Mastercard :)

#### **Come viene utilizzata per nascondere il messaggio**?![codificare il messaggio con la chiave pubblica.](https://cdn-images-1.medium.com/max/1200/1*y4KWfnXwvyCiGobOkHmAcw.gif)
*codificare il messaggio con la chiave pubblica.*

Ipotizziamo che Bob voglia mandare ad Alice una messaggio cifrato.  
Di che cosa ha bisogno Bob? 
Della chiave pubblica di Alice che può essere trasferita senza aver bisogno di un canale sicuro.  
Quindi Bob **cifra** il messaggio **con la chiave pubblica** di Alice e lo invia ad Alice stessa.  
Molto importante sottolineare che una volta che il messaggio è stato cifrato non è possibile decifrarlo con la stessa chiave pubblica.  
Quindi Alice per leggere il messaggio di Bob non deve far altro che decifrarlo con la sua **chiave privata**.

> Chiave pubblica cifra il messaggio 
> Chiave privata decifra il messaggio

#### Cosa succede se cifriamo il messaggio con la chiave privata e lo decifriamo con la chiave pubblica?

Asserendo che la chiave privata è **segreta** abbiamo la certezza che solo una persona può fornire una certa cifratura che può essere decifrata con la relativa chiave pubblica.

Questo non fornisce nessuna **cifratura segreta** in quanto la chiave pubblica può essere distribuita in un canale non sicuro, ma **autentica** il mittente dandoci la sicurezza che il messaggio provenga esattamente da quella persona.

![Autenticazione ottenuta con la chiave privata del mittente](https://cdn-images-1.medium.com/max/1200/1*YaGsjK2oG5-m9mpnywJALw.gif)
*Autenticazione ottenuta con la chiave privata del mittente*

Con l’aiuto dell’immagine si può spiegare più facilmente: 
- Il mittente Bob cifra il messaggio con la sua chiave privata 
- Invia il messaggio ad Alice  
- Alice con la chiave pubblica di Bob decifra il messaggio.

> Chiave privata cifra il messaggio (autenticazione) 
> Chiave pubblica decifra il messaggio (verifica)

#### Come possiamo ottenere l’autenticazione del mittente e la segretezza del messaggio?

Per ottenere anche la segretezza è possibile cifrare il messaggio con la chiave pubblica del destinatario proprio come abbiamo visto nel primo esempio.

![Autenticazione e segretezza del messaggio](https://cdn-images-1.medium.com/max/1200/1*NOEowUB9XpOcZVtLNdZePA.gif)
*Autenticazione e segretezza del messaggio*

Con l’aiuto dell’immagine si può spiegare più facilmente: 
- Il mittente Bob cifra il messaggio con la sua chiave privata ottenendo così il messaggio autenticato. 
- Bob utilizza su tale messaggio la chiave pubblica di Alice, cosi da ottenere la segretezza. 
- Il messaggio viene inviato ad Alice 
- Alice con la sua chiave privata decifra il messaggio. 
- Alice con la chiave pubblica di Bob decifra il messaggio. 
- Alice può leggere il messaggio in chiaro.

#### Che cosa è la firma digitale?

La firma digitale può essere definita come una forma di autenticazione.  
A differenza di quanto abbiamo appena visto, la firma digitale utilizza un riassunto del messaggio detto **digest** o **hash del messaggio**. 
Utilizzando un algoritmo di hash otteniamo una dimensione fissa da una dimensione variabile. 
Ad esempio Bitcoin utilizza molto spesso l’algoritmo **SHA256**, che da una dimensione variabile restituisce sempre una dimensione di **256bit** (64 caratteri esadecimali). 
Così la firma digitale è rappresentata dal messaggio hash cifrato.

![Firma digitale](https://cdn-images-1.medium.com/max/1200/1*dCSS4jFsbHBGZdS4UytOwA.gif)
*Firma digitale*

Con l’aiuto dell’immagine si può spiegare più facilmente: 
- Bob applica l’algoritmo di hash (SHA256 ad esempio) sul messaggio in chiaro, ottenendo così il **digest**. 
- Utilizza la sua chiave privata per cifrare il **digest**. Ottenendo così la firma digitale e l’autenticazione. 
- Invia ad Alice il messaggio in chiaro, la firma e la chiave pubblica. 
- Alice applica sulla firma la chiave pubblica di Bob ottenendo così il digest. 
- Alice applica sul messaggio in chiaro lo stesso algoritmo di hash (SHA256) ottenendo il digest del messaggio. 
- Alice confronta il digest appena ottenuto con quello di Bob. Se i digest sono uguali la firma è stata verificata e siamo sicuri che il messaggio non è stato alterato. Ricorda che se il messaggio cambia il digest non è più lo stesso.

Adesso è più chiaro capire come si identifica il vero possessore di bitcoin.

Come? Solo il possessore di una certa chiave privata può fornire una data firma, firmando il messaggio (transaction data rappresenta il nostro digest).  
Il **digest** poi verrà controllato dal protocollo Bitcoin per verificare la transazione stessa!

Nei primi capitoli del libro [**Bitcoin dalla teoria alla pratica**](https://www.amazon.it/Bitcoin-Dalla-teoria-alla-pratica/dp/B07SNNNL2P/) mettiamo in pratica la crittografia asimmetrica con esempi concreti e reali!

Che cosa risolve quindi la **firma digitale**?

- **Integrità**: Il messaggio non deve essere alterato durante la trasmissione. Bob manda un messaggio a Alice con scritto W i bitcoin. 
Peter lo intercetta cambiandolo con W gli ether. 
Alice deve essere in grado di accorgersi di tale cambiamento.
- **Autenticità**: Alice deve essere sicura che il messaggio che ha ricevuto sia stato inviato da Bob, e non da Peter che si è *spacciato *per Bob.
- **Non ripudio**: il mittente non potrà disconoscere il messaggio che ha firmato.

Bitcoin non utilizza l’algoritmo RSA, utilizza invece le [**curve ellittiche**](https://it.wikipedia.org/wiki/Crittografia_ellittica).  
Anche questo algoritmo offre la possibilità di cifrare i messaggi e di effettuare le firme. Per la natura con cui è stato sviluppato l’algoritmo è più veloce in esecuzione rispetto a RSA.

Direi che dalla [**scitala**](https://medium.com/@bitcoindallateoriallapratica/come-nasce-la-crittografia-fino-al-bitcoin-parte-prima-68756d6715a9) alla **crittografia asimmetrica** ne abbiamo fatta di strada!
