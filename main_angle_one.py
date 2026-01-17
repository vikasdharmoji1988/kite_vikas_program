from get_angle_one_script_list import get_angel_one_instrument_list
from get_angleone_option_symbol_and_token import get_angleone_option_symbol_and_token
import pandas as pd
if __name__=="__main__":
    # ===============
    # step- get symbol
    # ===============
    df_angle_one_instrument_list=get_angel_one_instrument_list()
    exchange_seg_value='NFO'
    actual_strike_value="26000"
    expiry_date_value='13JAN2026'
    dict_pe_ce_token=get_angleone_option_symbol_and_token(df_angle_one_instrument_list,
                                            exch_seg_value=exchange_seg_value,
                                            expiry_date_value=expiry_date_value,
                                            actual_strike_value=actual_strike_value)
    
    # ========================
    # step-get iv value
    # =======================
    from angle_one.get_angle_one_smart_api_and_session import get_angle_one_smart_api_and_session
    smartapi,angle_one_session=get_angle_one_smart_api_and_session()
    
    list_token=[str(dict_pe_ce_token['pe_token']),str(dict_pe_ce_token['ce_token'])]
    request_params = {
    "mode": "FULL",
    "exchangeTokens": {
        "NFO": list_token # Replace with the actual token from Scrip Master
    } }  
    quote=smartapi.getMarketData(**request_params)
    quote=smartapi.optionGreek(**request_params)
    dict_data=quote["data"]
    list_fetched=dict_data["fetched"]
    print("fetched=",list_fetched)
    for i in list_fetched:
        df_script=pd.DataFrame(i)    
        print(df_script.columns)
        break