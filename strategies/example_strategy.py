from utils.types import Strategy, Gamble, History

class ExampleStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.name = "Example Strategy"
        self.author = "author1pustakpathaka"

    def play(self, balance: float, rounds_left: int, history: History) -> Gamble:
        # always bet 1% of balance w/ 60% win chance
        bet_amount = balance * 0.01
        return Gamble(bet_amount, 0.6)
