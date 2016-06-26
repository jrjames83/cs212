def straight(ranks):
	for x in range(0,len(ranks)-1):
		if abs(ranks[x] - ranks[x+1]) > 1:
			return False
	return True


# print straight([1,2,3,4,5])
# print straight([1,2,3,4,6])
# print straight([6,4,3,2,1])


sf = "6C 7C 8C 9C TC".split()
fk = "9D 9H 9S 9C 7D".split()

# print sf
# print set([y for x,y in sf])
# print set([y for x,y in fk])

def flush(hand):
    "Return True if all the cards have the same suit."
    return len(set([y for x,y in hand])) == 1

# print flush(sf)
# print flush(fk)


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    counts = {}
    for x in ranks:
    	if x in counts.keys():
    		counts[x] +=1
    	else:
    		counts[x] = 1
    return counts[x] == n

