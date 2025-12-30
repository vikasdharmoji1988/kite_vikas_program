from kiteconnect import KiteConnect
import os
import datetime as dt
import pandas as pd
from get_token_of_script import get_instrument_token_of_script
from get_kite_secret import get_kite_secret
def get_historical_data(api_key1,access_token1,instrument_token1,date_intervel_number,interval_type):
    try:
        kite = KiteConnect(api_key=api_key1)
        kite.set_access_token(access_token1)
        # get  historical data from todays day 
        #=====================================
        #step-1 get from date
        #====================================
        from datetime import date
        from_date1 = date.today().strftime("%Y-%m-%d")
        print("step-1 get from date=",from_date1)
        #=============================================
        #step-2 to older date
        #=================
        from get_older_day import get_older_date
        to_date1 =get_older_date(from_date=from_date1,days=date_intervel_number)
        print("step-2 older day",to_date1)
        # ===================================
        # step-3 used historical data method of kite connect
        # ===========================================
        historical_data=kite.historical_data(instrument_token=instrument_token1,from_date=to_date1,to_date=from_date1,interval=interval_type)
        # historical_data=kite.historical_data(instrument_token='738561',from_date=to_date1,to_date=from_date1,interval='day')
        df_historcal_data=pd.DataFrame(historical_data) 
    except Exception as e:
        print("error in get_historical_data=",e)
    else:
        return df_historcal_data
# 
    # 
    # 
    # last_index = df_historcal_data.ndim
    # print("step-2.Last Index=", last_index)
    # if last_index>=maximum_day_of_trading :   
    #     if OHCL_condition not in df_historcal_data.columns:
    #         raise ValueError(f"Invalid OHCL_condition '{OHCL_condition}'. Choose from {list(df_historcal_data.columns)}")
             
    #     df_close_sma=df_historcal_data[OHCL_condition].rolling(window=moving_average_window).mean()
    #     # df_close_ema=df_historcal_data['close'].ewm(span=200,adjust=False).mean()
    #     return(df_close_sma.iloc[-1])
    # else:
    #     return("Error:1_number of trading=",last_index)

if __name__ == "__main__":
    # access_token = open(r'C:\VikasData\KiteConnect\OUT\Chatpter_1_UseFul_API\Step_1_Automatically_login_kite\access_token.txt','r').read()
    # key_secret = open(r'C:\VikasData\KiteConnect\OUT\Chatpter_1_UseFul_API\Step_1_Automatically_login_kite\api_key_0625.txt','r').read().split()
    # api_key2=key_secret[0]

    #=======================
    #step-access_token & api_key
    #=======================
    access_token,api_key=get_kite_secret()
    # ===============================
    # 
    # ===============================
    df_excel=pd.read_excel(r"C:\VikasData\KiteConnect\temp\testing\instrument_list\instrument_list.xlsx",sheet_name='instrument')
    nifty_50_script_name="NIFTY 50"
    nifty_50_symbol_name="NIFTY 50"
    nifty_50_token=get_instrument_token_of_script(df_excel,nifty_50_script_name,nifty_50_symbol_name)
    print(nifty_50_token)
    # ==============================
    # 
    # ================================
    historical_data_of_nifty50=get_historical_data(api_key1=api_key,access_token1=access_token,instrument_token1=nifty_50_token,date_intervel_number=45,interval_type='day')
    print(historical_data_of_nifty50)


