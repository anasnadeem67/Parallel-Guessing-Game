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
# Thread functions
# ----------------------------
def function_A():
    print(threading.currentThread().getName() + '--> starting \n')
    time.sleep(2)
    
    # Guessing game
    won, attempts = simulate_game()
    print(f'{threading.currentThread().getName()} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')
    
    print(threading.currentThread().getName() + '--> exiting \n')

def function_B():
    print(threading.currentThread().getName() + '--> starting \n')
    time.sleep(2)
    
    won, attempts = simulate_game()
    print(f'{threading.currentThread().getName()} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')
    
    print(threading.currentThread().getName() + '--> exiting \n')

def function_C():
    print(threading.currentThread().getName() + '--> starting \n')
    time.sleep(2)
    
    won, attempts = simulate_game()
    print(f'{threading.currentThread().getName()} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')
    
    print(threading.currentThread().getName() + '--> exiting \n')

# ----------------------------
# Main Function
# ----------------------------
if __name__ == "__main__":
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
