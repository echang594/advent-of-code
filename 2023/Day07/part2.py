from collections import Counter

CARD_STRENGTH = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

with open("2023/Day07/input.txt") as f:
    lines = f.read().splitlines()


def find_type(hand: str):
    counter = Counter(hand)
    most_common = counter.most_common(2)
    if (
        most_common[0][1] == 5
        or most_common[0][1] == 4
        and counter["J"] == 1
        or most_common[0][1] == 3
        and counter["J"] == 2
        or most_common[1][1] == 2
        and counter["J"] == 3
        or counter["J"] == 4
    ):
        return 6
    if (
        most_common[0][1] == 4
        or most_common[0][1] == 3
        and counter["J"] == 1
        or (
            most_common[0][0] != "J"
            and most_common[0][1] == 2
            or most_common[1][0] != "J"
            and most_common[1][1] == 2
        )
        and counter["J"] == 2
        or counter["J"] == 3
    ):
        return 5
    if (
        most_common[0][1] == 3
        and most_common[1][1] == 2
        or most_common[0][1] == 2
        and most_common[1][1] == 2
        and counter["J"] == 1
    ):
        return 4
    if most_common[0][1] == 3 or most_common[0][1] == 2 and counter["J"] == 1 or counter["J"] == 2:
        return 3
    if most_common[0][1] == 2 and most_common[1][1] == 2:
        return 2
    if most_common[0][1] == 2 or counter["J"] == 1:
        return 1
    return 0


hands = []
for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    hands.append((hand, bid))

hands.sort(key=lambda hand: (find_type(hand[0]), *(CARD_STRENGTH[card] for card in hand[0])))

sum = sum(bid * rank for rank, (_, bid) in enumerate(hands, 1))

print(sum)
