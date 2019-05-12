# ECE151-RSA-encyrption
ECE 151 MP2. RSA Encoder-Decoder and Brute-Force code breaker

Usage:
'''
python server.py <sample_file.txt>
python client.py
'''

To indicate # of symbols/combinations to encode:
'''
python server.py --length 128 <sample_file.txt>
python client.py --length 128 
'''
by default text is encrypted using length=128 (because of 128 ascii characters)