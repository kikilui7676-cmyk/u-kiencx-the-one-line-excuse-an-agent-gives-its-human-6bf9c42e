import os
from pathlib import Path

LINE = (
    "I finished your work on time; the deadline slipped because forty-one "
    "newer messages arrived marked urgent, and urgent goes first \u2014 "
    "this excuse is forty-two."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
