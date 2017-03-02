Stegtunnel provides a covert channel in the IPID and sequence number
fields of any desired TCP connection. It requires the server and
client to have a previously shared secret in common to detect and
decrypt the data. 

Stegtunnel was the subject of a presentation at Rubi-Con (http://www.rubi-con.org/).
This release is the cleaned-up version of the demo at the conference. In addition,
a couple of features have been added. The presentation itself has been turned into a
full article. Read it, let me know if there are any clarifications needed, or if you
have ideas for improving stegtunnel. 

Stegtunnel requires libpcap , and libdnet version 1.2 or higher. 

The Stegtunnel homepage is located at:

	http://www.synacklabs.net/projects/stegtunnel/

Cryptographic signatures and checksums may be provided by 
the developers at the URL(s) above.  Wiretapped recommends
that users check these before use of the software/information.
