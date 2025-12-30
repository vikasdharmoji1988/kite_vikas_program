# -*- coding: utf-8 -*-
"""
Zerodha kiteconnect automated authentication

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from kiteconnect import KiteConnect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import time
import os
from pyotp import TOTP
print("Step-0.login_url=Enter")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
def autologin():
     token_path = "C:\\VikasData\\KiteConnect\\OUT\\Chatpter_1_UseFul_API\\Step_1_Automatically_login_kite\\api_key_0625.txt"
     key_secret = open(token_path,'r').read().split()
     kite = KiteConnect(api_key=key_secret[0])
     print("Step-1.login_url=",kite.login_url())
 # Set up the Chrome driver service
     service = Service(r"C:\\VikasData\\KiteConnect\\OUT\\Chatpter_1_UseFul_API\\Step_1_Automatically_login_kite\\chromedriver.exe")
       # Path to your chromedriver executable
     service.start()
    # Print the service URL
    # print(service.service_url())
 
     options = webdriver.ChromeOptions()
   
    #  options.add_argument('--headless')
  
    #  options = options.to_capabilities()

     chrome_options = webdriver.ChromeOptions()
     chrome_options.debugger_address = "localhost:9222"  # Connect to the running instance
    #  driver = webdriver.Chrome(options=chrome_options)

# Now you can open any URL

    # Optionally, create a WebDriver instance
     driver = webdriver.Chrome(service=service)
     driver.get(kite.login_url())
     driver.implicitly_wait(10)
     print("Step-2.Chrome browser webdriver is updated & goes to login page of kite zerodha site")
     username = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
     password = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')  
     username.send_keys(key_secret[2])
     password.send_keys(key_secret[3])
     driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
     driver.implicitly_wait(10)
     print("Step-3.taken login id & password")
     pin = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[1]/input')
     print("Step-5.pin popup")
     totp = TOTP(key_secret[4])
     token = totp.now()
     pin.send_keys(token)
    #  driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form/div[2]/button').click()
    #  driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/button')
    #  driver.implicitly_wait(100)
     print("Step-6.google token taken")
     i=0
     while driver.current_url.find("request_token=")==-1 :
          i=i+1
          print(i)
          driver.implicitly_wait(10)
    #  WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
     print("step-7 get url=",driver.current_url)
     request_token=driver.current_url.split('request_token=')[1]
    
     with open("C:\\VikasData\\KiteConnect\\OUT\\Chatpter_1_UseFul_API\\Step_1_Automatically_login_kite\\request_token.txt", 'w') as the_file:
      the_file.write(request_token)
     print("step-8 request_token=",request_token)
     driver.quit()   
     return key_secret,request_token  

#         # Retrieve and save the request token

# # driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/button').click()
      
#     #   driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/button').click()
if __name__=='__main__':
 key_secret_And_request_token =autologin()

# # generating and storing access token - valid till 6 am the next day
 request_token =key_secret_And_request_token[1]# open("C:\\VikasData\\KiteConnect\\OUT\\Chatpter_1_UseFul_API\\Step_1_Automatically_login_kite\\request_token.txt",'r').read()
 key_secret = key_secret_And_request_token[0]#open("C:\\VikasData\\KiteConnect\\OUT\\Chatpter_1_UseFul_API\\Step_1_Automatically_login_kite\\api_key.txt",'r').read().split()
 kite = KiteConnect(api_key=key_secret[0])
 data = kite.generate_session(request_token, api_secret=key_secret[1])
 with open(r'C:\VikasData\KiteConnect\OUT\Chatpter_1_UseFul_API\Step_1_Automatically_login_kite\access_token.txt', 'w') as file:
        file.write(data["access_token"])
        print("step-9 access_token=",data["access_token"])

 print("Step-10=Login into kite is completed")