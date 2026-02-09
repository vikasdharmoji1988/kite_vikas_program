import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
from dhanhq import dhanhq
from dhanhq import marketfeed
from dhanhq import orderupdate
# from dhanhq import DhanContext, dhanhq
import requests
import webbrowser

def get_dhan_client_id_api_key_api_secret():
    list_dhan=[]
    with open(r"C:\VikasData\KiteConnect\OUT\dhan\dhan_login.txt","r",encoding="utf-8") as f:
     list_dhan=f.read().splitlines()
    client_id=str(list_dhan[0]).split("=")[1]
    api_key=str(list_dhan[1]).split("=")[1]
    api_secret=str(list_dhan[2]).split("=")[1]
    return client_id,api_key,api_secret




# print(api_key)
# print(api_secret)
# # dhan_context = DhanContext("client_id","access_token")
# dhan = dhanhq(dhan_context)


# dhanhq.dhanhq
