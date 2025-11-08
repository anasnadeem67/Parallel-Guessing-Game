# Chapter 03 - Parallel Programming in Python

This repository contains Python scripts demonstrating **Threading, Locks, RLocks, Semaphores, Events, Conditions, Barriers, and Multiprocessing** concepts. Each file implements a specific concept or pattern for parallel execution.

---

## Table of Contents

1. [Guessing Game](#guessing-game)
2. [Threading Examples](#threading-examples)
3. [Thread Synchronization](#thread-synchronization)
4. [Multiprocessing Examples](#multiprocessing-examples)
5. [Process Synchronization](#process-synchronization)
6. [Process Pool](#process-pool)
7. [Spawning Processes](#spawning-processes)
8. [How to Run](#how-to-run)
9. [Notes](#notes)

---

## Guessing Game

**File:** `parallel_guessing_game.py`

- Simulates a random number guessing game.
- Each game has a secret number and limited attempts.
- Demonstrates sequential simulation of multiple games.

**Sample Output:**
Game 1: Lost, Attempts: 10
Game 2: Won, Attempts: 3


---

## Threading Examples

**Files:**
- `MyThreadClass.py`
- `MyThreadClass_lock.py`
- `MyThreadClass_lock_2.py`
- `Thread_definition.py`
- `Thread_determine.py`
- `Thread_name_and_processes.py`
- `Barrier.py`

**Concepts Covered:**
- Thread creation and execution
- Thread join
- Locks (`threading.Lock`)
- Reentrant Locks (`threading.RLock`)
- Barrier synchronization
- Thread names and process IDs

---

## Thread Synchronization

**Files:**
- `Condition.py` – Producer/Consumer using `threading.Condition`
- `Event.py` – Producer/Consumer using `threading.Event`
- `Semaphore.py` – Producer/Consumer using `threading.Semaphore`
- `Threading_with_queue.py` – Queue-based producer/consumer

**Concepts Covered:**
- Coordinating multiple threads
- Waiting and notifying
- Shared data protection
- Event signaling

---

## Multiprocessing Examples

**Files:**
- `communicating_with_pipe.py` – Using `multiprocessing.Pipe`
- `communicating_with_queue.py` – Using `multiprocessing.Queue`
- `killing_processes.py` – Terminating processes
- `myFunc.py` – Simple function for processes
- `naming_processes.py` – Process names
- `process_in_subclass.py` – Custom process subclass
- `process_pool.py` – Process Pool
- `processes_barrier.py` – Process synchronization with barrier
- `run_background_processes.py` – Daemon and non-daemon processes
- `run_background_processes_no_daemons.py` – Non-daemon background processes
- `spawning_processes.py` – Spawning processes sequentially
- `spawning_processes_namespace.py` – Spawning processes using `__name__ == '__main__'`

**Concepts Covered:**
- Process creation and execution
- Pipe and Queue communication
- Process termination and joining
- Daemon vs non-daemon processes
- Process synchronization (Barrier, Lock)
- Process pools and map
- Namespaces and spawn method

---

## Process Synchronization

**Concepts & Files:**
- Barrier synchronization (`processes_barrier.py`)
- Locks (`MyThreadClass_lock.py`, `MyThreadClass_lock_2.py`)
- Reentrant Locks (`Rlock.py`)
- Semaphores (`Semaphore.py`)

---

## Process Pool

**File:** `process_pool.py`

- Demonstrates using a **Process Pool** to map a function across multiple inputs.
- Reduces process creation overhead.

---

## Spawning Processes with Tasks

**Files:**
- `spawning_processes.py`
- `spawning_processes_namespace.py`

- Shows how to spawn multiple processes and run a function (`myFunc`) with arguments.
- Can integrate small tasks like the **Guessing Game** inside each process.

---

## How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/Parallel-Programming-Python.git
cd Parallel-Programming-Python
