# Step-by-Step Guide: Creating the Word Blackjack Repository on GitHub

This guide walks you through publishing your local project as a GitHub repository. Estimated time: 10 minutes (or 5, if you type fast — which, as a Word Blackjack player, you should).

---

## Prerequisites

- A [GitHub account](https://github.com)
- [Git](https://git-scm.com/) installed on your machine
- The project folder ready on your computer

---

## Step 1 — Clean Up the Old Files

Before initialising Git, remove the legacy files that have been superseded by the new package structure. From the project root folder, delete:

- `main.py` (replaced by `word_blackjack/__main__.py`)
- `word_blackjack.py` (replaced by `word_blackjack/engine.py`)
- `engWords.txt` (moved to `word_blackjack/data/english_words.txt`)
- `__pycache__/` folder
- `.DS_Store`

On macOS / Linux:

```bash
rm main.py word_blackjack.py engWords.txt .DS_Store
rm -rf __pycache__/
```

---

## Step 2 — Create the Repository on GitHub

1. Go to [github.com/new](https://github.com/new)
2. Fill in the details:
   - **Repository name:** `word-blackjack`
   - **Description:** `A terminal-based multiplayer word game — like Blackjack, but with words. Built in Python.`
   - **Visibility:** Public (or Private, your call)
   - **DO NOT** tick "Add a README", ".gitignore", or "Choose a licence" — we already have all of these locally.
3. Click **Create repository**

---

## Step 3 — Initialise Git Locally

Open a terminal in the project folder and run:

```bash
cd /path/to/word-blackjack
git init
git add .
git commit -m "Initial commit: Word Blackjack v1.0.0"
```

---

## Step 4 — Connect to GitHub and Push

Copy the remote URL from the GitHub page you just created (it will look like `https://github.com/YOUR_USERNAME/word-blackjack.git`), then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/word-blackjack.git
git branch -M main
git push -u origin main
```

---

## Step 5 — Configure Repository Settings on GitHub

Once pushed, head to your repository's **Settings** page on GitHub and tidy things up:

### 5a — About Section (sidebar)

Click the gear icon next to "About" on the repository's main page:

- **Description:** `A terminal-based multiplayer word game — like Blackjack, but with words. Built in Python.`
- **Website:** *(leave blank unless you deploy it somewhere)*
- **Topics:** Add the following tags:
  - `python`
  - `python3`
  - `word-game`
  - `terminal-game`
  - `cli-game`
  - `blackjack`
  - `multiplayer`
  - `console-game`
  - `game`
  - `vocabulary`

### 5b — Social Preview (optional but recommended)

Under **Settings → General**, you can upload a social preview image (1280×640px recommended). This is the image that appears when someone shares your repo link on social media or Slack. A fun pixel-art card + word mashup would be on-brand.

---

## Step 6 — Verify Everything Looks Right

Check your repository page and confirm:

- [x] README renders properly with the table, code blocks, and structure tree
- [x] LICENSE is detected by GitHub (you should see "MIT License" in the sidebar)
- [x] `.gitignore` is working (no `__pycache__/`, `.DS_Store`, etc.)
- [x] Topics appear under the repository name
- [x] The word list file is present at `word_blackjack/data/english_words.txt`

---

## Step 7 — Test the Game from a Fresh Clone

To make sure everything works for anyone who clones the repo:

```bash
cd /tmp
git clone https://github.com/YOUR_USERNAME/word-blackjack.git
cd word-blackjack
python -m word_blackjack
```

If you see `Word Blackjack v1.0` and the game starts, you're golden.

---

## Optional Extras

### Create a Release

1. Go to **Releases** → **Create a new release**
2. Tag: `v1.0.0`
3. Title: `v1.0.0 — Initial Release`
4. Description: Something like:
   > The first official release of Word Blackjack. Supports 2–7 players, three difficulty levels, and over 235,000 English words. May your vocabulary be ever in your favour.
5. Click **Publish release**

### Enable GitHub Discussions

If you want to build a community (even a tiny one): **Settings → General → Features → Discussions** — tick the box. It gives people a place to share epic word combos or suggest features.

---

That's it! Your repository is live, professional, and ready for the world. Now go play a round — you've earned it. 🎩
