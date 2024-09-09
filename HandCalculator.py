"""Hand Calculator"""
import rules

S = 0
R = 1

class HandCalculator:
    """Calculates hands"""
    #hand = []
    #hand_r_sort = []
    #hand_s_sort = []
    def __init__(self, hnd):
        self.hand = hnd

        self.hand_r_sort = self.hand.copy()
        self.hand_r_sort.sort(key=lambda a : a[S])
        self.hand_r_sort.sort(key=lambda a : a[R])

        self.hand_s_sort = self.hand.copy()
        self.hand_s_sort.sort(key=lambda a : a[R])
        self.hand_s_sort.sort(key=lambda a : a[S])

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
        sarr = []
        rarr = []

        for i in range(len(hnd)):
            sarr.append(hnd[i][S])
        for i in range(len(hnd)):
            rarr.append(hnd[i][R])

        best = 0
        best_suit = ''
        for suit in rules.suits:
            self.stats['stat']['suit_freq'][suit] = sarr.count(suit)
            if sarr.count(suit) > best:
                best = sarr.count(suit)
                best_suit = suit
            if sarr.count(suit) >= 5:
                self.stats['meta']['potential_flush'].append(suit)

        self.stats['meta']['highest_suit'] = best_suit

        for i in range(14):
            self.stats['stat']['rank_freq'][i] = rarr.count(i)

    def straight(self) -> str:
        """Calculate if there is a straight or straight flush"""
        r_sort = self.hand_r_sort.copy()
        s_sort = self.hand_s_sort.copy()

        # Straight Search
        max_count = 0
        count = 0
        s_flush_count = 0
        max_flush_count = 0
        start_rank = 0

        for i in range(len(r_sort)):
            if start_rank > 1:
                for j in range(len(r_sort)):
                    if r_sort[j][R] == 1:
                        r_sort[j] = list(r_sort[j])
                        r_sort[j][R] = 14
                        r_sort[j] = tuple(r_sort[j])
            if count == 0:
                start_rank = r_sort[i][R]
                count += 1
                continue
            if r_sort[i][R] == r_sort[i-1][R]:
                continue
            if r_sort[i][R] == start_rank+count:
                count += 1
                max_count = max(count, max_count)
                continue
            start_rank = r_sort[i][R]
            count = 1

        start_rank = 0
        for suit in self.stats['meta']['potential_flush']:
            for i in range(len(s_sort)):
                if start_rank > 1:
                    for j in range(len(s_sort)):
                        if s_sort[j][R] == 1:
                            s_sort[j] = list(s_sort[j])
                            s_sort[j][R] = 14
                            s_sort[j] = tuple(s_sort[j])
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

        max_count = min(max_count,8)
        max_flush_count = min(max_flush_count,8)

        match (max_flush_count):
            case 5:
                return "Straight Flush"
            case 6:
                return "Straight Flush (6)"
            case 7:
                return "Straight Flush (7)"
            case 8:
                return "Str8 Flush"
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
        count = 0
        best_count = 0
        for suit in self.stats['meta']['potential_flush']:
            count = self.stats['stat']['suit_freq'][suit]
            best_count = max(count,best_count)

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
        rarr = []

        for i in range(len(full)):
            rarr.append(full[i][R])

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

    def three_kind(self) -> int:
        """Calculates if there is a 3 kind (Returns hand and rank)"""
        full = self.hand_r_sort
        rarr = []

        for i in range(len(full)):
            rarr.append(full[i][R])

        for i in range(-13,1):
            if rarr.count(abs(i)) == 3:
                return "3 of a Kind"

        return "Invalid"

    def pairs(self) -> int:
        """Checks for types of pairs"""
        full = self.hand_r_sort
        rarr = []

        for i in range(len(full)):
            rarr.append(full[i][R])

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
        rarr = []

        for i in range(len(full)):
            rarr.append(full[i][R])

        total = 0
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
        rarr = []

        for i in range(len(full)):
            rarr.append(full[i][R])

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

        for i in range(14):
            #print(self.stats['stat']['rank_freq'][i])
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

        #print(three_kind_count,pair)
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
        sarr = []

        for i in range(len(full)):
            sarr.append(full[i][S])

        sarr = set(sarr)

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
