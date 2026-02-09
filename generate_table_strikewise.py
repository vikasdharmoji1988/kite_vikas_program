import pandas as pd
import os
import traceback
# 2026-02-10
def generate_table_strikewise(folder_path,sheet_name):
 list_file_name=[]
 for root,dir,files in os.walk(folder_path):
  for file in files:
    if file.endswith(".xlsx"):
        try:
            list_file_name.append(int(file.replace(".xlsx","")))
        except:
             pass
  list_file_name.sort()
  return list_file_name


if __name__=="__main__":
  output_folder_location=r"C:\VikasData\KiteConnect\temp\10-02-26\06_02_2026_09_19_28_Vs9&\output_folder"
  expiry_date="2026-02-10"
  list_file_names=generate_table_strikewise(output_folder_location,expiry_date)
  dict_for_keys={"strike":"0",
                 "expiry_date":"",
                 "current_date":"",
                 "current_day":"",
                 "current_market_time":"",
                 "ce_strike_position":"",
                 "ce_value":"0",
                 "ce_change_in_price_%":"",
                 "ce_change_in_oi_%":"",
                 "ce_ivp":"",
                 "ce_change_in_ivp":"",
                 "ce_iv":"0",
                 "ce_change_in_iv":"",
                 "pe_strike_position":"",
                 "pe_value":"0",
                 "pe_change_in_price_%":"",
                 "pe_change_in_oi_%":"",
                 "pe_ivp":"",
                 "pe_change_in_ivp":"",
                 "pe_iv":"0",
                 "pe_change_in_iv":"",
                 }
  for i in list_file_names: 
    excel_path=os.path.join(output_folder_location,f"{i}.xlsx")
    df_excel=pd.read_excel(excel_path,sheet_name=expiry_date)
    dict_for_keys['strike']=str(i)
    dict_for_keys['expiry_date']=df_excel.loc[df_excel.index[-1],'expiry_date']
    dict_for_keys['current_date']=df_excel.loc[df_excel.index[-1],'current_date']
    dict_for_keys['current_day']=df_excel.loc[df_excel.index[-1],'current_day']
    dict_for_keys['current_market_time']=df_excel.loc[df_excel.index[-1],'current_market_time']

  # =============================================================================================
  # ce
  # ===========================================================================================
    dict_for_keys['ce_strike_position']=df_excel.loc[df_excel.index[-1],'ce_strike_position']
    dict_for_keys['ce_value']=df_excel.loc[df_excel.index[-1],'ce_value']
    prev_ce = float(df_excel.loc[df_excel.index[-2], 'ce_value'])
    curr_ce = float(df_excel.loc[df_excel.index[-1], 'ce_value'])
    change_in_value = prev_ce - curr_ce
    if prev_ce != 0:
        change_in_value_percentage = (change_in_value / prev_ce) * 100
    else:
        change_in_value_percentage = 0  # or None
    dict_for_keys['ce_change_in_price_%']=change_in_value_percentage
    dict_for_keys['ce_change_in_oi_%']=df_excel.loc[df_excel.index[-1], 'ce_change_in_oi_percentage']

    prev_ce_ivp = float(df_excel.loc[df_excel.index[-2], 'ce_ivp'])
    curr_ce_ivp = float(df_excel.loc[df_excel.index[-1], 'ce_ivp'])
    change_in_ce_ivp = prev_ce_ivp- curr_ce_ivp
    dict_for_keys['ce_ivp']=df_excel.loc[df_excel.index[-1], 'ce_ivp']
    dict_for_keys['ce_change_in_ivp']=str(change_in_ce_ivp)
    dict_for_keys['ce_iv']=df_excel.loc[df_excel.index[-1], 'ce_impliedVolatility']
    prev_ce_iv = float(df_excel.loc[df_excel.index[-2], 'ce_impliedVolatility'])
    curr_ce_iv = float(df_excel.loc[df_excel.index[-1], 'ce_impliedVolatility'])
    change_in_ce_iv = prev_ce_iv- curr_ce_iv
    dict_for_keys['ce_change_in_iv']=str(change_in_ce_iv)
# ========================================================================================================================
# PE condition
# ========================================================================================================================
    dict_for_keys['pe_strike_position']=df_excel.loc[df_excel.index[-1],'pe_strike_position']
    dict_for_keys['pe_value']=df_excel.loc[df_excel.index[-1],'pe_value']
    prev_pe = float(df_excel.loc[df_excel.index[-2], 'pe_value'])
    curr_pe = float(df_excel.loc[df_excel.index[-1], 'pe_value'])
    change_in_pe_value = prev_pe - curr_pe
    if prev_pe != 0:
        change_in_pe_value_percentage = (change_in_pe_value / prev_pe) * 100
    else:
        change_in_pe_value_percentage = 0  # or None
    dict_for_keys['pe_change_in_price_%']=change_in_pe_value_percentage
    dict_for_keys['pe_change_in_oi_%']=df_excel.loc[df_excel.index[-1], 'pe_change_in_oi_percentage']

    prev_pe_ivp = float(df_excel.loc[df_excel.index[-2], 'pe_ivp'])
    curr_pe_ivp = float(df_excel.loc[df_excel.index[-1], 'pe_ivp'])
    change_in_pe_ivp = prev_pe_ivp- curr_pe_ivp
    dict_for_keys['pe_ivp']=df_excel.loc[df_excel.index[-1], 'pe_ivp']
    dict_for_keys['pe_change_in_ivp']=str(change_in_pe_ivp)
    dict_for_keys['pe_iv']=df_excel.loc[df_excel.index[-1], 'pe_impliedVolatility']
    prev_pe_iv = float(df_excel.loc[df_excel.index[-2], 'pe_impliedVolatility'])
    curr_pe_iv = float(df_excel.loc[df_excel.index[-1], 'pe_impliedVolatility'])
    change_in_pe_iv = prev_pe_iv- curr_pe_iv
    dict_for_keys['pe_change_in_iv']=str(change_in_pe_iv)
    print(dict_for_keys)
    # strike_info={"strike":"","strike_symbol":"",
    #               "expiry_date":"",
    #               "current_date":"",
    #                "current_day":"",
    #                "current_market_time":"",
    #                 "ce_token":"",
    #                 "ce_strike_position":"",
    #                  "ce_value":"",
    #                  "ce_oi":"",
    #                  "ce_change_in_oi":"",
    #                   "ce_change_in_oi_percentage":"",
    #                   "ce_impliedVolatility":"",
    #                    "ce_ivp":"","pe_token":"","pe_strike_position":"","pe_value":"","pe_oi":"","pe_change_in_oi":"","total_pcr":"","change_in_oi_pcr":"","pe_impliedVolatility":"","pe_ivp":"","ivp":"","india_vix":"","current_iv":""}
        #    excel_path=os.path.join(root,file)
    #    df_from_location=pd.read_excel(rf"{excel_path}",sheet_name=sheet_name)
    #    num_times=num_times+1


