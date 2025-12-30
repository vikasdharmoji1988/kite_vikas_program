from kiteconnect import KiteConnect
from get_kite_secret import get_kite_secret
import pandas as pd
import openpyxl

if __name__=="__main__":
        
    access_token,api_key=get_kite_secret()
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)


    list_instrument=[10359298]
    quotes_option=kite.quote(list_instrument)
    oi=quotes_option["10359298"]["oi"]
    print(quotes_option)
    # print("access_token=",access_token)
    # # Get all F&O instruments
    # inst = kite.instruments("NFO")
    # df = pd.DataFrame(inst)

    # df.to_excel(r"C:\VikasData\KiteConnect\temp\testing\nfo.xlsx",sheet_name="nfo_testing",index=None)
    # print(df)
