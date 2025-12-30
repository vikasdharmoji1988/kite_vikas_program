# import os
# script_path = os.path.abspath(__file__)
# project_folder = os.path.dirname(script_path)
# output_file= project_folder+"\\"+'all_instrument_list.txt'
# print(output_file)

def get_atm_value(script_value):   
    nifty_value_in_str=str(script_value)
    nifty_last_two_digit=int(nifty_value_in_str[-2:])
    nifty_first_three_digit=nifty_value_in_str[0:3]+"00"
    atm_value=0
    if nifty_last_two_digit<25 and nifty_last_two_digit >0 :
     atm_value=int(nifty_first_three_digit)
    
    if nifty_last_two_digit<50 and nifty_last_two_digit >25 :
     atm_value=int(nifty_first_three_digit)+50
    
    if nifty_last_two_digit>50 and nifty_last_two_digit <75 :
     atm_value=int(nifty_first_three_digit)+50

    if nifty_last_two_digit>75:
     atm_value=int(nifty_first_three_digit)+100
    
    if nifty_last_two_digit==0:
     atm_value=int(nifty_first_three_digit)
    if nifty_last_two_digit==50:
     atm_value=int(nifty_first_three_digit)+50

    if nifty_last_two_digit==25:
     atm_value=int(nifty_first_three_digit)
    if nifty_last_two_digit==50:
     atm_value=int(nifty_first_three_digit)+100
    
    return atm_value

if __name__=="__main__":
 atm_value=get_atm_value(23350)
 print(atm_value)
