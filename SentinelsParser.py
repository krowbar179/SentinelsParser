from FileCompare import FileParser

#File parser specifically for parsing Sentinels of the Mulitverse pastebin files.
#Currently has no additional functionality

class SentinelsParser(FileParser):
	"""docstring for SentinelsParser"""
	def __init__(self, filenames):
		super(SentinelsParser, self).__init__(filenames)

