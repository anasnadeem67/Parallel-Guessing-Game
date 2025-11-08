# merged_process_pool_guessing_game.py

import multiprocessing
import random
import time

# ----------------------------
# Guessing Game Function
# ----------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game(_):
    """Simulate one guessing game for pool worker.
       The argument is ignored; used for pool.map compatibility."""
    secret = random.randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            return f"Won in {attempts} attempts"
    return f"Lost in {ATTEMPT_LIMIT} attempts"

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    # Number of simulated games
    total_games = 20

    # Using 4 pool workers
    pool = multiprocessing.Pool(processes=4)

    # pool.map passes each item in the list to simulate_game
    # We just use a list of dummy values [0..total_games-1]
    pool_outputs = pool.map(simulate_game, range(total_games))

    pool.close()
    pool.join()

    # Print results
    for i, result in enumerate(pool_outputs, start=1):
        print(f"Game {i}: {result}")

    print("All games completed using Process Pool.")
