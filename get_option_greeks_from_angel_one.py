
import pandas as pd
def get_option_greeks_from_angelone(smartapi,expiryday):
    print(type(expiryday))
    request_data = {
        "name": "",
        "expirydate": ""
        # "13JAN2026"  # Format: DDMMMYYYY
    }
    request_data["name"]="NIFTY"
    request_data["expirydate"]=expiryday
    optionGreeks = smartapi.optionGreek(request_data)
    # print(type(optionGreeks['data']))
    return optionGreeks['data']

if __name__=="__main__":
 from get_angle_one_smart_api_and_session import get_angle_one_smart_api_and_session
 smartapi,angle_one_session=get_angle_one_smart_api_and_session()
 list_option_greeks=[]
 list_option_greeks=get_option_greeks_from_angelone(smartapi,"20JAN2026")
 print(list_option_greeks)
#  for i in list_option_greeks:
#     df_option_greeeks=pd.DataFrame([i])
#     if df_option_greeeks.iloc[0]['strikePrice']=="25700.000000":
#        print(df_option_greeeks.iloc[0]['impliedVolatility'])
#     break
    #    print(df_option_greeeks.iloc[0]['impliedVolatility'])
       

# quote = smartapi.optionGreek(
#     exchange="NSE",
#     name="NIFTY",
#     expirydate="13JAN2026"
# )
# print(quote)