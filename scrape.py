#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from pathlib import Path

#cwd = os.path.dirname(os.path.abspath(chromedriver))
driver = webdriver.Chrome(executable_path='/home/ac0chisse/Holberton/Projects/Lost_and_Found_apk/chromedriver')

def load_auth():
    super_path = os.path.dirname(os.path.abspath(__file__))
    try:
        with open("{}/auth_data.json".format(super_path.rsplit("/", 1)[0]), "r") as json_file:
            return json.load(json_file)
    except IOError:
        print("Authorization data not found")
        sys.exit()

def login_form_entry():
    driver.get('https://intranet.hbtn.io/auth/sign_in')
    user = self.json_data["intra_user_key"]
    pwd = self.json_data["intra_pass_key"]
    u = driver.find_element_by_name('user[login]')
    u.driver.send_keys(user)
    p = driver.find_element_by_name('user[password')
    p.driver.send_keys(pwd)
    p.driver.send_keys(keys.RETURN)
    
    sleep(60)
    driver.close

if __name__ == '__main__':
    scrape()