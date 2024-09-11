"""Test sets"""
from hand_calulator import HandCalculator
import rules

# Test Cases
Str8_Flush = [
    ('Spade', 1), ('Spade', 2), ('Spade', 3), ('Spade', 4),
    ('Spade', 5), ('Spade', 6), ('Spade', 7), ('Spade', 8),
    ('Heart', 1), ('Heart', 2), ('Heart', 3)
]

Str8_Clog = [
    ('Spade', 1), ('Heart', 2), ('Diamond', 3), ('Club', 4),
    ('Star', 5), ('Cup', 6), ('Shield', 7), ('Moon', 8),
    ('Spade', 9), ('Heart', 10), ('Diamond', 11)
]

Eight_of_a_Kind = [
    ('Spade', 3), ('Heart', 3), ('Diamond', 3), ('Club', 3),
    ('Star', 3), ('Cup', 3), ('Shield', 3), ('Moon', 3),
    ('Spade', 4), ('Heart', 4), ('Diamond', 4)
]

The_Partners = [
    ('Spade', 2), ('Heart', 2), ('Diamond', 2), ('Club', 2),
    ('Spade', 7), ('Heart', 7), ('Diamond', 7), ('Club', 7),
    ('Star', 8), ('Cup', 8), ('Shield', 8)
]

Four_Pair = [
    ('Spade', 5), ('Heart', 5),
    ('Diamond', 9), ('Heart', 9),
    ('Spade', 12), ('Diamond', 12),
    ('Shield', 13), ('Spade', 13),
    ('Spade', 1), ('Heart', 1), ('Diamond', 1)
]

The_Mansion = [
    ('Spade', 4), ('Heart', 4), ('Diamond', 4), ('Club', 4), ('Star', 4),
    ('Spade', 6), ('Heart', 6), ('Diamond', 6),
    ('Cup', 7), ('Shield', 7), ('Moon', 7)
]

Eight_Card_Clog = [
    ('Spade', 9), ('Heart', 2), ('Diamond', 5), ('Club', 0),
    ('Star', 8), ('Cup', 10), ('Shield', 1), ('Moon', 0),
    ('Spade', 4), ('Heart', 6), ('Diamond', 11)
]

Eight_Card_Flush = [
    ('Heart', 1), ('Heart', 4), ('Heart', 7), ('Heart', 10),
    ('Heart', 8), ('Heart', 7), ('Heart', 8), ('Heart', 11),
    ('Heart', 3), ('Heart', 6), ('Heart', 13)
]

Str8 = [
    ('Spade', 1), ('Heart', 2), ('Heart', 3), ('Heart', 4),
    ('Heart', 5), ('Cup', 6), ('Shield', 7), ('Moon', 8),
    ('Moon', 9), ('Spade', 10), ('Spade', 11)
]

Straight_Flush_7 = [
    ('Star', 5), ('Star', 6), ('Star', 7), ('Star', 8),
    ('Star', 9), ('Star', 10), ('Star', 11),
    ('Cup', 1), ('Cup', 2), ('Cup', 3), ('Cup', 0)
]

Straight_Clog_7 = [
    ('Spade', 1), ('Heart', 2), ('Diamond', 3), ('Club', 4),
    ('Star', 5), ('Cup', 6), ('Shield', 7),
    ('Club', 1), ('Spade', 1), ('Heart', 10), ('Diamond', 11)
]

Seven_of_a_Kind = [
    ('Club', 8), ('Shield', 8), ('Cup', 8), ('Star', 8),
    ('Club', 8), ('Diamond', 8), ('Heart', 8),
    ('Diamond', 9), ('Heart', 9), ('Diamond', 9), ('Club', 9)
]

The_Duplex = [
    ('Spade', 10), ('Moon', 10), ('Diamond', 10), ('Club', 10),
    ('Star', 13), ('Cup', 13), ('Shield', 13),
    ('Shield', 2), ('Shield', 8), ('Moon', 2), ('Diamond', 7)
]

Seven_Card_Clog = [
    ('Spade', 3), ('Heart', 5), ('Diamond', 6), ('Club', 7),
    ('Star', 8), ('Cup', 8), ('Shield', 10),
    ('Spade', 12), ('Spade', 12), ('Heart', 13), ('Diamond', 0)
]

