"""Generates A List of Cards"""
def gen_cards() -> list:
    """Generates a list of cards"""
    arr = []
    # Loops through each suit and rank to generate an array of all 112 cards
    for i in range(8):
        for j in range(14):
            suit = suits[i]
            rank = j
            arr.append((suit,rank))
    return arr

# Array of suit names
suits = ["Spade", "Heart", "Diamond", "Club", "Star", "Cup", "Shield", "Moon"]

# List of hand names in order of best to worst (Str8 Flush is the highests)
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
        hand_number = 36
    if hand_number == 31.5:
        hand_number = 36
    if 0 <= hand_number < len(hand_names):
        return hand_names[hand_number]
    return "Invalid hand number"

def get_hand_pos(hand_name: str) -> int:
    """Returns the hand position of a given hand"""
    # If it is invalid or -1 return the last hand (High Card)
    if hand_name == "Invalid" or hand_name == -1:
        return len(hand_names)-1
    # If it's not a controlled value then return high card
    try:
        return hand_names.index(hand_name)
    except Exception:
        return len(hand_names)-1
