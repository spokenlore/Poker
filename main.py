from generate import *
from check import *
from analyze import *

import random, io, os, re

def main():
	# Generates samples using filename, and number of hands
	# generateSamples("sampleHands.txt", 100000)
	# Takes inputfile of sample hands, and outputs a file with the 'winning' hand of those cards
	# winningHands("sampleHands.txt", "winningHands.txt")
	# Utilizes inputfile of winninghands, counts combinations of each type of hand
	analyze("winningHands.txt", "analysis.txt")

if __name__ == '__main__':
	main()