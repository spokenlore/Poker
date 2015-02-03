import random, io, os

from checks import *

class Hand:
	def __init__(self, hand):
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

class Card:
	def __init__(self, card):
		self.card = ""
		self.suit = ""
		self.num = ""
		if card[0] == 'c':
			self.suit = "clubs"
		elif card[0] == 's':
			self.suit = "spades"
		elif card[0] == 'h':
			self.suit = "hearts"
		else: 
			self.suit = "diamonds"

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

def initDeck():
	deck = []
	suits = ["d", "c", "h", "s"]
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
	for x in suits:
		for y in cards:
			deck.append(x+str(y))
	newdeck = []
	for y in deck:
		drop = int(random.random()*len(deck))
		newdeck.append(deck[drop])
	return newdeck

def generateSamples(filename, numSamples):
	with open(filename, "w") as outputfile:
		for x in xrange(0,numSamples+1):
			deck = initDeck()
			openingHand = deck[0] + " " + deck[1] + " " + deck[2] + " " + deck[3] + " " + deck[4] + "\n"
			outputfile.write(openingHand)

def checkHands(inputfile, outputfile):
	hand = 1
	with open(inputfile, 'r') as input:
		with open(outputfile, 'w') as output:
			while(hand):
				hand = input.readline()
				output.write(analyze(hand))

def readHand(hand):
	playerhand = Hand(hand)
	# playerhand.display()
	return playerhand

def analyzeHand(HandObject):
	suits = HandObject.suits()
	cards = HandObject.cards()

	flush = checkFlush(suits)
	straight = checkStraight(cards)
	straightflush = checkStraightFlush(straight, flush)
	# quad = checkQuad(cards)
	# triple = checkTriple(cards)
	# twopair = checkTwoPair(cards)
	# pair = checkPair(cards)

	print suits
	print cards


# readHands("samples.txt", "analysis.txt")
# readHand("c4 s5 h6 d10 cA")
currentHand = readHand("c4 s5 h6 d10 cA")
analyzeHand(currentHand)