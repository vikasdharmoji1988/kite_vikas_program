import pandas as pd
def get_instrument_token_of_script(df_of_instrument:pd.DataFrame,script_name:str,script_symbol:str,output_name_of_column:str="instrument_token"):
    df_required=df_of_instrument[(df_of_instrument['name']==script_name) & (df_of_instrument['tradingsymbol']==script_symbol)]
    if df_required.empty==True:
        return None
    return df_required.iloc[0][output_name_of_column]

if __name__=="__main__":
    df_excel=pd.read_excel(r"C:\VikasData\KiteConnect\temp\testing\instrument_list\instrument_list.xlsx",sheet_name='instrument')
    nifty_50_script_name="NIFTY 50"
    nifty_50_symbol_name="NIFTY 50"
    nifty_50_token=get_instrument_token_of_script(df_excel,nifty_50_script_name,nifty_50_symbol_name)
    print(nifty_50_token)
    