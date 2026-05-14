employees = []

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        salary = input("Enter salary: ")

        employee = {
            "Name": name,
            "Age": age,
            "Salary": salary
        }

        employees.append(employee)

        print("Employee added")

    elif choice == "2":
        print("\nEmployee Details")

        for emp in employees:
            print(emp)

    elif choice == "3":
        search = input("Enter employee name to search: ")

        found = False

        for emp in employees:
            if emp["Name"] == search:
                print(emp)
                found = True

        if found == False:
            print("Employee not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")