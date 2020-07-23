#!/usr/bin/python

import sys
import random
import gibberish # https://pypi.org/project/gibberish/

if len(sys.argv) <2 :
	print "Provide an argument consisting of the number of lines of output you want"
	print "Example: " + sys.argv[0] + " 100"
	sys.exit (1)

lines = int(sys.argv[1])

streets = ['RD', 'ROAD', 'DR', 'DRIVE', 'AVE', 'AVENUE', 'CIR', 'CIRCLE', 'WAY', 'ST', 'STREET', 'ALY', 'ALLEY', 'BROOK', 'BRK', 'PARKWAY', 'PKWY']

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


for x in range(lines):
	secure_random = random.SystemRandom()
	string = "\"" + gibberish.generate_word() + " " + gibberish.generate_word() + "\",\"" + '{:03d}'.format(random.randint(1,999)) + "-" + '{:02d}'.format(random.randint(1,99)) + "-" + '{:04d}'.format(random.randint(1,9999)) + "\",\"" '{:03d}'.format(random.randint(1,999)) + " " + gibberish.generate_word() + " " + secure_random.choice(streets) + " " + gibberish.generate_word() + ", " + secure_random.choice(states) + " " + '{:05d}'.format(random.randint(1,99999)) + "\""
	string = string.upper();
	print(string)
