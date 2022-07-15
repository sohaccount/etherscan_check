# coding: utf-8
from audioop import add
from discordwebhook import Discord
import time
import yaml
from twilio.rest import Client
from etherscan import Etherscan
import os

ut = time.time()

eth = Etherscan(os.environ["etherscan_api"])

def push_discord(content):
    discord = Discord(url=os.environ["discord_webhooks"])
    discord.post(content=content)

def add_liqudity_check(event, context):
    txns = eth.get_normal_txs_by_address(address=os.environ["address"],startblock=0,endblock=999999999,sort="asc")
    for i in txns:
        if (ut - 120) < int(i["timeStamp"]) <= ut and i["functionName"] == "addLiquidity(address tokenA, address tokenB, uint256 amountADesired, uint256 amountBDesired, uint256 amountAMin, uint256 amountBMin, address to, uint256 deadline)":
            # push_discord("流動性の追加がありました。")
            # push_discord(f'https://etherscan.io/tx/{i["hash"]}')
            emergency_call(os.environ["account_sid"], os.environ["auth_token"])

def emergency_call(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to= os.environ["to"],
        from_= os.environ["from"],
        twiml="<Response><Say>Liquidity has been added to dooar. Please check.Liquidity has been added to dooar. Please check.Liquidity has been added to dooar. Please check.Liquidity has been added to dooar. Please check.Liquidity has been added to dooar. Please check.Liquidity has been added to dooar. Please check.Liquidity has been added to dooar. Please check.</Say></Response>",
    )
    print(call.sid)