

# I was messing around, and did a program that says programs and stuff, but first says what keys you press. To exit the main thing just press 'esc'
import psutil
import time
import os
import sys
from pynput.keyboard import Key, Listener


def on_press(key):
    print('{0} pressed'.format(key))


def on_release(key):
    print('{0} release'.format(key))

    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released


def main():

    while True:

        # CPU Usage and Memory Usage of the computer in percentage form.

        cpu = psutil.cpu_percent()  # CPU Usage in percentage form.

        memory = psutil.virtual_memory()  # Memory usage of the computer in percentage form.

        memory = memory[2]  # Gets the third value from the tuple which is the memory usage in percentage form.

        print("CPU Usage: " + str(cpu) + "%")  # Prints out CPU usage in percentage form to console.

        print("Memory Usage: " + str(memory) + "%")  # Prints out Memory usage in percentage form to console.

        print("\n")  # Prints a new line for formatting purposes.

        time.sleep(1)  # Sleeps for 1 second before repeating the loop again to get updated values for CPU and Memory usage.

        os.system('cls')  # Clears the console so that it doesn't get cluttered with old values from previous loops.

        # Processes running on the computer.

        processes = psutil.pids()  # Gets all the process IDs of all the processes running on the computer.

        for process in processes:  # Loops through all the process IDs and prints out their names to console.

            p = psutil.Process(process)  # Gets a process object from a process ID.

            print(p.name())  # Prints out the name of the process to console.

        print("\n")  # Prints a new line for formatting purposes.

        time.sleep(1)  # Sleeps for 1 second before repeating the loop again to get updated values for CPU and Memory usage.

        os.system('cls')  # Clears the console so that it doesn't get cluttered with old values from previous loops.

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


if __name__ == "__main__":
    main()