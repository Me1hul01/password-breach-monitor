import requests
import hashlib
import sys


def requests_api_data(query_chars):
    url = 'https://api.pwnedpasswords.com/range/' + query_chars
    res = requests.get(url)

    if res.status_code != 200:
     raise RuntimeError(f"Error Fetching:{res.status_code},check your api and try again")
    return res

def get_password_leaks_count(hashes,hashes_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:

     if h==hashes_to_check:
        return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars = sha1password[:5]
    remaining = sha1password[5:]
    response = requests_api_data(first5_chars)
    return get_password_leaks_count(response, remaining)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            Message=(f"{password} is found {count} times")
            return Message
        else:
            return None


main(sys.argv[1:])






