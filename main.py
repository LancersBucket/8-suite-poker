"""Simulation"""
import random
import time
from sys import exit as sys_exit
import json
import rules
from hand_calulator import HandCalculator
import plotgen
import testsets as ts

# Configuration

# Total cards to work with
TOTAL_CARDS = rules.gen_cards()

# Number of players
PLAYERS = 1

# Number of games
GAMES = 10000

# Running tests before simulation to verify calculator. Will abort if any test fails.
TESTS = False

# Log each hand and what it calculated it as
LOG = False

# Display a chart of the data at the end of the simulation
CHART = True

S = 0
R = 1

totals = {
    'meta': {
        'games_played': 0,
        'players': 0,
        'completed': 0
    },
    'totals': {}
}

def sim_hand():
    """Simulates the hands"""
    dealt_cards = []
    player_hands = []
    cards_left = TOTAL_CARDS.copy()

    # Deal 8 Table Cards
    for _ in range(8):
        index = random.randrange(0,len(cards_left)-1)
        dealt_cards.append(cards_left[index])
        cards_left.pop(index)

    # Deal hand of 3 to each player
    for j in range(PLAYERS):
        player_hands.append([])
        for _ in range(3):
            index = random.randrange(0,len(cards_left)-1)
            player_hands[j].append(cards_left[index])
            cards_left.pop(index)

        # Calculate the hand
        hand = HandCalculator(dealt_cards+player_hands[j])
        r = hand.calc_hand()

        # Add the total to the return dict
        try:
            totals['totals'][rules.get_hand_name(r)] += 1
        except Exception:
            pass
        # If there is logging enabled, log the hand and what it returned
        if LOG:
            with open("log.log",'a',encoding='UTF-8') as logger:
                logger.write(f'{rules.get_hand_name(r)} | {hand.hand}\n')

if __name__ == "__main__":
    # If tests is enabled, run the tests before starting and abort if not all tests pass
    if TESTS:
        if not ts.run_tests():
            print("Not all tests passed, aborting...")
            sys_exit()

    # Initilize the logging file
    if LOG:
        with open("log.txt",'w',encoding='UTF-8') as log:
            log.write("")

    # Initialize the total dict
    for i in rules.hand_names:
        totals['totals'][i] = 0

    print(f"Starting simulation... ({GAMES} games, {PLAYERS} player(s); {GAMES*PLAYERS} hands)")

    # Start the time for the simulation and simulate all the hands
    start = time.time()

    totals['meta']['games_played'] = GAMES
    totals['meta']['players'] = PLAYERS

    for l in range(GAMES):
        sim_hand()

    # End the sim time and retrun status
    end = time.time()
    print(f"Simulated {GAMES*PLAYERS} hands in {round(end - start,5)} seconds")
    totals['meta']['completed'] = end

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(totals, f, ensure_ascii=False, indent=4)

    # Plot the data
    if CHART:
        plotgen.plot()

    sys_exit()
