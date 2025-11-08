# merged_guessing_game_with_pipe.py

import multiprocessing
import random

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
            return True, attempts  # game won
    return False, ATTEMPT_LIMIT  # game lost

# ----------------------------
# Pipe-Based Processes
# ----------------------------
def create_games(pipe, num_games=5):
    """Send game results through the pipe."""
    output_pipe, _ = pipe
    for _ in range(num_games):
        won, attempts = simulate_game()
        result = f"{'Won' if won else 'Lost'} in {attempts} attempts"
        output_pipe.send(result)
    output_pipe.close()

def process_pipe(pipe_1, pipe_2):
    """Receive from first pipe, transform and send to second."""
    _, input_pipe = pipe_1
    output_pipe, _ = pipe_2
    try:
        while True:
            result = input_pipe.recv()
            # Example transformation: append " -> Processed"
            output_pipe.send(f"{result} -> Processed")
    except EOFError:
        output_pipe.close()

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == '__main__':
    # First pipe: send raw game results
    pipe_1 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=create_games, args=(pipe_1,))
    p1.start()

    # Second pipe: receive game results and "process" them
    pipe_2 = multiprocessing.Pipe(True)
    p2 = multiprocessing.Process(target=process_pipe, args=(pipe_1, pipe_2))
    p2.start()

    # Close unused ends in main
    pipe_1[0].close()
    pipe_2[0].close()

    print("Game Results (processed through pipes):")
    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("End of games")

    # Wait for child processes to finish
    p1.join()
    p2.join()
