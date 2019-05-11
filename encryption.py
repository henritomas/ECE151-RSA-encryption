"""
Single Character encryption (128 ascii)
"""
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l","--length", help="atleast 2^bits required to represent a symbol", default='128')
args = parser.parse_args()

length = int(args.length)
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def keygen(length):
    
    return n, e