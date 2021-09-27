<img src="https://chromeunboxed.com/wp-content/uploads/2019/10/GooglePasswordManagerCheckup.jpg" width="400" align="right"/>

[![GitHub license](https://img.shields.io/github/license/adrinorosario/Newfangled-Password-Checker?style=flat-square)](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/LICENSE)

# Newfangled-Password-Checker
An advanced and state of the art password checker created using Python3. It is a modern secure program that helps in checking if your passwords have ever been hacked. 

## How it works?

The program uses a ```SHA1``` algorithm to check if the passwords have been leaked or if they have been hacked. The, by sending a hashed version of the password (only first 5 characters of the hashed passwords) to [Pwned Passwords](https://haveibeenpwned.com/Passwords) to check if they have been exploited. Through the response recieved, the function checks if the passwords have been leaked or hacked.

However, the API is never going to know the  full hash and therefore never, ever be able to guess the password. It'll just know that we have this tiny bit of a hash function that can match any thousands or even a million of passwords.

## Usage
Using the primary file: Open your terminal in the directory of the file and type in/copy paste the snippet- 
   ```
   python3 check.py password
   ```
replace ```password``` with your password. Additionally, you can check as many as passwords you want, like: 
```
python3 check.py password1 password2
```
just have a `space` between each input.

Now, the [OOP version](https://github.com/adrinorosario/Newfangled-Password-Checker/tree/main/OOP%20Version) works in a different way such that you can check each element in a set or a given word or number and check how many times each symbol/number/alphabet/etc has been hacked. For using this version, open up your terminal in the OOP folder and type in the command:
```
python3 sample.py <example>
```
Replace the example with your own choice.
#### The OOP version checks only for a single operator or digit or element: for example- $. It checks only for $.
## Program Files
• Primary file- [check.py](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/check.py)
 I recommend that you use the [Primary file](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/check.py) for safety.  

• Usefully Commented File- [checkpass.py](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/References/checkpass.py)- does the same jobs as the primary file.

• Check out the [OOP version](https://github.com/adrinorosario/Newfangled-Password-Checker/tree/main/OOP%20Version).

• [References](https://github.com/adrinorosario/Newfangled-Password-Checker/tree/main/References)- useful files related to the program and repository.

## Support
[SHA1 History](https://en.m.wikipedia.org/wiki/SHA-1)

[SHA1 Hash Generator]( https://passwordsgenerator.net/sha1-hash-generator/) tool- used in this project.

[Secure Hash Algorithms](https://brilliant.org/wiki/secure-hashing-algorithms/) Overview.

[Hashes.com](https://hashes.com/en/decrypt/hash)- decrypt all kinds of hashes.

[hashlib](https://docs.python.org/3/library/hashlib.html) Python3 module for decrypting and encoding Secure Hash Algorithms.

## License- [MIT](https://github.com/adrinorosario/Newfangled-Password-Checker/blob/main/LICENSE)
