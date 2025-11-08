# merged_spawning_processes_guessing_game.py

import multiprocessing
import random
from datetime import datetime

# ----------------------------
# myFunc logic (from spawning_processes.py)
# ----------------------------
def myFunc(i):
    print(f'Calling myFunc from process n°: {i}')
    for j in range(0, i):
        print(f'Output from myFunc: {j}')

    # Mini Guessing Game
    ATTEMPT_LIMIT = 10
    NUMBERS_RANGE = (1, 100)
    secret = random.randint(*NUMBERS_RANGE)
    for attempt in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            result = f"Process {i}: Won in {attempt} attempts"
            break
    else:
        result = f"Process {i}: Lost in {ATTEMPT_LIMIT} attempts"

    now = datetime.now()
    print(f"{result} | Time: {now}")

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    processes = []
    for i in range(6):
        p = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes finished.")
