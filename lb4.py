# Flight details dictionary
flight_details = {
    "AI161E90": {"From": "BLR", "To": "BOM", "Price": 5600},
    "BR161F91": {"From": "BOM", "To": "BBI", "Price": 6750},
    "AI161F99": {"From": "BBI", "To": "BLR", "Price": 8210},
    "VS171E20": {"From": "JLR", "To": "BBI", "Price": 5500},
    "AS171G30": {"From": "HYD", "To": "JLR", "Price": 4400},
    "AI131F49": {"From": "HYD", "To": "BOM", "Price": 3499}
}

def get_flights(criteria, value):
    flights = []
    if criteria == "Flight ID":
        if value in flight_details:
            flights.append((value, flight_details[value]))
    else:
        for flight_id, details in flight_details.items():
            if details[criteria] == value:
                flights.append((flight_id, details))
    return flights



while True:
    print("Choose an option:")
    print("1. Search by Flight ID")
    print("2. Search by source city")
    print("3. Search by destination city")
    print("4. Quit")
    choice = int(input())

    if choice == 1:
        flight_id = input("Enter Flight ID: ")
        flights = get_flights("Flight ID", flight_id)
    elif choice == 2:
        source_city = input("Enter source city: ")
        flights = get_flights("From", source_city)
    elif choice == 3:
        destination_city = input("Enter destination city: ")
        flights = get_flights("To", destination_city)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
        continue

    if flights:
        print("Matching Flights:")
        for flight_id, details in flights:
            print("Flight ID:", flight_id)
            for key, value in details.items():
                print(key + ":", value)
            print()
    else:
        print("No matching flights found.")
