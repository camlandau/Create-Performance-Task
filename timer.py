'''
INSTRUCTIONS:

- RUN: Execute the code (`python3 timer.py` in your command line).
- INPUT: Once prompted, enter the amount of seconds you would like counted down.
- OUTPUT: Wait the allotted time and and wait for your command line to read `Done!!`.
'''

# Importing time module for use in timing of countdown.
import time

# While the input passes a valid value...
while True:
    try:
        # Taking user input for countdown amount.
        secondsInput = int(input('Set a timer for (in seconds): '))
        break
    except ValueError:
        # If you input a character, string, or any other data type than an integer, it will throw this error.
        print('Please input a valid integer. Try again!')

cdQueue = []


def setQueue(arr, length):
    # Filling timer queue with the length of the countdown.
    for x in range(1, length + 1):
        arr.insert(0, x)


def playCountdown(queue):
    for x in range(0, len(queue) + 1):
        if x == len(queue):
            # Once the countdown finishes, print done to signify the end of the timer.
            print('Done!!')
        else:
            print(queue[x])
            time.sleep(1)


# Setting queue for the timer.
setQueue(cdQueue, secondsInput)

# Calling the queue for the timer to be printed to the console.
playCountdown(cdQueue)
