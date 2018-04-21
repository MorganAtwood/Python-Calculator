#CIT 432 Final: Calculator v1.3
#8/20/2017
#Morgan Atwood

import math
import os


# Sends result to OS's clipboard
def clipboard(r):
    r = str(r)
    command = 'echo ' + r + '| clip'
    os.system(command)
    return

# adds values
def add(x, y):
    r = x + y
    clipboard(r)
    return r

# subtracts values
def subtract(x, y):
    r = x - y
    clipboard(r)
    return r

# multiplies values
def multiply(x, y):
    r = x * y
    clipboard(r)
    return r

# divides values
def divide(x, y):
    r = x / y
    clipboard(r)
    return r
# squareroot of number
def sqrt(x):
    r = x**(.5)
    clipboard(r)
    return r
#Menu
def menu():
    print ("\n" * 50)
    print("Morgan's Python Calculator v1.3")
    print("Select operation.")
    print("(1) Add")
    print("(2) Subtract")
    print("(3) Multiply")
    print("(4) Divide")
    print("(5) Square Root")
    print("(6) Exit")
    print('')
    
    # Take input from the user 
    choice = int(input("Enter Operator Number: "))
    
    if choice < 5:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == 1:
            print ("\n" * 50)
            print(num1,"+",num2,"=", add(num1,num2))
            print("Copied to Clipboard!")
            print('\n')   
            input("Press Enter to continue...")           
            menu()
        
        elif choice == 2:
            print ("\n" * 50)
            print(num1,"-",num2,"=", subtract(num1,num2))
            print("Copied to Clipboard!")
            print('\n')   
            input("Press Enter to continue...")            
            
            menu()
        
        elif choice == 3:
            print ("\n" * 50)
            print(num1,"*",num2,"=", multiply(num1,num2))
            print("Copied to Clipboard!")
            print('\n')   
            input("Press Enter to continue...")
            menu()
        
        elif choice == 4:
            print ("\n" * 50)
            print(num1,"/",num2,"=", divide(num1,num2)) 
            print("Copied to Clipboard!")
            print('\n')   
            input("Press Enter to continue...")
            menu()
            
    elif choice == 5 : 
        num1 =  int(input("Enter Number: "))
    
        if choice == 5:
            print ("\n" * 50)
            print(num1,'**','1/2','=',sqrt(num1))
            print("Copied to Clipboard!")
            print('\n')   
            input("Press Enter to continue...")
            menu()
            
    elif choice == 6: 
        print("Thank you for using Morgan's Calculator")
    
    else:
        print("Invalid input, please try again.")
        input("Press Enter to continue...")
        menu()
#Program Starts        
menu()