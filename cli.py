import argparse

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import get_logger
from bot.client import BinanceClient
from config import API_KEY, API_SECRET

logger = get_logger()

client = BinanceClient(API_KEY, API_SECRET)


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol",required=True)
    parser.add_argument("--side",required=True)
    parser.add_argument("--type",required=True)
    parser.add_argument("--quantity",type=float, required=True)
    parser.add_argument("--price",type= float)

    args = parser.parse_args()
    
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price

    try:
        #Validate Inputs
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        logger.info(f"Order Request: {symbol} {side} {order_type} {quantity} {price}")

        print("\nOrder Request Summary")
        print("---------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)
        print("Price:", price)

        #Execute Order
        if order_type == "MARKET":
            response = client.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.place_limit_order(
                symbol= symbol,
                side= side,
                quantity= quantity,
                price= price
            )
        
        logger.info(f"API Response : {response}")

        print("\nOrder Response")
        print("------------------------")

        print("Order ID: ", response.get("orderId"))
        print("Status: ", response.get("status"))
        print("Executed Qty: ", response.get("executedQty"))
        print("Average Price: ", response.get("avgPrice"))

        print("\nOrder placed successfully!")

    except Exception as e:

        logger.error(f"Error occurred: {str(e)}")

        print("\nOrder failed!")
        print("Error:", str(e))


if __name__ == "__main__":
    main()
