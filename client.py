#client.py

import socket                   # Import socket module
import rsa_encryption as rsa
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-l","--length", type=int, help="atleast 2^bits required to represent a symbol", default='128')
args = parser.parse_args()

primes = rsa.primes

if args.length < 128:
   print "Error: Atleast a value of 128 required to represent all ASCII characters uniquely."
   sys.exit()
elif args.length > primes[-1]*primes[-2]:
   print "Error: Using primes higher than 293 (length > 82919) is outside the scope of this project."
   sys.exit()

n,e,d = rsa.keygen(args.length)

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

filename = "received_file.txt"

with open(filename, 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)
f.close()

rsa.decode(filename, n, d)

print('Successfully get the file')
s.close()
print('connection closed')