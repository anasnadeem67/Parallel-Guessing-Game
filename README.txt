
Parallel Number Guessing Game using Multiprocessing and Multithreading


🧠 Overview
This project demonstrates how a simple Python game, “Guess the Number”, can be implemented using parallel programming concepts. It compares the performance of multiprocessing and multithreading when running the same task multiple times simultaneously.

⚙️ Concepts Used
Multiprocessing: Runs multiple processes in parallel, utilizing multiple CPU cores.
Multithreading: Runs multiple threads within a single process, sharing memory.
Random Number Generation: Generates a random number for each game instance.
Time Measurement: Calculates total execution time for both approaches.

📜 Working Explanation
1. Each process or thread runs an independent instance of the “Guess the Number” game.
2. A random number between 1 and 100 is generated.
3. Each game has 10 random attempts to guess the correct number.
4. The total time taken for all processes and threads to complete is recorded.
5. The output compares the execution times of multiprocessing and multithreading.

💡 Purpose
The project helps to:
Understand the difference between multiprocessing and multithreading.
Measure how parallel execution improves performance.
Learn how CPU-bound tasks behave under both methods.

🧩 Modules Used
import random
import time
import threading
import multiprocessing

🕹️ How to Run
1. Save the file as parallel_guess_game.py.
2. Open the terminal and execute:
python parallel_guess_game.py
3. The program will display the total time taken for both multiprocessing and multithreading tests.

📊 Sample Output
Starting Multiprocessing test with 10 processes...
Process 1 started.
Process 2 started.
...
Process 10 completed.
Multiprocessing time = 1.45 seconds

Starting Multithreading test with 10 threads...
Thread 1 started.
Thread 2 started.
...
Thread 10 completed.
Multithreading time = 9.51 seconds

📈 Observation
Multiprocessing is generally faster because each process runs on a separate CPU core.
Multithreading is slower in Python due to the Global Interpreter Lock (GIL), which limits true parallel execution for CPU-bound tasks.


👨‍🏫 Project Information
Student Name: Anas Nadeem
Roll No: 23SP-102-CS
Course: Parallel and Distributed Computing
Instructor: Miss Rameen
Language: Python 3