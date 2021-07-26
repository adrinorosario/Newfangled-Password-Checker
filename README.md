<img src="https://chromeunboxed.com/wp-content/uploads/2019/10/GooglePasswordManagerCheckup.jpg" width="400" align="right"/>

# Newfangled-Password-Checker
An advanced and state of the art password checker created using Python3. It is a modern secure program that helps in checking if your passwords have ever been hacked. 

The program uses a ```SHA1``` algorithm to check if our passwords have been leaked anywhere or if they have been hacked. We send a hashed version of our password to [Pwned Passwords API](https://haveibeenpwned.com/Passwords) and check if they have been exploited. Then, through the response we recieve, we see if they have been leaked/hacked.

However, the API is never going to know the  full hash and therefore never, ever be able to guess our password. It'll just know that we have this tiny bit of a hash function that can match any thousands or even a million of passwords.
