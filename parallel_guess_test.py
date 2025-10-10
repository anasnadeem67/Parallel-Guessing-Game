# parallel_guess_test.py
import random
import time
import threading
import multiprocessing
import queue

ATTEMPT_LIMIT = 10
NUMBERS_RANGE = (1, 100)

def simulate_game(attempt_limit=ATTEMPT_LIMIT, numbers_range=NUMBERS_RANGE):
    """Simulate one guessing game where guesses are random.
       Returns tuple: (won:bool, attempts_used:int, secret:int)
    """
    secret = random.randint(*numbers_range)
    attempts = 0
    while attempts < attempt_limit:
        attempts += 1
        guess = random.randint(*numbers_range)
        if guess == secret:
            return True, attempts, secret
    return False, attempts, secret

# ---------- Thread worker ----------
def thread_worker(result_queue, games_per_worker):
    """Each thread runs games_per_worker simulated games and pushes results."""
    wins = 0
    total_attempts = 0
    for _ in range(games_per_worker):
        won, attempts, _ = simulate_game()
        wins += 1 if won else 0
        total_attempts += attempts
    # push a summary tuple
    result_queue.put(("thread", wins, total_attempts))

# ---------- Process worker ----------
def process_worker(result_queue, games_per_worker):
    wins = 0
    total_attempts = 0
    for _ in range(games_per_worker):
        won, attempts, _ = simulate_game()
        wins += 1 if won else 0
        total_attempts += attempts
    result_queue.put(("process", wins, total_attempts))

# ---------- Runner helpers ----------
def run_thread_test(worker_count, games_per_worker):
    q = queue.Queue()
    threads = []
    start = time.time()
    for _ in range(worker_count):
        t = threading.Thread(target=thread_worker, args=(q, games_per_worker))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()

    # collect results
    total_wins = total_attempts = 0
    while not q.empty():
        _, w, a = q.get()
        total_wins += w
        total_attempts += a
    return end - start, total_wins, total_attempts

def run_process_test(worker_count, games_per_worker):
    # multiprocessing.Queue must be used for inter-process comms
    q = multiprocessing.Queue()
    procs = []
    start = time.time()
    for _ in range(worker_count):
        p = multiprocessing.Process(target=process_worker, args=(q, games_per_worker))
        procs.append(p)
        p.start()
    for p in procs:
        p.join()
    end = time.time()

    total_wins = total_attempts = 0
    # gather all items from queue
    while not q.empty():
        try:
            kind, w, a = q.get_nowait()
            total_wins += w
            total_attempts += a
        except Exception:
            break
    return end - start, total_wins, total_attempts

# ---------- Main: run tests for several worker counts ----------
if __name__ == "__main__":
    # choose worker counts you want to test
    worker_counts = [5, 15, 25]      # tum 15, 25 etc bolay thay — yahan add/modify karo
    games_per_worker = 100           # har worker kitne simulated games chalaye
    print("Starting parallel guessing simulation tests")
    print(f"Each simulated game has attempt limit = {ATTEMPT_LIMIT}, range = {NUMBERS_RANGE}")
    print()

    for wc in worker_counts:
        print(f"--- Workers: {wc}   (games_per_worker = {games_per_worker}) ---")
        t_time, t_wins, t_attempts = run_thread_test(wc, games_per_worker)
        print(f"Threads => time: {t_time:.4f}s  | total simulated games: {wc*games_per_worker} | wins: {t_wins} | avg attempts/game: {t_attempts/(wc*games_per_worker):.2f}")

        p_time, p_wins, p_attempts = run_process_test(wc, games_per_worker)
        print(f"Procs   => time: {p_time:.4f}s  | total simulated games: {wc*games_per_worker} | wins: {p_wins} | avg attempts/game: {p_attempts/(wc*games_per_worker):.2f}")

        print()

    print("Done.")
