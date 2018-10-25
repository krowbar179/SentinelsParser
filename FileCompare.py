import sys
import math

class FileParser(object):
	"""docstring for FileParser"""
	def __init__(self, filenames):
		super(FileParser, self).__init__()
		self.filenames = filenames
		self.dictList = []
		for fName in filenames:
			readFile = open(fName, 'r')
			lines = readFile.read().splitlines()
			readFile.close()

			lineDict = {}
			for line in lines:
				if not (line in lineDict.keys()):
					lineDict[line] = 1
				else:
					lineDict[line] += 1
			self.dictList.append(lineDict)
		
	def addFile(self, fName):
		readFile = open(fName, 'r')
		lines = readFile.read().splitlines()
		readFile.close()
		lineDict = {}
		for line in lines:
			if not (line in lineDict.keys()):
				lineDict[line] = 1
			else:
				lineDict[line] += 1
		dictList.append(lineDict)

	def intersectDict(self):
		interDict = {}
		for parseDict in self.dictList:
			if not interDict:
				interDict = parseDict
			else:
				nextIter = {}
				for entry in interDict.keys():
					if entry not in parseDict.keys():
						del interDict[entry]
					else:
						interDict[entry] = min(interDict[entry], parseDict[entry])
		return interDict

	def unionList(self):
		union = []

		