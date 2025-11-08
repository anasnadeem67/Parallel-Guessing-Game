from threading import Thread
import time
import os
import random

# ----------------------------
# Guessing Game constants
# ----------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game():
    """Simulate one guessing game."""
    secret = random.randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            return True, attempts
    return False, ATTEMPT_LIMIT

# ----------------------------
# Thread Class
# ----------------------------
class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"ID of process running {self.name}: {os.getpid()}")

        # Run guessing game
        won, attempts = simulate_game()
        print(f'{self.name} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')

# ----------------------------
# Main Function
# ----------------------------
def main():
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")

    # Thread Running
    thread1.start()
    thread2.start()

    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("End")

if __name__ == "__main__":
    main()
