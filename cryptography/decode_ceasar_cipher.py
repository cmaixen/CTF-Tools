# -*- coding: utf-8 -*-
"""
Created on Sat Mar 4 11:16:45 2017

@author: cmaixen
"""


import sys
from guess_language import guess_language

def decode_ceasar_cipher(argv):

    cipher=argv[0].lower()
    keyspace = []
    print('\nAll Options:')
    print('------------\n')
    for x in range(26):
        result = []
        for i in cipher:
           if i == " " or i == "." or i.isdigit():
             result.append(i) 
           else:
             result.append(str(chr(97 + (((ord(i) - 97) - x) % 26 ))))

        print("".join(result))
        keyspace.append("".join(result))
    

    for j in keyspace:
        lang = guess_language(j)
        if lang == 'en': 

            print("\nFound Valid Decription: " + j + '\n')


 

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        print("Usage: python decode_ceasar_cipher.py ciphertext")
    decode_ceasar_cipher(sys.argv[1:])
