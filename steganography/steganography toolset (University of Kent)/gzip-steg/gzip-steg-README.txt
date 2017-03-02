gzip-steg is a patch for gzip 1.2.4 that hides
information inside a compressed file.

* gzip-steg-1.2.4.patch is a patch against gzip 1.2.4
  (instructions are included in the file itself)

* gzip-steg-1.2.4.tar.gz is a version of the software
  that has already been patched.

The original author of the patches was Andrew Brown.
A small patch to fix a bug was supplied by Ken Pizzini.

Documentation:

(By Andrew Brown)

USER INTERFACE

   A new option is added to gzip, "-s" or "--steg", that provides for the
   hiding/revealing of files. You hide files during compression and
   reveal them during decompression. e.g.

   gzip -s file-to-hide file-to-compress

   This will hide "file-to-hide" inside file-to-compress as it is
   compressed. Extracting a file could be done like this:

   gunzip -s file-to-extract-to compressed-file

   This will simultaneously decompress the compressed file and extract
   the hidden file to file-to-extract-to. To extract the hidden file
   without uncompressing you might do the following:

   gzip -cds file-to-extract-to compressed-file > /dev/null


   HOW IT'S DONE

   gzip uses LZ77 which compresses data by storing length/offset pairs
   that refer back in the uncompressed data stream to previous
   occurrences of the information being compressed. gzip considers a
   length of 3 to be the shortest acceptable length. We allow gzip to
   find the length/offset pairs and then do the following.

   If the length is at least 5 then we subtract 1 and set bit 0 to the
   value of the bit that we need to hide. We have now hidden information
   in the length without pushing it beyond a valid value.  Drawbacks are
   a slight decrease in compression (very slight) since we have to
   disallow lengths of 4 and some of our meddling will decrease the
   actual matched length by 1. The hidden file is totally invisible to
   the normal operation of gzip, gunzip et al and (if encrypted) will
   only be visible to those in the know. When the "-s" flag is not used
   gzip performs as normal.

   Testing was performed on a 486/33 running Linux, using a 1Mb tar file
   to hide the test information inside. The patched files (inflate.c,
   deflate.c, gzip.c) should compile OK on any system that can compile
   gzip, although non-Unix users may have trouble applying the patches in
   the first place. My tests have shown that you can hide about 1 Kbyte
   in every 100 Kbytes of uncompressed data.
