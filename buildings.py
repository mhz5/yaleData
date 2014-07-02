import sys
import string

f = open('building_codes', 'r')

line = f.readline()
print 'Code,Building,Address'
line = f.readline()
while line != '':
	# Split by tab, join by comma, eliminate whitespace after comma,
	# remove trailing newline, add city to address
	csvLine = ','.join(line.split('\t')).replace(', ', ',').rstrip('\n')
	print csvLine + ' New Haven CT';
	line = f.readline()
