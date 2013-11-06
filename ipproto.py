#!/usr/bin/python

import urllib2
import csv
import re

url = 'http://www.iana.org/assignments/protocol-numbers/protocol-numbers-1.csv'
listname = '_ipproto_to_str'

try:
	f = urllib2.urlopen(url)
except urllib2.HTTPError as e:
	print "Error retrieving %s (%s %s)" % (url, e.code, e.reason)
	exit()
except urllib2.URLError as e:
	print "Error retrieving %s (%s)" % (url, e.reason)
	exit()

for p in csv.reader(f):
	# 143-252 (Unassigned)
	if re.match("^\d+\-\d+$", p[0]):
		begin, end = re.split("-", p[0])
		for i in range(int(begin),int(end),1):
			print "%s[%s] = '%s (%s)'" % (listname, i, "Unassigned", i)
	# regular int
	elif re.match("^\d+$", p[0]):
		# no keyword -> Unknown (NNN)
		if p[1] == "":
			print "%s[%s] = '%s (%s)'" % (listname, p[0], "Unknown", p[0])
		# plain NNN -> keyword xlate
		else:
			print "%s[%s] = '%s'" % (listname, p[0], p[1])
	else:
		pass
