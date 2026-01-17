import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
import pandas as pd
from datetime import datetime, timedelta
# from angleone_login import get_angle_one_smart_api_and_session
# from get_option_greeks_from_angel_one import get_option_greeks_from_angelone
def get_angelone_historical_indiavix(smartapi):
    to_date = datetime.now()
    from_date = to_date - timedelta(days=365)

    params = {
        "exchange": "NSE",
        "symboltoken": "99926017",   # India VIX token
        "interval": "ONE_DAY",
        "fromdate": from_date.strftime("%Y-%m-%d %H:%M"),
        "todate": to_date.strftime("%Y-%m-%d %H:%M")
    }

    vix_data = smartapi.getCandleData(params)
    # print("vix_data=",vix_data)
    df = pd.DataFrame(vix_data["data"],
                    columns=["time","open","high","low","close","volume"])

    historical_iv = df["close"].copy()
    return historical_iv

if __name__=="__main__":
    from angle_one.get_angle_one_smart_api_and_session import get_angle_one_smart_api_and_session
    smartapi,angle_one_session=get_angle_one_smart_api_and_session()
    df_historical_india_vix=get_angelone_historical_indiavix(smartapi)
    iv_ce_current=0
    iv_pe_current=0
    list_option_greeks=[]
    from get_option_greeks_from_angel_one import get_option_greeks_from_angelone
    list_option_greeks=get_option_greeks_from_angelone(smartapi,"20JAN2026")
    for i in list_option_greeks:
        df_option_greeeks=pd.DataFrame([i])
        if df_option_greeeks.iloc[0]['strikePrice']=="25750.000000" and df_option_greeeks.iloc[0]['optionType']=="CE":
         iv_ce_current=df_option_greeeks.iloc[0]['impliedVolatility']
        if df_option_greeeks.iloc[0]['strikePrice']=="25800.000000" and df_option_greeeks.iloc[0]['optionType']=="PE":
         iv_pe_current=df_option_greeeks.iloc[0]['impliedVolatility']        
    # ============================================
    # step-get ivp
    # =============================================
    print("ce_current=",iv_ce_current)
    print("pe_current=",iv_pe_current)
    iv_current=float(iv_ce_current)+float(iv_pe_current)
    ivp = (df_historical_india_vix < float(iv_current)).sum() / len(df_historical_india_vix) * 100
    print(f"NIFTY IVP: {ivp:.2f}%")
    # current_vix = df_historical_india_vix.iloc[-1]
    # ivp2 = (df_historical_india_vix < current_vix).mean() * 100
    # print("ivp2=",ivp2)