import requests
import hashlib


def request_api_data(hash_char):   
    url = 'https://api.pwnedpasswords.com/range/'+hash_char
    res = requests.get(url)  # fetches data from the url and stores it in res
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check the API and try again')
    return res


def password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())  # sepetares the hash and count
    for h, count in hashes:  # h stores the hash and count stores the number of times it's been cracked
        if h == hash_to_check:
            return count
    return 0 

    

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # encodes the password in sha1 hash
    first5_chars, rest = sha1password[:5],sha1password[5:] 
    response = request_api_data(first5_chars)  # passes the first five chars in the funct and receives matching responses
    return password_leak_count(response, rest)
    

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found to be leaked {count} times. Change your password!')
        else:
            print(f'{password} was not found to be leaked. Carry on!')
    return 'done!'


if __name__ == '__main__':
    print("-------------------Welcome To The Password Checker!!!-------------------")
    usr_inp = input('Enter password(s) to be checked for leaks: ')
    splited = usr_inp.split()
    main(splited)
    print("-------------------Thanks For Using The Password Checker!!!-------------------")