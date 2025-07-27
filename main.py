print("Welcome to Basic Tools made by Krish Soni\n")
print("1. Calculator")
print("2. Prime Number Checker")
print("3. Dice Roller")
print("4. Stopwatch")
print("5. All Factors Finder")
print("6. Quadratic Equation Solver")
print("7. Even or Odd Checker\n")

operation = int(input("Enter your operation number: "))

if operation == 1:
    print("\nWelcome to Basic Calculator")
    operation1 = input("Select your operation (+, -, *, /, square, cube, root, %): ")

    if operation1 in ["+", "-", "*", "/", "square", "cube", "root", "%"]:
        digit1 = input("Enter your first digit: ")
        if "." in digit1:
            digit11 = float(digit1)
            nig = 1  
        else:
            digit11 = int(digit1)
            nig = 0

        if operation1 in ["+", "-", "*", "/", "%"]:
            digit2 = input("Enter your second digit: ")
            if "." in digit2:
                digit22 = float(digit2)
                nig = 1
            else:
                digit22 = int(digit2)

        # Perform operations
        if operation1 == "+":
            print(f"Result: {digit11 + digit22}")
        elif operation1 == "-":
            print(f"result: {digit11 - digit22}")
        elif operation1 == "*":
            print(f"result: {digit11 * digit22}")
        elif operation1 == "/":
            if digit22 == 0:
                print("cannot divide by 0")
            else:
                result = digit11 / digit22
                if nig == 1:
                    print(f"Result: {result:.2f}")
                else:
                    print(f"Result: {result}")
        elif operation1 == "%":
            print(f"result: {digit11 % digit22}")
        elif operation1 == "square":
            print(f"square: {digit11 ** 2}")
        elif operation1 == "cube":
            print(f"cube: {digit11 ** 3}")
        elif operation1 == "root":
            print(f"square root: {digit11 ** 0.5}")
    else:
        print("Invalid operation selected.")


if operation == 2:
    prime_check = int(input("enter your number: "))
    if prime_check < 2:
        print("your number is not prime")

    for i in range(2, int(prime_check ** 0.5) + 1):
        if prime_check % i == 0:
            print("your number is not prime")
            break
    else:
        print("your number is prime")

if operation == 3:
    import random
    random_roll = random.randint(1, 6)
    print(f"The dice has been rolled and the result is {random_roll}")

if operation == 4:
    import time
    time_input = int(input("enter countdowntime in seconds : "))
    while time_input > 0:
        print(time_input)
        time.sleep(1)
        time_input = time_input - 1
    if time_input == 0:
        print("your time has ended")

if operation == 5:
    factor_input = int(input("enter your number : "))
    list1 = []
    factor2 = factor_input + 1
    for i in range(1, factor_input + 1):
        if factor_input % i == 0:
            list1.append(i)
    print(list1)

if operation == 6:
    print("enter the values for ax² + bx + c")
    equationa = int(input("enter value for a : "))
    equationb = int(input("enter value for b : "))
    equationc = int(input("enter value for c : "))
    equation4 = (equationb ** 2) - 4 * equationa * equationc
    equation5 = equation4 ** 0.5
    equation6 = (-equationb + equation5) / (2 * equationa)
    equation7 = (-equationb - equation5) / (2 * equationa)
    print(f"The values for x will be {equation6:.2f} and {equation7:.2f}")


if operation == 7:
    evenorodd = int(input("enter your number: "))
    if evenorodd % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")
            

            
        
        


