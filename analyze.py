def analyzeOccurences(inputfile, outputfile):
	# create 'dictionary' of hands
	totalhands = 0
	# Patterns = compileRegEx()
	with open(inputfile, 'r') as input:
		a = {}
		with open(outputfile, 'w') as output:
			bestHand = input.readline()
			while(1):
				if bestHand == '':
					sorted_a = sorted(a.items(), key = lambda x:x[1])
					for x in xrange(len(sorted_a)-1, 0, -1)	:
						output.write("%s: %s\n" % (str(sorted_a[x][0]), str(sorted_a[x][1])))
					break
				else:
					key = bestHand[:-1]
					if key in a:
						a[key] += 1
					else:
						a[key] = 1
					bestHand = input.readline()

def compileRegEx():
	RegExArr = []

# 	re.compile()
# 	return RegExArr
