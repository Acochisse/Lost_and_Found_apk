#!/usr/bin/python3
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
        print("Writing auth_data failed. please retry. *username* *password*")

if __name__ == "__main__":
    auth_check()
