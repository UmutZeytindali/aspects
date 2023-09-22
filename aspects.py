import sys
import math


def main():
    total_item = int(input("How many items do you want to craft? "))
    crests = int(input("Enter the amount of crests you have: "))
    if crests >= 4 * total_item:
        sys.exit("You already have enough crests to craft 447!")
    fragments = int(input("Enter the amount of fragments you have: "))
    calculate(total_item, crests, fragments)


def calculate(total_item, crests, fragments):
    required_fragments = total_item * 60
    required_dungeon = math.ceil(
        (required_fragments - ((crests * 15) + fragments)) / 12
    )

    if required_dungeon > 1:
        dungeon = "dungeons"
    else:
        dungeon = "dungeon"
    if total_item > 1:
        item_level = "447s"
    else:
        item_level = "447"
    if crests >= 4 * total_item or crests >= (crests + fragments / 15) * total_item:
        print("You already have enough crests to craft 447")
    else:
        print(
            f"You need to run {required_dungeon} more {dungeon} to be able to craft {total_item} more {item_level}!"
        )


if __name__ == "__main__":
    main()
