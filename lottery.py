# ************************
# ** Parse lottery data **
# ************************
#pass in a dict of files and the number of balls in the draw
files = {'lotto-draw-history.csv':6, 'euromillions-draw-history.csv':5}
for file in files.keys():
	inputData = open(file, 'r')
	drawSize = files[file]
	processedData = []
	for line in inputData:
		allElements = line.split(',')
		if 'DrawDate' not in allElements:
			numbers = allElements[1:drawSize + 1]
			numbers = map(int, numbers)
			processedData.append(numbers)
	processedData.pop(0)
	inputData.close()

	def findHighestBallValue(listofdraws):
		foundMax = 0
		for draw in listofdraws:
			if max(draw) > foundMax:
				foundMax = max(draw)
		return foundMax

	def optimaldraw(listofdraws, usemostfrequent, drawsize):
		maxValue = findHighestBallValue(listofdraws) + 1
		freqList = [0] * maxValue
		for draw in listofdraws:
			for ball in draw:
				freqList[ball] += 1

		freqDict = dict(zip(range(1, maxValue), freqList[1:]))
		freqList.sort(reverse=usemostfrequent)
		optimal = []

		if usemostfrequent:
			rangestart = 0
			rangeend = drawsize
		else:
			rangestart = 1
			rangeend = drawsize + rangestart

		for i in freqList[rangestart:rangeend]:
			sublist = [ball for (ball, frequency) in freqDict.items() if frequency == i]
			x = drawsize - len(optimal)
			y = len(sublist)
			if y > x:
				sublist = sublist[:x]
			optimal += sublist
			for item in sublist:
				freqDict.pop(item)
		return optimal

	print("Most frequent in " + file + ": " + str(optimaldraw(processedData, True, drawSize)))
	print("Least frequent in " + file + ": " + str(optimaldraw(processedData, False, drawSize)))