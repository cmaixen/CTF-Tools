#POOR RSA

[Source](https://github.com/ctfs/write-ups-2017/tree/master/alexctf-2017/cryptography/cr4-poor-rsa-200)

We have an RSA public key, and what is likely to be the flag encrypted with the corresponding private key.

```bash
	$ openssl rsa -pubin -in key.pub -text -noout
	Public-Key: (399 bit)
	Modulus:
	    52:a9:9e:24:9e:e7:cf:3c:0c:bf:96:3a:00:96:61:
	    77:2b:c9:cd:f6:e1:e3:fb:fc:6e:44:a0:7a:5e:0f:
	    89:44:57:a9:f8:1c:3a:e1:32:ac:56:83:d3:5b:28:
	    ba:5c:32:42:43
	Exponent: 65537 (0x10001)
```
With a key length smaller than 512 bits, it should not be too difficult to factor. Indeed, a lookup of n (or the Modulus) on the [factordb.com](http://factordb.com/index.php?query=833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019) website reveals the two factors. (Convert the hex representation to an integer)
All what is left is converting all parameters in a format openssl understands, and decrypt the flag:

```python
	import gmpy2
	
	p = 863653476616376575308866344984576466644942572246900013156919
	q = 965445304326998194798282228842484732438457170595999523426901
	e = 65537
	d = gmpy2.invert(e, (p - 1) * (q - 1))
	
	print '''asn1=SEQUENCE:rsa_key
	
	[rsa_key]
	version=INTEGER:0
	modulus=INTEGER:{n}
	pubExp=INTEGER:{e}
	privExp=INTEGER:{e1}
	p=INTEGER:{p}
	q=INTEGER:{q}
	e1=INTEGER:{e1}
	e2=INTEGER:{e2}
	coeff=INTEGER:{coeff}'''.format(
	    n=p * q,
	    e=e,
	    p=p,
	    q=q,
	    e1=d % (p - 1),
	    e2=d % (q - 1),
	    coeff=gmpy2.invert(q, p),
	)
```

A few openssl commands later, we have the flag!

```bash
$ ./build.py > priv.conf
$ openssl asn1parse -genconf priv.conf -out priv.der -noout
$ base64 -d flag.b64 | openssl rsautl -decrypt -inkey priv.der -keyform der
ALEXCTF{SMALL_PRIMES_ARE_BAD}
```