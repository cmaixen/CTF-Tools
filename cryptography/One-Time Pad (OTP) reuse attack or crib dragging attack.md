
[Source](http://badbytes.io/2017/02/07/alexctf-2017/ "Permalink to AlexCTF 2017 – B A D B Y T E S")

# AlexCTF 2017 – B A D B Y T E S

**CR2: Many time secrets (100)**  
_This time Fady learned from his old mistake and decided to use onetime pad as his encryption technique, but he never knew why people call it one time pad!_  
We are given this file containing multiple lines of ciphertext.

![][15]  
Based on the description of the challenge, the ciphertext is vulnerable to OTP reuse attacks. Each line of the ciphertext has been encrypted with the same one-time-pad and therefore is vulnerable to the [crib dragging attack][16]. We can launch this attack using a tool called [FeatherDuster][17]:

![][18]  
At this point, we have the ciphertext and the plain text. Since this is OTP encrypted, we can XOR cipher and plain to get the key. Im sure there is a much easier way to do this, I just went in this direction at the time. Translate cipher and plain to binary and then perform an XOR:

![][19]

[15]: http://badbytes.io/wp-content/uploads/2017/02/cr2_1.png
[16]: http://samwho.co.uk/blog/2015/07/18/toying-with-cryptography-crib-dragging
[17]: https://github.com/nccgroup/featherduster
[18]: http://badbytes.io/wp-content/uploads/2017/02/cr2_2-700x450.png
[19]: http://badbytes.io/wp-content/uploads/2017/02/cr2_3-700x239.png
