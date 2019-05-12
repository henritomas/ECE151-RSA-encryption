# ECE151-RSA-encryption
ECE 151 MP2. RSA Encoder-Decoder and Brute-Force code breaker

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

## Input and Output Files
- alice.txt : test file from Project Gutenberg containing L. Caroll's Alice in Wonderland in text.
- encrypted_file.txt : file after RSA encryption.
- received_file.txt : file after being transferred through TCP. Should ideally be identical to encrypted_file.txt.
- decrypted_file.txt: file after being transferred AND decrypted. The final output file.

