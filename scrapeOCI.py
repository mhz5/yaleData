from bs4 import BeautifulSoup
import httplib
import urllib2
import re 		# Regular expression
from pprint import pprint

baseUrl = 'http://students.yale.edu/oci/resultDetail.jsp?'
term = '&term=201401'

classHtml = urllib2.urlopen('http://students.yale.edu/oci/resultDetail.jsp?course=23297&term=201401').read()

for i in range(23330, 23333):
	fullUrl = baseUrl + 'course=' + str(i) + term

	print '>' * 30 + '\n'
	print 'SCRAPING: ' + fullUrl
	
	# Try to scrape the class. Move on to next one if unable to establish HTTP connection.
	response = None
	try:
		response = urllib2.urlopen(fullUrl)
	except urllib2.HTTPError:
		print 'Class ' + str(i) + ' does not exist!'
		continue
		
	html = response.read()
	soup = BeautifulSoup(html)

	main = soup.body('table')[1].tr('td')
	# info provides course code, name, professor, meeting times, and building
	info = main[0].table('tr')
	
	code = info[0].td.string
	if code == None:
		code = info[0].td.a.string
	
	name = info[1].td.b.string
	if name == None:
		name = info[1].td.b.p.string

	prof = info[2].td.a.string
	meet = info[3].td.string

	semester = main[5].table.tr('td')[0].string
	if len(main) >= 9:
		reqs = main[8].string
	else:
		reqs = "No listed requirements"


	descTable = soup.body('table')[1].find_next_sibling()
	desc = descTable.tr.td.get_text()
	if desc == None:
		desc = descTable.tr.td.p.get_text()
	# desc = soup.body('table')[2].tr.td.string
	# if desc == None:
	# 	desc = soup.body('table')[2].tr.td.p.string
	print 'Code: ' + code
	print 'Name: ' + name 
	print 'Prof: ' + prof
	print 'Meet: ' + meet
	print 'Semester: ' + semester
	print 'Requirements: ' +  reqs
	print 'Description: ' + desc
	print '=' * 30 + '\n'

	# print(soup.prettify())

