
Source: http://ftp.mirrorservice.org/sites/ftp.wiretapped.net/pub/security/steganography/

# Steganography Tool Repository from University of Kent

Steganography is the process of hiding a secret message within a larger
one in such a way that others can not discern the presence or contents
of the hidden message. The Steganography directory contains software
that hides, detects and retrieves information from files using
steganographic processes.

## Blindside
Blindside is a command-line utility for Unix that hides information
inside .BMP (bitmap) files. Source and precompiled binaries are
available.


## Gifshuffle
gifshuffle is used to conceal messages in GIF images by shuffling
the colourmap, which leaves the image visibly unchanged. gifshuffle
works with all GIF images, including those with transparency and
animation, and in addition provides compression and encryption of
the concealed message.


## gzip-steg
gzip-steg is a patch for gzip (GNU zip) that hides information
inside a compressed file. It is available as a patch against a
standard gzip source tree and a pre-patched source tree. gzip-steg
was originally written by Andrew Brown in 1994.


## Hide4PGP
Hide4PGP was designed to supplement PGP by allowing users to hide
encrypted information inside uncompressed .BMP (bitmap) and .WAV
files. It is available as Unix and Win32 source. Win32 binaries are
also available.


## JPHIDE and JPSEEK
JPHIDE and JPSEEK are programs which allow you to hide a file in a
JPEG image. The design objective was not simply to hide a file but
rather to do this in such a way that it is impossible to prove that
the host file contains a hidden file. Given a typical visual image,
a low insertion rate (under 5%) and the absence of the original
file, it is not possible to conclude with any worthwhile certainty
that the host file contains inserted data. As the insertion
percentage increases the statistical nature of the jpeg
coefficients differs from "normal" to the extent that it raises
suspicion. Above 15% the effects begin to become visible to the
naked eye.
    

## mandsteg (& gifextract)
MandelSteg will create a Mandelbrot image, storing your data in the
specified bit of the image pixels, after which GIFExtract can be
used by the recipient to extract that bit-plane of the image.


## mp3stego
MP3Stego will hide information in MP3 files during the compression
process. The data is first compressed, encrypted and then hidden in
the MP3 bit stream. Unix source and Windows binaries are available.


## ncovert
NCovert allows you to hide your network file transfers across the
Internet. By utilizing packet forgery, NCovert hides your file
transfer by cloaking it in seemingly harmless data. Advanced
features allow you to hide your true IP address, and with careful
planning you can hide the target's true IP address as well.


## nicetext
nicetext is a package that converts any file into
pseudo-natural-language text and can recover the original file from
the "nice text". The expandable set of tools can create custom
dictionaries from a variety of sources, simulate many different
writing styles by example and alternatively use
Context-Free-Grammars to control writing style.


## outguess
OutGuess is a universal steganographic tool that allows the
insertion of hidden information into the redundant bits of data
sources. The nature of the data source is irrelevant to the core of
OutGuess. The program relies on data specific handlers that will
extract redundant bits and write them back after modification. In
this version the PNM and JPEG image formats are supported.


## snow
snow is used to conceal messages in ASCII text by appending
whitespace to the end of lines. Because spaces and tabs are
generally not visible in text viewers, the message is effectively
hidden from casual observers. And if the built-in encryption is
used, the message cannot be read even if it is detected.


## stealth
Stealth is a tool which takes a PGP encrypted message, and strips
any standard headers off to ensure that the result looks like
random noise, and if the PGP random number generators are secure,
and if IDEA, and RSA (RSA when normalised) produce good quality
random numbers, the result should look like white noise, and stand
up to ananlysis as being indistinguishable as white noise.


## stegdetect
Stegdetect is an automated tool for detecting steganographic
content in images. It is capable of detecting several different
steganographic methods to embed hidden information in JPEG images.
Currently, the detectable schemes are: jsteg, jphide (unix and
windows), invisible secrets, and outguess 01.3b. OutGuess 0.2 can
not be detected using these techniques.


## steghide
Steghide is a steganography program which embeds a secret message
in a cover file by replacing some of the least significant bits of
the cover file with bits of the secret message. After that, the
secret message is imperceptible and can only be extracted with the
correct passphrase.


## stegtunnel
Stegtunnel provides a covert channel in the IPID and sequence number
fields of any desired TCP connection. It requires the server and client
to have a previously shared secret in common to detect and decrypt the
data.



(Note: This list of software and information available at Wiretapped is not
exhaustive. Users are encouraged to browse and search the archive and read
any available "-README.txt" files that are available)

