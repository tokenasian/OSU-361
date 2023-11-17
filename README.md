# Alpaca Trading Microservice Communication Contract

The README guidelines below contains instructions for programmatically requesting and receiving data from the microservice. 

**Requesting Data**

To programmatically request data from the Alpaca Microservice, you can use the provided Python functions in the `alpaca_trading.py` file. 

```
from alpaca_trading import place_order

api_key = ""
secret_key = ""
symbol = "AAPL"  # example stock
quantity = 10    # example quantity
side = "buy"     # 'buy' or 'sell' based on your trade type

result = place_order(api_key, secret_key, symbol, quantity, side)
print("Response:")
print(result)
```

**Receiving Data**

The Alpaca Microservice provides functions to retrieve open positions, open orders, and more `alpaca_trading.py` file. 

```
from alpaca_trading import get_account_positions

api_key = ""
secret_key = ""

result = get_account_positions(api_key, secret_key)
print("Account Positions:")
print(result)
```
