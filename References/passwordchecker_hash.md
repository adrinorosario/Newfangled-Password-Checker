# This File is the Notes of checkpass.py Python Script

### We want to send the hashed version of our password to our API.

### The API uses a modern technique, which allows someone to recieve information about us yet still not know who we are.

### We only give the First 5 CHARACTERS of our hashed password. This API has a list of all passwords that have been leaked, these leaked ones are hashed with SHA1 Algorithm. It's going to look in it's database of all these passwords and pick all the hashed passwords that have the first 5 chars that match first 5 of ours.

### This way,with the response, we're going to get all the passwords that are hashed that have this{first 5 hash of our password} so that on our end, when we receive that response, we can check the rest of the hash function this way.

### This API is never going to know our full hash and therefore never, ever be able to guess our password. They'll just know that we have this tiny bit of a hash function that can match any hundreds of passwords.

### You should use 'utf-8'

