#!/usr/bin/python3
## Creates a json file that is used by scrape
import sys
import json

def auth_check():
    try:
        with open('auth_data.json', 'r') as fp:
            data = json.load(fp)
            print("auth_data found.")
    except:
        if not sys.argv[1]:
            print("Holberton Username is missing")
        if not sys.argv[2]:
            print("Holberton Password is missing")
        else:
            intra_user = sys.argv[1]
            intra_pass = sys.argv[2]
            auth = {"intra_user_key": intra_user, "intra_pass_key": intra_pass, 'API_key': 'Db55801b283adfd75532275e6c1b8b28='}
            with open('auth_data.json', 'w') as outfile:
                json.dump(auth, outfile)
