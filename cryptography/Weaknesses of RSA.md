[Source](http://www.di-mgt.com.au/rsa_alg.html)
# Weaknesses in RSA

All possible weaknesses of RSA.

## Small encryption exponent
If you use a small exponent like `e=3` **_and_** send the same message to different recipients **_and_** just use the RSA algorithm without adding random padding to the message, then an eavesdropper could recover the plaintext. 
* Theorie: [Cracking RSA](http://www.di-mgt.com.au/crt.html#crackingrsa)

## Small encryption exponent and small message
If you use `e=3` and just encrypt a small message m without padding where `m3 < n` then your ciphertext c can easily be broken by simply computing its real cube root. For example, if we have the public key `(n, e) = (25777, 3)` and just encrypt the small message `m = 10` then the ciphertext is `c = 1000`. The secure properties of RSA encryption only work if `me > n`. 

## Using the same key for encryption and signing
Given that the underlying mathematics is the same for encryption and signing, only in reverse, if an attacker can convince a key holder to sign an unformatted encrypted message using the same key then she gets the original. 

## Using a common modulus for different users
Do not use the same modulus n with different (ei, di) pairs for different users in a group. Given his own pair (e1, d1), user 1 can factorize the common n into p and q and hence compute the private exponents di of all the other users. 
* [How to factorize N given d](http://www.di-mgt.com.au/rsa_factorize_n.html): Explains in pseudo-code how to quikly factorize N when d and e are known.

## Acting as an oracle
There are techniques to recover the plaintext if a user just blindly returns the RSA transformation of the input. So don't do that. 

## Also
* [RSA with small prime](RSA with small prime.md): This can be looked up or even calculated.
* [Weak RSA-keys](http://pentestmonkey.net/blog/metasploit-ssh-key-database): Weak SSH Keys for Debian OpenSSL Vulnerability
# Solutions

1. Don't use the same RSA key for encryption and signing.
2. Don't encrypt or sign a blind message.
3. If using PKCS#v1.5 encoding, use `e=0x10001` for your public exponent.
4. Always format your input before encrypting or signing.
5. Always add _fresh_ random padding - at least 8 bytes - to your message before encrypting.
6. When decrypting, check the format of the decrypted block. If it is not as expected, return an error message, not the decrypted string.
7. Similarly, when verifying a signature, if there is any error whatsoever, just respond with "Invalid Signature".
