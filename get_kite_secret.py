from kiteconnect import KiteConnect
def get_kite_secret():
    base_folder=r"C:\VikasData\KiteConnect\OUT\Chatpter_1_UseFul_API\Step_1_Automatically_login_kite"
    access_token = str(open(rf'{base_folder}\access_token.txt','r').read())
    key_secret = open(rf'{base_folder}\api_key_0625.txt','r').read().split()
    # key_secret = str(open(rf'{base_folder}\api_key_0625.txt','r').read())
    # print(key_secret)
    api_key2=str(key_secret[0])
    return access_token,api_key2
if __name__=="__main__":
    access_token,api_key=get_kite_secret()
    print(access_token)
    print(api_key)
      

