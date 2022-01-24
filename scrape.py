#!/usr/bin/python3
## Scrapes Holberton Intranet to create a log in form
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import json
import time


#cwd = os.path.dirname(os.path.abspath(chromedriver))
#driver = webdriver.Chrome(executable_path='/home/ac0chisse/Holberton/Projects/Lost_and_Found-apk/chromedriver')
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()

def login_form_entry():
    #super_path = os.path.dirname(os.path.abspath(__file__))
    try:
         with open("auth_data.json", 'r') as fp:
            jsondata = json.load(fp)
            print("auth_data found.")
    except IOError:
        print("Authorization data not found. Please run ./auth_data.py *Username* *Password*")
        sys.exit()

    driver.maximize_window
    user = jsondata['intra_user_key']
    pwd = jsondata['intra_pass_key']
    address = "https://intranet.hbtn.io/auth/sign_in"
    driver.get(address)
    u = driver.find_element_by_name("user[login]")
    u.send_keys(user)
    p = driver.find_element_by_name("user[password]")
    p.send_keys(pwd)
    p.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.get("https://intranet.hbtn.io/dashboards/my_planning")
    time.sleep(1)
    cal = driver.find_element_by_name("day_tab")
    driver.execute_script("arguments[0].scrollIntoView(true);", cal)
    time.sleep(180)
    driver.close
    

if __name__ == '__main__':
    login_form_entry()