class HospitalScheduler:
    def __init__(self):
        self.schedule = {}
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.limit_per_slot = 3

    def get_contact_number(self, prompt):
        """Helper function to safely get mobile number as int"""
        try:
            number = int(input(prompt).strip())
            return number
        except ValueError:
            print("Invalid number! Please enter digits only.")
            return None

    def reserve_slot(self):
        print("=== Reserve Appointment ===")
        pname = input("Enter patient name: ").strip()
        page = input("Enter patient age: ").strip()
        contact = self.get_contact_number("Enter mobile number: ")
        if contact is None:
            return
        doc_name = input("Enter preferred doctor: ").strip()

        if doc_name not in self.schedule:
            self.schedule[doc_name] = {slot: [] for slot in self.slots}

        # check duplicate appointment
        for doc, timings in self.schedule.items():
            for patients in timings.values():
                for record in patients:
                    if record["contact"] == contact:
                        print("You already have an appointment booked!")
                        return

        # show available slots
        print(f"Available slots for Dr.{doc_name}:")
        for slot in self.slots:
            print(f"{slot}: {len(self.schedule[doc_name][slot])}/{self.limit_per_slot} booked")

        pick_slot = input("Enter desired slot: ").strip()
        if pick_slot not in self.slots:
            print("Invalid time slot!")
            return

        if len(self.schedule[doc_name][pick_slot]) >= self.limit_per_slot:
            print("Sorry, this slot is full. Try another one.")
            return

        # confirm booking
        self.schedule[doc_name][pick_slot].append({
            "name": pname,
            "age": page,
            "contact": contact
        })
        print(f"Appointment confirmed with Dr.{doc_name} at {pick_slot}.")

    def check_booking(self):
        print("=== View Appointment ===")
        contact = self.get_contact_number("Enter your mobile number: ")
        if contact is None:
            return
        found = False
        for doc, timings in self.schedule.items():
            for slot, patients in timings.items():
                for record in patients:
                    if record["contact"] == contact:
                        print(f"Appointment: Dr.{doc} at {slot}, Patient: {record['name']}, Age: {record['age']}")
                        found = True
        if not found:
            print("No booking found for this number.")

    def remove_booking(self):
        print("=== Cancel Appointment ===")
        contact = self.get_contact_number("Enter your mobile number: ")
        if contact is None:
            return
        found = False
        for doc, timings in self.schedule.items():
            for slot, patients in timings.items():
                for record in patients:
                    if record["contact"] == contact:
                        patients.remove(record)
                        print(f"Appointment cancelled for Dr.{doc} at {slot}.")
                        found = True
                        return
        if not found:
            print("No booking found for this number.")


# --- Main Menu ---
hospital = HospitalScheduler()

while True:
    print("\n=== Hospital Appointment System ===")
    print("1. Reserve Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")
    option = input("Enter your choice: ").strip()

    if option == "1":
        hospital.reserve_slot()
    elif option == "2":
        hospital.check_booking()
    elif option == "3":
        hospital.remove_booking()
    elif option == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Try again.")
