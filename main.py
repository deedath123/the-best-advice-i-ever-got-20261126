#!/usr/bin/env python3
"""Best advice entry: one sentence, written to /output/entry.txt."""

import os

ENTRY = (
    "When I was sixteen, my grandfather handed me his dented toolbox at 5 AM "
    "and said, \"Son, nobody remembers how fast you started — "
    "they remember whether you showed up when it broke.\""
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.count(".") + text.count("!") + text.count("?") >= 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
