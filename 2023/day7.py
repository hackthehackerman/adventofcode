import enum
from util import tolines
from collections import Counter
import functools

def partone():
    lines = tolines("input/day7")
    hands = []
    for line in lines:
        hand,bid = line.split(" ")
        hands.append([hand,bid])
    
    def score(hand):
        # Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > one pair > high card
        c = Counter(hand)
        if  c.most_common(1)[0][1] == 5:
            # five of a kind
            return 7
        elif c.most_common(1)[0][1]==4:
            # four of a kind
            return 6
        elif c.most_common(2)[0][1] == 3 and c.most_common(2)[1][1] == 2:
            # full house
            return 5
        elif c.most_common(2)[0][1] == 3:
            # three of a kind
            return 4
        elif c.most_common(3)[0][1] == 2 and c.most_common(3)[1][1] == 2:
            # two pair
            return 3
        elif c.most_common(2)[0][1] == 2:
            # one pair
            return 2
        else:
            # high card
            return 1
            
        
    
    def compare(item1, item2):
        # Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > one pair > high card
        rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        hand1 = item1[0]
        hand2 = item2[0]
        
        if score(hand1) > score(hand2):
            return 1
        elif score(hand1) < score(hand2):
            return -1
        else:
            for i in range(5):
                if rank.index(hand1[i]) < rank.index(hand2[i]):
                    return 1
                elif rank.index(hand1[i]) > rank.index(hand2[i]):
                    return -1
            return 0
        
    hands.sort(key=functools.cmp_to_key(compare))
    ret = 0
    for idx, hand in enumerate(hands):
        h, b = hand
        ret += (idx+1) * int(b)
    return ret 
    
def parttwo():
    lines = tolines("input/day7")
    hands = []
    for line in lines:
        hand,bid = line.split(" ")
        hands.append([hand,bid])
    
    def score(hand):
        # Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > one pair > high card
        cc = Counter(hand)
        hand_copy = hand.replace("J","")
        c = Counter(hand_copy)
        # if "J" in hand:
            # print(hand,cc,c,c.most_common(1))
        if len(c.most_common(1)) == 0:
            c["J"] = 5
        else:
            c[c.most_common(1)[0][0]] += cc["J"]

        
        if  c.most_common(1)[0][1] == 5:
            # five of a kind
            return 7
        elif c.most_common(1)[0][1]==4:
            # four of a kind
            return 6
        elif c.most_common(2)[0][1] == 3 and c.most_common(2)[1][1] == 2:
            # full house
            return 5
        elif c.most_common(2)[0][1] == 3:
            # three of a kind
            return 4
        elif c.most_common(3)[0][1] == 2 and c.most_common(3)[1][1] == 2:
            # two pair
            return 3
        elif c.most_common(2)[0][1] == 2:
            # one pair
            return 2
        else:
            # high card
            return 1
            
        
    
    def compare(item1, item2):
        # Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > one pair > high card
        rank = ["A", "K", "Q",  "T", "9", "8", "7", "6", "5", "4", "3", "2","J"]
        hand1 : str = item1[0]
        hand2 : str = item2[0]
        
        if score(hand1) > score(hand2):
            return 1
        elif score(hand1) < score(hand2):
            return -1
        else:
            for i in range(5):
                if rank.index(hand1[i]) < rank.index(hand2[i]):
                    return 1
                elif rank.index(hand1[i]) > rank.index(hand2[i]):
                    return -1
            return 0
        
    hands.sort(key=functools.cmp_to_key(compare))
    ret = 0
    for idx, hand in enumerate(hands):
        h, b = hand
        
        ret += (idx+1) * int(b)
    return ret 

print("part one:", partone())
print("part two:", parttwo())
