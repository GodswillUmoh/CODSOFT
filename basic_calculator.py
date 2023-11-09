print("Welcome to the Basic Arithmetic Calculator!\n ")

    # receiving input from users
while True:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    user_operation = input("Select an operation:\n1. Multiplication\n2. Addition\n3. Subtraction:\nEnter your choice (1/2/3): ")

    #Computation formulas
    if user_operation == "1":
        formula = num1 * num2
        print("Result: ",formula)

    elif user_operation == "2":
        formula = num1 + num2
        print("Result: ",formula)

    elif user_operation == "3":
        formula = num1 - num2
        print("Result: ",formula)
    else:
        ("Invalid Selection ")
        print("You have not selected any number!")

    #Asking user to repeat or quit process
    repeat_quit = input("Do you want to perform another calculation? (yes/no):\n ").upper()
    if repeat_quit == "yes".upper():
        continue

    else:
        print("Thank you for using the Basic Arithmetic Calculator! Have a great day!")
        break
