from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        """
        Initialize Binance client for testnet.
        """
        self.client = Client(api_key, api_secret, testnet=True)

    
    def place_market_order(self, symbol, side, quantity):
        """
        Place a Market order.
        """
        order = self.client.futures_create_order(
            symbol = symbol,
            side = side,
            type = "MARKET",
            quantity = quantity
        )
        return order
    
    def place_limit_order(self, symbol, side, quantity, price):
        """
        Place a LIMIT order
        """
        order = self.client.futures_create_order(
            symbol = symbol,
            side = side,
            type = "LIMIT",
            quantity = quantity,
            price = price,
            timeInForce = "GTC"
        )
        return order