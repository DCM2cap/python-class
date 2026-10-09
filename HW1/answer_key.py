#Just as a brief not, I have been doing alot of work building High frequency trading systems so this is the first thing that came to me.  I have done a bunch of work in this realm previously

#answer key

FAIR_VALUE = 10237
HALF_SPREAD = 15
TICK_SIZE = 25


def up_to_tick(price, tick):
    return ((price + tick - 1) // tick) * tick
    # Adding the tick - 1 pushes any price not on a tick up to the next, so the floor division lands on it.  A price on a tick doesn"t touch it.  This is the kicker here and if not added it blows up.

bid = ((FAIR_VALUE - HALF_SPREAD) // TICK_SIZE) * TICK_SIZE
ask = up_to_tick(FAIR_VALUE + HALF_SPREAD, TICK_SIZE)

print('Bid: ' + str(bid))
print('Ask: ' + str(ask))
print('Spread: ' + str(ask - bid))