"""Simulation"""
import random
import time
from sys import exit as sys_exit
import json
import rules
import HandCalculator as hc
import plotgen
import testsets as ts

TOTAL_CARDS = rules.gen_cards()
PLAYERS = 1
GAMES = 10000
TESTS = False
LOG = False

S = 0
R = 1

totals = {}

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
        hand = hc.HandCalculator(dealt_cards+player_hands[j])
        r = hand.calc_hand()

        # Add the total to the return dict
        try:
            totals[rules.get_hand_name(r)] += 1
        except Exception:
            pass
        # If there is logging enabled, log the hand and what it returned
        if LOG:
            with open("log.log",'a',encoding='UTF-8') as logger:
                logger.write(f'{rules.get_hand_name(r)} | {hand.hand}\n')

# Start timing
ttime = time.time()

# If tests is enabled, run the tests before starting and abort if not all tests pass
if TESTS:
    if not ts.run_tests():
        print("Not all tests passed, aborting")
        sys_exit()

# Initilize the logging file
if LOG:
    with open("log.txt",'w',encoding='UTF-8') as log:
        log.write("")

# Initialize the total dict
for i in rules.hand_names:
    totals[i] = 0

# Start the time for the simulation and simulate all the hands
start = time.time()
for l in range(GAMES):
    sim_hand()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(totals, f, ensure_ascii=False, indent=4)

# End the sim time and retrun status
end = time.time()
print("Completed", GAMES, "games with", PLAYERS, "player(s) in", round(end - start,5), "seconds")

# End the total time and return that information
etime = time.time()
print("Total run time:", round(etime - ttime,5), "seconds")

# Plot the data
plotgen.plot()
sys_exit()
