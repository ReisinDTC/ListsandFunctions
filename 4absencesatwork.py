# Constants
TERMINATION_SYMBOL = '$'

# Function to calculate average absence days
def calculate_average(absence_list):
    total_days = sum(absence_list)
    num_employees = len(absence_list)
    return total_days / num_employees if num_employees > 0 else 0

# Function to find the person with the most days of absence
def find_most_absent(employees, absences):
    max_absence_index = absences.index(max(absences))
    return employees[max_absence_index], absences[max_absence_index]

# Function to list people not absent at all
def list_not_absent(employees, absences):
    return [employees[i] for i in range(len(employees)) if absences[i] == 0]

# Function to list people absent above average
def list_above_average(employees, absences, average):
    return [(employees[i], absences[i]) for i in range(len(employees)) if absences[i] > average]

# Main program
def main():
    employees = []
    absences = []

    # Input loop
    while True:
        input_data = input("Enter employee name and days absent (or $ to end): ")

        if input_data == TERMINATION_SYMBOL:
            break

        try:
            name, days_absent = input_data.split()
            employees.append(name)
            absences.append(int(days_absent))
        except ValueError:
            print("Invalid input format. Please enter employee name and days absent.")

    # Calculate results
    average_days = calculate_average(absences)
    most_absent_name, most_absent_days = find_most_absent(employees, absences)
    not_absent_list = list_not_absent(employees, absences)
    above_average_list = list_above_average(employees, absences, average_days)

    # Print results
    print("\nResults:")
    print(f"Average number of days staff were absent: {average_days:.2f}")
    print(f"Person with most days absent: {most_absent_name} with {most_absent_days} days")
    print("List of people not absent at all:")
    for name in not_absent_list:
        print(name)
    print("\nList of people absent above average:")
    for name, days in above_average_list:
        print(f"{name} {days} days")

