from create_folder import create_folder
from create_date_time_str import create_date_time_str
from get_unique_character_str import get_unique_character_str
from get_kite_secret import get_kite_secret
from list_all_instrument_script import get_instruments
from save_in_txt_file import save_in_txt_file
from save_list_in_csv import save_list_to_csv
import openpyxl
import pandas as pd
def get_instrument_data(access_token,working_path):
    try:
        #=======================
        #step-get all instrument in txt
        #======================
        data_instrument = get_instruments(access_token)
        # =====================
        # step-save instrument data in txt file
        # ==================
        instrument_folder_path=rf"{working_path}\instrument_list"
        x=create_folder(instrument_folder_path)
        input_txt_file_path=rf"{instrument_folder_path}\instrument_list.txt"
        instrument_list_txt_file_path=save_in_txt_file(data_instrument,input_txt_file_path)
        print("txt_file_path=",instrument_list_txt_file_path)
        # ==========================
        # step-convert data into df in xlsx
        # ==========================
        df_instrument=pd.read_csv(instrument_list_txt_file_path)
        df_instrument.to_excel(rf"{instrument_folder_path}\instrument_list.xlsx",sheet_name="instrument",index=None)
        # print(df_instrument.head())
        #==========================
        # step-get data frame of ce & txt file & .xlsx of it
        # =========================
        df_ce=df_instrument[df_instrument['instrument_type']=="CE"].copy()
        df_ce.to_excel(rf"{instrument_folder_path}\df_ce.xlsx",sheet_name="instrument",index=None)
        #=================================
        # step-get data frame of pe & txt file & .xlsx of it
        #=================================
        df_pe=df_instrument[df_instrument["instrument_type"]=="PE"].copy()
        df_pe.to_excel(rf"{instrument_folder_path}\df_pe.xlsx",sheet_name="instrument",index=None)
        # =============================
        # step-get data from of fut
        # =============================
        df_fut=df_instrument[df_instrument["instrument_type"]=="FUT"].copy()
        df_fut.to_excel(rf"{instrument_folder_path}\df_fut.xlsx",sheet_name="instrument",index=None)
        # ===========================
        # step-get data from eq
        # ==========================
        df_eq=df_instrument[df_instrument["instrument_type"]=="EQ"].copy()
        df_eq.to_excel(rf"{instrument_folder_path}\df_eq.xlsx",sheet_name="instrument",index=None)
    except Exception as e:
        print("Error_num-1006: error in get_instrument_data",e)
    else:
        return df_instrument,df_ce,df_pe,df_eq,df_fut

if __name__=="__main__":
    # Error_num-1006: error in create_date_time_unique_str
    # ======================
    # create folder
    # ======================
    base_folder_path=r"C:\VikasData\KiteConnect\temp"
    date_time_str= create_date_time_str()
    already_exist=()
    unique_char=get_unique_character_str(already_exist,1,1,1,1)
    base_folder_name=rf"{date_time_str}_{unique_char}"
    working_path=rf"{base_folder_path}\{base_folder_name}"
    x=create_folder(working_path)
    print("base_folder=",x)
    #=======================
    #step-access_token & api_key
    #=======================
    access_token,api_key=get_kite_secret()
    # =======================
    # step-get data_frame
    # ===================
    df_instrument,df_ce,df_pe,df_eq,df_fut=get_instrument_data(access_token,working_path)