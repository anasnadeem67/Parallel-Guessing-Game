# merged_myFunc_guessing_game.py

import multiprocessing
import random
import time

# ----------------------------
# myFunc from your file
# ----------------------------
def myFunc(i):
    print(f'Calling myFunc from process n°: {i}')
    for j in range(i):
        print(f'Output from myFunc: {j}')
    print(f'myFunc {i} finished\n')

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
def process_worker(proc_id, num_games=5):
    print(f"Starting process {proc_id}...\n")

    # Call myFunc
    myFunc(proc_id)

    # Run guessing games
    for i in range(num_games):
        result = simulate_game()
        print(f"Process {proc_id} - Game {i+1}: {result}")
        time.sleep(0.5)

    print(f"Process {proc_id} finished all games.\n")

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    num_processes = 3  # number of parallel processes
    processes = []

    for pid in range(1, num_processes+1):
        p = multiprocessing.Process(target=process_worker, args=(pid, 5))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed.")
