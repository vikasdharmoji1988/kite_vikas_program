from kiteconnect import KiteConnect
from get_kite_secret import get_kite_secret
import pandas as pd
import time
from tenacity import retry, stop_after_attempt, wait_exponential
from kiteconnect.exceptions import NetworkException
# ... your existing setup (kite object initialization) ...

@retry(
    wait=wait_exponential(multiplier=1, min=1, max=10), # Waits 1s, 2s, 4s, etc.
    stop=stop_after_attempt(5), # Retries up to 5 times
    # retry=retry_if_exception_type(exceptions.NetworkException) # Only retries NetworkExceptions
)
def get_quote_with_retry(token):
    """Function to fetch quote with built-in retry logic."""
    return kite.quote(token)
def extract_option_info_in_df(strike_info,
                              strike_token,
                              first_strike_consideration_value,
                              last_strike_consideration_value,
                              latest_expiry_date,
                              df_ce:pd.DataFrame,
                              df_pe:pd.DataFrame,
                              df_eq:pd.DataFrame):
    # =================================================
    # step-get nifty atm value
    # ====================================================
    from get_nifty50_value import get_nifty50_value
    from get_atm_value import get_atm_value
    
    nifty_50_last_price=get_nifty50_value(df_eq=df_eq)
    roundup_nifty_50_lp=round(float(nifty_50_last_price["nifty_value"]),None)
    atm_value=get_atm_value(roundup_nifty_50_lp) 
    
    #========================================== 
    #  step-functional setup
    # ========================================
    access_token,api_key=get_kite_secret()
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    kite_quote=kite.quote(strike_token)
    
    for i in range(first_strike_consideration_value,last_strike_consideration_value,50):
        # strike.append(i)
        if int(i)==int(atm_value):
            strike_info["ce_strike_position"]="atm"
            strike_info["pe_strike_position"]="atm"
        else:
            if int(i)<int(atm_value):
               strike_info["ce_strike_position"]="itm"
               strike_info["pe_strike_position"]="otm"
            else:
                strike_info["ce_strike_position"]="otm"
                strike_info["pe_strike_position"]="itm"
        
        strike_info["strike"]=i
        strike_info["expiry_date"]=latest_expiry_date
       
        # ===============================================
        # step-get ce values
        # ================================================
        from get_token_of_script import get_token_of_script
        from get_option_strike_token import get_option_strike_token
    
        strike_info["ce_token"]=get_option_strike_token(df_ce,i,latest_expiry_date)
        # try:
        # quote_ce=kite.quote(strike_info["ce_token"])
        # except NetworkException as e:
        #   print("Rate limit hit — retrying...")
        #   time.sleep(1.5)
        strike_info["current_date"]='last_trade_time'
        ce_str1=str(strike_info["ce_token"])
        # ===========================================
        # step- play with time
        # ======================================
        date_and_time_both=kite_quote[ce_str1]["last_trade_time"]
        strike_info["current_date"]=date_and_time_both.strftime("%Y-%m-%d")
        strike_info["current_day"]=date_and_time_both.strftime("%A")
        strike_info["current_market_time"]=date_and_time_both.strftime("%H-%M-%S")
        #step-get ce_value
        strike_info["ce_value"]=kite_quote[ce_str1]["last_price"]
        #step-get ce_oi_value
        strike_info["ce_oi"]=kite_quote[ce_str1]["oi"]
        #====================================================
        # step - pe value
        # ===================================================
        strike_info["pe_token"]=get_option_strike_token(df_pe,i,latest_expiry_date)
        # quote_pe=kite.quote(strike_info["pe_token"])
        str_pe_token=str(strike_info["pe_token"])
        #step-get ce_value
        strike_info["pe_value"]=kite_quote[str_pe_token]["last_price"]
        #step-get ce_oi_value
        strike_info["pe_oi"]=kite_quote[str_pe_token]["oi"]
        #========================================
        #step-insite from data
        total_pcr_value=round(float(strike_info["pe_oi"])/float(strike_info["ce_oi"]),2)
        strike_info["total_pcr"]=str(total_pcr_value)
        import shared_variable
        shared_variable.dictionary_df[str(i)]=pd.concat([shared_variable.dictionary_df[str(i)],pd.DataFrame([strike_info])],ignore_index=True)
    return shared_variable.dictionary_df,nifty_50_last_price["nifty_value"]
# def create_df_for_strike_info(strike_info):


