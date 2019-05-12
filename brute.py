from langdetect import detect
import sys
import argparse
import math

import array 
primes = array.array('i', [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293])  
flag = 0

efile = open("received_file.txt", 'rb')
line = efile.read()
	
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
	
for x in range(0, 61):
	p = primes[x]
	q = primes[x+1]
	n = p*q
	phi = (p-1)*(q-1)
		
	e = 3
	while True:
		if gcd(e, phi)!=1:
			e+=1
			continue

		for j in range(2, phi):
			d = j
			if (e*d - 1)%phi == 0:
				break
        
		if e > phi - 1:
			print("Error: no value of ed compatible for chosen n.")
		elif (e*d - 1)%phi == 0:
			break
		
	line_decoded = line.split('-')
	line_decoded = [int(c) for c in line_decoded]
	#Decode
	line_decoded = [c**d % n for c in line_decoded]
	line_decoded = [chr(c) for c in line_decoded]
	line_out = ''.join(line_decoded)
	
	if line_out[0] == 'P' and line_out[1] == 'r' and line_out[2] == 'o':
		#flag = 1
		break


outfile = "snitch.txt"
with open(outfile, 'wb') as g:
	g.write(line_out)    
g.close()
	