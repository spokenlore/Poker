def analyze(inputfile, outputfile):
	# create 'dictionary' of hands

	# Patterns = compileRegEx()
	with open(inputfile, 'r') as input:
		a = {}
		with open(outputfile, 'w') as output:
			bestHand = input.readline()
			while(1):
				if bestHand == '':
					for key in a:
						output.write("%s: %s\n" % (key, a[key]))
					break
				else:
					key = bestHand[:-1]
					if key in a:
						a[key] += 1
					else:
						a[key] = 1
					bestHand = input.readline()


# def compileRegEx():
# 	RegExArr = []

# 	re.compile()
# 	return RegExArr
