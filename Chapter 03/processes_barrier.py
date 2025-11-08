# merged_processes_barrier_guessing_game.py

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from datetime import datetime
import random
import time

# ----------------------------
# Guessing Game Function
# ----------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game_barrier(serializer):
    """Simulate guessing game and print result with barrier serialization"""
    name = multiprocessing.current_process().name
    secret = random.randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            result = f"Won in {attempts} attempts"
            break
    else:
        result = f"Lost in {ATTEMPT_LIMIT} attempts"
    
    now = time.time()
    with serializer:
        print(f"{name} | {datetime.fromtimestamp(now)} | Result: {result}")

def simulate_game_no_barrier():
    """Simulate guessing game without barrier"""
    name = multiprocessing.current_process().name
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
# Main
# ----------------------------
if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()

    # Processes using Barrier
    Process(name='p1 - barrier', target=lambda: (synchronizer.wait(), simulate_game_barrier(serializer))).start()
    Process(name='p2 - barrier', target=lambda: (synchronizer.wait(), simulate_game_barrier(serializer))).start()

    # Processes without Barrier
    Process(name='p3 - no_barrier', target=simulate_game_no_barrier).start()
    Process(name='p4 - no_barrier', target=simulate_game_no_barrier).start()
