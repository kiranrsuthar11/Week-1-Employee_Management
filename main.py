import json


employees = []


# adddd employeess

def add_employee():
    print("\n================ ADD EMPLOYEESS =======================")

    employee_id = input("Enter Employee ID: ").strip()

    if employee_id == "":
        print("Employee ID cannot be blank.")
        return

    for employee in employees:
        if employee["id"].lower() == employee_id.lower():
            print("Employee ID already exists.")
            return

    name = input("Enter Employee Name: ").strip()

    if name == "":
        print("Employee name cannot be blank.")
        return

    try:
        age = int(input("Enter Age: "))

        if age < 18 or age > 65:
            print("Age must be between 18 and 65.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    department = input("Enter Department: ").strip()

    if department == "":
        print("Department cannot be blank.")
        return

    role = input("Enter Role: ").strip()

    if role == "":
        print("Role cannot be blank.")
        return

    try:
        salary = float(input("Enter Salary: "))

        if salary < 0:
            print("Salary cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid salary.")
        return

    try:
        joining_year = int(input("Enter Joining Year: "))

        if joining_year < 2000:
            print("Joining year must be 2000 or later.")
            return

    except ValueError:
        print("Please enter a valid joining year.")
        return

    print("\nSelect Employment Status")
    print("1. Active")
    print("2. Inactive")
    print("3. On Leave")

    status_choice = input("Enter choice: ").strip()

    if status_choice == "1":
        status = "Active"

    elif status_choice == "2":
        status = "Inactive"

    elif status_choice == "3":
        status = "On Leave"

    else:
        print("Invalid status choice.")
        return

    employee = {
        "id": employee_id,
        "name": name,
        "age": age,
        "department": department,
        "role": role,
        "salary": salary,
        "joining_year": joining_year,
        "status": status
    }

    employees.append(employee)

    print("\nEmployee added successfully.")


# viewww employees

def view_employees():
    print("\n========== ALL EMPLOYEES ==========")

    if not employees:
        print("No employees found.")
        return

    print("-" * 110)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<6}"
        f"{'Department':<15}"
        f"{'Role':<20}"
        f"{'Salary':<12}"
        f"{'Year':<8}"
        f"{'Status':<12}"
    )

    print("-" * 110)

    for employee in employees:
        print(
            f"{employee['id']:<10}"
            f"{employee['name']:<20}"
            f"{employee['age']:<6}"
            f"{employee['department']:<15}"
            f"{employee['role']:<20}"
            f"{employee['salary']:<12.2f}"
            f"{employee['joining_year']:<8}"
            f"{employee['status']:<12}"
        )

    print("-" * 110)


# search

def search_employee():
    print("\n========== SEARCH EMPLOYEE ==========")

    print("1. Search by Employee ID")
    print("2. Search by Name")
    print("3. Search by Department")

    choice = input("Enter choice: ").strip()

    if choice not in ["1", "2", "3"]:
        print("Invalid choice.")
        return

    search_value = input("Enter search value: ").strip().lower()

    if search_value == "":
        print("Search value cannot be blank.")
        return

    found = False

    for employee in employees:

        if (
            (choice == "1" and employee["id"].lower() == search_value)
            or
            (choice == "2" and search_value in employee["name"].lower())
            or
            (choice == "3" and search_value in employee["department"].lower())
        ):

            print("\nEmployee Found")
            print("----------------------------")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Age:", employee["age"])
            print("Department:", employee["department"])
            print("Role:", employee["role"])
            print("Salary: ₹", employee["salary"])
            print("Joining Year:", employee["joining_year"])
            print("Status:", employee["status"])

            found = True

    if not found:
        print("Employee not found.")


# update

