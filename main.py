print("Welcome to Basic Tools made by Krish Soni\n")
print("1. Calculator")
print("2. Prime Number Checker")
print("3. Dice Roller")
print("4. Stopwatch")
print("5. All Factors Finder")
print("6. Quadratic Equation Solver")
print("7. Even or Odd Checker")
print("8. Lcm and Hcf calculator")
print("9. Random password generator")
print("10. Fibonacci series")
print("11. Rock Paper Scissors")
print("12. Number guessing game")
print("13. Find countries with starting letter")
print("14. Pythagorous finder")
print("15. Trignometry Calc\n")

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

if operation == 8:
    def hcf(a, b):
        while b != 0:
            a, b = b , a % b
        return a

    def lcm(a, b):
        return abs(a * b) // hcf(a, b)
    hcf1 = int(input("enter your first number : "))
    hcf2 = int(input("enter your second number : "))
    hcf3 = print(f"your lcm will be {lcm(hcf1, hcf2)} and hcf will be {hcf(hcf1, hcf2)}")


if operation == 9:
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    pass2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    pass3 = ["@", "#", "$", "&", ".", "!", "*"]
    import random
    pass4 = random.sample(pass1, 7)
    pass5 = random.sample(pass2 , 3)
    pass6 = random.sample(pass3, 1)
    pass7 = pass4 + pass5 + pass6
    random.shuffle(pass7)
    pass9 = ''.join(pass7)
    print(pass9)

if operation == 10:
    list2 = []
    f1 = 0
    f2 = 1
    f3 = int(input("enter the number of terms: "))
    for i in range(f3):
        f1, f2 = f2, f1 + f2
        list2.append(f1)

    print(list2)

if operation == 11:
    import random
    print("welcome to rock paper scissors")
    rock1 = input("enter your choice rock,paper or scissors : ").lower()
    rock2 = random.randint(1,3)
    if rock1 == "rock":
        rocky = 1
    if rock1 == "paper":
        rocky = 2
    if rock1 == "scissors":
        rocky = 3
    if rock2 == 1:
        print("I had choosen  Rock")
        rocky1 = 1
    if rock2 == 2:
        print("I had choosen Paper")
        rocky1 = 2
    if rock2 == 3:
        rocky1 = 3
        print("I had choosen scissors")
    if rocky == rocky1:
        print("We have a tie")
    if rocky == 1 and rocky1 == 3:
        print("YOU HAVE WON")
    if rocky == 3 and rocky1 == 1:
        print("YOU HAVE LOST")
    if rocky == 2 and rocky1 == 1:
        print("YOU HAVE LOST")
    if rocky == 1 and rocky1 == 2:
        print("YOU HAVE LOST")
    if rocky == 3 and rocky1 == 2:
        print("YOU HAVE WON")
    if rocky == 2 and rocky == 3:
        print("YOU HAVE LOST")

if operation == 12:
    import random
    rand3 = 0
    print("Welcome to Number guessing game you have to choose a random number between 1 to 50")
    while True:
        rand1 = random.randint(1, 50)
        rand2 = input("Enter your guess : ")
        rand3 = rand3 + 1
        if rand2 != rand1:
            print("Wrong guess try agian")
        if rand2 == rand1:
            print(f"you have guessed the right number {rand1} in {rand3} retries")
            break
        if rand3 == 5:
            if rand1 % 2 == 0:
                print("your number is even")
            else:
                print("your number is odd")
        if rand3 == 10:
            print("you reached maximum retries")
            break
        if rand3 == 7:
            for i in range(1, 26):
                if i == rand1:
                    print("your number is between 1 to 25")
            else:
                print("your number is between 26-50")

if operation == 13:
    country = input("enter your first lettter: ").upper()
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
        "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
        "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
        "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
        "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
        "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti",
        "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
        "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
        "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
        "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
        "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
        "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
        "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
        "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
        "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
        "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
        "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea",
        "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
        "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
        "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
        "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
        "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
        "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
        "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
        "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
        "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    for i in range(len(countries)):
        country1 = str(countries[i])
        list(country1)
        if country == country1[0]:
            print(country1)

