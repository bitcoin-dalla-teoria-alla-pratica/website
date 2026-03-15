---
title: "Crittografia Pt III"
date: 2019-09-12T10:00:00+01:00
slug: "crittografia-pt-iii"
draft: false
author: "Alessio Barnini"
description: "L’arte del nascondere — monoalfabetica vs polialfabetica"
tags:
  - "Crittografia"
categories:
  - "Bitcoin"
---

---

### Crittografia Pt III

#### L’arte del nascondere — **monoalfabetica vs polialfabetica** Nell’[articolo precedente](/posts/crittografia-pt-ii/) abbiamo affrontato il tema degli alfabeti.  
In particolare sostituzione **monoalfabetica** e **polialfabetica**. Aumentiamo ancora il nostro vocabolario, sfruttando Wikipedia.

--- **monoalfabetica** è un sistema crittografico che utilizza un alfabeto per il testo in chiaro e una permutazione dello stesso per il testo cifrato. **polialfabetica** è un sistema crittografico che fa uso di un numero più o meno grande di *alfabeti* per sostituire le lettere del messaggio.

---

Ok, non è chiarissimo, almeno per me.  
Facciamo un esempio partendo dal sistema crittografico **monoalfabetico**. 
Scriviamo l’alfabeto *classico. (26 lettere)*

```bash
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```


Scegliamo un altro alfabeto con cui cifrare il nostro messaggio. Il requisito è che sia anch’esso composto da 26 lettere. 
Ad esempio:

```bash
MNOPQRSTUVWXYZABCDEFGHIJKL
```


Ora quello che dobbiamo fare è cifrare il messaggio.

Il messaggio in chiaro è BARNO. **Alfabeto chiaro .** `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z` **Alfabeto cifrante** `M N O P Q R S T U V W X Y Z A B C D E F G H I J K L` **Testo chiaro ….**. `B A R N O` **Testo cifrato ….**. `N M D Z A`

Il procedimento è semplice.  
La lettera **B** di **B** ARNO corrisponde alla lettera **N** dell’alfabeto cifrante. 
La lettera **A** di B **A** RNO corrisponde alla lettera **M** dell’alfabeto cifrante. 
La lettera **R** di BA **R** NO corrisponde alla lettera **D** dell’alfabeto cifrante. 
La lettera **N** di BAR **N** O corrisponde alla lettera **Z** dell’alfabeto cifrante. 
La lettera **O** di BARN **O** corrisponde alla lettera **A** dell’alfabeto cifrante.

Per rendere più difficile la decifratura alla **crittoanalisi**, venne adottata la crittografia **polialfabetica**, che utilizza più dizionari risolvendo così anche le [frequenza di testo](https://it.wikipedia.org/wiki/Analisi_delle_frequenze). 
Facciamo un esempio, cifrando sempre la parola BARNO e aggiungendo un dizionario, ad esempio:

```bash
ZABCDEFGHIJKLMNOPQRSTUVWXY
```


**Alfabeto chiaro…..**. `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z` **Alfabeto cifrante M** `M N O P Q R S T U V W X Y Z A B C D E F G H I J K L` **Alfabeto cifrante Z**. `Z A B C D E F G H I J K L M N O P Q R S T U V W X Y` **Testo chiaro …….**. `B A R N O` **Testo cifrato …….**. `N Z D M A`

Il dizionario M è il dizionario utilizzato nell’esempio precedente, il dizionario Z è il nuovo dizionario. Come otteniamo questo risultato?

La lettera **B** di **B** ARNO corrisponde alla lettera **N** dell’alfabeto cifrante M. 
La lettera **A** di B **A** RNO corrisponde alla lettera **Z** dell’alfabeto cifrante Z. 
La lettera **R** di BA **R** NO corrisponde alla lettera **D** dell’alfabeto cifrante M. 
La lettera **N** di BAR **N** O corrisponde alla lettera **M** dell’alfabeto cifrante Z. 
La lettera **O** di BARN **O** corrisponde alla lettera **A** dell’alfabeto cifrante M.

Con questa strategia anche se BARNO avesse avuto una doppia(BARRNO) il testo cifrato avrebbe avuto due lettere diverse( **DQ** ) .  
In questo caso la **chiave** è **MZ**. Se non vi sembra potente immaginate di utilizzare 5 vocabolari per la parola BARNO.

```bash
__|____________________________a | abcdefghijklmnopqrstuvwxyz

b | bcdefghijklmnopqrstuvwxyza

c | cdefghijklmnopqrstuvwxyzab

d | defghijklmnopqrstuvwxyzabc

e | efghijklmnopqrstuvwxyzabcd

f | fghijklmnopqrstuvwxyzabcde

g | ghijklmnopqrstuvwxyzabcdef

h | hijklmnopqrstuvwxyzabcdefg

i | ijklmnopqrstuvwxyzabcdefgh

j | jklmnopqrstuvwxyzabcdefghi

k | klmnopqrstuvwxyzabcdefghij

l | lmnopqrstuvwxyzabcdefghijk

m | mnopqrstuvwxyzabcdefghijkl

n | nopqrstuvwxyzabcdefghijklm

o | opqrstuvwxyzabcdefghijklmn

p | pqrstuvwxyzabcdefghijklmno

q | qrstuvwxyzabcdefghijklmnop

r | rstuvwxyzabcdefghijklmnopq

s | stuvwxyzabcdefghijklmnopqr

t | tuvwxyzabcdefghijklmnopqrs

u | uvwxyzabcdefghijklmnopqrst

v | vwxyzabcdefghijklmnopqrstu

w | wxyzabcdefghijklmnopqrstuv

x | xyzabcdefghijklmnopqrstuvw

y | yzabcdefghijklmnopqrstuvwx

z | zabcdefghijklmnopqrstuvwxy
```


Vi consiglio questo [sito](http://people.unipmn.it/catenacc/NotteRicercatori/crittografia_2009/polialfabetica.html) molto utile per fare delle prove. 
Nel prossimo articolo affronteremo una tecnica che restituisce un risultato di [cifratura perfetto](https://it.wikipedia.org/wiki/Cifrario_perfetto).
