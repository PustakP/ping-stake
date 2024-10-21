from game import run_strategy
from utils.types import Strategy
import os
import importlib

def load_strategies():
    # load all strats from strategies dir
    strategies = []
    strategy_dir = 'strategies'
    for filename in os.listdir(strategy_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'strategies.{filename[:-3]}'
            module = importlib.import_module(module_name)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Strategy) and attr != Strategy:
                    strategies.append(attr())
    return strategies

def main():
    strategies = load_strategies()
    
    print("=== ping-stake game results ===")
    print(f"Total strategies: {len(strategies)}")
    print("-------------------------------")
    
    for strategy in strategies:
        print(f"Running strategy: {strategy.name} by {strategy.author}")
        final_balance = run_strategy(strategy)
        print(f"Final balance: ${final_balance:.2f}")
        print(f"Profit/Loss: ${final_balance - 10000:.2f}")
        print("-------------------------------")
    
    print("=== game over ===")

if __name__ == "__main__":
    main()
