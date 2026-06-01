class Student:
    # Constructor to initialize the student details
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        
        # Validating marks (assuming out of 100)
        if 0 <= marks <= 100:
            self.marks = marks
        else:
            print("Error: Marks should be between 0 and 100. Setting to 0 by default.")
            self.marks = 0

    # Method to calculate and return grade
    def calculate_grade(self):
        if self.marks >= 90:
            return "A (Excellent)"
        elif self.marks >= 75:
            return "B (Good)"
        elif self.marks >= 50:
            return "C (Average)"
        elif self.marks >= 33:
            return "D (Pass)"
        else:
            return "F (Fail)"

    # Method to display student details nicely
    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_number}")
        print(f"Marks      : {self.marks}/100")
        print(f"Grade      : {self.calculate_grade()}")
        print("-----------------------\n")


# --- Testing the Student Management Code (Basic Usage) ---
if __name__ == "__main__":
    print("Welcome to Student Management System!")
    
    # 1. Create first student
    student1 = Student("Akhilesh", 101, 88)
    student1.display_details()
    
    # 2. Create another student
    student2 = Student("Rahul", 102, 45)
    student2.display_details()
    
    # 3. Create a student with invalid marks to test validation
    student3 = Student("Vikas", 103, 120)
    student3.display_details()
