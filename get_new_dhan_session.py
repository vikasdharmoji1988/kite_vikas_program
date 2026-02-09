import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
from dhanhq import dhanhq
from dhanhq import marketfeed
from dhanhq import orderupdate
# from dhanhq import DhanContext, dhanhq
import requests
import webbrowser
import pandas as pd

# list_dhan=open(r"C:\VikasData\KiteConnect\OUT\dhan\dhan_login.txt","r").read()

# client_id=str(list_dhan[0]).split("=")[1]
def get_new_dhan_session(clent_id,access_token):
    try:
     dhan_session = dhanhq(clent_id,access_token)
     return dhan_session
    except Exception as e:
     print("issue in get_new_dhan_session",e)

if __name__=="__main__":
    from get_dhan_client_id_api_key_api_secret import get_dhan_client_id_api_key_api_secret
    client_id,api_key,api_secret=get_dhan_client_id_api_key_api_secret()

    from dhan.get_dhan_consentappid import generate_dhan_consentappid
    dhan_consent_id=generate_dhan_consentappid(api_key.strip(),api_secret.strip(),client_id.strip())

    from open_dhan_browser_url_to_enter_credential import open_dhan_brower_url_to_enter_credential
    token_id=open_dhan_brower_url_to_enter_credential(dhan_consent_id)
    
    from get_dhan_access_token import get_dhan_access_token
    dhan_access_token=get_dhan_access_token(token_id,api_key,api_secret)
    dhan_session=get_new_dhan_session(client_id,dhan_access_token)

  
#  dhan_session = dhanhq("1110046774","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzY5NTE0Mzg0LCJpYXQiOjE3Njk0Mjc5ODQsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTEwMDQ2Nzc0In0.CI27Ue_e0gZIkC1G4atks1-jWmXhaEJ4MJFNPqOxFCCL-N1rLYvGVlsnGnyH_HIeJqYXjxqpnARHuZfXU6GQ_A")
# dict_1=dhan_context.option_chain(under_security_id=13,under_exchange_segment="IDX_I",expiry="2026-01-27")
# print(dict_1['data'])

# df_dhan_option_chain=pd.DataFrame(dict_1['data'])
# Quick connectivity test
# profile = dhan_context.get_fund_limits()
# print(df_dhan_option_chain)
# dhan = dhanhq(dhan_context)