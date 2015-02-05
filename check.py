RoyalFlush = 0
StraightFlush = 0
Quads = 0
FullHouse = 0
Flush = 0
Straight = 0
Triples = 0
TwoPairs = 0
Pairs = 0
HighCard = 0
TotalHands = 0

class Hand:
	def __init__(self, hand):
		if hand[-1] == '\n':
			hand = hand[:-1]

		fullhand = hand.split(" ")

		self.card1 = Card(fullhand[0])
		self.card2 = Card(fullhand[1])
		self.card3 = Card(fullhand[2])
		self.card4 = Card(fullhand[3])
		self.card5 = Card(fullhand[4])

	def display(self):
		print "The current cards in hand are:"
		self.card1.display() 
		self.card2.display()
		self.card3.display()
		self.card4.display()
		self.card5.display()

	def suits(self):
		arr = []
		arr.append(self.card1.suit)
		arr.append(self.card2.suit)
		arr.append(self.card3.suit)
		arr.append(self.card4.suit)
		arr.append(self.card5.suit)
		return arr

	def cards(self):
		arr = []
		arr.append(self.card1.num)
		arr.append(self.card2.num)
		arr.append(self.card3.num)
		arr.append(self.card4.num)
		arr.append(self.card5.num)
		return arr

	def num(self):
		arr = []
		arr.append(self.card1.card)
		arr.append(self.card2.card)
		arr.append(self.card3.card)
		arr.append(self.card4.card)
		arr.append(self.card5.card)
		return arr

class Card:
	def __init__(self, card):
		self.card = ""
		self.suit = ""
		self.num = ""
		if card[0] == 'c':
			self.suit = "Clubs"
		elif card[0] == 's':
			self.suit = "Spades"
		elif card[0] == 'h':
			self.suit = "Hearts"
		else: 
			self.suit = "Diamonds"

		self.card = str(card[1:])
		if self.card == 'J':
			self.num = 11
		elif self.card == 'Q':
			self.num = 12
		elif self.card == 'K':
			self.num = 13
		elif self.card == 'A':
			self.num = 14
		else:
			self.num = int(self.card)
	def display(self):
		print self.card + " of " + self.suit
		
def bestSet(HandObject):
	global RoyalFlush, StraightFlush, Quads, FullHouse, Flush, Straight
	global Triples, TwoPairs, Pairs, HighCard, TotalHands

	suits = HandObject.suits()
	cards = sorted(HandObject.cards())
	nums = sorted(HandObject.num())

	flush = checkFlush(suits)
	straight = checkStraight(cards)
	fullHouse = checkFullHouse(cards)

	TotalHands += 1

	if straight and flush and cards[-1] == 14:
		RoyalFlush += 1
		return "Royal Flush of %s" % (suits[0])
	elif straight and flush:
		StraightFlush += 1
		return "Straight Flush of %s, %s high" % (suits[0], convert(cards[-1]))
	elif straight:
		Straight += 1
		return "Straight, %s high" % (convert(cards[-1]))
	elif flush:
		Flush += 1
		return "Flush of %s, %s high" % (suits[0], convert(cards[-1]))
	elif checkQuad(cards):
		Quads += 1
		return "Quad %ss" % (convert(cards[2]))
	elif checkFullHouse(cards):
		FullHouse += 1
		if cards[2] == cards[1]:
			return "%ss full of %ss" % (convert(cards[2]), convert(cards[3]))
		else:
			return "%ss full of %ss" % (convert(cards[2]), convert(cards[1]))
	elif checkTriple(cards):
		Triples += 1
		return "Triple %ss" % (convert(cards[2]))
	elif checkTwoPair(cards):
		TwoPairs += 1
		if cards[0] == cards[1] and cards[2] == cards[3]:
			return "Two Pair, %ss and %ss" % (convert(cards[0]), convert(cards[2]))
		else:
			return "Two Pair, %ss and %ss" % (convert(cards[1]), convert(cards[3]))
	elif checkPair(cards):
		Pairs += 1
		if cards[0] == cards[1]:
			return "Pair of %ss" % (convert(cards[0]))
		elif cards[1] == cards[2]:
			return "Pair of %ss" % (convert(cards[1]))
		elif cards[2] == cards[3]:
			return "Pair of %ss" % (convert(cards[2]))
		else:
			return "Pair of %ss" % (convert(cards[3]))
	else:
		HighCard += 1
		return "High card, %s" % (convert(cards[-1]))

def winningHands(inputfile, outputfile):
	hand = 1
	with open(inputfile, 'r') as input:
		with open(outputfile, 'w') as output:
			while(hand):
				playerhand = input.readline()
				if playerhand == '':
					break
				playerhand = Hand(playerhand)
				output.write(bestSet(playerhand))
				output.write("\n")

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

def displayCombinations(outputfile):
	with open(outputfile, 'w') as output:
		output.write("%s: %s\n" % ("Royal Flushes", RoyalFlush))
		output.write("%s: %s\n" % ("Straight Flushes", StraightFlush))
		output.write("%s: %s\n" % ("Quadruples", Quads))
		output.write("%s: %s\n" % ("Full Houses", FullHouse))
		output.write("%s: %s\n" % ("Flushes", Flush))
		output.write("%s: %s\n" % ("Straights", Straight))
		output.write("%s: %s\n" % ("Triples", Triples))
		output.write("%s: %s\n" % ("Two Pairs", TwoPairs))
		output.write("%s: %s\n" % ("Pairs", Pairs))
		output.write("%s: %s\n" % ("High Cards", HighCard))
		output.write("%s: %s" % ("Total Hands", TotalHands))
