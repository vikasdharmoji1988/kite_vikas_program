import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
import requests

# reference-
# curl --location 'https://auth.dhan.co/app/consumeApp-consent?tokenId={Token ID}' \
# --header 'app_id: {API Key}' \
# --header 'app_secret: {API Secret}'

def get_dhan_access_token(tokenId,api_id,api_secret):
    str_url="https://auth.dhan.co/app/consumeApp-consent"

    dict_params={
        "tokenId":tokenId
        }
    
    dict_headers={
        "app_id":api_id,
        "app_secret":api_secret
    }

    request_response=requests.get(url=str_url,params=dict_params,headers=dict_headers)
    if request_response.status_code!=200:
        print("issue in get_dhan_access_token",request_response.raise_for_status)
    else:
        access_token=get_dhan_access_token(token_id,api_key,api_secret)
        return access_token
        


if __name__=="__main__":
    from get_dhan_client_id_api_key_api_secret import get_dhan_client_id_api_key_api_secret
    client_id,api_key,api_secret=get_dhan_client_id_api_key_api_secret()

    from get_dhan_consentappid import get_dhan_consentappid
    dhan_consent_id=get_dhan_consentappid(api_key.strip(),api_secret.strip(),client_id.strip())

    from open_dhan_browser_url_to_enter_credential import open_dhan_brower_url_to_enter_credential
    token_id=open_dhan_brower_url_to_enter_credential(dhan_consent_id)
    
    dhan_access_token=get_dhan_access_token(token_id,api_key,api_secret)
    with open(r"C:\VikasData\KiteConnect\OUT\dhan\dhan_access_token.txt","w") as f:
        f.wite(dhan_access_token)
    
