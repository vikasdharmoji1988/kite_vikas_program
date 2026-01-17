import pandas as pd
from get_angle_one_script_list import get_angel_one_instrument_list
def get_angleone_option_symbol_and_token(df_angle_one_instrument_list,exch_seg_value,expiry_date_value,actual_strike_value):
    try:
        strike_value=int(actual_strike_value+"00")
        df_angle_one_instrument_list.to_excel(rf"C:\VikasData\KiteConnect\temp\mastersheet_1.xlsx",index=False)
        # print(df_angle_one_instrument_list.head(5))
        df_required1=df_angle_one_instrument_list[df_angle_one_instrument_list['exch_seg']==exch_seg_value].copy()
        df_required2=df_required1[df_required1['expiry']==expiry_date_value].copy()
        df_required3=df_required2[df_required2['strike']==strike_value].copy()
        df_ce=df_required3[df_required3['symbol'].str.endswith('CE',na=False)].copy()
        df_pe=df_required3[df_required3['symbol'].str.endswith('PE',na=False)].copy()
        ce_symbol=df_ce.iloc[0]['symbol']
        ce_token=df_ce.iloc[0]['token']
        pe_symbol=df_pe.iloc[0]['symbol']
        pe_token=df_pe.iloc[0]['token']
        
        result={"ce_symbol":ce_symbol,"ce_token":ce_token,"pe_symbol":pe_symbol,"pe_token":pe_token}
     
        return result
    except Exception as e:
        return e
if __name__=="__main__":
    df_angle_one_instrument_list=get_angel_one_instrument_list()
    exchange_seg_value='NFO'
    actual_strike_value="26000"
    expiry_date_value='13JAN2026'
    result=get_angleone_option_symbol_and_token(df_angle_one_instrument_list,
                                          exch_seg_value=exchange_seg_value,
                                          expiry_date_value=expiry_date_value,
                                          actual_strike_value=actual_strike_value)
    print("Result=",result)