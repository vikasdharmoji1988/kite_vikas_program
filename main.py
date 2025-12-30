from create_folder import create_folder
from create_date_time_str import create_date_time_str
from get_unique_character_str import get_unique_character_str
from get_kite_secret import get_kite_secret
from get_instrument_data import get_instrument_data
from get_token_of_script import get_instrument_token_of_script
from kiteconnect import KiteConnect
from datetime import datetime

if __name__=="__main__":
    # Error_num-1006: error in create_date_time_unique_str
    # ======================
    # create folder
    # ======================
    base_folder_path=r"C:\VikasData\KiteConnect\temp"
    date_time_str= create_date_time_str()
    already_exist=()
    unique_char=get_unique_character_str(already_exist,1,1,1,1)
    base_folder_name=rf"{date_time_str}_{unique_char}"
    working_path=rf"{base_folder_path}\{base_folder_name}"
    x=create_folder(working_path)
    print("base_folder=",x)
    #=======================
    #step-access_token & api_key
    #=======================
    access_token,api_key=get_kite_secret()
    # =======================
    # step-get data_frame
    # ===================
    df_instrument,df_ce,df_pe,df_eq,df_fut=get_instrument_data(access_token,working_path)
    # =======================
    # step-get data_frame_of_nifty_ce
    # ========================
    df_nifty_ce=df_ce[df_ce['name']=="NIFTY"].copy()
    df_nifty_pe=df_pe[df_pe['name']=="NIFTY"].copy()
    df_indices_eq=df_eq[df_eq['segment']=="INDICES"].copy()
    # =========================
    # step-get value of nifty 
    # =========================
    nifty_50_script_name="NIFTY 50"
    nifty_50_symbol_name="NIFTY 50"
    nifty_50_token=get_instrument_token_of_script(df_eq,nifty_50_script_name,nifty_50_symbol_name)
    # ===========================
    # step-get nifty value
    # ===========================
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    nifty_50_quote=kite.quote(nifty_50_token)
    nifty_50_last_price=nifty_50_quote[f"{nifty_50_token}"]["last_price"]
    print("nifty_50_last_price=",nifty_50_last_price) 
    roundup_nifty_50_lp=round(nifty_50_last_price,None)
    # ========================
    # step-get atm value
    # ========================
    from get_atm_value import get_atm_value
    atm_value=get_atm_value(roundup_nifty_50_lp)
    # =======================
    # step-first strike value 
    # =======================
    strike_info={"strike_value":"","token":"","expiry_date":"","day":"","time_now":"","is_atm_now":"","oi":"","change_in_oi":""}
    first_strike_consideration_value=atm_value-500
    last_strike_consideration_value=atm_value+500
    strike=[]
    for i in range(first_strike_consideration_value,last_strike_consideration_value,50):
        strike.append(i)
    #===============================
    #step-get current expiry date
    #===============================
    list_expiry_date=[]
    expiry_date_tuple=()
    for i in df_ce['expiry']:
        list_expiry_date.append(i)
    
    expiry_date_tuple=tuple(list_expiry_date)
    latest_expiry_date=max(datetime.strptime(d,"%Y-%m-%d") for d in expiry_date_tuple)
    print("latet_expiry_date",latest_expiry_date)