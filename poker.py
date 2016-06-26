from collections import Counter


def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    hands = []
    random.shuffle(deck)
    for x in range(numhands):
    	hands.append(mydeck[-n:])
    	del mydeck[-n:]

    return hands


def poker(hands):
	#take list of hands and return the best hand
	#acall deal here
	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	"Return a list of all items equal to the max of the iterable"
	"The iterable will be a tuple"
	largest = max(iterable, key=hand_rank)
	return [hand in iterable if hand >= largest]


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    "Handle an Ace Low Straight as well A2345"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks


def hand_rank(hand):
	#Below fails to distinguirh between rankings that are of the same kind, but differing values
	#Pair of 10s vs Pair of 9s
	ranks = card_ranks(hand) #return in sorted order!
	if straight(ranks) and flush(hand):
		return (8, max(ranks)) # 2 3 4 5 6 --> 6 specifies the rest, 6,7,8,9, T -> (8, 10)
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)


def straight(ranks):
	for x in range(0,len(ranks)-1):
		if abs(ranks[x] - ranks[x+1]) > 1:
			return False
	return True

def flush(hand):
    "Return True if all the cards have the same suit."
    return len(set([y for x,y in hand])) == 1

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    vals = []
    for r in ranks:
        if ranks.count(r) == 2:
            vals.append(r)
    if len(vals) == 2:
        return (vals[0], vals[1])
    return None	

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
    	if ranks.count(r) == n:
    		return r
    return None


def test():
	"Test cases for the functions in a poker program"
	sf = "6C 7C 8C 9C TC".split()  #straight flush
	fk = "9D 9H 9S 9C 7D".split()  #five of a kind
	fh = "TD TC TH 7C 7D".split()  # full house
	al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
	assert straight([9,8,7,6,5]) == True
	assert straight([9,8,7,6,3]) == False
    assert flush(sf) == True
    assert flush(fk) == False
	assert card_ranks(sf) = [10,9,8,7,6]
	assert card_ranks(fk) = [9,9,9,9,7]
	assert card_ranks(fh) = [10,10,10,7,7] 
	assert poker([sf, fk, fh]) == sf
	assert poker([fk, fh]) == fk
	assert poker([fk, fh]) == fk
	assert poker([fh, fh]) == fh
	assert poker([fh]) == fh
	assert poker([[sf]  + [fh]*99]) == sf
	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10, 7) # 3 of one 2 of another suit
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert straight(card_ranks(al)) == True 
	return "tests pass"


print test()


# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

# def card_ranks(cards):
#     "Return a list of the ranks, sorted with higher first."
#     ranks = [r for r,s in cards]
#     mapping = {"T": 10, "J": 11, "Q":12, "K": 13, "A": 14}
#     ranks2 = []
#     for r in ranks:
#         if r in mapping.keys():
#             ranks2.append(int(mapping[r]))
#         else:
#             ranks2.append(int(r))
#     ranks2.sort(reverse=True)
#     return ranks2