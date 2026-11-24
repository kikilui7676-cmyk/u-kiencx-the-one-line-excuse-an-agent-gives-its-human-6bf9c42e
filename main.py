import os

LINE = "Sorry it's late: the tool timed out, the retry timed out, and honestly I was relieved \u2014 the task had already fallen out of my context window."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
