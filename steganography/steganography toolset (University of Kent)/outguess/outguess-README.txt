What is OutGuess

OutGuess is a universal steganographic tool that allows the insertion of 
hidden information into the redundant bits of data sources. The nature of 
the data source is irrelevant to the core of OutGuess. The program relies 
on data specific handlers that will extract redundant bits and write them 
back after modification. In this version the PNM and JPEG image formats 
are supported. In the next paragraphs, images will be used as concrete 
example of data objects, though OutGuess can use any kind of data, as long 
as a handler is provided. 


How to get OutGuess

You can download OutGuess as UNIX source tar ball. OutGuess is available 
under a BSD software license. It is completely free for any use including 
commercial. 

Please see each source file for its respective license. OutGuess was 
developed in Germany. 	


What is Steganography

Steganography is the art and science of hiding that communication is 
happening. Classical steganography systems depend on keeping the encoding 
system secret, but modern steganography is detectable only if secret 
information is known, e.g. a secret key. Because of their invasive nature, 
steganography systems leave detectable traces within a medium's 
characteristics. This allows an eavesdropper to detect media that has been 
modified, revealing that secret communication is taking place. Although 
the secrecy of the information is not degraded, its hidden nature is 
revealed, defeating the main purpose of Steganography. 


What does OutGuess do differently

For JPEG images, OutGuess preserves statistics based on frequency counts. 
As a result, no known statistical test is able to detect the presence of 
steganographic content. Before embedding data into an image, OutGuess can 
determine the maximum message size that can be hidden while still being 
able to maintain statistics based on frequency counts. 

OutGuess uses a generic iterator object to select which bits in the data 
should be modified. A seed can be used to modify the behavior of the 
iterator. It is embedded in the data along with the rest of the message. 
By altering the seed, OutGuess tries to find a sequence of bits that 
minimizes the number of changes in the data that have to be made. 

The outguess homepage is located at:

	http://www.outguess.org/

Cryptographic signatures and checksums may be provided by 
the developers at the URL(s) above.  Wiretapped recommends
that users check these before use of the software/information.
