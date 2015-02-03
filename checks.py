def checkFlush(suits):
	suit1 = suits[0]

	for x in suits:
		if x != suit1:
			return False
	return True

def checkStraight(cards):
	if cards[0]+4 == cards[1]+3 == cards[2]+2 == cards[3]+1 == cards[4]:
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