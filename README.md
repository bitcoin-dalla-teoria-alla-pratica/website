# Corso Bitcoin — corsobitcoin.com

Sito statico del progetto editoriale [**Corso Bitcoin**](https://corsobitcoin.com), dedicato alla comprensione tecnica approfondita del protocollo Bitcoin.

Articoli, libri e risorse su crittografia, chiavi, transazioni, script, blockchain e nodi Bitcoin — tutto con esempi pratici e verificabili.

---

## Stack

| Componente | Tecnologia |
|---|---|
| Static site generator | [Hugo](https://gohugo.io/) |
| Tema | [Terminal](https://github.com/panr/hugo-theme-terminal) (submodule) |
| Ricerca | [Pagefind](https://pagefind.app/) |
| Deploy | [Vercel](https://vercel.com/) |

---

## Sviluppo locale

**Prerequisiti:** Hugo installato ([istruzioni](https://gohugo.io/installation/))

```bash
# Clona il repo con il submodule del tema
git clone --recurse-submodules https://github.com/bitcoin-dalla-teoria-alla-pratica/corsobitcoin.git
cd corsobitcoin

# Avvia il server locale
hugo server
```

Il sito è disponibile su `http://localhost:1313`.

> Se hai già clonato senza `--recurse-submodules`, esegui:
> ```bash
> git submodule update --init --recursive
> ```

---

## Build

```bash
# Build del sito + indice di ricerca Pagefind
hugo && npx pagefind@latest --site public
```

L'output è nella cartella `public/`.

---

## Struttura del progetto

```
content/
  posts/       # Articoli tecnici
  prodotti/    # Pagine dei libri e del video corso
  about.md     # Chi siamo
layouts/       # Override dei template Hugo (estende il tema Terminal)
assets/css/    # CSS personalizzato (extended.css)
static/        # Immagini, favicon, llms.txt
themes/
  terminal/    # Tema (git submodule)
hugo.toml      # Configurazione Hugo
vercel.json    # Configurazione build Vercel
```

---

## Deploy

Il deploy è automatico su Vercel ad ogni push su `main`.

Il comando di build configurato in `vercel.json` è:
```
hugo && npx pagefind@latest --site public
```

---

## Autori

- **Alessio Barnini** — sviluppatore, formatore, autore dei libri
- **Alessandro Aglietti** — co-autore dei libri Bitcoin dalla teoria alla pratica e Bitcoin In Action

---

## Licenza

I contenuti (articoli, testi) sono di proprietà degli autori.
Il codice del sito (template, CSS) è liberamente ispezionabile.
