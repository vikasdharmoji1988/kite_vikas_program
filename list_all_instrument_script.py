# -*- coding: utf-8 -*-
"""
Getting historical data using Kite API

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from kiteconnect import KiteConnect
import os
import datetime as dt
import pandas as pd
import requests
# cwd = os.chdir("D:\\Udemy\\Zerodha KiteConnect API\\1_account_authorization")

def get_instruments(access_token: str):
    try:
        """
        Fetches the list of instruments from the Kite API.

        Args:
            access_token (str): The access token for Kite API authorization (format: 'api_key:access_token').

        Returns:
            list: Parsed instrument data as text (CSV format).
        """
        url = "https://api.kite.trade/instruments"
        headers = {
            "X-Kite-Version": "3",
            "Authorization": f"token {access_token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching instruments: {response.status_code} - {response.text}")

        # The response is a CSV text; return as string or parse if needed
        
    except Exception as e:
        print("Error_num-1004: error in get_instruments:",e)
    else:
        return response.text
    

def main():
    """
    Main function to test get_instruments().
    """
    # Example: input your access_token below in format "api_key:access_token"
    access_token = input("Enter your Kite access_token (format api_key:access_token): ").strip()

    try:
        data = get_instruments(access_token)
        print("✅ Instruments data received successfully.")
        print("\nFirst 500 characters:\n")
        print(data[:500])  # print first few lines for preview
    except Exception as e:
        print(f"❌ {e}")

#generate trading session
if __name__=="__main__":
    access_token = open(r'C:\VikasData\KiteConnect\OUT\Chatpter_1_UseFul_API\Step_1_Automatically_login_kite\access_token.txt','r').read()
    key_secret = open(r'C:\VikasData\KiteConnect\OUT\Chatpter_1_UseFul_API\Step_1_Automatically_login_kite\api_key_0625.txt','r').read().split()
    kite = KiteConnect(api_key=key_secret[0])
    kite.set_access_token(access_token)
    try:
        data = get_instruments(access_token)
   # print first few lines for preview
    except Exception as e:
        print(f"❌ {e}")
    # list_of_all_instruments=kite.instruments()
     # Save response text to file
    # Current script path
    script_path = os.path.abspath(__file__)
    # Project folder (directory containing the script)
    project_folder = os.path.dirname(script_path)
    output_file= project_folder+"\\"+'all_instrument_list.txt'

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(data)
    # print("script_path=",script_path)
    from save_list_in_csv import save_list_to_csv
    df = pd.read_csv(filepath_or_buffer=output_file)
    output_file=project_folder+"\\"+'all_instrument_list.csv'
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(output_file)
    # print(df.head())
    # all_instrument_in_csv=save_list_to_csv(df,project_folder,"all_instrument_list.csv")
    # print(all_instrument_in_csv)



