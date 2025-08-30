class TravelBooking:
    def __init__(self):
        self.routes_prices = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Mysore": 300,
            "Chennai to Coimbatore": 350
        }
        self.bookings = {}   # ticket_no: {passenger details}
        self.ticket_counter = 1
        self.capacity = 40

    def start(self):
        while True:
            print("\n=== Travel Booking System ===")
            print("1. Display Routes")
            print("2. Reserve Seat")
            print("3. Show Ticket")
            print("4. Cancel Booking")
            print("5. Exit")
            option = input("Enter your choice: ").strip()

            if option == "1":
                self.display_routes()
            elif option == "2":
                self.reserve_seat()
            elif option == "3":
                self.show_ticket()
            elif option == "4":
                self.cancel_booking()
            elif option == "5":
                print("Shutting down system...")
                break
            else:
                print("Invalid option! Please select 1-5.")

    def display_routes(self):
        print("\nAvailable Routes:")
        for route, cost in self.routes_prices.items():
            print(f"{route} - ₹{cost}")

    def reserve_seat(self):
        pname = input("Passenger Name: ").strip()

        try:
            page = int(input("Age in years: ").strip())
            if page <= 0 or page > 120:
                print("Invalid age range!")
                return
        except ValueError:
            print("Invalid age input!")
            return

        pmobile = input("Mobile (10 digits): ").strip()
        if not (pmobile.isdigit() and len(pmobile) == 10):
            print("Invalid mobile number!")
            return

        print("\nAvailable Routes:")
        for route in self.routes_prices:
            print(route)

        route_inp = input("Enter desired route: ").strip()
        chosen_route = None
        for route in self.routes_prices:
            if route_inp.lower() == route.lower():
                chosen_route = route
                break

        if chosen_route is None:
            print("Route not found!")
            return

        booked = sum(1 for b in self.bookings.values() if b["route"] == chosen_route)
        if booked >= self.capacity:
            print("All seats booked on this bus!")
            return

        seat_no = booked + 1
        t_id = self.ticket_counter
        self.ticket_counter += 1

        self.bookings[t_id] = {
            "name": pname,
            "age": page,
            "mobile": pmobile,
            "route": chosen_route,
            "seat": seat_no
        }

        print(f"Booking Confirmed! Ticket ID: {t_id}, Seat: {seat_no}, Price: ₹{self.routes_prices[chosen_route]}")

    def show_ticket(self):
        t_input = input("Enter Ticket ID: ").strip()
        if not t_input.isdigit():
            print("Invalid Ticket ID!")
            return
        t_id = int(t_input)

        if t_id in self.bookings:
            b = self.bookings[t_id]
            print(f"Ticket ID: {t_id}, Name: {b['name']}, Age: {b['age']}, "
                  f"Mobile: {b['mobile']}, Route: {b['route']}, Seat: {b['seat']}, Price: ₹{self.routes_prices[b['route']]}")
        else:
            print("Ticket not found.")

    def cancel_booking(self):
        t_input = input("Enter Ticket ID to cancel: ").strip()
        if not t_input.isdigit():
            print("Invalid Ticket ID!")
            return
        t_id = int(t_input)

        if t_id in self.bookings:
            del self.bookings[t_id]
            print(f"Ticket ID {t_id} cancelled successfully.")
        else:
            print("Ticket not found.")


# Run the program
system = TravelBooking()
system.start()
