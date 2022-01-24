#!/usr/bin/python3
## Creates a json file that is used by scrape
import sys
import json

def auth_check():
    intra_user = sys.argv[1]
    intra_pass = sys.argv[2]
    auth = {"intra_user_key": intra_user, "intra_pass_key": intra_pass, 'API_key': 'Db55801b283adfd75532275e6c1b8b28='}
    try:
        with open('auth_data.json', 'w') as outfile:
            print("Writing file...")
            return json.dump(auth, outfile)
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

        print("Writing auth_data failed. please retry. *username* *password*")

if __name__ == "__main__":
    auth_check()
 main
