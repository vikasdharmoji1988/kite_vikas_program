import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
from create_folder import create_folder
from create_date_time_str import create_date_time_str
from get_unique_character_str import get_unique_character_str
from get_kite_secret import get_kite_secret
from get_instrument_data import get_instrument_data
from get_token_of_script import get_token_of_script
from kiteconnect import KiteConnect
from datetime import datetime
import pandas as pd
import logging
import time as t
from angle_one.get_option_greeks_from_angel_one import get_option_greeks_from_angelone
from angle_one.get_angle_one_smart_api_and_session import get_angle_one_smart_api_and_session
from angle_one.get_angelone_historical_vix import get_angelone_historical_indiavix
from angle_one.get_angle_one_smart_api_and_session import get_angle_one_smart_api_and_session
if __name__=="__main__":
    # Error_num-1006: error in create_date_time_unique_str
    # ===========================================================
    # 
    # ===========================================================
    # 1. Setup Logging (This tells you WHERE it freezes)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


    # ======================
    # create folder
    # ======================
    base_folder_path=r"C:\VikasData\KiteConnect\temp\20_01_26"
    date_time_str= create_date_time_str()
    already_exist=()
    unique_char=get_unique_character_str(already_exist,1,1,1,1)
    base_folder_name=rf"{date_time_str}_{unique_char}"
    working_path=rf"{base_folder_path}\{base_folder_name}"
    x=create_folder(working_path)
    output_folder_path=rf"{working_path}\output_folder"
    y=create_folder(output_folder_path)
    print("base_folder=",x)
    #=======================
    #step-access_token & api_key
    #=======================
    access_token,api_key=get_kite_secret()
    # =======================
    # step- angel one
    # =======================
    # from angle_one.angleone_login import get_angle_one_smart_api_and_session
    smartapi,angle_one_session=get_angle_one_smart_api_and_session()
    # ===============================================================
    try:
     t.sleep(9)
     df_historical_india_vix=get_angelone_historical_indiavix(smartapi)
    except Exception as exception:
     print("issue in df_historical_india_vix=",exception)
     smartapi,angle_one_session=get_angle_one_smart_api_and_session()
     t.sleep(9)
     df_historical_india_vix=get_angelone_historical_indiavix(smartapi)

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
    #===============================
    #step-get expiry dates
    # remove if today is expiry & time is more than 3.30pm
    #===============================
    today1=datetime.today()
    today_date_in_str=today1.strftime("%Y-%m-%d")
    nowhour=today1.hour
    nowminute=today1.minute

    list_expiry_date=[]
    for i in df_nifty_ce['expiry']:
        if i != today_date_in_str:
            list_expiry_date.append(i)
        else:
            if nowhour <15:
                list_expiry_date.append(i)
            elif nowhour==15 and nowminute <31:
                list_expiry_date.append(i)                      
    #===================================
    #step-get current expiry dates
    #==================================
    expiry_date_tuple=tuple(set(list_expiry_date))
    print(expiry_date_tuple) 
    # print(expiry_date_tuple)
    latest_expiry_date=min(datetime.strptime(d,"%Y-%m-%d") for d in expiry_date_tuple)
    latest_expiry_date=latest_expiry_date.strftime("%Y-%m-%d")
    print("latest_expiry_date=",latest_expiry_date)
    # =========================
    # step-get value of nifty 
    # =========================
    # nifty_50_script_name="NIFTY 50"
    # nifty_50_symbol_name="NIFTY 50"
    # nifty_50_token=get_token_of_script(df_eq,nifty_50_script_name,nifty_50_symbol_name)
    # ===========================
    # step-get nifty value
    # ===========================
    # kite = KiteConnect(api_key=api_key)
    # kite.set_access_token(access_token)
    # nifty_50_quote=kite.quote(nifty_50_token)
    # nifty_50_last_price=nifty_50_quote[f"{nifty_50_token}"]["last_price"]
    # print("nifty_50_last_price=",nifty_50_last_price) 
    from get_nifty50_value import get_nifty50_value
    nifty_50_last_price={}
    nifty_50_last_price=get_nifty50_value(df_eq=df_eq)
    roundup_nifty_50_lp=round(float(nifty_50_last_price["nifty_value"]),None)
    # ========================
    # step-get atm value
    # ========================
    from get_atm_value import get_atm_value
    atm_value=get_atm_value(roundup_nifty_50_lp)
    # =======================
    # step-first strike value 
    # =======================
    # strike_info={"strike":"","strike_symbol":"","expiry_date":"","current_date":"","current_day":"","current_market_time":"","ce_token":"","ce_strike_position":"","ce_value":"","ce_oi":"","ce_change_in_oi":"","ce_change_in_oi_percentage":"","pe_token":"","pe_strike_position":"","pe_value":"","pe_oi":"","pe_change_in_oi":"","total_pcr":"","change_in_oi_pcr":""}
    first_strike_consideration_value=atm_value-500
    last_strike_consideration_value=atm_value+500
    # **************************************************************************************
    # **************************************************************************************
    # **************************************************************************************
    # =========================
    # step-drived input
    # ==========================
    strike_info={"strike":"","strike_symbol":"","expiry_date":"","current_date":"","current_day":"","current_market_time":"","ce_token":"","ce_strike_position":"","ce_value":"","ce_oi":"","ce_change_in_oi":"","ce_change_in_oi_percentage":"","ce_impliedVolatility":"","ce_ivp":"","pe_token":"","pe_strike_position":"","pe_value":"","pe_oi":"","pe_change_in_oi":"","total_pcr":"","change_in_oi_pcr":"","pe_impliedVolatility":"","pe_ivp":"","ivp":"","india_vix":"","current_iv":""}
    strike=[]
    strike_token=[]
    nifty_value_list=[]
    nifty_value_list.append(nifty_50_last_price["nifty_value"])
    
    # global dictionary_df
    # dictionary_df={}
    import shared_variable
    from get_option_strike_token import get_option_strike_token

    for i in range(first_strike_consideration_value,last_strike_consideration_value,50):
        df_example=pd.DataFrame(columns=strike_info.keys())
        shared_variable.dictionary_df.update({str(i):df_example})
        strike.append(i)
        strike_token.append(get_option_strike_token(df_ce,i,latest_expiry_date))
        strike_token.append(get_option_strike_token(df_pe,i,latest_expiry_date))
    
    # strike_token.append(nifty_50_last_price["nifty_50_token"])
    # ===========================================================
    # step-trial
    # =============================================================
    from extract_option_info_in_df import extract_option_info_in_df
    from datetime import time
    import time as t
    # today2=datetime.today
    start_time=datetime.now()
    today2=start_time.date()
    end_time=datetime.combine(today2,time(hour=23,minute=30,second=30))
    current_time=start_time
    
    from datetime import timedelta
    step_current=timedelta(seconds=150)
