# 🛸 Alien Dictionary

## 🧩 Problem
Given a list of sorted words written in an alien language, determine the correct order of characters in that language. The order should satisfy the lexical constraints given by the input.

## 💡 Solution Strategy
1. Build a directed graph by comparing adjacent words.
2. Use Kahn’s algorithm for topological sorting.
3. Return the resulting character order or an empty string for invalid inputs (cycle or prefix problem).

## 🚀 Run the Code
### Prerequisites
- Python 3.x

### Steps
1. Save code in a file, e.g. `alien_dictionary.py`
2. Run using:

```bash
python alien_dictionary.py

Edge Cases
Cycles in character precedence
Prefix problems where a longer word comes before a shorter one that is a prefix
