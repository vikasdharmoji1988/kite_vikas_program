import matplotlib.pyplot as plt
import pandas as pd

# input dataframe col names-
# dict_for_keys={"strike":"0",
#                  "expiry_date":"",
#                  "current_date":"",
#                  "current_day":"",
#                  "current_market_time":"",
#                  "ce_strike_position":"",
#                  "ce_value":"0",
#                  "ce_change_in_price_%":"",
#                  "ce_change_in_oi_%":"",
#                  "ce_ivp":"",
#                  "ce_change_in_ivp":"",
#                  "ce_iv":"0",
#                  "ce_change_in_iv":"",
#                  "pe_strike_position":"",
#                  "pe_value":"0",
#                  "pe_change_in_price_%":"",
#                  "pe_change_in_oi_%":"",
#                  "pe_ivp":"",
#                  "pe_change_in_ivp":"",
#                  "pe_iv":"0",
#                  "pe_change_in_iv":"",
#                  }
  
def plot_strike_vs_per_change_in_ce(df_input:pd.DataFrame,ce_oi_threshold):
    df_strike=df_input[df_input['strike']!=0]
    list_of_num_ce_col=["ce_change_in_oi_%"]
    df_input["ce_change_in_oi_%"]=pd.to_numeric(df_input["ce_change_in_oi_%"],errors="coerce")
    plt.figure()
    plt.plot(df_strike['strike'],df_input["ce_change_in_oi_%"])
    plt.xlabel("strike")
    plt.ylabel("ce_change_in_%")
    plt.title("strike vs ce change in %")
    plt.grid()
    plt.show()

if __name__=="__main__":
     output_folder_location=r"C:\VikasData\KiteConnect\temp\10-02-26\06_02_2026_09_19_28_Vs9&\output_folder"
     expiry_date="2026-02-10"
     from create_df_of_last_values import create_df_of_last_values
     df_1=create_df_of_last_values(output_folder_location,expiry_date)
     plot_strike_vs_per_change_in_ce(df_1,10)
 
    # """
    # Generates and saves option analysis graphs.

    # Features:
    # - Combined CE & PE graphs
    # - ATM vertical line
    # - Threshold highlight
    # - Separate ITM charts
    # - Auto folder creation
