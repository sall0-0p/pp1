# Made by Orest Antoniuk
import time
sleep = time.sleep

# Tasks are here.
def task1():
    x = 5

    print(x)

def task2():
    name = input("Enter your name: ")

    print("Hello " + name)

def task3():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter rate: "))

    print("Pay: " + str(hours * rate) + "zł")

def task4():
    width = 17
    height = 12.0
    
    result1 = width//2
    result2 = width/2.0
    result3 = height / 3
    result4 = 1 + 2 * 5

    print(result1, type(result1))
    print(result2, type(result2))
    print(result3, type(result3))
    print(result4, type(result4))

def task5():
    celsius_value = int(input("Put your Celsius Value: "))
    print(str((celsius_value * 9 / 5) + 32) + "°F")

# dict
tasks = {
    1: task1,
    2: task2,
    3: task3,
    4: task4,
    5: task5,
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
    print("Pick task you want to check (1-6)")
    sleep(0.02)
    print(" You can type q to exit program")
    sleep(0.02)
    print(" or type 'all' to run all tasks at once!")

    return input("  // ")

# run all function, runs all tasks one after another:
def run_all():
    for key in tasks:
        print("Performing task " + str(key))
        tasks[key]()

        print("")
        sleep(0.1)
        
# function for getting correct action from prompt:
def get_option(prompt):
    if prompt == "q":
        return 'quit'
    elif prompt == "all":
        sleep(0.05)
        print("")
        run_all()
        return 'all'
    elif prompt == "windows95":
        sleep(2)
        print("""
             ________________________________________________
            /                                                \\
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> _                                 |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
        """)
        print("")
        print("Art by -Roland Hangg-")
        print("")

        return 'art'

    elif int(prompt) > 0 and int(prompt) <= 6:
        sleep(0.05)
        print("")
        print("Running task: " + prompt)
        tasks[int(prompt)]() 

        return 'task'
    else:
        print("Incorrect :<")
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
        break