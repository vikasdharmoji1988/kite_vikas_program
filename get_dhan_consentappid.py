import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
from dhanhq import dhanhq
from dhanhq import marketfeed
from dhanhq import orderupdate
import sys
# from dhanhq import DhanContext, dhanhq
import requests
import webbrowser


# list_dhan=open(r"C:\VikasData\KiteConnect\OUT\dhan\dhan_login.txt","r").read()

# client_id=str(list_dhan[0]).split("=")[1]

# dhan_context = DhanContext("client_id","access_token")
# dhan = dhanhq(dhan_context)


# dhanhq.dhanhq

# print(list_dhan)
def get_dhan_consentappid(app_id,api_secret,client_id):
    try:
        url="https://auth.dhan.co/app/generate-consent"
        params={
            "client_id":str(client_id)
            
        }
        header={
            "app_id":str(app_id),
            "app_secret":str(client_id)
        }
        dhan_request=requests.post(url=url,params=params,headers=header,timeout=10)
        if dhan_request.status_code!=200:
            # raise Exception(f"HTTP {dhan_request.status_code}: {dhan_request.text}")
            return "error in generate_dhan_consentappid:" f"HTTP {dhan_request.status_code}: {dhan_request.text}"
        else:          
            data=dhan_request.json()
            return data['consentAppId']
    except Exception as e:
            print ("error in generate_dhan_consentappid:",e)
            sys.exit()

if __name__=="__main__":
    from get_dhan_client_id_api_key_api_secret import get_dhan_client_id_api_key_api_secret
    client_id,api_key,api_secret=get_dhan_client_id_api_key_api_secret()
    dhan_consent_id=get_dhan_consentappid(api_key.strip(),api_secret.strip(),client_id.strip())
    print(dhan_consent_id)
  
# dhan_login = DhanLogin("YOUR_CLIENT_ID")
# app_id = "YOUR_APP_ID"
# app_secret = "YOUR_APP_SECRET"

# # Step 1: Generate Consent and Open Browser for Login
# consent_id = dhan_login.generate_login_session(app_id, app_secret)

# # Step 2: Consume Token ID (After user logs in and gets Token ID from redirect URL)
# token_id = "TOKEN_ID_FROM_REDIRECT_URL"
# access_token = dhan_login.consume_token_id(token_id, app_id, app_secret)
# print(access_token)