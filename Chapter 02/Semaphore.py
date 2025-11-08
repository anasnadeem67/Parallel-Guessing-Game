import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

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
# Semaphore & Shared Item
# ----------------------------
semaphore = threading.Semaphore(0)
item = 0

# ----------------------------
# Consumer
# ----------------------------
def consumer():
    global item
    logging.info('Consumer is waiting')
    semaphore.acquire()
    logging.info(f'Consumer notify: item number {item}')
    
    # Run guessing game while consuming
    won, attempts = simulate_game()
    logging.info(f"Consumer guessing game: {'Won' if won else 'Lost'} in {attempts} attempts")

# ----------------------------
# Producer
# ----------------------------
def producer():
    global item
    time.sleep(1)  # simulate work
    item = random.randint(0, 1000)
    logging.info(f'Producer notify: item number {item}')
    
    # Run guessing game while producing
    won, attempts = simulate_game()
    logging.info(f"Producer guessing game: {'Won' if won else 'Lost'} in {attempts} attempts")
    
    semaphore.release()

# ----------------------------
# Main Function
# ----------------------------
def main():
    for i in range(5):  # repeat few times to keep output reasonable
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__ == "__main__":
    main()
