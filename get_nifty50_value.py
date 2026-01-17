from get_token_of_script import get_token_of_script
from get_kite_secret import get_kite_secret
import pandas as pd
from kiteconnect import KiteConnect
import time
def get_nifty50_value(df_eq:pd.DataFrame):
    # =========================
    # step-get value of nifty 
    # =========================
    nifty_50_script_name="NIFTY 50"
    nifty_50_symbol_name="NIFTY 50"
    nifty_50_token=get_token_of_script(df_eq,nifty_50_script_name,nifty_50_symbol_name)
    # ===========================
    # step-get nifty value
    # ===========================
    access_token,api_key=get_kite_secret()
    
    try:
      kite = KiteConnect(api_key=api_key)
      kite.set_access_token(access_token)
      nifty_50_quote=kite.quote([nifty_50_token])
      nifty_50_last_price=nifty_50_quote[f"{nifty_50_token}"]["last_price"]
    except:
      kite = KiteConnect(api_key=api_key)
      kite.set_access_token(access_token)
      nifty_50_quote=kite.quote([nifty_50_token])
      nifty_50_last_price=nifty_50_quote[f"{nifty_50_token}"]["last_price"]
      
    # print("nifty_50_last_price=",nifty_50_last_price) 
    # roundup_nifty_50_lp=round(nifty_50_last_price,None)
    return {"nifty_value":str(nifty_50_last_price),"nifty_token":str(nifty_50_token)}

if __name__=="__main__":
    df_eq=pd.read_excel(r"C:\VikasData\KiteConnect\temp\testing\instrument_list\df_eq.xlsx",sheet_name='instrument')
    nifty_value={}
    nifty_value=get_nifty50_value(df_eq=df_eq)
    print(nifty_value["nifty_value"])