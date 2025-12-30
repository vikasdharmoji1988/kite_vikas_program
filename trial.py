from datetime import datetime 

today1=datetime.today()
# today1.isoformat
d=today1.strftime("%Y-%m-%d")
dt=datetime.strptime(d,"%Y-%m-%d")
week_day=today1.strftime("%A")
day_time_hours=today1.hour
print(day_time_hours)