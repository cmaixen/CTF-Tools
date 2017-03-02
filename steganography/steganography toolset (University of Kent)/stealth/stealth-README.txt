PGP Stealth

A PGP tool for steganography

Stealth is a tool which takes a PGP encrypted message, and strips any 
standard headers off to ensure that the result looks like random noise, 
and if the PGP random number generators are secure, and if IDEA, and RSA 
(RSA when normalised) produce good quality random numbers, the result 
should look like white noise, and stand up to ananlysis as being 
indistinguishable as white noise. 

You would probably not normally use stealth directly, but use it 
conconjuction with a steganographic appliciation. Or it if you are writing 
a steganographic application. Stealth could also be used to produce random 
numbers (just uuencode the output and email it), if you are happy with 
your only plausible deniability being: "it was the output from my random 
number generator for Fred to analyse". 

Stealth 1.0, 1.1, 1.2, (and an unreleased 1.3) were written by Henry 
Hastur <alt.security.pgp> (ie if you want to send email to Henry write a 
message for his attention in the USENET group alt.security.pgp). Henry 
Hastur is a nym. 

Stealth 2.0 is Henry's version 1.1 modified to incorporate an improvement 
in the randomness of the RSA header part of the PGP encrypted message. The 
improvement (discussed by Hal Finney normalising RSA key exchange blocks 
allows a reversible transformation of the RSA block which produces a 
rectangular distribution for the data, which covers the full range. Bodo 
Moeller <3moeller@informatik.uni-hamburg.de> also discussed the problem in 
sci.crypt, and helped formulate the final algorithm used. 

Stealth versions 1.x while the output looked random to casual inspection, 
suffered from a weakness with RSA encrypted PGP messages. A knowledgeable 
opponent with a few samples of stealth output would have been able to tell 
that the stealth output was originally started with an RSA header with a 
high degree of certainty. That could be disastrous, as the whole point of 
using stealth and steganography is to avoid the detection of a hidden data 
stream, and to use some other larger, noisy data stream to provide 
plausible deniability. 

The technical reason for this leak of information is that the RSA header 
(see the pgformat.txt file which comes with the PGP distribution for 
details) is by definition less than the RSA modulus. This continues to be 
the case after stealthing by stealth 1.x, and a few sample messages would 
lead to the increasingly implausible (from a deniability point of view) 
situation of random data always being less than a particular point (the 
RSA modulus of your public key).  Stealth 2.0 fixes this problem. 

Note from Adam Back (homepage host):

I am not over confident about the random number generation in stealth 
2.01b (beta) so don't bet anything serious on it yet. 

I hope to improve stealth2.01 soon, so that I have more confidence in the 
resilience to attacks relying on large amounts of known plaintext, and 
even to attacks relying on the capture of the users randseed.bin. 

The stealth homepage is located at:

	http://www.cypherspace.org/~adam/stealth/

Cryptographic signatures and checksums may be provided by 
the developers at the URL(s) above.  Wiretapped recommends
that users check these before use of the software/information.
