
class SpeedingTicketSystem:
    def __init__(self):
        self.speeders = []
        self.total_fines = 0

    def calculate_fine(self, amount_over_limit):
        if amount_over_limit < 10:
            return 30
        elif 10 <= amount_over_limit <= 14:
            return 80
        elif 15 <= amount_over_limit <= 19:
            return 120
        elif 20 <= amount_over_limit <= 24:
            return 170
        elif 25 <= amount_over_limit <= 29:
            return 230
        elif 30 <= amount_over_limit <= 34:
            return 300
        elif 35 <= amount_over_limit <= 39:
            return 400
        elif 40 <= amount_over_limit <= 44:
            return 510
        else:
            return 630

    def process_speeder(self, name, amount_over_limit):
        warrant_list = ["James Wilson", "Helga Norman", "Zachary Conroy"]
        if name in warrant_list:
            print(f"{name.upper()} - WARRANT TO ARREST")
        else:
            fine = self.calculate_fine(amount_over_limit)
            self.total_fines += fine
            self.speeders.append({"Name": name, "Amount Over Limit": amount_over_limit, "Fine": fine})
            print(f"{name} to be fined ${fine}\n#############")

    def display_summary(self):
        print("Total fines:", len(self.speeders))
        for index, speeder in enumerate(self.speeders, start=1):
            print(f"{index}) Name: {speeder['Name']} Amount Over Limit: {speeder['Amount Over Limit']}")
        print("Total amount of fines: ${}".format(self.total_fines))


def main():
    ticket_system = SpeedingTicketSystem()

    while True:
        name = input("Enter name of speeder: ")
        if name.lower() == "stop":
            break

        amount_over_limit = int(input("Enter the amount over speed limit: "))
        ticket_system.process_speeder(name, amount_over_limit)

    ticket_system.display_summary()
