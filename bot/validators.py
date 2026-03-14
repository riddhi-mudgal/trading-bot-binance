def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty")
    
def validate_side(side):
    valid_sides = ["BUY","SELL"]
    if side not in valid_sides:
        raise ValueError(f"Side must be one of {valid_sides}")
    
def validate_order_type(order_type):
    valid_types = ["MARKET","LIMIT"]
    if order_type not in valid_types:
        raise ValueError(f"Order type must be one of {valid_types}")

def validate_quantity(quantity):
    if quantity < 0:
        raise ValueError("Quantity must be greater than 0")

def validate_price(price,order_type):
    if order_type=="LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")
    