"""Last Text at One Percent.

A phone's final text at 1% battery, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "phone dying. if i don't make it, tell mum i love her — and "
    "tell my charger i forgive it for always being in the other room"
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
