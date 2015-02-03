def checkFlush(suits):
	suit1 = suits[0]

	for x in suits:
		if x != suit1:
			return False
	return True

def checkStraight(cards):
	if int(cards[0])+4 == int(cards[1])+3 == int(cards[2])+2 == int(cards[3])+1 == int(cards[4]):
		return True
	else:
		return False

def checkQuad(cards):
	if cards[0] == cards[1] == cards[2] == cards[3] or cards[1] == cards[2] == cards[3] == cards[4]:
		return True
	else:
		return False

def checkTriple(cards):
	if (cards[0] == cards[1] == cards[2]) or (cards[1] == cards[2] == cards[3]) or (cards[2] == cards[3] == cards[4]):
		return True
	else:
		return False

def checkTwoPair(cards):
	if cards[0] == cards[1] and cards[2] == cards[3]:
		return True
	elif cards[1] == cards[2] and cards[3] == cards[4]:
		return True
	else:
		return False

def checkFullHouse(cards):
	if (cards[0] == cards[1] == cards[2]) and (cards[3] == cards[4]):
		return True
	elif (cards[0] == cards[1]) and (cards[2] == cards[3] == cards[4]):
		return True
	else:
		return False

def checkPair(cards):
	if cards[0] == cards[1] or cards[1] == cards[2] or cards[2] == cards[3] or cards[3] == cards[4]:
		return True
	else:
		return False

def convert(card):
	if card == 14:
		return 'A'
	elif card == 13:
		return 'K'
	elif card == 12:
		return 'Q'
	elif card == 11:
		return 'J'
	else:
		return card
