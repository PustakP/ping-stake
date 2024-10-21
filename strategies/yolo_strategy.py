from utils.types import Strategy, Gamble, History

class YoloStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.name = "YOLO Strategy"
        self.author = "mueheheh"

    def play(self, balance: float, rounds_left: int, history: History) -> Gamble:
        # yolo: all-in w/ max risk
        return Gamble(balance, 0.99)  # bet all, 99% risk (max allowed)
