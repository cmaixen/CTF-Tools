#Useful Tools

*Tools used for solving Steganography challenges*

- [Convert](http://www.imagemagick.org/script/convert.php) - Convert images b/w formats and apply filters
- [Exif](http://manpages.ubuntu.com/manpages/trusty/man1/exif.1.html) - Shows EXIF information in JPEG files
- [Exiftool](https://linux.die.net/man/1/exiftool) - Read and write meta information in files
- [Exiv2](http://www.exiv2.org/manpage.html) - Image metadata manipulation tool
- [ImageMagick](http://www.imagemagick.org/script/index.php) - Tool for manipulating images
- [Outguess](https://www.freebsd.org/cgi/man.cgi?query=outguess+&apropos=0&sektion=0&manpath=FreeBSD+Ports+5.1-RELEASE&format=html) - Universal steganographic tool
- [Pngtools](http://www.stillhq.com/pngtools/) - For various analysis related to PNGs
  - `apt-get install pngtools`
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) - Used to deblur and fix defocused images
- [Steganabara](https://www.openhub.net/p/steganabara) -  Tool for stegano analysis written in Java
- [Stegbreak](https://linux.die.net/man/1/stegbreak) - Launches brute-force dictionary attacks on JPG image
- [Steghide](http://steghide.sourceforge.net/) - Hide data in various kind of images
- [Stegsolve](http://www.caesum.com/handbook/Stegsolve.jar) - Apply various steganography techniques to images
- [Zsteg](https://github.com/zed-0xff/zsteg): detect stegano-hidden data in PNG & BMP

# Tips

* **If you have a PNG, check if it is an 8-bit colormap.** An 8-bit colormap is a typical place where things are hidden in a steganography challenge.

    ```bash
    $ file doge_stege.png
    doge_stege.png: PNG image data, 680 x 510, 8-bit colormap, non-interlaced
    ```
