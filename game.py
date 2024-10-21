import random
from typing import List
from utils.types import Strategy, Gamble, History

class Game:
    def __init__(self, strategy: Strategy, initial_balance: float = 10000, total_rounds: int = 1000):
        self.strategy = strategy
        self.balance = initial_balance
        self.rounds_left = total_rounds
        self.history: History = []

    def play_round(self) -> bool:
        # get strat decision
        gamble = self.strategy.play(self.balance, self.rounds_left, self.history)
        
        # chk if valid bet
        if gamble.amount_bet > self.balance or gamble.amount_bet < 0 or not 0 <= gamble.risk <= 1:
            return False

        # det outcome
        win = random.random() < gamble.risk
        
        # upd balance
        if win:
            self.balance += gamble.amount_bet * (1 / gamble.risk - 1)
        else:
            self.balance -= gamble.amount_bet

        # upd history and rounds
        self.history.append(win)
        self.rounds_left -= 1

        return self.balance > 0 and self.rounds_left > 0

    def run(self) -> float:
        while self.play_round():
            pass
        return self.balance

def run_strategy(strategy: Strategy) -> float:
    game = Game(strategy)
    return game.run()
