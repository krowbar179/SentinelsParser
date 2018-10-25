import sys
from SentinelsParser import SentinelsParser
from os import listdir, chdir
from os.path import isfile, join

#modify this line to modify which directory files are pulled from

chdir('pastebin')

allFiles = [file for file in listdir('.') if file.endswith('.txt')]

parser = SentinelsParser(allFiles)
output = ""
for line in sorted(parser.intersectDict().items()):
	output += str(line) + '\n'

chdir("..")
writeFile = open('output.txt', 'w')
writeFile.write(output)
writeFile.close()
print output