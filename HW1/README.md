------------------------------------------------ END OF DEFINITIONS AND MISCELLANY --------------------------------------------------------------------------------

This was my favorite part of the entire homework.  I decided, much to my workloads chugrin that I was going to get super creative with this and develope what I have been doing alot of math on.  I have already floated some of my work, last year, around a little bit of the math department but frankly I was trying to impliment and work on things in control theory, and stochastic calculus...Graduate level math, and I didn't full understand what I was talking about.  This was fun because the math is simple and there is no toxic flow(people with better info than you) working against you.  

A market maker or liquidity provider is a trader who continuously offers bid and asks, on the fair value of something.  They offer to both buy and sell a stock at a given price with the information of what they think the fair or actual value of something is, and the distance between the bid(What they are offering to buy at) an the ask(What they are offering to sell at) is called the spread.  The spread is how Makers make money, and the larger the spread the more of it.  Markets move to fast now adays to do this mentally or on a piece of paper, so models need to be implimented in code(usually cpp bc of runtime).  The exchange we are trading on only accepts prices that are whole multiples of a tick, so each price must be sorted onto a tick.  Think of a ladder where each rung is a tick, and up one rung of the later is up a tick, and down one rung of the later is down a tick.  The bid is down the ask is up.  Now if you round the wrong way the quote is much tighter than intended and we take on more risk than we chose. So go ahead and buy low and sell high.

Goal is to create a model that sorts onto these:

fair_value = 10237      cents, what our model is saying the thing we are trading is worth
half_spread = 15        cents that are either side of fair value
tick_size = 25          cents

and we want it to print these three lines which are our quotes:

Bid: 10200
Ask: 10275
Spread: 75

Requirements:

1, You want to write a function 'up_to_tick(price, tick)' that returns the smallest multiple of 'tick' that is at or above 'price'
2. All of the printed numbers must be in whole cents, so there cant be decimal points.
3. Must be generalized enought that it works if the top three variables change to the values specified below



fair_value  half_spread  tick_size    Bid    Ask  Spread
     10237          15         25  10200    10275      75
     10240           10        25  10225   10250      25
       500            3          1    497    503       6
      1000            1        100    900   1100     200
    
Frankly this was a pain to align and it still isn't.  

This question is meant to assess students abilities on floor division/modulo to snapping onto a grid and rounding up only.  Rounding down is obvious, so one has to get creative when rounding up. There are a few snags that might catch someone trying to do this.  One is visualizing and designing the grid or ladder that the ticks sit on, and then accurately catching the edge case where one of the ticks might come back as a decimal. Specifics aside the most challenging part of this is picking an angle to go at it, as most of the information here is fresh to most people, so a longer background on the subject matter is probably important.

As I finish this I realize that I might have done too much here and might get dinged for it