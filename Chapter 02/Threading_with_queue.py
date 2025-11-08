""""Thread synchronisation with queue + guessing game"""

from threading import Thread
from queue import Queue
import time
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
# Producer Thread
# ----------------------------
class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Producer notify : item N°{item} appended to queue by {self.name}')
            
            # Run guessing game
            won, attempts = simulate_game()
            print(f'{self.name} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')
            
            time.sleep(1)

# ----------------------------
# Consumer Thread
# ----------------------------
class Consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print(f'Consumer notify : {item} popped from queue by {self.name}')
            
            # Run guessing game
            won, attempts = simulate_game()
            print(f'{self.name} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')
            
            self.queue.task_done()

# ----------------------------
# Main Function
# ----------------------------
if __name__ == '__main__':
    queue = Queue()

    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    # Consumers run infinitely in this example; we may join for a limited time
    # If needed, we can add queue.join() with timeout or a sentinel value to stop consumers
