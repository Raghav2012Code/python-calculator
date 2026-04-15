while True:
    print("Welcome to the calculator.")
    print("\nWhat is the operation you want to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    option = input("Enter option: ")
    
    if option == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    
    elif option == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    
    elif option == "3":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} * {num2} = {num1 * num2}")
    
    elif option == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    
    elif option == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")