while True: # Infinite loop to handle total restarts
    try:
        count_of_loop = 0

        while current_time <= end_time:

            count_of_loop += 1
            # print(shared_variable.dictionary_df)
            dictionary_df_1, nifty_last_price = extract_option_info_in_df(
                strike_info,
                strike_token,
                first_strike_consideration_value,
                last_strike_consideration_value,
                latest_expiry_date,
                df_ce,
                df_pe,
                df_eq=df_eq
            )
            
            list_option_greeks=[]
            try:
               
                expiry_date_in_month_format=datetime.strptime(latest_expiry_date, "%Y-%m-%d").strftime("%d%b%Y").upper()
                list_option_greeks=get_option_greeks_from_angelone(smartapi,expiry_date_in_month_format)
            except Exception as exception:
                t.sleep(10)
                smartapi,angle_one_session=get_angle_one_smart_api_and_session()
                expiry_date_in_month_format=datetime.strptime(latest_expiry_date, "%Y-%m-%d").strftime("%d%b%Y").upper()
                list_option_greeks=get_option_greeks_from_angelone(smartapi,expiry_date_in_month_format)
                print("issue in last option greeeks")
                continue

            for i in range(first_strike_consideration_value,
                        last_strike_consideration_value, 50):

                df_output = dictionary_df_1[str(i)]
                index_count = df_output.shape[0]
                
                iv_ce=0
                iv_pe=0
                idx_1=df_output.index[index_count-1]
                df_output.loc[idx_1,"india_vix"]=str(df_historical_india_vix.iloc[-1])
                for j in list_option_greeks:
                    # t.sleep(10)
                                   
                    df_option_greeeks=pd.DataFrame([j])
                    if df_option_greeeks.iloc[0]['strikePrice']==str(i)+".000000" and df_option_greeeks.iloc[0]['optionType']=="CE":
                      df_output.loc[idx_1, "ce_impliedVolatility"]=df_option_greeeks.iloc[0]['impliedVolatility']
                      iv_ce=float(df_option_greeeks.iloc[0]['impliedVolatility'])

                    if df_option_greeeks.iloc[0]['strikePrice']==str(i)+".000000" and df_option_greeeks.iloc[0]['optionType']=="PE":
                      df_output.loc[idx_1, "pe_impliedVolatility"]=df_option_greeeks.iloc[0]['impliedVolatility']
                      iv_pe=float(df_option_greeeks.iloc[0]['impliedVolatility'])
                # t.sleep(9)


                iv_current=(float(iv_ce)+float(iv_pe))/2
                df_output.loc[idx_1, "current_iv"]=str(iv_current)
                sum_of_historical_vix_ce=(df_historical_india_vix < iv_ce).sum()
                print(sum_of_historical_vix_ce)
                sum_of_historical_vix_pe=(df_historical_india_vix < iv_pe).sum()
                print(sum_of_historical_vix_pe)
                sum_of_historical_vix_current=(df_historical_india_vix < iv_current).sum()
                print(sum_of_historical_vix_current)
                num_historical_iv=len(df_historical_india_vix)
                print(num_historical_iv)
            
                if iv_ce!=0 and df_historical_india_vix.empty==False:
                    ivp_ce_divide=sum_of_historical_vix_ce/num_historical_iv
                    ivp_ce=ivp_ce_divide* 100
                    df_output.loc[idx_1, "ce_ivp"]=str(ivp_ce)

                if iv_pe!=0 and df_historical_india_vix.empty==False:
                    ivp_pe_divide=sum_of_historical_vix_pe/num_historical_iv
                    ivp_pe = ivp_pe_divide* 100
                    df_output.loc[idx_1, "pe_ivp"]=str(ivp_pe)
                
                if iv_current!=0 and df_historical_india_vix.empty==False:
                    ivp_divided=sum_of_historical_vix_current/num_historical_iv
                    ivp=ivp_divided*100
                    df_output.loc[idx_1, "ivp"]=str(ivp)
                if index_count > 1:
                    idx = df_output.index[index_count-1]
                    prev_idx = df_output.index[index_count-2]

                    last_ce_oi  = float(df_output.loc[idx,  "ce_oi"])
                    prev_ce_oi  = float(df_output.loc[prev_idx, "ce_oi"])
                    change_oi_ce = last_ce_oi - prev_ce_oi

                    last_pe_oi  = float(df_output.loc[idx,  "pe_oi"])
                    prev_pe_oi  = float(df_output.loc[prev_idx, "pe_oi"])
                    change_oi_pe = last_pe_oi - prev_pe_oi

                    pcr_change = change_oi_pe/change_oi_ce if change_oi_ce != 0 else None

                    df_output.loc[idx, "ce_change_in_oi"] = change_oi_ce
                    df_output.loc[idx, "ce_change_in_oi_percentage"] = (change_oi_ce/prev_ce_oi)*100

                    df_output.loc[idx, "pe_change_in_oi"] = change_oi_pe
                    df_output.loc[idx, "pe_change_in_oi_percentage"] = (change_oi_pe/prev_pe_oi)*100

                    df_output.loc[idx, "change_in_oi_pcr"] = pcr_change

                    # drop last row only if BOTH are zero
                    if change_oi_ce == 0 and change_oi_pe == 0:
                        df_output.drop(df_output.index[-1], inplace=True)
                        print("drop & time=",datetime.now().strftime("%H-%M-%S"))
                    elif prev_ce_oi ==last_ce_oi and prev_pe_oi==last_pe_oi:
                        df_output.drop(df_output.index[-1], inplace=True)
                        print("drop & time=",datetime.now().strftime("%H-%M-%S"))
                df_output.to_excel(
                    rf"{output_folder_path}\{str(i)}.xlsx",
                    sheet_name=str(latest_expiry_date)
                )

            nifty_value_list.append(nifty_last_price)

            df_nifty_value = pd.DataFrame(nifty_value_list, columns=["Numbers"])
            df_nifty_value.to_excel(
                rf"{output_folder_path}\nifty_value.xlsx",
                sheet_name="nifty50",
                index=False
            )

            print("step complete=", count_of_loop,"& time=",datetime.now().strftime("%H-%M-%S"))

            t.sleep(150)
            current_time = datetime.now()

    except Exception as global_e:
            logging.error(f"Global Crash: {global_e}. Restarting entire bot in 60s...")
            t.sleep(60)

# issues to solve-exception: [Errno 13] Permission denied: 'C:\\VikasData\\KiteConnect\\temp\\tuesday\\06_01_2026_09_06_59_Pu2%\\output_folder\\26200.xlsx'                        