Seven_Card_Flush = [
    ('Cup', 1), ('Cup', 2), ('Cup', 8), ('Cup', 4),
    ('Cup', 5), ('Cup', 8), ('Cup', 7),
    ('Spade', 8), ('Spade', 9), ('Spade', 10), ('Spade', 11)
]

Seven_Card_Straight = [
    ('Shield', 5), ('Diamond', 7), ('Shield', 6),
    ('Star', 9), ('Cup', 10), ('Shield', 11), ('Cup', 12),
    ('Cup', 1), ('Diamond', 2), ('Cup', 3), ('Cup', 4)
]

Straight_Flush_6 = [
    ('Diamond', 4), ('Diamond', 5), ('Diamond', 6),
    ('Diamond', 7), ('Diamond', 8), ('Diamond', 9),
    ('Club', 0), ('Club', 2), ('Club', 0), ('Club', 4), ('Club', 0)
]

Straight_Clog_6 = [
    ('Spade', 1), ('Heart', 2), ('Diamond', 3),
    ('Club', 4), ('Star', 5),
    ('Cup', 6), ('Spade', 13), ('Heart', 8), ('Diamond', 9), ('Club', 10), ('Star', 2)
]

Six_of_a_Kind = [
    ('Shield', 9), ('Cup', 9), ('Shield', 9),
    ('Club', 9), ('Diamond', 9), ('Heart', 9),
    ('Spade', 10), ('Heart', 10), ('Diamond', 10), ('Club', 10), ('Shield', 10)
]

Two_Triplets = [
    ('Heart', 11), ('Diamond', 11), ('Heart', 11),
    ('Spade', 4), ('Spade', 4), ('Heart', 4),
    ('Diamond', 0), ('Spade', 1), ('Heart', 9), ('Diamond', 2), ('Club', 13)
]

Three_Pair = [
    ('Diamond', 7), ('Club', 7),
    ('Star', 5), ('Club', 5),
    ('Shield', 1), ('Club', 1),
    ('Spade', 2), ('Club', 9), ('Club', 13), ('Club', 0), ('Star', 4)
]

The_Apartment = [
    ('Spade', 3), ('Star', 3), ('Shield', 3), ('Spade', 3),
    ('Spade', 12), ('Club', 12),
    ('Club', 0), ('Club', 1), ('Star', 5), ('Star', 2), ('Shield', 7)
]

Clog_6 = [
    ('Spade', 8), ('Heart', 9), ('Diamond', 10),
    ('Club', 11), ('Star', 0), ('Club', 0),
    ('Shield', 1), ('Club', 2), ('Club', 7), ('Club', 4), ('Club', 5)
]

Flush_6 = [
    ('Shield', 2), ('Shield', 4), ('Shield', 6),
    ('Shield', 8), ('Shield', 0), ('Shield', 12),
    ('Club', 1), ('Club', 3), ('Club', 13), ('Club', 7), ('Club', 9)
]

Straight_6 = [
    ('Moon', 0), ('Spade', 1), ('Heart', 2),
    ('Moon', 3), ('Moon', 4), ('Star', 5),
    ('Moon', 13), ('Shield', 7), ('Moon', 8), ('Spade', 9), ('Heart', 10)
]

Straight_Flush = [
    ('Cup', 9), ('Spade', 10), ('Cup', 11),
    ('Spade', 12), ('Heart', 1),
    ('Club', 1), ('Club', 2), ('Club', 3), ('Club', 4), ('Club', 5), ('Cup', 1)
]

Straight_Clog = [
    ('Spade', 1), ('Heart', 2), ('Diamond', 3),
    ('Club', 4), ('Cup', 5),
    ('Cup', 12), ('Spade', 7), ('Spade', 8), ('Spade', 9), ('Heart', 10), ('Cup', 2)
]

Five_of_a_Kind = [
    ('Diamond', 5), ('Club', 5), ('Star', 5), ('Cup', 5),
    ('Club', 5), ('Club', 8), ('Diamond', 9), ('Diamond', 12), ('Diamond', 13), ('Club', 0), ('Star', 7)
]

Four_of_a_Kind = [
    ('Diamond', 5), ('Club', 5), ('Star', 5), ('Cup', 5),
    ('Club', 6), ('Club', 8), ('Diamond', 9), ('Diamond', 12), ('Diamond', 13), ('Club', 0), ('Star', 7)
]

