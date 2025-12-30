import os
import pandas as pd
# *****************
# step-get common_path parameter
common_path=r'C:\VikasData\KiteConnect\OUT'
# *****************
# step-path of common csv of all instrument
universal_csv_path=common_path+r'\all_instrument_list.csv'
#*******************
#step-convert csv to data frame
df_instrument=pd.read_csv(filepath_or_buffer=universal_csv_path)
#*******************
#step-to get number of instrument type
instrument_type=df_instrument['instrument_type'].unique()
#********************
#step-to create df of equity instrument type only
df_eq=pd.DataFrame(columns=df_instrument.columns)
num_instance=0
req_num_instance=0
# print(df_eq)
for x in df_instrument['instrument_type']:
  if x=='EQ':
     req_num_instance=req_num_instance+1
     df_eq.loc[len(df_eq)]=df_instrument.iloc[num_instance].values
  if x=='':
     break
  num_instance=num_instance+1
print('done')
  

