import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
import pandas as pd
def get_dhan_option_chain(dhan_session,security_id,exchange_segment,expiry_date_yy_mm_dd):
    try:
      dic_option_chain=dhan_session.option_chain(under_security_id=security_id,under_exchange_segment=exchange_segment,expiry=expiry_date_yy_mm_dd)
      # dic_nifty_option_chain=get_dhan_option_chain(dhan_session,13,"IDX_I","2026-02-03")
      # dic_option_chain=dic_nifty_option_chain['data']['oc']
      return dic_option_chain ['data'] ['data']
    except Exception as e:
      print("issue in get_dhan_option_chain",e)

if __name__=="__main__":
    from get_dhan_client_id_api_key_api_secret import get_dhan_client_id_api_key_api_secret
    client_id,api_key,api_secret=get_dhan_client_id_api_key_api_secret()

    # from get_dhan_consentappid import get_dhan_consentappid
    # dhan_consent_id=get_dhan_consentappid(api_key.strip(),api_secret.strip(),client_id.strip())

    # from open_dhan_browser_url_to_enter_credential import open_dhan_brower_url_to_enter_credential
    # token_id=open_dhan_brower_url_to_enter_credential(dhan_consent_id)
    
    # from get_dhan_access_token import get_dhan_access_token
    # dhan_access_token=get_dhan_access_token(token_id,api_key,api_secret)
    
    dhan_access_token=open(r"C:\VikasData\KiteConnect\OUT\dhan\dhan_access_token.txt").read()
    
    from get_new_dhan_session import get_new_dhan_session
    dhan_session=get_new_dhan_session(client_id,dhan_access_token)
    dic_nifty_option_chain=get_dhan_option_chain(dhan_session,13,"IDX_I","2026-02-03")
    dic_dhan_option_valuewise=dic_nifty_option_chain['oc']['19800.000000']['ce']['implied_volatility']
    # df_dhan_nifty_option=pd.DataFrame(dic_dhan_option_valuewise)

    print(dic_dhan_option_valuewise)

# print(dict_1['data'])