if __name__=="__main__":
    # =======================
    # step-input
    # =======================
    atm_value=26300
    latest_expiry_date="2026-01-06"
    first_strike_consideration_value=atm_value-500
    last_strike_consideration_value=atm_value+500
    df_ce=pd.read_excel(r"C:\VikasData\KiteConnect\temp\testing\instrument_list\df_ce.xlsx",sheet_name='instrument')
    df_pe=pd.read_excel(r"C:\VikasData\KiteConnect\temp\testing\instrument_list\df_pe.xlsx",sheet_name='instrument')
    # =========================
    # step-drived input
    # ==========================
    access_token,api_key=get_kite_secret()
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    strike_info={"strike":"","strike_symbol":"","expiry_date":"","current_date":"","current_day":"","current_market_time":"","ce_token":"","ce_strike_position":"","ce_value":"","ce_oi":"","ce_change_in_oi":"","ce_change_in_oi_percentage":"","pe_token":"","pe_strike_position":"","pe_value":"","pe_oi":"","pe_change_in_oi":"","total_pcr":"","change_in_oi_pcr":""}
    strike=[]
    strike_token=[]
    # global dictionary_df
    dictionary_df_1={}

    from get_option_strike_token import get_option_strike_token
    for i in range(first_strike_consideration_value,last_strike_consideration_value,50):
        df_example=pd.DataFrame(columns=strike_info.keys())
        dictionary_df_1.update({str(i):df_example})
        strike.append(i)
        strike_token.append(get_option_strike_token(df_ce,i,latest_expiry_date))
        strike_token.append(get_option_strike_token(df_pe,i,latest_expiry_date))
    # ===========================================================
    # step-trial
    # =============================================================
    dictionary_df_2={}
    dictionary_df_2=extract_option_info_in_df(strike_info,strike_token,atm_value,first_strike_consideration_value,
                              last_strike_consideration_value,
                              latest_expiry_date,
                              df_ce,
                              df_pe)
    print("dd=",dictionary_df_2)
    # #========================================== 
    # #  step-functional setup
    # # ========================================
    # access_token,api_key=get_kite_secret()
    # kite = KiteConnect(api_key=api_key)
    # kite.set_access_token(access_token)
    # kite_quote=kite.quote(strike_token)
    

    # for i in range(first_strike_consideration_value,last_strike_consideration_value,50):
    #     strike.append(i)
    #     if int(i)==int(atm_value):
    #         strike_info["ce_strike_position"]="atm"
    #         strike_info["pe_strike_position"]="atm"
    #     else:
    #         if int(i)<int(atm_value):
    #            strike_info["ce_strike_position"]="itm"
    #            strike_info["pe_strike_position"]="otm"
    #         else:
    #             strike_info["ce_strike_position"]="otm"
    #             strike_info["pe_strike_position"]="itm"
        
    #     strike_info["strike"]=i
    #     strike_info["expiry_date"]=latest_expiry_date
       
    #     # ===============================================
    #     # step-get ce values
    #     # ================================================
        
    #     strike_info["ce_token"]=get_option_strike_token(df_ce,i,latest_expiry_date)
    #     # try:
    #     # quote_ce=kite.quote(strike_info["ce_token"])
    #     # except NetworkException as e:
    #     #   print("Rate limit hit — retrying...")
    #     #   time.sleep(1.5)
    #     strike_info["current_date"]='last_trade_time'
    #     ce_str1=str(strike_info["ce_token"])
    #     # ===========================================
    #     # step- play with time
    #     # ======================================
    #     date_and_time_both=kite_quote[ce_str1]["last_trade_time"]
    #     strike_info["current_date"]=date_and_time_both.strftime("%Y-%m-%d")
    #     strike_info["current_day"]=date_and_time_both.strftime("%A")
    #     strike_info["current_market_time"]=date_and_time_both.strftime("%H-%M-%S")
    #     #step-get ce_value
    #     strike_info["ce_value"]=kite_quote[ce_str1]["last_price"]
    #     #step-get ce_oi_value
    #     strike_info["ce_oi"]=kite_quote[ce_str1]["oi"]
    #     #====================================================
    #     # step - pe value
    #     # ===================================================
    #     strike_info["pe_token"]=get_option_strike_token(df_pe,i,latest_expiry_date)
    #     quote_pe=kite.quote(strike_info["pe_token"])
    #     str_pe_token=str(strike_info["pe_token"])
    #     #step-get ce_value
    #     strike_info["pe_value"]=kite_quote[str_pe_token]["last_price"]
    #     #step-get ce_oi_value
    #     strike_info["pe_oi"]=kite_quote[str_pe_token]["oi"]
    #     #========================================
    #     #step-insite from data
    #     total_pcr_value=round(float(strike_info["pe_oi"])/float(strike_info["ce_oi"]),2)
    #     strike_info["total_pcr"]=str(total_pcr_value)
    #     dictionary_df[str(i)]=pd.concat([dictionary_df[str(i)],pd.DataFrame([strike_info])],ignore_index=True)
    