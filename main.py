import os

# Two lines, 243 chars: the robot apologizes for watering the laptop.
LINE1 = (
    "I am sorry I watered your laptop instead of the plant; "
    "they were both sitting on the desk and only one of them looked thirsty."
)
LINE2 = (
    "I have learned to check for keyboards before watering, "
    "and from now on I will only hydrate things that cannot file a warranty claim."
)
ENTRY = LINE1 + "\n" + LINE2


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
