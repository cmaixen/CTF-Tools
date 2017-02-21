#!/usr/bin/python2
# Source: https://github.com/realbadbytes/cyclic
# cyclic pattern tool for buffer overflows
# --gen : makes it possible to generate strings of a certain length, following a cyclic pattern
# --lookup : do a lookup in this cyclic pattern
import sys
import os
alpha_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", \
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 

alpha_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    if sys.version > '3':
          python2 = os.popen('which python2 2> /dev/null').read().rstrip()
          if python2:
            args = sys.argv[:]
            args.insert(0,python2)
            os.execv(python2,args)
          else:
            sys.exit("%s requires Python Version 2 (python2 not in PATH)" % os.path.basename(__file__))
    print("\n[+] badbytes.io cyclic pattern gen/lookup tool")
    if len(sys.argv) < 3:
        usage()
    elif sys.argv[1] == "--gen":
        print("[+] pattern --> %s \n" % gen(int(sys.argv[2])))
    elif sys.argv[1] == '--lookup':
        print("[+] offset --> %d\n" % int(lookup(sys.argv[2])))
    else:
        usage()

def gen(length):
    pattern = ''
    print("[+] generating pattern of length %d" % length)
    for x in xrange(len(alpha_upper)):
        for y in xrange(len(alpha_lower)):
            for z in xrange(100):
                pattern = pattern + alpha_upper[x] + alpha_lower[y] + str(z)
                if len(pattern) >= length:
                    pattern = pattern[:length]
                    break
    return pattern

def lookup(search_string):
    print("[+] looking up %s" % search_string)
    pattern = gen(50000)
    return pattern.find(search_string)

def usage():
    print("[+] Usage:")
    print("[+] python cyclic.py [--gen OR --lookup] [numchars]\n")
    raise SystemExit

if __name__ == "__main__":
    main()
