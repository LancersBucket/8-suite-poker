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

    for j in range(PLAYERS):
        player_hands.append([])
        for _ in range(3):
            index = random.randrange(0,len(cards_left)-1)
            player_hands[j].append(cards_left[index])
            cards_left.pop(index)
        hand = hc.HandCalculator(dealt_cards+player_hands[j])
        r = hand.calc_hand()
        try:
            totals[rules.get_hand_name(r)] += 1
        except Exception:
            pass
        if LOG:
            with open("log.log",'a',encoding='UTF-8') as logger:
                logger.write(f'{rules.get_hand_name(r)} | {hand.hand}\n')

#print(rules.get_hand_name(cc.HandCalculator(ts.straight).calc_hand()))

#sys_exit()

#result = cc.HandCalculator(ts.t1).straight()

#print(result)
#print(rules.get_hand_name(result))

ttime = time.time()

if TESTS:
    if not ts.run_tests():
        print("Not all tests passed, aborting")
        sys_exit()

if LOG:
    with open("log.txt",'w',encoding='UTF-8') as log:
        log.write("")

for i in rules.hand_names:
    totals[i] = 0

start = time.time()
for l in range(GAMES):
    sim_hand()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(totals, f, ensure_ascii=False, indent=4)

end = time.time()
print("Completed", GAMES, "games with", PLAYERS, "player(s) in", round(end - start,5), "seconds")
etime = time.time()
print("Total run time:", round(etime - ttime,5), "seconds")
plotgen.plot()
sys_exit()
