"""
The Order Gatekeeper
"""


def check_order(side, price, best_bid, best_ask):
    """
    Goal is to check what a limit order is relative to the current best bid and ask.
    
    Your inputs:
      side: str, a 'buy' or 'sell'
      price: int, order price in cents (not guaranteed to be valid)
      best_bid, best_ask: ints, guaranteed 1 <= best_bid < best_ask <= 99
    Your outputs:
      Five str: 'rejected', 'trades immediately',
      'new best price', 'ties best price', 'worse than best price'
    """
    if price < 1 or price > 99:
        return 'rejected'
    if side == 'buy':
        if price >= best_ask:
            return 'trades immediately'
        elif price > best_bid:
            return 'new best price'
        elif price == best_bid:
            return 'ties best price'
        else:
            return 'worse than best price'
    else:
        if price <= best_bid:
            return 'trades immediately'
        elif price < best_ask:
            return 'new best price'
        elif price == best_ask:
            return 'ties best price'
        else:
            return 'worse than best price'


def check_no_order(side, price, best_bid, best_ask):
    """
    Converting a NO order by turning it into its equivalent
    YES order.  Basically, buying a NO at q is selling YES at 100 - q, and the inverse is true where
    selling NO at q is buying YES at 100 - q.

    Inputs and outputs are the exact same as check_order, except side
    describes the NO order while best_bid/best_ask still describe
    the YES market.
    """
    if side == 'buy':
        return check_order('sell', 100 - price, best_bid, best_ask)
    else:
        return check_order('buy', 100 - price, best_bid, best_ask)