# main.py - Main Program for Multi-Utility Toolkit
# Name: SWEETI SINGH
# Project: File Operations
import datetime
import math
import random
import uuid
import time
import file_operations

def main():
    while True:
        print("\n================================")
        print("Welcome to Multi-Utility Toolkit")
        print("================================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("================================")
        
        choice = input("Enter your choice: ")
        
        # 1. Datetime Operations
        if choice == '1':
            while True:
                print("\nDatetime and Time Operations:")
                print("1. Display current date and time")
                print("2. Calculate difference between two dates/times")
                print("3. Format date into custom format")
                print("4. Stopwatch")
                print("5. Countdown Timer")
                print("6. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ")
                print("==============================")
                
                if sub_choice == '1':
                    now = datetime.datetime.now()
                    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
                    print("==============================")
                    
                elif sub_choice == '2':
                    date1_str = input("Enter the first date (YYYY-MM-DD): ")
                    date2_str = input("Enter the second date (YYYY-MM-DD): ")
                    d1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
                    d2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
                    diff = d2 - d1
                    print("Difference:", abs(diff.days), "days")
                    print("==============================")
                    
                elif sub_choice == '3':
                    date_str = input("Enter date (YYYY-MM-DD): ")
                    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                    fmt = input("Enter custom format (e.g. %d-%m-%Y): ")
                    print("Formatted Date:", d.strftime(fmt))
                    print("==============================")
                    
                elif sub_choice == '4':
                    input("Press Enter to start stopwatch...")
                    start = time.time()
                    input("Press Enter to stop stopwatch...")
                    end = time.time()
                    print("Elapsed Time:", round(end - start, 2), "seconds")
                    print("==============================")
                    
                elif sub_choice == '5':
                    sec = int(input("Enter countdown time in seconds: "))
                    while sec > 0:
                        print("Time remaining:", sec, "seconds")
                        time.sleep(1)
                        sec -= 1
                    print("Time's up!")
                    print("==============================")
                    
                elif sub_choice == '6':
                    break
                    
        # 2. Mathematical Operations
        elif choice == '2':
            while True:
                print("\nMathematical Operations:")
                print("1. Calculate Factorial")
                print("2. Solve Compound Interest")
                print("3. Trigonometric Calculations")
                print("4. Area of Geometric Shapes")
                print("5. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ")
                
                if sub_choice == '1':
                    num = int(input("Enter a number: "))
                    print("Factorial:", math.factorial(num))
                    print("==============================")
                    
                elif sub_choice == '2':
                    p = float(input("Enter principal amount: "))
                    r = float(input("Enter rate of interest (in %): "))
                    t = float(input("Enter time (in years): "))
                    ci = p * ((1 + r / 100) ** t)
                    print("Compound Interest:", round(ci, 2))
                    print("==============================")
                    
                elif sub_choice == '3':
                    angle = float(input("Enter angle in degrees: "))
                    rad = math.radians(angle)
                    print("Sin:", math.sin(rad))
                    print("Cos:", math.cos(rad))
                    print("Tan:", math.tan(rad))
                    print("==============================")
                    
                elif sub_choice == '4':
                    shape = input("Enter shape (circle/rectangle): ")
                    if shape == "circle":
                        rad = float(input("Enter radius: "))
                        print("Area:", math.pi * (rad ** 2))
                    elif shape == "rectangle":
                        l = float(input("Enter length: "))
                        w = float(input("Enter width: "))
                        print("Area:", l * w)
                    print("==============================")
                    
                elif sub_choice == '5':
                    break
                    
        # 3. Random Data Generation
        elif choice == '3':
            while True:
                print("\nRandom Data Generation:")
                print("1. Generate Random Number")
                print("2. Generate Random List")
                print("3. Create Random Password")
                print("4. Generate Random OTP")
                print("5. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ")
                
                if sub_choice == '1':
                    low = int(input("Enter lower bound: "))
                    high = int(input("Enter upper bound: "))
                    print("Random Number:", random.randint(low, high))
                    print("==============================")
                    
                elif sub_choice == '2':
                    size = int(input("Enter list size: "))
                    lst = []
                    for i in range(size):
                        lst.append(random.randint(1, 100))
                    print("Random List:", lst)
                    print("==============================")
                    
                elif sub_choice == '3':
                    length = int(input("Enter password length: "))
                    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@"
                    pwd = ""
                    for i in range(length):
                        pwd += random.choice(chars)
                    print("Generated Password:", pwd)
                    print("==============================")
                    
                elif sub_choice == '4':
                    otp = random.randint(1000, 9999)
                    print("Generated OTP:", otp)
                    print("==============================")
                    
                elif sub_choice == '5':
                    break
                    
        # 4. Generate Unique Identifiers (UUID)
        elif choice == '4':
            print("Generated UUID:", uuid.uuid4())
            print("==============================")
            
        # 5. File Operations (Calls custom module)
        elif choice == '5':
            while True:
                print("\nFile Operations:")
                print("1. Create a new file")
                print("2. Write to a file")
                print("3. Read from a file")
                print("4. Append to a file")
                print("5. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ")
                
                if sub_choice == '1':
                    fname = input("Enter file name: ")
                    file_operations.create_file(fname)
                    print("==============================")
                elif sub_choice == '2':
                    fname = input("Enter file name: ")
                    data = input("Enter data to write: ")
                    file_operations.write_file(fname, data)
                    print("==============================")
                elif sub_choice == '3':
                    fname = input("Enter file name: ")
                    file_operations.read_file(fname)
                    print("==============================")
                elif sub_choice == '4':
                    fname = input("Enter file name: ")
                    data = input("Enter data to append: ")
                    file_operations.append_file(fname, data)
                    print("==============================")
                elif sub_choice == '5':
                    break
                    
        # 6. Explore Module Attributes
        elif choice == '6':
            mod_name = input("Enter module name to explore: ")
            if mod_name == "math":
                print("Available Attributes in math module:")
                print(dir(math))
            elif mod_name == "random":
                print("Available Attributes in random module:")
                print(dir(random))
            else:
                print("Attributes:", dir())
            print("==============================")
            
        # 7. Exit
        elif choice == '7':
            print("================================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("================================")
            break
        else:
            print("Invalid choice. Please choose between 1 and 7.")

if __name__ == "__main__":
    main()