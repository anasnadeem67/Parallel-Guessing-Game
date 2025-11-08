import threading
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
# Thread function
# ----------------------------
def my_func(thread_number):
    print(f'my_func called by thread N°{thread_number}')
    
    # Run guessing game
    won, attempts = simulate_game()
    print(f'Thread N°{thread_number} guessing game: {"Won" if won else "Lost"} in {attempts} attempts')

# ----------------------------
# Main Function
# ----------------------------
def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()  # wait for all threads to finish

if __name__ == "__main__":
    main()
