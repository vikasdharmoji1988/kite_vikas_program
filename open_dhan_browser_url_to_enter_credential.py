import sys
sys.path.append(r'C:\VikasData\KiteConnect\OUT')
import webbrowser
import threading 
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import threading
import webbrowser

# ---------------- Callback Server ----------------

class DhanCallbackHandler(BaseHTTPRequestHandler):
    token_id = None

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)

        if "tokenId" in query:
            DhanCallbackHandler.token_id = query["tokenId"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                b"Login successful. You can close this tab."
            )
        else:
            self.send_response(400)
            self.end_headers()

# ---------------- Start Server ----------------

def start_server():
    server = HTTPServer(("localhost", 8000), DhanCallbackHandler)
    server.handle_request()   # waits for ONE redirect only

def open_dhan_brower_url_to_enter_credential(consentappid):
 try:
#   t = threading.Thread(target=start_server)
#   t.start()
    # Start server in background
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    webbrowser.open("https://auth.dhan.co/login/consentApp-login?consentAppId="+consentappid)
  # Wait until redirect happens
    server_thread.join()
    # Final result
    return DhanCallbackHandler.token_id
 except Exception as e:
  print("error in open_dhan_brower_url_to_enter_credential:",e)
if __name__=="__main__":
    from get_dhan_client_id_api_key_api_secret import get_dhan_client_id_api_key_api_secret
    client_id,api_key,api_secret=get_dhan_client_id_api_key_api_secret()
    from dhan.get_dhan_consentappid import generate_dhan_consentappid
    dhan_consent_id=generate_dhan_consentappid(api_key.strip(),api_secret.strip(),client_id.strip())
    token_id=open_dhan_brower_url_to_enter_credential(dhan_consent_id)
    print(token_id)

