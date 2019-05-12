"""
Single Character encryption (128 ascii)
"""
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-l","--length", help="atleast 2^bits required to represent a symbol", default='128')
args = parser.parse_args()

length = int(args.length)
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163 ,167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

if length < 128:
    print "Error: Atleast a value of 128 required to represent all ASCII characters uniquely."
    sys.exit()
elif length > primes[-1]*primes[-2]:
    print "Error: Using primes higher than 293 (length > 82919) is outside the scope of this project."
    sys.exit()

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def keygen(length):

    for i in range(len(primes)):
        p, q = primes[i], primes[i+1]
        n = p*q
        phi = (p-1)*(q-1)
        if n > length:
            break

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

    return n, e, d

def encode(filename, n, e):
    raw_file = open(filename, 'rb')

    line = raw_file.read(4096)
    line_encoded = []
    while line:
        for m_raw in line:
            m_code = str(ord(m_raw)**e % n)
            line_encoded.append(m_code)
        line = raw_file.read(4096)
    raw_file.close()
    encrypted_data = '-'.join(line_encoded)
    
    with open('encrypted_file.txt', 'wb') as f:
        f.write(encrypted_data)
    f.close()
    
def decode(filename, n, d):
    efile = open(filename, 'rb')

    line = efile.read()
    line_decoded = line.split('-')
    line_decoded = [int(x) for x in line_decoded]
    #Decode
    line_decoded = [x**d % n for x in line_decoded]
    line_decoded = [chr(x) for x in line_decoded]
    line_out = ''.join(line_decoded)

    outfile = "decrypted_file.txt"
    with open(outfile, 'wb') as f:
        f.write(line_out)    
    f.close()
    
        


if __name__ == '__main__':
    n, e, d = keygen(length)
    print("n:%d e:%d d:%d" % (n,e,d))
    encode('alice.txt', n, e)
    decode('encrypted_file.txt', n, d)