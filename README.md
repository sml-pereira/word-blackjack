# Word Blackjack 🃏

**Like Blackjack, but the only thing you're gambling is your vocabulary.**

Word Blackjack is a terminal-based multiplayer word game where players take turns saying words that connect to the previous one — by starting with the same letter, rhyming, or both. First to 21 points wins. No cards, no chips, just words and a healthy dose of competitive spirit.

---

## How It Works

The game kicks off with a random letter from A to Z. Each player, in turn, must type a valid English word that relates to the previous one. Points are awarded based on how cleverly the word connects:

| Points | Condition |
|--------|-----------|
| **1** | Your word starts with the same letter as the previous word |
| **3** | Your word rhymes with the previous word (same last 3 letters) |
| **7** | Both of the above — the holy grail of Word Blackjack |

The first player (or team, if you're feeling dramatic) to reach **21 points** wins the game.

### Additional Rules

- **Players:** 2 to 7 (because 8 would be chaos).
- **Games:** Choose an odd number between 1 and 7 to avoid draws in multi-game sessions.
- **Difficulty:** Three levels controlling how many turns each player gets — 20, 10, or 5 turns per player. Choose wisely.
- **No repeats:** Previously used words are off limits. Your memory is part of the game.

### In-Game Options

During your turn, instead of typing a word, you can use these single-letter commands:

- `l` — List all valid words played so far
- `s` — Show current stats and averages
- `q` — Quit the game (no judgement... well, maybe a little)

---

## Installation

### Prerequisites

- Python 3.7 or later
- A terminal
- At least one friend (optional but recommended)

### Clone and Run

```bash
git clone https://github.com/YOUR_USERNAME/word-blackjack.git
cd word-blackjack
python -m word_blackjack
```

That's it. No dependencies to install, no virtual environments to set up, no existential crises about package managers. Pure Python.

---

## Project Structure

```
word-blackjack/
├── word_blackjack/
│   ├── __init__.py          # Package metadata
│   ├── __main__.py          # Entry point (python -m word_blackjack)
│   ├── engine.py            # All game logic and functions
│   └── data/
│       └── english_words.txt  # ~236k English words for validation
├── .gitignore
├── LICENSE                  # MIT License
├── LICENSE-DATA             # Licence notice for the word list
├── README.md                # You are here
├── requirements.txt         # Spoiler: it's empty (no dependencies)
└── setup.py                 # For pip install / distribution
```

---

## Contributing

This is a casual, just-for-fun project — but contributions are welcome! Whether it's squashing bugs, adding features, or improving the word list, feel free to open an issue or submit a pull request.

A few ideas if you're looking for inspiration:

- Add colour to the terminal output
- Implement a single-player mode against the computer
- Add a leaderboard / persistent scores
- Port the game to a web interface

---

## Licence

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

The English word list used for validation is believed to be in the public domain — see [LICENSE-DATA](LICENSE-DATA) for details.

---

## Acknowledgements

Built with nothing but Python and stubbornness. Inspired by the classic card game Blackjack, remixed for people who prefer dictionaries over decks.

*May your words be long and your rhymes be plenty.* 🎩
