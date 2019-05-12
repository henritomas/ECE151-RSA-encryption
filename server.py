# server.py

import socket                   # Import socket module
import rsa_encryption as rsa
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("infile", type=str, help="file to be encrypted using RSA")
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

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    rsa.encode(args.infile, n, e)

    f = open('encrypted_file.txt','rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.close()
    break