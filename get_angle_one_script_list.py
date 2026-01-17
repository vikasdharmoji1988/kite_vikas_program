import pandas as pd

def get_angel_one_instrument_list():
    url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
    # Load directly into a DataFrame
    df = pd.read_json(url)
    # Set the token as the index for faster lookups later
    df.set_index('token', inplace=False)
    return df

if __name__=="__main__":
    try:
        df_angle_one_instrument_list=get_angel_one_instrument_list()
        df_angle_one_instrument_list.to_excel(rf"C:\VikasData\KiteConnect\temp\mastersheet_1.xlsx",index=False)
        # print(df_angle_one_instrument_list.head(5))
        df_required1=df_angle_one_instrument_list[df_angle_one_instrument_list['exch_seg']=='NFO'].copy()
        df_required2=df_required1[df_required1['expiry']=='20JAN2026'].copy()
        df_required=df_required2[df_required2['strike']==2600000].copy()
        print(df_required)
    except Exception as e:
        print("e",e)