# merged_killing_guessing_game.py

import multiprocessing
import random
import time

# ----------------------------
# Guessing Game Function
# ----------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game():
    """Simulate one guessing game."""
    secret = random.randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            return f"Won in {attempts} attempts"
    return f"Lost in {ATTEMPT_LIMIT} attempts"

# ----------------------------
# Worker Function
# ----------------------------
def guessing_worker(num_games=5):
    print("Starting guessing games process")
    for i in range(num_games):
        result = simulate_game()
        print(f"Game {i+1}: {result}")
        time.sleep(1)
    print("Finished guessing games process")

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    p = multiprocessing.Process(target=guessing_worker, args=(10,))  # run 10 games
    print('Process before execution:', p, p.is_alive())

    p.start()
    print('Process running:', p, p.is_alive())

    # Terminate the process after 3 seconds (for demonstration)
    time.sleep(3)
    print('Terminating process now...')
    p.terminate()
    print('Process terminated:', p, p.is_alive())

    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
