#### Note- I'm working on fixing the bugs in the [Object Oriented Programming Version](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/OOP%20Version/checker.py) of this program. The final submission will be pushed before September 31, 2021.

#### Web version comming in 2022.

<img src="https://chromeunboxed.com/wp-content/uploads/2019/10/GooglePasswordManagerCheckup.jpg" width="400" align="right"/>

# Newfangled-Password-Checker
An advanced and state of the art password checker created using Python3. It is a modern secure program that helps in checking if your passwords have ever been hacked. 

The program uses a ```SHA1``` algorithm to check if the passwords have been leaked or if they have been hacked. The, by sending a hashed version of the password (only first 5 characters of the hashed passwords) to [Pwned Passwords](https://haveibeenpwned.com/Passwords) to check if they have been exploited. Through the response recieved, the function checks if the passwords have been leaked or hacked.

However, the API is never going to know the  full hash and therefore never, ever be able to guess the password. It'll just know that we have this tiny bit of a hash function that can match any thousands or even a million of passwords.

• Primary initial file- [check.py](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/check.py)

• Usefully Commented File- [checkpass.py](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/References/checkpass.py)

• [References](https://github.com/adrinorosario/Newfangled-Password-Checker/tree/main/References)- useful files related to the program and repository.

• Check out the [Object Oriented Programming Version](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/OOP%20Version/checker.py)

## Useful links
[SHA1 History](https://en.m.wikipedia.org/wiki/SHA-1)

[SHA1 Hash Generator]( https://passwordsgenerator.net/sha1-hash-generator/) tool- used in this project.

[Secure Hash Algorithms](https://brilliant.org/wiki/secure-hashing-algorithms/) Overview.

[Hashes.com](https://hashes.com/en/decrypt/hash)- decrypt all kinds of hashes.

[hashlib](https://docs.python.org/3/library/hashlib.html) Python3 module for decrypting and encoding Secure Hash Algorithms.

