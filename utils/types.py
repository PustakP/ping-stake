from typing import List, NamedTuple, Tuple

class Gamble(NamedTuple):
    amount_bet: float
    win_percentage: float

MutableHistory = List[bool]
History = Tuple[bool, ...]

class Strategy:
    def __init__(self):
        self.name: str = ''
        self.author: str = ''
    
    def begin(self, balance: float, rounds_left: int) -> Gamble:
        return

    def turn(self, balance: float, rounds_left: int, history: History) -> Gamble:
        return
