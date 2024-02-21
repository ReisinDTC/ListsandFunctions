children_list = []  # Global list to keep track of children

def welcome_screen():
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

def drop_off():
    name = input("Enter the name of the child to check in: ")
    children_list.append(name)
    print(f"{name} has been added to the role.")

def pick_up():
    name = input("Enter the name of the child to check out: ")
    if name in children_list:
        children_list.remove(name)
        print(f"{name} has been checked out successfully.")
    else:
        print(f"Error: {name} is not in the list. Please check the name.")

def calc_cost():
    hours = int(input("Enter the number of hours to charge: "))
    charge = len(children_list) * 12 * hours
    print(f"The total charge for {len(children_list)} children for {hours} hours is ${charge}.")

def print_roll():
    print("Current roll list:")
    for child in children_list:
        print(child)

def main():
    choice = 0

    while choice != 5:
        welcome_screen()
        choice = int(input("Enter your choice (number between 1 and 5): "))
        print()

        if choice == 1:
            drop_off()
        elif choice == 2:
            pick_up()
        elif choice == 3:
            calc_cost()
        elif choice == 4:
            print_roll()
        elif choice == 5:
            print("Goodbye")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

