import requests
import hashlib
import sys


class Requester:
    def __init__(self, api):
        self.api = api

    def request_api_data(self, query_character):
        url = self.api + query_character
        response = requests.get(url)

        if response:
            try:
                if response.status_code != 200:
                    raise RuntimeError(
                        f'Error {response.status_code}: check API')
                return response
            except RuntimeError:
                print('ERROR- not 200')


class ExploitationChecker(Requester):
    def __init__(self, x=None):
        self.x = x

    def get_password_leaks_count(self, hashes, hash_to_check):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for h, count in hashes:
            if h == hash_to_check:
                return count
        return self.x  # return 0


class PwnedPasswords(ExploitationChecker):
    def __init__(self, y=None):
        self.y = y

    def pwned_api_check(self, password):
        sha1password = hashlib.sha1(
            password.encode('utf-8')).hexdigest().upper()
        first5, tail = sha1password[:5], sha1password[5:]
        response = ExploitationChecker.request_api_data(first5)
        return ExploitationChecker.get_password_leaks_count(response, tail)


class Finale(PwnedPasswords):
    def __init__(self, password):
        self.password = password

    def main(self):

        count = PwnedPasswords.pwned_api_check(self.password)
        if count:
            print(
                f'{self.password} was found {count} times-- TiMe TO ChanGe Your PaSSword')
        else:
            print(f'{self.password} not found, Carry On!')


api = Requester('https://api.pwnedpasswords.com/range/')
print([Finale('adrinorosariojamesadrinorosariojames')])
