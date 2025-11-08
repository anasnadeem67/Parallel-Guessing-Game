# merged_run_background_guessing_game.py

import multiprocessing
import random
import time
from datetime import datetime

# ----------------------------
# Guessing Game Function
# ----------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game(name):
    """Simulate one guessing game and print result"""
    secret = random.randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            result = f"Won in {attempts} attempts"
            break
    else:
        result = f"Lost in {ATTEMPT_LIMIT} attempts"
    
    now = time.time()
    print(f"{name} | {datetime.fromtimestamp(now)} | Result: {result}")

# ----------------------------
# Target Function for Processes
# ----------------------------
def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}")
    
    # Run guessing game 5 times for background process
    if name == 'background_process':
        for i in range(5):
            simulate_game(name)
            time.sleep(1)
    else:  # Run guessing game 5 times for NO_background_process
        for i in range(5,10):
            simulate_game(name)
            time.sleep(1)
    
    print(f"Exiting {name}")

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()

    background_process.join()
    NO_background_process.join()
    
    print("All background and non-background processes completed.")
