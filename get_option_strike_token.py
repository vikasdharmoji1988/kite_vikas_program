import pandas as pd
def get_option_strike_token(df_strike_expiry:pd.DataFrame,strike_value,strike_expiry):
    strike_value=int(strike_value)
    # print(strike_value)
    # print(df_strike_expiry)
    df_required=df_strike_expiry[(df_strike_expiry['strike']==strike_value) & (df_strike_expiry['expiry']==strike_expiry)].copy()
    # print("df_required=",df_required)
    return df_required.iloc[0]['instrument_token']

if __name__=="__main__":
    df_excel=pd.read_excel(r"C:\VikasData\KiteConnect\temp\testing\instrument_list\df_ce.xlsx",sheet_name='instrument')
    strike_value="25950"
    strike_expiry="2025-12-30"
    print(df_excel.info())
    nifty_50_token=get_option_strike_token(df_excel,strike_value,strike_expiry)
    print(nifty_50_token)