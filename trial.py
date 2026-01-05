from datetime import datetime 
import pandas as pd
today1=datetime.today()
# today1.isoformat
d=today1.strftime("%Y-%m-%d")
dt=datetime.strptime(d,"%Y-%m-%d")
week_day=today1.strftime("%A")
day_time_hours=today1.hour
print(day_time_hours)

atm_value=26300
    # =========================
    # step-data frame
    # ==========================
strike_info={"strike":"","strike_symbol":"","expiry_date":"","current_date":"","current_day":"","current_market_time":"","ce_token":"","ce_strike_position":"","ce_value":"","ce_oi":"","ce_change_in_oi":"","ce_change_in_oi_percentage":"","pe_token":"","pe_strike_position":"","pe_value":"","pe_oi":"","pe_change_in_oi":"","total_pcr":"","change_in_oi_pcr":""}
first_strike_consideration_value=atm_value-500
last_strike_consideration_value=atm_value+500
strike=[]
dictionary_df={}
for i in range(first_strike_consideration_value,last_strike_consideration_value,50):
    df_example=pd.DataFrame(columns=strike_info.keys())
    dictionary_df.update({str(i):df_example})
print(dictionary_df)