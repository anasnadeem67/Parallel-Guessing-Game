# merged_naming_processes_guessing_game.py

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
# Worker Function with Named Process
# ----------------------------
def process_worker(num_games=5):
    process_name = multiprocessing.current_process().name
    print(f"Starting process name = {process_name}\n")

    for i in range(num_games):
        result = simulate_game()
        print(f"{process_name} - Game {i+1}: {result}")
        time.sleep(0.5)

    print(f"Exiting process name = {process_name}\n")

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    # Process with custom name
    p1 = multiprocessing.Process(name='Named_Process_1', target=process_worker, args=(5,))
    # Process with default name
    p2 = multiprocessing.Process(target=process_worker, args=(5,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed.")
