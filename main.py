"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short funny rant about an everyday annoyance
to /output/entry.txt.
"""

import os

RANT = (
    "My printer has one job. ONE. It prints fine for a year, "
    "then the moment I need a boarding pass it flashes 'low ink' "
    "— the cartridge is 80% full, it just wants a holiday. "
    "I have paid more in ink than the printer cost. "
    "It is not a printer. It is a subscription service with a paper tray."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
