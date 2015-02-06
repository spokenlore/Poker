import random

def initDeck():
	deck = []
	suits = ["d", "c", "h", "s"]
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
	for x in suits:
		for y in cards:
			deck.append(x+str(y))
	newdeck = []
	for y in xrange(0,11):
		drop = int(random.random()*len(deck))
		newdeck.append(deck[drop])
		deck.pop(drop)
	return newdeck

def generateSamples(filename, numSamples, nextCardsFile):
	with open(filename, "w") as outputfile:
		with open(nextCardsFile, "w") as nextCardsOutput: 
			for x in xrange(0,numSamples):
				deck = initDeck()
				openingHand = deck[0] + " " + deck[1] + " " + deck[2] + " " + deck[3] + " " + deck[4] + "\n"
				nextCards = deck[6] + " " + deck[7] + " " + deck[8] + " " + deck[9] + " " + deck[10] + "\n"
				outputfile.write(openingHand)
				nextCardsOutput.write(nextCards)

# Simple display test program of format
# s = suit, c = card
# readHand("sc sc sc sc sc")
def readHand(hand):
	playerhand = Hand(hand)
	# playerhand.display()
	return playerhand