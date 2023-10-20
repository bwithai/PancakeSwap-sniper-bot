from web3 import Web3
from web3.middleware import geth_poa_middleware
import asyncio
# import config
import time

# add your blockchain connection information
bsc = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))

transaction_info = web3.eth.get_transaction("0x89383df09d52f2245fd7cb2c22617f00a0f0295baf097c33ac21015cb3de3d68")
print(transaction_info)
value_wei = int(transaction_info['value'])
bnb_price_in_wei = 1e18  # 1 BNB in wei
value_bnb = value_wei / bnb_price_in_wei
print(f"Value (in BNB): {value_bnb} BNB")

Token0= "0x55d398326f99059fF775485246999027B3197955"
Token1= "0xD0955d41CC657923B8Ff395A480734a4F45ffb7c"
liquidity_pool_address= "0xe3547388f28dB087565184cc7F9bb8Ce6a38613a"
transactionHash = "0xfb36192745e3e304accfedd9b67a6d4eddb8fad123706d658111623d114a621b"