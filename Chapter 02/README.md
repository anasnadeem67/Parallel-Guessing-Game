# Parallel Guessing Game - Python Threading & Multiprocessing Assignment

This project contains multiple Python scripts demonstrating different threading, multiprocessing, and synchronization concepts in Python. Each script is implemented with proper logging, threading, and process control techniques.

---

## File Overview

### 1. `parallel_guess_test.py`
- Simulates a guessing game using **threads** and **processes**.
- Each worker (thread/process) runs multiple simulated games.
- Collects and prints performance metrics like total wins, total attempts, average attempts per game, and execution time.

### 2. `Barrier.py`
- Demonstrates Python **threading Barrier**.
- Simulates a race with multiple runners.
- Threads wait at the barrier until all runners reach it.

### 3. `Condition.py`
- Demonstrates **threading Condition**.
- Classic **Producer-Consumer problem** implementation using a shared list and condition synchronization.

### 4. `Event.py`
- Demonstrates **threading Event**.
- Producer signals the consumer when new items are added.

### 5. `MyThreadClass.py`, `MyThreadClass_lock.py`, `MyThreadClass_lock_2.py`
- Demonstrates **thread creation and execution**.
- Includes examples using **Lock** to control access to shared resources.
- Shows thread running, sleeping, and joining with execution time.

### 6. `Rlock.py`
- Demonstrates **threading RLock (re-entrant lock)**.
- Safe addition and removal of items in a shared box using multiple threads.

### 7. `Semaphore.py`
- Demonstrates **threading Semaphore**.
- Producer-consumer problem using a semaphore for synchronization.

### 8. `Thread_definition.py`
- Simple **thread creation** example.
- Each thread calls a function and prints its thread number.

### 9. `Thread_determine.py`
- Demonstrates **naming threads**.
- Three threads executing different functions concurrently.

### 10. `Thread_name_and_processes.py`
- Shows **thread names and process IDs**.
- Demonstrates thread identification.

### 11. `Threading_with_queue.py`
- Producer-Consumer problem using **threading with queue.Queue()**.
- Multiple consumer threads consume items produced in the queue.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/<username>/Parallel-Guessing-Game.git
cd Parallel-Guessing-Game
