import csv
from Employee import Employee

def read_csv(filename):
    employees = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        try:
            next(reader)  # Skip header
        except StopIteration:
            print("CSV file is empty or does not contain a header.")
            return employees
        for row in reader:
            employee = Employee(*row)
            employees.append(employee)
    return employees

def write_csv(employees, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Date of Employment", "Salary", "Department"])
        for employee in employees:
            writer.writerow([employee.first_name, employee.last_name, employee.date_of_employment, employee.salary, employee.department])

def add_employee(employees):
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    date_of_employment = input("Enter employee's date of employment: ")
    salary = input("Enter employee's salary: ")
    department = input("Enter department name: ")
    new_employee = Employee(first_name, last_name, date_of_employment, salary, department)
    employees.append(new_employee)

def update_employee(employees):
    emp_id = input("Enter employee ID to update: ")
    for employee in employees:
        if str(employee.employee_id) == emp_id:
            employee.first_name = input("Update employee's first name: ")
            employee.last_name = input("Update employee's last name: ")
            employee.date_of_employment = input("Update employee's date of employment: ")
            employee.salary = input("Update employee's salary: ")
            employee.department = input("Update department name: ")
            print("Employee updated successfully.")
            return
    print("Employee ID not found.")

def list_employees(employees):
    print("List of Employees:")
    for employee in employees:
        print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}")

def delete_employee(employees):
    emp_id = input("Enter employee ID to delete: ")
    for employee in employees:
        if str(employee.employee_id) == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully.")
            return
    print("Employee ID not found.")

def menu():
    input_file = 'employee.csv'
    employees = read_csv(input_file)

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. List All Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            update_employee(employees)
        elif choice == '3':
            delete_employee(employees)
        elif choice == '4':
            list_employees(employees)
        elif choice == '5':
            write_csv(employees, input_file)
            print("Data has been written to 'employees.csv'.")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
