number1 = int(input("\nWhat is the first number you want to perform the operation with? "))
number2 = int(input("What is the second number you want to perform the operation with? "))

while True:
    print("Welcome to the calculator.")
    
    print("\n What is the operation you want to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    option = input("Enter option: ")

    if option == "1":
        print(str(number1) + " added to " + str(number2) + " is " + str(number1 + number2))

    elif option == "2":
        print(str(number1) + " subtracted with " + str(number2) + " is " + str(number1 - number2))

    elif option == "3":
        print(str(number1) + " multiplied to " + str(number2) + " is " + str(number1 * number2))

    elif option == "4":
        print(str(number1) + " divided by " + str(number2) + " is " + str(number1 / number2))

    elif option == "5":
        break
    
    else:
        continue