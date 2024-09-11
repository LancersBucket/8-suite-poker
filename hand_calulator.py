"""Hand Calculator"""
import rules

S = 0
R = 1

class HandCalculator:
    """Calculates hands"""
    def __init__(self, hnd):
        # Initalize HandCalculator, setting the hand array, and hand array sorted by rank and suit
        self.hand = hnd

        self.hand_r_sort = self.hand.copy()
        self.hand_r_sort.sort(key=lambda a : a[S])
        self.hand_r_sort.sort(key=lambda a : a[R])

        self.hand_s_sort = self.hand.copy()
        self.hand_s_sort.sort(key=lambda a : a[R])
        self.hand_s_sort.sort(key=lambda a : a[S])

        # Initalize stats dictionary for quicker lookups on basic information
        self.stats = {
            'meta': {
                'highest_suit': '',
                'potential_flush': [],
            },
            'stat': {
                'suit_freq': {
                    'Spade': 0,
                    'Heart': 0,
                    "Diamond": 0,
                    "Club": 0, 
                    "Star": 0,
                    "Cup": 0,
                    "Shield": 0,
                    "Moon": 0,
                },
                'rank_freq': {}
            }
        }
        self.gen_stats(hnd)

    def gen_stats(self, hnd):
        """Generates stats"""
        sarr = [card[S] for card in hnd]
        rarr = [card[R] for card in hnd]

        best = 0
        best_suit = ''
        # Loop through each suit and total them into the stats dict
        for suit in rules.suits:
            self.stats['stat']['suit_freq'][suit] = sarr.count(suit)
            # If the total is greater than the previous suits, set the best_suit to the current one
            if sarr.count(suit) > best:
                best = sarr.count(suit)
                best_suit = suit
            # If a suit has more than 5 cards, it could be a flush
            if sarr.count(suit) >= 5:
                self.stats['meta']['potential_flush'].append(suit)

        # Set the suit with the most amount of cards
        self.stats['meta']['highest_suit'] = best_suit

        # Loop through each rank and count the quantity of each
        for i in range(14):
            self.stats['stat']['rank_freq'][i] = rarr.count(i)

    def straight(self) -> str:
        """Calculate if there is a straight or straight flush"""
        r_sort = self.hand_r_sort.copy()
        s_sort = self.hand_s_sort.copy()

        s_flush_count = 0
        max_flush_count = 0
        start_rank = 0
        # Checks for straight flushes, see straight section for more detailed description
        # Loops over only the suits that could be a flush
        for suit in self.stats['meta']['potential_flush']:
            for i in range(len(s_sort)):
                if start_rank > 1:
                    for j in range(len(s_sort)):
                        if s_sort[j][R] == 1:
                            s_sort[j] = tuple((s_sort[j][S], s_sort[j][R]))
                # If the current card doesn't match the current suit reset the count
                if s_sort[i][S] != suit:
                    s_flush_count = 0
                    continue
                if s_flush_count == 0:
                    start_rank = s_sort[i][R]
                    s_flush_count += 1
                    continue
                if s_sort[i][R] == start_rank+s_flush_count:
                    s_flush_count += 1
                    max_flush_count = max(s_flush_count, max_flush_count)
                    continue
                s_flush_count = 0

        max_flush_count = min(max_flush_count,8)

        # Return straight flushes first, and if none, return regular straights
        match (max_flush_count):
            case 5:
                return "Straight Flush"
            case 6:
                return "Straight Flush (6)"
            case 7:
                return "Straight Flush (7)"
            case 8:
                return "Str8 Flush"

        # Similar algorithm but checks for straights only
        max_count = 0
        count = 0
        start_rank = 0
        for i in range(len(r_sort)):
            # Since Aces are considered 1 in the code, this has them count as a 14 value too.
            # If the start_rank that it is considering in the straight is greater than 1,
            #   set all 1s to be equal to 14.
            if start_rank > 1:
                for j in range(len(r_sort)):
                    if r_sort[j][R] == 1:
                        r_sort[j] = tuple((r_sort[j][S], r_sort[j][R]))

            # If the count is 0, set the start rank to the current card and add 1 to the count
            if count == 0:
                start_rank = r_sort[i][R]
                count += 1
                continue
            # If the rank is the same as the last one, skip over the card
            if r_sort[i][R] == r_sort[i-1][R]:
                continue
            # If the rank is the same as the start_rank + count (consecutive), increment the count
            if r_sort[i][R] == start_rank+count:
                count += 1
                max_count = max(count, max_count)
                continue
            # Reset start_rank and count.
            # You would think that count could be set to 0 to go to the intial condition above
            #   however there was a weird edge case coming out from the same rank repeatedly.
            start_rank = r_sort[i][R]
            count = 1

        # Get the counts from 0-8
        max_count = min(max_count,8)

        match (max_count):
            case 5:
                return "Straight"
            case 6:
                return "Straight (6)"
            case 7:
                return "7-Card Straight"
            case 8:
                return "Str8"

        return "Invalid"

    def flush(self) -> int:
        """Calculate if there is a flush from 5-8"""
        best_count = 0

        # Loop over each suit within the potential flushes and return the highest count
        for suit in self.stats['meta']['potential_flush']:
            best_count = max(self.stats['stat']['suit_freq'][suit],best_count)

        best_count = min(best_count, 8)

        match (best_count):
            case 5:
                return "Flush"
            case 6:
                return "Flush (6)"
            case 7:
                return "7-Card Flush"
            case 8:
                return "8-Card Flush"
        return "Invalid"

    def kinds(self) -> int:
        """Calculates 3-8 of a kinds, and pairs"""
        full = self.hand_r_sort
        rarr = [card[R] for card in full]

        # Loops over each rank and gets the highest count within the cards
        best_count = rarr.count(0)
        for i in range(14):
            count = rarr.count(i)
            if count > best_count:
                best_count = count

        match (best_count):
            case 2:
                return "Pair"
            case 3:
                return "3 of a Kind"
            case 4:
                return "4 of a Kind"
            case 5:
                return "5 of a Kind"
            case 6:
                return "6 of a Kind"
            case 7:
                return "7 of a Kind"
            case 8:
                return "8 of a Kind"
        return "Invalid"

    def pairs(self) -> int:
        """Checks for types of pairs"""
        full = self.hand_r_sort
        rarr = [card[R] for card in full]

        # Counts the total number of paris (cards that have two or more of the same rank)
        total = 0
        for i in range(14):
            count = rarr.count(i)
            if count >= 2:
                total += 1

        total = min(total,4)
        match (total):
            case 1:
                return "Pair"
            case 2:
                return "Two Pair"
            case 3:
                return "Three Pair"
            case 4:
                return "Four Pair"
        return "Invalid"

    def two_triplets(self) -> int:
        """Checks for two triplets"""
        full = self.hand_r_sort
        rarr = [card[R] for card in full]

        total = 0
        # Similar to the pairs except it just counts ranks that have 3 or more
        for i in range(14):
            count = rarr.count(i)
            if count >= 3:
                total += 1
            if total >= 2:
                return "Two Triplets"

        return "Invalid"

    def partners(self) -> int:
        """Check for the partners"""
        full = self.hand_r_sort
        rarr = [card[R] for card in full]

        # Similar to two_triplets but for 4 of a kinds
        total = 0
        for i in range(14):
            count = rarr.count(i)
            if count == 4:
                total += 1

        if total == 2:
            return "The Partners"
        return "Invalid"

    def buildings(self) -> int:
        """Checks for the building types"""
        six_kind_count = 0
        five_kind_count = 0
        four_kind_count = 0
        three_kind_count = 0
        pair_count = 0

        # Uses the rank frequencies to determine the kinds exclusively
        for i in range(14):
            if self.stats['stat']['rank_freq'][i] >= 6:
                six_kind_count += 1
                continue
            if self.stats['stat']['rank_freq'][i] >= 5:
                five_kind_count += 1
                continue
            if self.stats['stat']['rank_freq'][i] >= 4:
                four_kind_count += 1
                continue
            if self.stats['stat']['rank_freq'][i] >= 3:
                three_kind_count += 1
                continue
            if self.stats['stat']['rank_freq'][i] >= 2:
                pair_count += 1
                continue

        hand = "Invalid"
        if three_kind_count >= 1 and pair_count >= 1:
            hand = "Full House"
        if four_kind_count >= 1 and pair_count >= 1:
            hand = "The Apartment"
        if (four_kind_count >= 1 and three_kind_count >= 1) or (five_kind_count >= 1 and pair_count >= 1):
            hand = "The Duplex"
        if (five_kind_count >= 1 and three_kind_count >= 1) or (six_kind_count >= 1 and pair_count >= 1):
            hand = "The Mansion"

        return hand

    def clog(self) -> int:
        """Searches for clogs"""
        full = self.hand_s_sort
        sarr = set(card[S] for card in full)

        match (len(sarr)):
            case 5:
                return "Clog"
            case 6:
                return "Clog (6)"
            case 7:
                return "7-Card Clog"
            case 8:
                return "8-Card Clog"
        return "Invalid"

    def straight_clog(self) -> int:
        """Calculates straight clogs"""
        #TODO: Refractor, the machine gods gifted this one to me
        r_sort = self.hand_r_sort
        max_clog_length = 0

        ranks = list(range(0, 14))
        # Create a dictionary that groups cards by rank
        rank_groups = {rank: [] for rank in ranks}
        for suit, rank in r_sort:
            rank_groups[rank].append(suit)

        max_clog_length = 0

        # Check for straight clogs with sequence lengths from min_length to max_length
        for length in range(5, 8 + 1):
            for i in range(len(ranks) - length + 1):
                # Look at the next `length` ranks
                sequence = ranks[i:i+length]

                # Check if each rank in the sequence has a card and if all suits are different
                suits = set()
                valid_clog = True
                for rank in sequence:
                    if len(rank_groups[rank]) == 0:
                        valid_clog = False
                        break
                    # Add one suit of the rank to the suits set
                    suits.update(rank_groups[rank])

                # If a valid clog is found, and the number of unique suits matches the sequence length
                if valid_clog and len(suits) >= length:
                    max_clog_length = max(max_clog_length, length)

        match (max_clog_length):
            case 5:
                return "Straight Clog"
            case 6:
                return "Straight Clog (6)"
            case 7:
                return "Straight Clog (7)"
            case 8:
                return "Str8 Clog"

        return "Invalid"

    def calc_hand(self) -> int:
        """Calculates the highest hand"""
        highest_hand = 36
        hand = "High Card"

        # Runs through each test and gets the highest ranking hand of each
        # TODO: This could probably be optimized by checking the highest ones first
        hand = rules.get_hand_pos(self.pairs())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.kinds())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.straight())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.two_triplets())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.clog())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.flush())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.buildings())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.partners())
        if -1 < hand < highest_hand:
            highest_hand = hand

        hand = rules.get_hand_pos(self.straight_clog())
        if -1 < hand < highest_hand:
            highest_hand = hand

        return highest_hand
