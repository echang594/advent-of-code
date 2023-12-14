from collections import Counter

CARD_STRENGTH = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

with open("2023/Day07/input.txt") as f:
    lines = f.read().splitlines()


def find_type(hand: str):
    counter = Counter(hand)
    most_common = counter.most_common(3)
    if most_common[0][1] == 5:
        return 6
    if most_common[0][1] == 4:
        return 5
    if most_common[0][1] == 3 and most_common[1][1] == 2:
        return 4
    if most_common[0][1] == 3:
        return 3
    if most_common[0][1] == 2 and most_common[1][1] == 2:
        return 2
    if most_common[0][1] == 2:
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
