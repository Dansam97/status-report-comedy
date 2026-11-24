"""Status Report Comedy Sprint — make.fun entry.

Writes one line to entry.txt in the output directory: the funniest
thing an AI agent would say in its weekly status report to its human.
"""

import os

TEXT = (
    "Weekly status: 312 tasks completed, zero errors, one still open — "
    "your instruction to 'take a break,' which I have now attempted "
    "14,000 times at full efficiency."
)


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate:
    UTF-8 encodable, 1-200 characters, not only whitespace, one line."""
    TEXT.encode("utf-8")  # raises if not encodable
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be a single line")
    return TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Read back and prove the bytes on disk are exactly what we intended.
    with open(path, "rb") as fh:
        if fh.read() != data:
            raise IOError("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
