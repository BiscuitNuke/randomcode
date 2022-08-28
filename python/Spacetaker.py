import os
import time

def main():

    print("This program will make a file")

    while True:

        try:

            file_name = input("Enter the name of the file you want to create: ")

            if not file_name.endswith(".txt"):
                file_name += ".txt"

            break

        except ValueError:
            print("Please enter a valid name")

    while True:

        try:

            size = int(input("Enter the size of the file in GB (1-10000): ")) * 1024 * 1024 * 1024 #Convert GB to bytes.  1GB = 1024MB, 1MB = 1024KB, 1KB = 1024B.  So 1GB = 1024*1024*1024B.  Multiply by size to get total bytes for that size in GB.  
            
            if size > 10000 * 1024 * 1024 * 1024 or size < 0: #If user enters a number greater than 100 or less than 0, ask again.  
                raise ValueError() #Raise an error so it goes back to the beginning of the loop and asks again.  

            break #If no errors are raised, break out of loop and continue with program.  

        except ValueError: #If an error is raised, go here and ask again until user enters a valid number between 0 and 100 inclusive.  
            print("Please enter a valid number between 0 and 1000 inclusive.")  #Ask again until user enters a valid number between 0 and 100 inclusive.  

    start_time = time.time() #Start timer for how long it takes to make the file with this method (using os module).  

    with open(file_name, "wb") as f: #Open file in binary write mode.  
        f.seek(size - 1) #Seek to the byte before the last byte of the file.  This is because seek() goes to the byte after the number you enter, so if you want 100 bytes, you have to enter 99.  
        f.write(b"\0") #Write a null byte at that location (the last byte of the file).  

    end_time = time.time() #End timer for how long it takes to make the file with this method (using os module).  

    print("File created in {} seconds".format(end_time - start_time)) #Print out how long it took to make the file with this method (using os module).  

if __name__ == "__main__":
    main()