# merged_process_in_subclass_guessing_game.py

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
# Subclassed Process
# ----------------------------
class MyProcess(multiprocessing.Process):
    def run(self):
        print(f'Called run method in {self.name}')
        # Run 3 guessing games per process
        for i in range(3):
            result = simulate_game()
            print(f"{self.name} - Game {i+1}: {result}")
            time.sleep(0.5)
        print(f'Exiting {self.name}\n')

# ----------------------------
# Main
# ----------------------------
if __name__ == '__main__':
    processes = []

    # Create 5 subclassed processes
    for i in range(5):
        p = MyProcess(name=f"MyProcess_{i+1}")
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("All subclassed processes completed.")
