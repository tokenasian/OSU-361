import requests

BASE_URL = "https://paper-api.alpaca.markets/v2/"

API_KEY = ""
SECRET_KEY = ""


def place_order(api_key, secret_key, symbol, quantity, side):  # buy or sell order function
    url = BASE_URL + "orders"

    payload = {
        "symbol": symbol,
        "qty": quantity,
        "side": side,
        "type": "market",
        "time_in_force": "day"
    }

    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def get_open_buy_orders(api_key, secret_key): # buy function
    url = BASE_URL + "orders"

    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orders = response.json()
        return [order for order in orders if order["side"] == "buy"]
    else:
        print(f"Error fetching open orders. Status code: {response.status_code}")
        return None


def get_open_sell_orders(api_key, secret_key): # sell function
    url = BASE_URL + "orders"
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orders = response.json()
        return [order for order in orders if order["side"] == "sell"]
    else:
        print(f"Error fetching open orders. Status code: {response.status_code}")
        return None


def delete_order(api_key, secret_key, order_id): # delete by id
    url = BASE_URL + f"orders/{order_id}"
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key
    }
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Successfully canceled the order with the ID {order_id}")
    else:
        print(f"Error canceling the order with the ID {order_id}. Status code: {response.status_code}")


def get_open_positions(api_key, secret_key):
    url = BASE_URL + "positions"
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_open_orders(api_key, secret_key):
    url = BASE_URL + "orders"
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        orders = response.json()
        if not orders:
            print("No open orders.")
        else:
            print("Open Orders:")
            for order in orders:
                print(order)
        return orders
    else:
        print(f"Error fetching open orders. Status code: {response.status_code}")
        return None


def get_account_positions(api_key, secret_key):
    url = BASE_URL + "positions"
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def wrapper_function(api_key, secret_key):
    while True:
        request_type = input("Enter a request ('buy', 'sell', 'positions', 'orders', 'cancel_buy', 'cancel_sell', "
                             "or 'exit' to quit): ")
        if request_type == "exit":
            break
        elif request_type in ["buy", "sell"]:
            symbol = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            result = place_order(api_key, secret_key, symbol, quantity, request_type)
            print("Response:")
            print(result)
        elif request_type == "positions":
            result = get_account_positions(api_key, secret_key)
            print("Account Positions:")
            print(result)
        elif request_type == "orders":
            get_open_orders(api_key, secret_key)
        elif request_type == "cancel_buy":
            open_orders = get_open_orders(api_key, secret_key)
            if open_orders:
                print("Open orders found. Cancelling as requested...")
                for order in open_orders:
                    delete_order(api_key, secret_key, order['id'])
            else:
                print("No open orders to cancel.")
        elif request_type == "cancel_sell":
            open_sell_orders = get_open_sell_orders(api_key, secret_key)
            if open_sell_orders:
                print("Open sell orders found. Cancelling as requested...")
                for order in open_sell_orders:
                    delete_order(api_key, secret_key, order['id'])
            else:
                print("No open sell orders to cancel.")
        else:
            print("Invalid request.")


if __name__ == "__main__":
    api_key_outer = API_KEY
    secret_key_outer = SECRET_KEY

    wrapper_function(api_key_outer, secret_key_outer)
