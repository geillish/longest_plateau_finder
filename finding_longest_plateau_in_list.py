def find_the_plateau(listOfIntegers):
	plateauIntergers = []
	plateauCheck = []
	plateauHold = []
	for position in range(len(listOfIntegers)-1):
		if listOfIntegers[position] == listOfIntegers[position+1] and listOfIntegers[position] >= listOfIntegers[position-1] or listOfIntegers[position] == listOfIntegers[position-1] and listOfIntegers[position] != listOfIntegers[position+1]:
			plateauCheck.append(listOfIntegers[position])
		if len(plateauHold) == 0 and len(plateauCheck) != 0:
			if plateauCheck[-1] != plateauCheck [0]:
				plateauHold.append(plateauCheck[-1])
				del plateauCheck[-1]
		if len(plateauHold) != 0:
			if plateauHold[0] == plateauCheck[0]:
				plateauCheck.append(plateauHold[0])
				del plateauHold[0]
		if len(plateauCheck) != 0 and plateauCheck[0] != listOfIntegers[position]:
			while len(plateauCheck) != 0:
				if plateauCheck[0] > listOfIntegers[position]:
					plateauIntergers.append(plateauCheck[0])
					del plateauCheck[0]
				else:
					del plateauCheck[:]
	if len(plateauCheck) != 0:
		while len(plateauCheck) != 0:
			plateauIntergers.append(plateauCheck[0])
			del plateauCheck[0]
	return plateauIntergers

def find_the_longest_plateau(listOfIntegers):
	plateauPositions = find_the_plateau(listOfIntegers)
	longestPlateau = []
	longestPlateauTest = []
	longestPlateauTestCount = 0
	longestPlateauTest2 = []
	longestPlateauTest2Count = 0
	for position in range(len(plateauPositions)):
		if longestPlateauTestCount == 0 or longestPlateauTest[0] == plateauPositions[position]:
				longestPlateauTest.append(plateauPositions[position])
				longestPlateauTestCount += 1
		elif longestPlateauTest2Count == 0 or longestPlateauTest2[0] == plateauPositions[position]:
				longestPlateauTest2.append(plateauPositions[position])
				longestPlateauTest2Count += 1
	if longestPlateauTestCount > longestPlateauTest2Count:
		while longestPlateauTestCount != 0:
			longestPlateau.append(longestPlateauTest[0])
			del longestPlateauTest[0]
			longestPlateauTestCount -= 1
	elif longestPlateauTestCount < longestPlateauTest2Count:
		while longestPlateauTest2Count != 0:
			longestPlateau.append(longestPlateauTest2[0])
			del longestPlateauTest2[0]
			longestPlateauTest2Count -= 1
	return longestPlateau

def find_position_of_the_longest_plateau(listOfIntegers):
	list = listOfIntegers
	longestPlateau = find_the_longest_plateau(list)
	position = 0
	counter = len(longestPlateau)-1
	for integer in range(len(list)-2):
		if list[integer] == longestPlateau[0] and longestPlateau[0] == list[integer + counter]:
			position = integer
	return position

	
L1 = [1, 4, 3, 6, 8, 8, 8, 7, 10, 2, 4, 4, 4, 4, 6, 7, 7, 2]

L2 = [3, 6, 10, 10, 2, 4, 5, 6, 7, 3, 3, 3, 3, 3, 5, 5, 5, 1]

print(f"The position for the longest plateau in the first list is: {find_position_of_the_longest_plateau(L1)}")

print(f"The position for the longest plateau in the second list is: {find_position_of_the_longest_plateau(L2)}")
