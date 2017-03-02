MP3Stego will hide information in MP3 files during the
compression process. The data is first compressed, encrypted
and then hidden in the MP3 bit stream. Although MP3Stego has
been written with steganographic applications in mind it might
be used as a copyright marking system for MP3 files (weak but
still much better than the MPEG copyright flag defined by the
standard). Any opponent can uncompress the bit stream and
recompress it; this will delete the hidden information â€actually
this is the only attack we know yet â€but at the expense of severe
quality loss.

The hiding process takes place at the heart of the Layer III
encoding process namely in the inner_loop.  The inner loop
quantizes the input data and increases the quantizer step size
until the quantized data can be coded with the available number
of bits. Another loop checks that the distortions introduced by
the quantization do not exceed the threshold defined by the
psycho acoustic model. The part2_3_length variable contains the
number of main_data bits used for scalefactors and Huffman code
data in the MP3 bit stream. We encode the bits as its parity by
changing the end loop condition of the inner loop. Only randomly
chosen part2_3_length values are modified; the selection is done
using a pseudo random bit generator based on SHA-1.A

The mp3stego homepage is located at:

	http://www.cl.cam.ac.uk/~fapp2/steganography/mp3stego/

Cryptographic signatures and checksums may be provided by 
the developers at the URL(s) above.  Wiretapped recommends
that users check these before use of the software/information.
