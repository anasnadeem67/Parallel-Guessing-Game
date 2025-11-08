import threading
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
# Box Class with RLock
# ----------------------------
class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value
            # Run guessing game whenever box is modified
            won, attempts = simulate_game()
            print(f"Guessing game while modifying box: {'Won' if won else 'Lost'} in {attempts} attempts")

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

# ----------------------------
# Adder Thread
# ----------------------------
def adder(box, items):
    print(f"N° {items} items to ADD \n")
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print(f"ADDED one item --> {items} item(s) left to ADD \n")

# ----------------------------
# Remover Thread
# ----------------------------
def remover(box, items):
    print(f"N° {items} items to REMOVE \n")
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print(f"REMOVED one item --> {items} item(s) left to REMOVE \n")

# ----------------------------
# Main Function
# ----------------------------
def main():
    items = 10
    box = Box()

    t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1,10)))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
