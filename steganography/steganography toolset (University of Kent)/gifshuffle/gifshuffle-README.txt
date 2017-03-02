Gifshuffle

GIF colourmap steganography 

The program gifshuffle is used to conceal messages in GIF
images by shuffling the colourmap, which leaves the image
visibly unchanged. gifshuffle works with all GIF images,
including those with transparency and animation, and in
addition provides compression and encryption of the
concealed message. 

How does it work? 

Any list of n items can be sorted n! ways, meaning that
any particular ordering can represent a number in the
range [0, n!-1]. This number can in turn store approximately
log2(n!) bits of information. Thus, a GIF image with 256
colours can store up to 1675 bits (209 bytes) of information
by shuffling the colours in its colourmap.

The Gifshuffle homepage is located at:

	http://www.darkside.com.au/gifshuffle/

Cryptographic signatures and checksums may be provided by 
the developers at the URL(s) above.  Wiretapped recommends
that users check these before use of the software/information.