def update_employee():
    print("\n========== UPDATE EMPLOYEE ==========")

    employee_id = input("Enter Employee ID to update: ").strip()

    found_employee = None

    for employee in employees:
        if employee["id"].lower() == employee_id.lower():
            found_employee = employee
            break

    if found_employee is None:
        print("Employee not found.")
        return

    print("\nEmployee Found")
    print("Name:", found_employee["name"])
    print("Department:", found_employee["department"])
    print("Role:", found_employee["role"])
    print("Salary:", found_employee["salary"])
    print("Status:", found_employee["status"])

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Department")
    print("3. Role")
    print("4. Salary")
    print("5. Status")
    print("6. Cancel")

    choice = input("Enter choice: ").strip()

    if choice == "1":

        new_name = input("Enter new name: ").strip()

        if new_name == "":
            print("Name cannot be blank.")
            return

        found_employee["name"] = new_name
        print("Name updated successfully.")

    elif choice == "2":

        new_department = input("Enter new department: ").strip()

        if new_department == "":
            print("Department cannot be blank.")
            return

        found_employee["department"] = new_department
        print("Department updated successfully.")

    elif choice == "3":

        new_role = input("Enter new role: ").strip()

        if new_role == "":
            print("Role cannot be blank.")
            return

        found_employee["role"] = new_role
        print("Role updated successfully.")

    elif choice == "4":

        try:
            new_salary = float(input("Enter new salary: "))

            if new_salary < 0:
                print("Salary cannot be negative.")
                return

            found_employee["salary"] = new_salary

            print("Salary updated successfully.")

        except ValueError:
            print("Please enter a valid salary.")

    elif choice == "5":

        print("\nSelect New Status")
        print("1. Active")
        print("2. Inactive")
        print("3. On Leave")

        status_choice = input("Enter choice: ").strip()

        if status_choice == "1":
            found_employee["status"] = "Active"

        elif status_choice == "2":
            found_employee["status"] = "Inactive"

        elif status_choice == "3":
            found_employee["status"] = "On Leave"

        else:
            print("Invalid status choice.")
            return

        print("Status updated successfully.")

    elif choice == "6":

        print("Update cancelled.")

    else:

        print("Invalid choice.")


# delete emp

