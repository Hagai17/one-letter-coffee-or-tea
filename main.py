"""Write one letter to /output/entry.txt: A for coffee, B for tea.

The pick is A: coffee. It was duelled against B (tea) across the judge's
criteria in order — vivid, funny, truer, standing alone — and then
survived a revision round that steelmanned tea at full strength: tea
took the wit criterion and honestly contested trueness (an agent steeps;
it never needs waking), but it never took vividness, the first criterion,
and the pick stands. The full deliberation lives in candidates.md.
"""

import os

LETTER = "A"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
