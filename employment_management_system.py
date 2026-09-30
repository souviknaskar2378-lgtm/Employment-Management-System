import csv
import os

FILE_NAME = "employees.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Employee ID", "Name", "Department",
                "Designation", "Salary", "Phone"
            ])

def add_employee():
    print("\n--- Add Employee ---")
    emp_id = input("Enter Employee ID: ").strip()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Employee ID"] == emp_id:
                print("Employee ID already exists.")
                return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    designation = input("Enter Designation: ").strip()

    try:
        salary = float(input("Enter Salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary.")
        return

    phone = input("Enter Phone Number: ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            emp_id, name, department,
            designation, salary, phone
        ])

    print("Employee added successfully.")

def display_employees():
    print("\n--- All Employees ---")

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No employee records found.")
        return

    print("-" * 95)
    print(f"{'ID':<10}{'Name':<20}{'Department':<18}{'Designation':<18}{'Salary':<12}{'Phone':<15}")
    print("-" * 95)

    for row in rows:
        print(
            f"{row['Employee ID']:<10}"
            f"{row['Name']:<20}"
            f"{row['Department']:<18}"
            f"{row['Designation']:<18}"
            f"₹{float(row['Salary']):<11.2f}"
            f"{row['Phone']:<15}"
        )

    print("-" * 95)

def search_employee():
    print("\n--- Search Employee ---")
    emp_id = input("Enter Employee ID: ").strip()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Employee ID"] == emp_id:
                print("\nEmployee Found")
                print("Employee ID :", row["Employee ID"])
                print("Name        :", row["Name"])
                print("Department  :", row["Department"])
                print("Designation :", row["Designation"])
                print("Salary      : ₹" + row["Salary"])
                print("Phone       :", row["Phone"])
                return

    print("Employee not found.")

def update_employee():
    print("\n--- Update Employee ---")
    emp_id = input("Enter Employee ID: ").strip()

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    for row in rows:
        if row["Employee ID"] == emp_id:
            print("Press Enter to keep the existing value.")

            name = input(f"Name [{row['Name']}]: ").strip()
            department = input(f"Department [{row['Department']}]: ").strip()
            designation = input(f"Designation [{row['Designation']}]: ").strip()
            salary = input(f"Salary [{row['Salary']}]: ").strip()
            phone = input(f"Phone [{row['Phone']}]: ").strip()

            if name:
                row["Name"] = name
            if department:
                row["Department"] = department
            if designation:
                row["Designation"] = designation
            if salary:
                try:
                    salary_value = float(salary)
                    if salary_value < 0:
                        print("Invalid salary.")
                        return
                    row["Salary"] = str(salary_value)
                except ValueError:
                    print("Invalid salary.")
                    return
            if phone:
                row["Phone"] = phone

            save_records(rows)
            print("Employee updated successfully.")
            return

    print("Employee not found.")

def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = input("Enter Employee ID: ").strip()

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    new_rows = [row for row in rows if row["Employee ID"] != emp_id]

    if len(new_rows) == len(rows):
        print("Employee not found.")
        return

    save_records(new_rows)
    print("Employee deleted successfully.")

def salary_details():
    print("\n--- Salary Details ---")

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No employee records found.")
        return

    total = sum(float(row["Salary"]) for row in rows)
    average = total / len(rows)

    highest = max(rows, key=lambda row: float(row["Salary"]))
    lowest = min(rows, key=lambda row: float(row["Salary"]))

    print("Total Employees       :", len(rows))
    print(f"Total Salary          : ₹{total:.2f}")
    print(f"Average Salary        : ₹{average:.2f}")
    print(
        f"Highest Salary        : ₹{float(highest['Salary']):.2f} "
        f"({highest['Name']})"
    )
    print(
        f"Lowest Salary         : ₹{float(lowest['Salary']):.2f} "
        f"({lowest['Name']})"
    )

def department_employees():
    print("\n--- Department-wise Employees ---")
    department = input("Enter Department: ").strip().lower()

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    found = False

    for row in rows:
        if row["Department"].lower() == department:
            if not found:
                print("\nEmployees:")
                print("-" * 60)
            print(
                f"ID: {row['Employee ID']} | "
                f"Name: {row['Name']} | "
                f"Designation: {row['Designation']}"
            )
            found = True

    if not found:
        print("No employees found in this department.")

def save_records(rows):
    fieldnames = [
        "Employee ID", "Name", "Department",
        "Designation", "Salary", "Phone"
    ]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    initialize_file()

    while True:
        print("\n==========================================")
        print("       EMPLOYMENT MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Salary Details")
        print("7. Department-wise Employees")
        print("8. Exit")
        print("==========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            salary_details()
        elif choice == "7":
            department_employees()
        elif choice == "8":
            print("Thank you for using Employment Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
