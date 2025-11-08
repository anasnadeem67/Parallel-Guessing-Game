import threading
import time
import os
from threading import Thread
from random import randint

# ----------------------------
# Lock Definition
# ----------------------------
threadLock = threading.Lock()

# ----------------------------
# Guessing Game constants
# ----------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game():
    """Simulate one guessing game."""
    secret = randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = randint(*NUMBERS_RANGE)
        if guess == secret:
            return True, attempts
    return False, ATTEMPT_LIMIT

# ----------------------------
# Thread Class
# ----------------------------
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the Lock
        threadLock.acquire()
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        
        # Run guessing game while holding the lock
        won, attempts = simulate_game()
        print(f"---> {self.name} guessing game: {'Won' if won else 'Lost'} in {attempts} attempts\n")
        
        # Release the Lock
        threadLock.release()
        
        # Simulate some thread work
        time.sleep(self.duration)
        print(f"---> {self.name} over\n")

# ----------------------------
# Main function
# ----------------------------
def main():
    start_time = time.time()

    # Thread Creation
    threads = [MyThreadClass(f"Thread#{i+1}", randint(1,10)) for i in range(9)]

    # Start all threads
    for t in threads:
        t.start()

    # Join all threads
    for t in threads:
        t.join()

    print("End")
    print(f"--- {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()
