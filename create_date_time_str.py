from datetime import datetime


def create_date_time_str():
    try:
        today1=datetime.today()
        strday=today1.strftime("%d_%m_%Y")
        nowtime1=datetime.now()
        time_str=nowtime1.strftime("%H_%M_%S")
        str=f"{strday}_{time_str}"
    except Exception as e:
        print("Error_num-1002: error in create_date_time_unique_str:",e)
    else:
        return str
if __name__=="__main__":
   yz=create_date_time_str()
   print(yz)