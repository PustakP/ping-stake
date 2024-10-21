# ping-stake

a game where players create strats to maximize winnings

## how to play

1. create a new strat file in `strategies/` folder
2. implement the `Strategy` class w/ a `play` method
3. run `main.py` to test ur strat

## rules

- init balance: 10000
- total rounds: 1000
- each round, strat returns bet amt and risk
- win prob = risk, payout = 1/risk
- game ends when balance = 0 or rounds over

gl hf!
