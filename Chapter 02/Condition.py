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
condition = threading.Condition()

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
    def consume(self):
        with condition:
            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()

            items.pop()
            won, attempts = simulate_game()
            logging.info(f'consumed 1 item | guessing game: {"Won" if won else "Lost"} in {attempts} attempts')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()

# ----------------------------
# Producer thread
# ----------------------------
class Producer(threading.Thread):
    def produce(self):
        with condition:
            if len(items) == 10:
                logging.info('items produced {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total items {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.produce()

# ----------------------------
# Main
# ----------------------------
def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
