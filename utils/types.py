from typing import List, NamedTuple, Tuple

class Gamble(NamedTuple):
    amount_bet: float
    risk: float  # prob of winning (0 to 1)

History = List[bool]  # t for win, f for loss

class Strategy:
    def __init__(self):
        self.name: str = ''
        self.author: str = ''
    
    def play(self, balance: float, rounds_left: int, history: History) -> Gamble:
        # strat logic here
        return Gamble(0, 0.5)  # dflt: no bet, 50% risk
