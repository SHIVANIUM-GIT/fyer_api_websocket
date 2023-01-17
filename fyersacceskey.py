from datetime import date
from fyers_api import fyersModel
from fyers_api import accessToken
import os
from dotenv import load_dotenv
from fyers_api.Websocket import ws

load_dotenv()


client_id = os.getenv('client_id')
secret_key = os.getenv('secret_key')
redirect_uri = os.getenv('redirect_uri')

today = date.today().strftime("%Y-%m-%d")


def get_access_token():
    access = ""
    if not os.path.exists("./authcode"):
        print("Creating authcode directory")
        os.makedirs("./authcode")

    if not os.path.exists(f"authcode/{today}.txt"):
        session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key,
                                           redirect_uri=redirect_uri, response_type="code", grant_type="authorization_code")
        response = session.generate_authcode()
        print("Login Url : ", response)
        auth_code = input("Enter Auth Code : ")
        session.set_token(auth_code)
        access_token = session.generate_token()["access_token"]
        with open(f"authcode/{today}.txt", "w") as f:
            f.write(access_token)
    else:
        with open(f"authcode/{today}.txt", "r") as f:
            access = f.read()
    return access


access_token = get_access_token()


fyers = fyersModel.FyersModel(
    client_id=client_id, token=access_token, log_path=os.getcwd())

print(fyers.get_profile())
# print(fyers.funds())
# print(fyers.holdings())

newToken = f"{client_id}:{access_token}"
symbol = ['NSE:NIFTYBANK-INDEX']
cws = ws.FyersSocket(access_token=newToken,
                     run_background=False, log_path=os.getcwd())


def on_ticks(msg):
    ltp = msg[0]['ltp']
    high = msg[0]['high_price']
    low = msg[0]['low_price']
    print(f"ltp:{ltp},HIGH:{high},LOW:{low}")


cws.websocket_data = on_ticks
cws.subscribe(symbol=symbol, data_type="symbolData")
cws.keep_running()
# cws.unsubscribe(symbol=symbol)