def delete_employee():
    print("\n========== DELETE EMPLOYEE ==========")

    employee_id = input("Enter Employee ID to delete: ").strip()

    found_employee = None

    for employee in employees:
        if employee["id"].lower() == employee_id.lower():
            found_employee = employee
            break

    if found_employee is None:
        print("Employee not found.")
        return

    print("\nEmployee Found")
    print("Name:", found_employee["name"])
    print("Department:", found_employee["department"])

    confirmation = input(
        "Are you sure you want to delete this employee? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        employees.remove(found_employee)

        print("Employee deleted successfully.")

    elif confirmation == "no":

        print("Delete cancelled.")

    else:

        print("Please enter yes or no.")


# department report

def department_report():
    print("\n========== DEPARTMENT REPORT ==========")

    if not employees:
        print("No employees found.")
        return

    departments = {}

    for employee in employees:

        department = employee["department"]

        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1

    print("\nDepartment-wise Employee Count")
    print("----------------------------")

    for department, count in departments.items():
        print(department, ":", count)


# salaryy analysis

def salary_analysis():
    print("\n========== SALARY ANALYSIS ==========")

    if not employees:
        print("No employees found.")
        return

    total_salary = 0

    highest_employee = employees[0]
    lowest_employee = employees[0]

    for employee in employees:

        total_salary += employee["salary"]

        if employee["salary"] > highest_employee["salary"]:
            highest_employee = employee

        if employee["salary"] < lowest_employee["salary"]:
            lowest_employee = employee

    average_salary = total_salary / len(employees)

    print("Total Salary: ₹", round(total_salary, 2))
    print("Average Salary: ₹", round(average_salary, 2))

    print(
        "Highest Salary: ₹",
        highest_employee["salary"]
    )

    print(
        "Highest Paid Employee:",
        highest_employee["name"]
    )

    print(
        "Lowest Salary: ₹",
        lowest_employee["salary"]
    )

    print(
        "Lowest Paid Employee:",
        lowest_employee["name"]
    )


# employee statistical

def employee_statistics():
    print("\n========== EMPLOYEE STATISTICS ==========")

    if not employees:
        print("No employees found.")
        return

    total_employees = len(employees)

    active_count = 0
    inactive_count = 0
    leave_count = 0

    total_age = 0

    for employee in employees:

        total_age += employee["age"]

        if employee["status"] == "Active":
            active_count += 1

        elif employee["status"] == "Inactive":
            inactive_count += 1

        elif employee["status"] == "On Leave":
            leave_count += 1

    average_age = total_age / total_employees

    print("Total Employees:", total_employees)
    print("Active Employees:", active_count)
    print("Inactive Employees:", inactive_count)
    print("Employees On Leave:", leave_count)
    print("Average Age:", round(average_age, 2))


# filter employee

def filter_employees():
    print("\n========== FILTER EMPLOYEES ==========")

    if not employees:
        print("No employees found.")
        return

    print("1. Filter by Department")
    print("2. Salary Greater Than ₹50,000")
    print("3. Active Employees")
    print("4. Joined in 2026")

    choice = input("Enter choice: ").strip()

    found = False

    if choice == "1":

        department = input("Enter Department: ").strip().lower()

        for employee in employees:

            if employee["department"].lower() == department:

                print(
                    employee["id"],
                    "-",
                    employee["name"],
                    "-",
                    employee["department"],
                    "-",
                    employee["salary"]
                )

                found = True

    elif choice == "2":

        for employee in employees:

            if employee["salary"] > 50000:

                print(
                    employee["id"],
                    "-",
                    employee["name"],
                    "-",
                    employee["salary"]
                )

                found = True

    elif choice == "3":

        for employee in employees:

            if employee["status"] == "Active":

                print(
                    employee["id"],
                    "-",
                    employee["name"],
                    "-",
                    employee["status"]
                )

                found = True

    elif choice == "4":

        for employee in employees:

            if employee["joining_year"] == 2026:

                print(
                    employee["id"],
                    "-",
                    employee["name"],
                    "-",
                    employee["joining_year"]
                )

                found = True

    else:

        print("Invalid choice.")
        return

    if not found:
        print("No matching employees found.")


# final emp report

def final_employee_report():
    print("\n========== EMPLOYEE WORKFORCE REPORT ==========")

    if not employees:
        print("No employees found.")
        return

    total_employees = len(employees)

    active_count = 0
    inactive_count = 0
    leave_count = 0

    total_age = 0
    total_salary = 0

    departments = {}

    highest_employee = employees[0]
    lowest_employee = employees[0]

    for employee in employees:

        total_age += employee["age"]
        total_salary += employee["salary"]

        if employee["status"] == "Active":
            active_count += 1

        elif employee["status"] == "Inactive":
            inactive_count += 1

        elif employee["status"] == "On Leave":
            leave_count += 1

        department = employee["department"]

        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1

        if employee["salary"] > highest_employee["salary"]:
            highest_employee = employee

        if employee["salary"] < lowest_employee["salary"]:
            lowest_employee = employee

    average_age = total_age / total_employees
    average_salary = total_salary / total_employees

    print("\nTotal Employees:", total_employees)
    print("Active Employees:", active_count)
    print("Inactive Employees:", inactive_count)
    print("Employees On Leave:", leave_count)

    print("Average Age:", round(average_age, 2))
    print("Average Salary: ₹", round(average_salary, 2))

    print("Highest Salary: ₹", highest_employee["salary"])
    print("Highest Paid Employee:", highest_employee["name"])

    print("Lowest Salary: ₹", lowest_employee["salary"])
    print("Lowest Paid Employee:", lowest_employee["name"])

    print("\nDepartment Breakdown")
    print("----------------------------")

    for department, count in departments.items():
        print(department, ":", count)


# savee

def save_records():
    try:

        with open("employees.json", "w") as file:

            json.dump(employees, file, indent=4)

        print("\nEmployee records saved successfully.")

    except Exception as e:

        print("Error while saving records:", e)


# load 

def load_records():

    global employees

    try:

        with open("employees.json", "r") as file:

            employees = json.load(file)

        print("Employee records loaded successfully.")

    except FileNotFoundError:

        employees = []

        print("No existing employee records found.")

    except json.JSONDecodeError:

        employees = []

        print("Employee file is empty or invalid.")


# menuu

def main_menu():

    load_records()

    while True:

        print("\n")
        print("==============================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("==============================================")

        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Department-wise Employees")
        print("7. Salary Analysis")
        print("8. Employee Statistics")
        print("9. Filter Employees")
        print("10. Save Records")
        print("11. Employee Workforce Report")
        print("12. Exit")

        print("===============================================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_employee()

        elif choice == "2":

            view_employees()

        elif choice == "3":

            search_employee()

        elif choice == "4":

            update_employee()

        elif choice == "5":

            delete_employee()

        elif choice == "6":

            department_report()

        elif choice == "7":

            salary_analysis()

        elif choice == "8":

            employee_statistics()

        elif choice == "9":

            filter_employees()

        elif choice == "10":

            save_records()

        elif choice == "11":

            final_employee_report()

        elif choice == "12":

            save_records()

            print("\nThank you for using Employee Management System.")

            break

        else:

            print("Invalid choice. Please try again.")


#run

main_menu()