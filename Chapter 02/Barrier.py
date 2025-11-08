import random
from threading import Barrier, Thread
from time import ctime, sleep

# ------------------------------
# Game constants
# ------------------------------
ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

# ------------------------------
# Guessing Game function
# ------------------------------
def simulate_game():
    secret = random.randint(*NUMBERS_RANGE)
    for attempts in range(1, ATTEMPT_LIMIT + 1):
        guess = random.randint(*NUMBERS_RANGE)
        if guess == secret:
            return True, attempts
    return False, ATTEMPT_LIMIT

# ------------------------------
# Thread setup (Barrier Race)
# ------------------------------
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    # simulate race delay
    sleep(random.randint(2, 5))

    # Run a guessing game for this thread
    won, attempts = simulate_game()
    print(f"{name} finished race at: {ctime()}")
    print(f"{name} played guessing game -> {'Won' if won else 'Lost'} in {attempts} attempts\n")

    # Wait at barrier for other threads
    finish_line.wait()

def main():
    threads = []
    print("START RACE WITH GUESSING GAME!\n")
    for _ in range(num_runners):
        t = Thread(target=runner)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Race over and all games finished!")

if __name__ == "__main__":
    main()
