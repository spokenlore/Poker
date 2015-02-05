from generate import *
from check import *
from analyze import *

import random, io, os, operator

def main():
	# Generates samples using filename, and number of hands
	generateSamples("sampleHands.txt", 10000000)
	# Takes inputfile of sample hands, and outputs a file with the 'winning' hand of those cards
	winningHands("sampleHands.txt", "winningHands.txt")
	# Outputs combinations of each type of hand to a target outputfile
	displayCombinations("combinations.txt")
	# Utilizes inputfile of winninghands, counts occurrences each type of hand
	analyzeOccurences("winningHands.txt", "analysis.txt")

if __name__ == '__main__':
	main()