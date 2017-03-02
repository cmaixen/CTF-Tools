Stegdetect is an automated tool for detecting steganographic content in 
images. It is capable of detecting several different steganographic 
methods to embed hidden information in JPEG images. Currently, the 
detectable schemes are 

*	jsteg,
*	jphide (unix and windows),
*	invisible secrets,
*	and outguess 01.3b.

OutGuess 0.2 can not be detected using these techniques. 

Stegbreak is used to launch dictionary attacks against JSteg-Shell, JPHide 
and OutGuess 0.13b. 

Stegdetect and Stegbreak have been developed by Niels Provos. 

Example

$ stegdetect *.jpg
cold_dvd.jpg : outguess(old)(***) jphide(*)
dscf0001.jpg : negative
dscf0002.jpg : jsteg(***)
dscf0003.jpg : jphide(***)
[...]
$ stegbreak -tj dscf0002.jpg
Loaded 1 files...
dscf0002.jpg : jsteg(wonderland)
Processed 1 files, found 1 embeddings.
Time: 36 seconds: Cracks: 324123,   8915 c/s

The stegdetect homepage is located at:

	http://www.outguess.org/detection.php

Cryptographic signatures and checksums may be provided by 
the developers at the URL(s) above.  Wiretapped recommends
that users check these before use of the software/information.
