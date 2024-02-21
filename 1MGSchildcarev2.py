"""Program to manage children at MGS daycare - v2
Mr Bakers version to compare to mine
Created by Patrick Baker
13th Feb 2024
"""


# Function to calculate the cost for existing roll based on number of hours
def calcCost(number, hours2):
    rate = 12.00
    cost = number * hours2 * rate
    return cost

# Get the name of child and add to roll
def dropoff():
    name1 = input("What is the name of the child you are dropping off? ")
    roll.append(name1)
    print(f"{name1} was added to the roll. ")
    print()

# Get the name of child and, if on roll, remove name from roll.
def pickUp():
    name2 = input("What is the name of the child you are picking up? ")
    if name2 in roll:
        roll.remove(name2)
        print(name2, "was removed from the roll")
        print()
    else:
        print("There's no", name2, "here at present. Please chack name.")
        print()

# Print a list of names currently on the roll
def printRoll():
    print("MGS Daycare clients currently present are: ")
    for item in roll:
        print(f"\t{item}")
    print()


# Main routine
roll = []
choice=0
while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to the Child Day-Care Centre")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Check a child in")
    print("2 Check a child out")
    print("3 Calculate charge")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropoff()

    elif choice == 2:
        pickUp()

    elif choice == 3:
        hours = int(input("How many hours to charge for: "))
        print(f"The charge for looking after {len(roll)}children for"
              f"{hours} hours is ${calcCost(len(roll), hours):.2f}")

    elif choice == 4:
        printRoll()

    else:
        print("Goodbye")

