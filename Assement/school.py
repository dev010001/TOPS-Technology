class StudentRegistry:
    def __init__(self):
        self.records = {}   # Store student data
        self.current_id = 1 # Auto-generate student ID

    def start(self):
        while True:
            print("\n=== Student Registry System ===")
            print("1. Add New Student")
            print("2. Show Student Info")
            print("3. Edit Student Record")
            print("4. Delete Student")
            print("5. Exit")
            option = input("Enter your choice: ").strip()

            if option == "1":
                self.add_student()
            elif option == "2":
                self.show_student()
            elif option == "3":
                self.edit_student()
            elif option == "4":
                self.delete_student()
            elif option == "5":
                print("Closing system...")
                break
            else:
                print("Invalid choice! Please select 1-5.")

    def add_student(self):
        print("\n--- Add New Student ---")
        sname = input("Student Name: ").strip()

        try:
            sage = int(input("Age (5-18): ").strip())
            if sage < 5 or sage > 18:
                raise ValueError("Age must be between 5 and 18.")
        except ValueError as e:
            print("Invalid age!", e)
            return

        try:
            sclass = int(input("Class (1-12): ").strip())
            if sclass < 1 or sclass > 12:
                raise ValueError("Class must be between 1 and 12.")
        except ValueError as e:
            print("Invalid class!", e)
            return

        gmobile = input("Guardian Mobile (10 digits): ").strip()
        if not (gmobile.isdigit() and len(gmobile) == 10):
            print("Invalid mobile number!")
            return

        sid = self.current_id
        self.current_id += 1
        self.records[sid] = {
            "name": sname,
            "age": sage,
            "class": sclass,
            "mobile": gmobile
        }

        print(f"Student admitted successfully! Assigned ID: {sid}")

    def show_student(self):
        print("\n--- Show Student Info ---")
        sid_inp = input("Enter Student ID: ").strip()
        if not sid_inp.isdigit():
            print("Invalid ID format!")
            return
        sid = int(sid_inp)

        if sid in self.records:
            stu = self.records[sid]
            print(f"ID: {sid}, Name: {stu['name']}, Age: {stu['age']}, "
                  f"Class: {stu['class']}, Mobile: {stu['mobile']}")
        else:
            print("No record found for this ID.")

    def edit_student(self):
        print("\n--- Edit Student Record ---")
        sid_inp = input("Enter Student ID: ").strip()
        if not sid_inp.isdigit():
            print("Invalid ID format!")
            return
        sid = int(sid_inp)

        if sid not in self.records:
            print("No record found for this ID.")
            return

        print("1. Update Mobile Number")
        print("2. Update Class")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            new_mobile = input("Enter new 10-digit mobile: ").strip()
            if not (new_mobile.isdigit() and len(new_mobile) == 10):
                print("Invalid mobile number!")
                return
            self.records[sid]['mobile'] = new_mobile
            print("Mobile updated successfully.")
        elif choice == "2":
            try:
                new_class = int(input("Enter new class (1-12): ").strip())
                if new_class < 1 or new_class > 12:
                    raise ValueError("Class must be between 1 and 12.")
            except ValueError as e:
                print("Invalid class!", e)
                return
            self.records[sid]['class'] = new_class
            print("Class updated successfully.")
        else:
            print("Invalid choice!")

    def delete_student(self):
        print("\n--- Delete Student ---")
        sid_inp = input("Enter Student ID: ").strip()
        if not sid_inp.isdigit():
            print("Invalid ID format!")
            return
        sid = int(sid_inp)

        if sid in self.records:
            del self.records[sid]
            print(f"Student with ID {sid} removed successfully.")
        else:
            print("No record found for this ID.")


# --- Run the program ---
registry = StudentRegistry()
registry.start()
