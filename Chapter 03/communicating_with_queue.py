# merged_guessing_game_with_queue.py

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
# Producer Process
# ----------------------------
class Producer(multiprocessing.Process):
    def __init__(self, queue, num_games=5):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.num_games = num_games

    def run(self):
        for _ in range(self.num_games):
            result = simulate_game()
            self.queue.put(result)
            print(f"Producer: {result} appended to queue {self.name}")
            time.sleep(1)
            print(f"Queue size: {self.queue.qsize()}")

# ----------------------------
# Consumer Process
# ----------------------------
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Consumer: The queue is empty. Exiting.")
                break
            item = self.queue.get()
            print(f"Consumer: {item} popped from queue {self.name}")
            time.sleep(1)

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    queue = multiprocessing.Queue()
    producer_process = Producer(queue, num_games=10)
    consumer_process = Consumer(queue)

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("All games processed.")
