
import sys

def main():
    print("This program will take up memory")

    while True:
        try:
            size = int(input("How much memory do you want to use? (in MB) ")) * 1024 * 1024 #convert to bytes

            if size < 0: #if the user enters a negative number, raise an error
                raise ValueError()

            break #break out of the loop if the user enters a valid number

        except ValueError: #if the user enters an invalid number, tell them and ask again
            print("Please enter a positive integer.")

    data = bytearray(size) #create a bytearray of the specified size

    input("Press enter to exit") #wait for user input before exiting so they can see how much memory is being used in task manager or activity monitor. 
    
main()