# ECE151-RSA-encryption
ECE 151 MP2. RSA Encoder-Decoder and Brute-Force code breaker. 
- Implementation limits the encoding to only the use of prime numbers under 300, or up to approx. 16 bit encryption (at most 82,919 symbols). 
- The project is instead developed with low-end computers in mind, and is thus subpar to the standard 1024 bit encryption practical RSA uses. This project however uses less memory and time in key generation and encoding-decoding, in tradeoff to the strength of security. 

## Requirements:
- Python 2.7.16

## Usage:
```
python server.py <sample_file.txt>
python client.py
```
## To indicate # of symbols/combinations to encode:
```
python server.py --length 128 <sample_file.txt>
python client.py --length 128 
```
by default text is encrypted using length=128 (because of 128 ascii characters)

## Brute-Force Code Breaker:
```
python brute.py
```
given the first 3 characters of the file, brute.py is designed to crack the RSA cipher if the prime numbers used are under 100. 

## Input and Output Files
- alice.txt : test file from Project Gutenberg containing L. Caroll's Alice in Wonderland in text.
- encrypted_file.txt : file after RSA encryption.
- received_file.txt : file after being transferred through TCP. Should ideally be identical to encrypted_file.txt.
- decrypted_file.txt : file after being transferred AND decrypted. The final output file.
- snitch.txt : brute-force output
