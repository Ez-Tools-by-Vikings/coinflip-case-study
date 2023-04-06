# Fair CoinFlip - Case Study

## The problem

Coin flips are usually fair, assumed a fair coin, fair probability distribution and every other factor being equally fair, it's always 50:50 ..till it isn't!

Let's say you had a 20000 token pool with 10 token min amount to be played with

Regular users would go in and play at 10 tokens, the probability looks something like this

```
W - 0.5
L - 0.5
```

What about 2 flips though (unordered)

```
WW - 0.25
LL - 0.25
WL - 0.5
```

Let's take it to 3 flips (unordered)

```
WWW - 0.125
LLL - 0.125
WLL - 0.375
WWL - 0.375
```

In general, the formula for getting at least 1 W in n fair flips is:

$$
$$

So, if the user we to try 5 flips:

$$P(1_5) = 1-0.5^5 $$

$$
= 0.96875
$$

This is 96.875% chances of winning at least once, which is fairly high and you this might entice you to try your odds, but this isn't as simple.

Let's take bet amount in context and say the user always bets 10 tokens, if user makes 5 flips

These are the odds

```
0 W 5 L = 3.125% | P/L = -50
1 W 4 L = 15.63% | P/L = -30
2 W 3 L = 31.25% | P/L = -10
3 W 2 L = 31.25% | P/L = 10
4 W 1 L = 15.63% | P/L = 30
5 W 0 L = 3.125% | P/L = 50
```

Which as you can see balances out since these flips are fair. But let's consider house edge of 1%. Then the odds and P/L look like this:

```
0 W 5 L = 3.125% | P/L = -50
1 W 4 L = 15.63% | P/L = -30.2
2 W 3 L = 31.25% | P/L = -10.4
3 W 2 L = 31.25% | P/L = 9.4
4 W 1 L = 15.63% | P/L = 29.2
5 W 0 L = 3.125% | P/L = 49
```

This would usually be pretty secure way of ensuring the house always won but that is only true for fixed amount bets.

Let's take the case of variable amount bets, I start with 10 tokens and with each loss I double it, what happens then ?

```
First loss = -10
Second loss = - 10 - 20 = - 30
Third loss =  - 10 - 20 - 40 = -60
Fourth loss = - 10 - 20 - 40 - 80 = -160
Win on 5th turn (96.9% probability) = 160 * 1.98 = 316.8 - 310 = +6.8
Win on 6th turn (98.4% probability) = 320 * 1.98 = 633.6 = +3.6
```

on the 7th turn, player would incur a loss (640 \* 1.98 = 1267.2 - 1270 = -2.8)

We assume on 8th turn, user has a 100% probability of winning (99.6% rounded);

Let's figure out the ways a user can scalp the pool.

```
1W = +9.8 | P = 50%
1L 1W = +9.6 | P = 25%
2L 1W = +9.2 | P = 12.5%
3L 1W = +8.4 | P = 6.25%
4L 1W = +6.8 | P = 3.125%
5L 1W = +3.6 | P = 1.5625%
6L 1W = -2.8 | P = 0.78125%
7L 1W = -25.6 | P = 0.39%
```
