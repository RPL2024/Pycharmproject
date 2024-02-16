class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = []

    def mark_attendance(self, status):
        self.attendance.append(status)


class AttendanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added successfully.")
        else:
            print(f"Student {name} already exists.")

    def mark_attendance(self, name, status):
        if name in self.students:
            self.students[name].mark_attendance(status)
            print(f"Attendance marked for {name}: {status}")
        else:
            print(f"Student {name} not found.")

    def view_attendance(self, name):
        if name in self.students:
            print(f"Attendance for {name}: {self.students[name].attendance}")
        else:
            print(f"Student {name} not found.")

    def menu(self):
        while True:
            print("\nAttendance Tracker Menu:")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. View Attendance")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                self.add_student(name)
            elif choice == '2':
                name = input("Enter student's name: ")
                status = input("Enter attendance status (Present/Absent): ").capitalize()
                if status == "Present" or status == "Absent":
                    self.mark_attendance(name, status)
                else:
                    print("Invalid attendance status. Please enter 'Present' or 'Absent'.")
            elif choice == '3':
                name = input("Enter student's name: ")
                self.view_attendance(name)
            elif choice == '4':
                print("Exiting Attendance Tracker.")
                break
            else:
                print("Invalid choice. Please select again.")


if __name__ == "__main__":
    tracker = AttendanceTracker()
    tracker.menu()