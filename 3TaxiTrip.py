def taxi_tracker():
    # Get driver's name
    driver_name = input("Enter the driver's name: ")

    total_time = 0
    total_income = 0
    num_trips = 0

    while True:
        start_trip = input("Start a new trip? (yes/no): ").lower()

        if start_trip == 'no':
            break

        elif start_trip == 'yes':
            try:
                trip_time = float(input("Enter the time the trip took in minutes: "))
                if trip_time < 0:
                    print("Invalid trip time. Please enter a non-negative value.")
                    continue

                # Calculate cost
                trip_cost = 10 + 2 * trip_time

                # Update totals
                total_time += trip_time
                total_income += trip_cost
                num_trips += 1

                print(f"Trip cost: ${trip_cost:.2f}\n")

            except ValueError:
                print("Invalid input. Please enter a valid number for trip time.")

    # Print summary at the end of the day
    print("\nEnd of the day summary:")
    print(f"Driver's name: {driver_name}")
    print(f"Total time of all trips: {total_time:.2f} minutes")
    print(f"Average time of all trips: {total_time / num_trips:.2f} minutes")
    print(f"Total income for the day: ${total_income:.2f}")
    if num_trips > 0:
        print(f"Average cost of all trips: ${total_income / num_trips:.2f}")
    else:
        print("No trips recorded.")


