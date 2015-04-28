# ************************
# ** Parse lottery data **
# ************************
#pass in a dict of files and the number of balls in the draw
files = {'lotto-draw-history.csv':[[0,6], [6,2]],
         'euromillions-draw-history.csv':[[0,5], [5,2]]}
for file in files.keys():
	inputData = open(file, 'r')
	drawSizes = files[file]
	for subdraw in drawSizes:
		processedData = []
		for line in inputData:
			allElements = line.split(',') #csv
			if 'DrawDate' not in allElements:
				numbers = allElements[subdraw[0] + 1:subdraw[1] + 1] #extract numbers in range from each line
				numbers = map(int, numbers) #convert strings to numbers
				processedData.append(numbers)
		#processedData.pop(0)


		def findHighestBallValue(listofdraws):
			foundMax = 0
			for adraw in listofdraws:
				if max(adraw) > foundMax:
					foundMax = max(adraw)
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


			rangestart = 0
			rangeend = subdraw[1]

			for i in freqList[rangestart:rangeend]:
				sublist = [ball for (ball, frequency) in freqDict.items() if frequency == i]
				x = subdraw[1] - len(optimal)
				y = len(sublist)
				if y > x:
					sublist = sublist[:x]
				optimal += sublist
				for item in sublist:
					freqDict.pop(item)
			return optimal

		print("Most frequent in " + file + ": " + str(optimaldraw(processedData, True,  drawSizes)))
		print("Least frequent in " + file + ": " + str(optimaldraw(processedData, False, drawSizes)))
        inputData.close()