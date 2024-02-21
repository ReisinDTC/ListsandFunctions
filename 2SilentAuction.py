def silent_auction():
    item_name = input("What is the auction for? ")

    while True:
        try:
            reserve_price = float(input("What is the reserve price? $"))
            if reserve_price < 0:
                print("Reserve price cannot be negative. Please enter a valid amount.")
            else:
                break
        except ValueError:
            print("Invalid reserve price. Please enter a valid number.")

    print(f"\nThe auction for the {item_name} has started!\n")

    highest_bid = 0

    while True:
        print(f"Highest bid so far is ${highest_bid:.2f}")

        bid_input = input("What is your bid? ")

        if bid_input == '-1':
            break

        try:
            bid = float(bid_input)

            if bid > highest_bid:
                highest_bid = bid
                print(f"Highest bid so far is ${highest_bid:.2f}")
            else:
                print("Please enter a higher bid")
        except ValueError:
            print("Invalid bid. Please enter a valid number.")

    if highest_bid >= reserve_price:
        print(f"\nThe auction for the {item_name} finished with a bid of ${highest_bid:.2f}")
    else:
        print(f"\nThe auction for the {item_name} didn't sell. Reserve price not met.")


