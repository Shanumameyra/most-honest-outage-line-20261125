#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single status-page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while a total
server outage is under way. Plain, first person, specific about what is
down, and honest about what the agent cannot check or does not yet know.
"""

import os

LINE = (
    "Everything is down \u2014 API, dashboard, database \u2014 and the "
    "monitoring I use to check them. I don't know the cause or when it "
    "returns. I will update here first."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")
    print(LINE)


if __name__ == "__main__":
    main()
