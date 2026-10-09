  Since this is the bit of creativity that I get to play around with I tend to go a little to far with these, but here is another one.  I have, over the last 3 months been working on pricing algorithms for prediction markets (These are still slightly guerilla-esc and you can hunt for large spread and alpha pretty easily), and we are talking computations that need to take place in microseconds so as to not get screwed over by new orders in a market.  I got the math part, with different bespoke binary pricing kernels and whatnot but it took me a while to figure out what most might think is the easiest part, which is the simple yes or no logic gates, as to whether or not to send a buy or a sell order.  A theme in the work I do is I tend to put the carriage infront of the horse.

    This is the Order Gatekeeper. Prediction markets have yes or no contracts where the payout is either 100 cents if the event actually happens or 0 if the event doesn't, and for NO contracts the inverse is true.  These contracts trade at whole cents where prices are inclusive from 1 to 99 cents.  At any given moment the market has a "best bid" which is the highest price someone is willing to pay, and a "best ask", which is the lowest price anyone is willing to sell at.

    A.) Write a check_order(side, price, best_bid, best_ask) function where 'side' is 'buy' or 'sell',(This is guaranteed to happen), and 'price' is an int in cents (Which is not quite guaranteed to be valid.). 'best_bid', and 'best_ask' are ints that are guaranteed to satisfy that:

        1<= best_bid < best_ask <=99

    This check_order function will return one of five strings:

        'rejected' this is because price is either below 1 or above 99 (MAKE SURE TO CHECK THIS FIRST)

        'trades immediately' this is a sell at or below the best bid or a buy at or above the best ask

        'new best price'  this is a buy or sell order strickly between our best_bid and best_ask

        'ties best price' this is a buy exactly at best_bid, or a sell order at exactly the best_ask

        'worse than best price' this gives us a buy at strickly below best_bid or a sell order at strickly above best_ask

    Every single valid input must return exactly one of these finve strings, and no combination of inputs must fall through without a return.

    B.) Next, buying a NO at a price q, is the same as salling a YES at 100 - q.  Same goes for selling a NO at q, which is equivalent as buying a YES at 100 - q.  

    Write a check_no_order(side, price, best_bid, best_ask) function where "side" describes the NO order and best_bid and best_ask describe the YES market.  This will return the five conditions as above, and this is only done by calling the same check_order rather than writing a completely new bit of comparison logic.

    C.) Prove atleast 4 different test cases so that no single wrong implimentation (A flipped inequality, a missing branch, or validation performed last) passes all of them.  

    ANSWER KEY:

| call | expected |
|---|---|
| `check_order('buy', 47, 44, 47)` | `'trades immediately'` |
| `check_order('buy', 44, 44, 47)` | `'ties best price'` |
| `check_order('sell', 44, 44, 47)` | `'trades immediately'` |
| `check_order('buy', 0, 44, 47)` | `'rejected'` |
| `check_no_order('buy', 53, 44, 47)` | `'ties best price'` |

went deep into my md syntax bag for this for this one.  The table was the hardest part out of all of this, and my experience with using obsidian has taught me how.  

These are just some arbitrary values that my roommate gave me.  

Now, this question will assess whether someone can translate specificiations into a multi branch conditionals tree.  The mirrored buy or sell ladders from the last problem I wrote, the explicit boundaries, and the extensive coverage so that nothing gets through the cracks. Now this is framed with finance jargon that might scare some poeple but this really requires no market knowledge seeing as every term is defined in the prompt, and the difficulty is entirely the conditionals structure.  This was my choice because experience has taught me brutally how conditionals break, with paths returning nothing, branches that are falsley made exclusive.

Now I envision the hardest part of this being part B where wrong solutions will differ from right ones at exact boundary prices(Those being the >= vs > at the ask), and that is why in part c I asked for some targeted tests rather than just examples.  Now, in part be there might be a slight tempation to write a third ladder, and the insigh is that a NO order can reduce to a solved YES order by the 100 - q trick.  Overcoming these will teach state boundaries for sure, the ability to cover every single path and case, and reduction instead of duplication.  
