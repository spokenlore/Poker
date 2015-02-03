def checkFlush(suits):
	suit1 = suits[0]

	for x in suits:
		if x != suit1:
			return False
	return True

def checkStraight(cards):
	cards = cards.sort()

	card1 = cards[0]
	for x in cards:
		if x == card1+1:
			card1 = x
		else:
			return False
	return True

def checkStraightFlush(bool1, bool2):
	return bool1 and bool2