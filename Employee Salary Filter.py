def filter_employees(employees, min_salary, max_salary):
    """
    This function takes a list of tuples containing employee information, as well as two integer values representing
    a salary range. It filters the employees whose salary falls within the given range, sorts them by salary (highest
    to lowest), and prints their name and job title in a table format.
    """
    filtered_employees = []
    for name, job_title, salary in employees:
        if min_salary <= salary <= max_salary:
            filtered_employees.append((salary, name, job_title))
    if not filtered_employees:
        print("No employees found in the given salary range.")
        return
    filtered_employees = sorted(filtered_employees, reverse=True)
    print("{:<20} {:<20}".format("Name", "Job Title"))
    print("-" * 40)
    for salary, name, job_title in filtered_employees:
        print("{:<20} {:<20}".format(name, job_title))

# Prompt user for file name
while True:
    file_name = input("Please enter the name of the employee data file: ")
    try:
        with open(file_name, "r") as file:
            # Read employee data from file and store in a list of tuples
            employees = []
            for line in file:
                name, job_title, salary = line.strip().split(",")
                employees.append((name, job_title, int(salary)))

            # Print list of employees to verify data was read correctly
            print("List of employees in file {}:".format(file_name))
            for employee in employees:
                print(employee)

            # Prompt user for salary range and filter employees
            while True:
                salary_range = input("Please enter a salary range (min,max), or 'quit' to exit: ")
                if salary_range.lower() == "quit":
                    break
                try:
                    min_salary, max_salary = map(int, salary_range.split(","))
                    filter_employees(employees, min_salary, max_salary)
                except ValueError:
                    print("Invalid input. Please enter a valid salary range or 'quit' to exit.")
            break
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