Full_House = [
    ('Spade', 11), ('Heart', 11), ('Diamond', 11),
    ('Spade', 13), ('Star', 13),
    ('Heart', 9), ('Spade', 0), ('Heart', 6), ('Spade', 7), ('Heart', 1), ('Diamond', 2)
]

Flush = [
    ('Star', 6), ('Star', 7), ('Star', 8),
    ('Star', 9), ('Star', 0),
    ('Cup', 1), ('Cup', 0), ('Spade', 3), ('Cup', 13), ('Heart', 5), ('Heart', 6)
]

Clog = [
    ('Spade', 0), ('Heart', 13), ('Diamond', 2),
    ('Star', 3), ('Star', 4),
    ('Star', 5), ('Star', 6), ('Moon', 0), ('Moon', 8), ('Moon', 12), ('Moon', 10)
]

Straight = [
    ('Cup', 0), ('Shield', 10), ('Heart', 11),
    ('Heart', 12), ('Heart', 13),
    ('Diamond', 0), ('Diamond', 1), ('Diamond', 2), ('Cup', 3), ('Shield', 4), ('Heart', 0)
]

Three_of_a_Kind = [
    ('Spade', 0), ('Spade', 2), ('Star', 0),
    ('Star', 6), ('Shield', 8),
    ('Shield', 0), ('Spade', 12), ('Heart', 13), ('Heart', 1), ('Heart', 5), ('Star', 9)
]

Two_Pair = [
    ('Spade', 0), ('Spade', 2), ('Star', 0),
    ('Star', 6), ('Shield', 2),
    ('Shield', 10), ('Spade', 12), ('Heart', 13), ('Heart', 1), ('Heart', 5), ('Star', 9)
]

Pair = [
    ('Spade', 0), ('Spade', 2), ('Star', 0),
    ('Star', 6), ('Shield', 8),
    ('Shield', 10), ('Spade', 12), ('Heart', 13), ('Heart', 1), ('Heart', 5), ('Star', 9)
]

High_Card = [
    ('Spade', 0), ('Spade', 2), ('Star', 4),
    ('Star', 6), ('Shield', 8),
    ('Shield', 10), ('Spade', 12), ('Heart', 13), ('Heart', 1), ('Heart', 5), ('Star', 9)
]

group = [Str8_Flush, Str8_Clog, Eight_of_a_Kind, The_Partners, Four_Pair,
         The_Mansion, Eight_Card_Clog, Eight_Card_Flush, Str8, Straight_Flush_7,
         Straight_Clog_7, Seven_of_a_Kind, The_Duplex, Seven_Card_Clog, Seven_Card_Flush,
         Seven_Card_Straight, Straight_Flush_6, Straight_Clog_6, Six_of_a_Kind, Two_Triplets,
         Three_Pair, The_Apartment, Clog_6, Flush_6, Straight_6, Straight_Flush, Straight_Clog, Five_of_a_Kind,
         Four_of_a_Kind, Full_House, Flush, Clog, Straight, Three_of_a_Kind, Two_Pair, Pair, High_Card]

def print_human() -> None:
    """Prints cards in human readable format"""
    k = 0
    for g in group:
        print(f"{rules.get_hand_name(k)}:")
        for j in range(len(g)):
            rank = g[j][1]
            match (rank):
                case 1:
                    rank = 'A'
                case 11:
                    rank = 'J'
                case 12:
                    rank = 'Q'
                case 13:
                    rank = 'K'
            print(f"{rank} of {g[j][0]}s, ",end="")
            if j%3 == 2:
                print("")
        print("\n")
        k += 1

def run_tests():
    """Run test suite"""
    i = 0
    pss = 0
    for data in group:
        # Loops over each test set can calculates the hand
        hand = HandCalculator(data)
        # If the hand is equal to what the hand should be, it passes
        if rules.get_hand_name(i) == rules.get_hand_name(hand.calc_hand()):
            stat = "\033[92m(Pass)\033[0m"
            pss += 1
        else:
            stat = "\033[91m(Fail)\033[0m"

            # Print only the faild tests for simplicity
            print(f'{stat} Should Be: {rules.get_hand_name(i)}... is {rules.get_hand_name(hand.calc_hand())}')
        i += 1
    print(f'{pss}/{i} tests passed ({i-pss} failed)')

    # If all the tests passed, celebrate
    if pss == i:
        print("All tests passed! :D")
        return True

    return False

if __name__ == "__main__":
    run_tests()
