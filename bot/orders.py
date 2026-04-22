import logging

logger = logging.getLogger(__name__)

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = client.futures_create_order(**params)

        
        logger.info(
            f"Order placed successfully | "
            f"ID: {response.get('orderId')} | "
            f"Status: {response.get('status')} | "
            f"Symbol: {response.get('symbol')}"
        )

        logger.debug(f"Full response: {response}")

        return response

    except Exception as e:
        logger.error(
            f"Order failed | Symbol: {symbol} | Side: {side} | "
            f"Type: {order_type} | Error: {str(e)}"
        )
        raise