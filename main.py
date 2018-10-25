import sys
from SentinelsParser import SentinelsParser
from os import listdir, chdir
from os.path import isfile, join

#modify this line to modify which directory files are pulled from

chdir('pastebin')

allFiles = [file for file in listdir('.') if file.endswith('.txt')]

parser = SentinelsParser(allFiles)
for line in parser.intersectDict().items():
	print line
'''
for file in listdir('.'):
	print file
'''