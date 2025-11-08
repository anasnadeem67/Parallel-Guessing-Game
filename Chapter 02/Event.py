import logging
import threading
import time
import random

# ----------------------------
# Logging setup
# ----------------------------
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()

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
# Consumer thread
# ----------------------------
class Consumer(threading.Thread):
    def run(self):
        while True:
            time.sleep(2)
            event.wait()  # wait until producer sets the event
            if items:     # check if item exists
                item = items.pop()
                won, attempts = simulate_game()
                logging.info(f'Consumer popped {item} | guessing game: {"Won" if won else "Lost"} in {attempts} attempts')
            event.clear()  # reset the event

# ----------------------------
# Producer thread
# ----------------------------
class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info(f'Producer appended {item}')
            event.set()  # notify consumer

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
