# -*- coding: utf-8 -*-

import hashlib
import requests
import argparse
import re

def check_leak(x):

    SHA1 = hashlib.sha1(x.encode('utf-8'))
    hash_string = SHA1.hexdigest().upper()
    prefix = hash_string[0:5]

    header = {
        'User-Agent': 'password checker'
    }

    url = "https://api.pwnedpasswords.com/range/{}".format(prefix)

    req = requests.get(url, headers=header).content.decode('utf-8')
    # split the result twice - each line into key, value pairs of hash-postfixes and the usage count.
    hashes = dict(t.split(":") for t in req.split('\r\n'))

    # add the prefix to the key values (hashes) of the hashes dictionary
    hashes = dict((prefix + key, value) for (key, value) in hashes.items())

    for item_hash in hashes:
        if item_hash == hash_string:
            print("\nOh no — pwned!")
            print("{} has previously appeared in a data breach, used {} times, and should never be used. ".format(x,hashes[hash_string]))
            break

    if hash_string != item_hash:
        print("\nGood news — no pwnage found!")
        print("{} wasn't found in any of the Pwned Passwords loaded into Have I Been Pwned.".format(x))

    exit()

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--password", help="enter your password")
args = parser.parse_args()

argv = vars(args)
x = argv['password']

if args.password:
    check_leak(x)
else:
    print("No password supplied\n")
    parser.print_help()


'''
-References-
https://haveibeenpwned.com/API/v3#PwnedPasswords
https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

'''