if operation == 14:
    print("pythagorous finder")
    pytha = input("what do you want to find (height, base, hypotenuse) : ").lower()
    if pytha == "height":
        base = float(input("enter length of base : "))
        hypo = float(input("enter length of hypotenuse : "))
        height = (hypo ** 2) -  (base ** 2)
        print(f"The length of height will be {height ** 0.5}")
    if pytha == "base":
        height = float(input("enter length of height : "))
        hypo = float(input("enter length of hypotenuse : "))
        base = (hypo ** 2) - (height ** 2)
        print(f"The length of base will be {base ** 0.5}")
    if pytha == "hypotenuse":
        base = float(input("enter length of base : "))
        height = float(input("enter length of height : "))
        hypo = (base ** 2) + (height ** 2)
        print(f"The length of hypotenuse will be {hypo ** 0.5}")

if operation == 15:
    import math
    print("Welcome to Trigonometry")
    print("""
        A
        |\\
        | \\
        |  \\
        |   \\
        |    \\
        |     \\
        |______\\ C
        B
    """)

    trig = input("enter what you wanna find(opposite , adjacent , hypotenuse) : ").lower()
    trig1 = input("which angle measurement you have(ANGLE A OR ANGLE C) : ").upper()
    trig2 = input("which length you have alredy(opposite, adjacent, hypotenuse): ").lower()
    if trig == trig2:
        print("you can't find same things bruh")
        exit()

    if trig == "opposite":
        
        if trig1 == "A":
            if trig2 == "adjacent":
                adja = float(input("enter the length of adjacent : "))
                angle = int(input(f"enter the angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.tan(rad)
                rad2 = rad1 * adja
                print(f"The length of opposite side will be {rad2:.2f}")

            if trig2 == "hypotenuse":
                hypo = float(input("enter the length of hypotenuse"))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.sin(rad)
                rad2 = rad1 * hypo
                print(f"The length of opposite side will be {rad2:.2f}")

        if trig1 == "C":
            if trig2 == "adjacent":
                adja = float(input("enter the length of adjacent : "))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.tan(rad)
                rad2 = rad1 * adja
                print(f"The length of opposite side will be {rad2:.2f}")

            if trig2 == "hypotenuse":
                hypo = float(input("enter the length of hypotenuse"))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.sin(rad)
                rad2 = rad1 * hypo
                print(f"The length of opposite side will be {rad2:.2f}")

    if trig == "adjacent":
        if trig1 == "A" or trig1 == "C":
            if trig2 == "opposite":
                opp = float(input("enter the length of opposite"))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.tan(rad)
                rad2 = opp / rad1
                print(f"The length of adjacent side will be {rad2:.2f}")

            if trig2 == "hypotenuse":
                hypo = float(input("enter the length of hypotenuse"))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.cos(rad)
                rad2 = rad1 * hypo
                print(f"The length of adjacent side will be {rad2:.2f}")

    if trig == "hypotenuse":
        if trig1 == "A" or trig1 == "C":
            if trig2 == "opposite":
                opp = float(input("enter the length of opposite"))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.sin(rad)
                rad2 = opp / rad1
                print(f"The length of hypotenuse side will be {rad2:.2f}")

            if trig2 == "adjacent":
                adja = float(input("enter the length of adjacent : "))
                angle = int(input(f"enter the Angle of {trig1} : "))
                rad = math.radians(angle)
                rad1 = math.cos(rad)
                rad2 = adja / rad1
                print(f"The length of hypotenuse side will be {rad2:.2f}")
                
                
                
                
        
                

            
                
                
                
                
            
            
        
           
                
                
                
                
                



           # height = float(input("enter the length of adjacent"))
          #  hypo = float(input("enter the length of hypotenuse"))
        # angle = int(input(f"enter the length of Angle {trig1}"))

        




















