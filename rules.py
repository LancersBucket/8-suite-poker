"""Generates A List of Cards"""
def gen_cards() -> list:
    """Generates a list of cards"""
    arr = []
    for i in range(8):
        for j in range(14):
            suit = ""
            rank = -1
            match i:
                case 0:
                    suit = "Spade"
                case 1:
                    suit = "Heart"
                case 2:
                    suit = "Diamond"
                case 3:
                    suit = "Club"
                case 4:
                    suit = "Star"
                case 5:
                    suit = "Cup"
                case 6:
                    suit = "Shield"
                case 7:
                    suit = "Moon"
            rank = j
            arr.append((suit,rank))
    return arr

"""
0	Str8 Flush
1	Str8 Clog
2	8 of a Kind
3	The Partners
4	Four Pair
5	The Mansion
6	8-Card Clog
7	8-Card Flush
8	Str8
9	Straight Flush (7)
10	Straight Clog (7)
11	7 of a Kind
12	The Duplex
13	7-Card Clog
14	7-Card Flush
15	7-Card Straight
16	Straight Flush (6)
17	Straight Clog (6)
18	6 of a Kind
19	Two Triplets
20	Three Pair
21	The Apartment
22	Clog (6)
23	Flush (6)
24	Straight (6)
25	Straight Flush
26	Straight Clog
27	5 of a Kind
28	4 of a Kind
29	Full House
30	Flush
31	Clog 
32	3 of a Kind
33	Two Pair
34	Pair
35	High Card
"""

hand_names = [
    "Str8 Flush",
    "Str8 Clog",
    "8 of a Kind",
    "The Partners",
    "Four Pair",
    "The Mansion",
    "8-Card Clog",
    "8-Card Flush",
    "Str8",
    "Straight Flush (7)",
    "Straight Clog (7)",
    "7 of a Kind",
    "The Duplex",
    "7-Card Clog",
    "7-Card Flush",
    "7-Card Straight",
    "Straight Flush (6)",
    "Straight Clog (6)",
    "6 of a Kind",
    "Two Triplets",
    "Three Pair",
    "The Apartment",
    "Clog (6)",
    "Flush (6)",
    "Straight (6)",
    "Straight Flush",
    "Straight Clog",
    "5 of a Kind",
    "4 of a Kind",
    "Full House",
    "Flush",
    "Clog",
    "Straight",
    "3 of a Kind",
    "Two Pair",
    "Pair",
    "High Card",
]

def get_hand_name(hand_number: int) -> str:
    """Returns a hand name from an index"""
    if hand_number == -1:
        hand_number = 35
    if hand_number == 31.5:
        hand_number = 36
    if 0 <= hand_number < len(hand_names):
        return hand_names[hand_number]
    return "Invalid hand number"

def get_hand_pos(hand_name: str) -> int:
    """Returns the hand position of a given hand"""
    if hand_name == "Invalid" or hand_name == -1:
        return len(hand_names)-1
    try:
        return hand_names.index(hand_name)
    except Exception:
        return len(hand_names)-1

suits = ["Spade", "Heart", "Diamond", "Club", "Star", "Cup", "Shield", "Moon"]
