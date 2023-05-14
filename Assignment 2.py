# A nested list/two-dimension array obtained from ChatGPT that contains employee records
# Each employee record consists of employee name, gender, age, job title and monthly income
employees = [
    ['John Smith', 'Male', 32, 'Software Developer', 5500],
    ['Mary Johnson', 'Female', 28, 'Marketing Manager', 6000],
    ['David Lee', 'Male', 45, 'Senior Project Manager', 8000],
    ['Lisa Chen', 'Female', 36, 'Financial Analyst', 6500],
    ['Robert Brown', 'Male', 29, 'Data Scientist', 7000],
    ['Samantha Davis', 'Female', 33, 'Operations Manager', 7500],
    ['Michael Wilson', 'Male', 41, 'IT Manager', 8500],
    ['Emily White', 'Female', 27, 'HR Specialist', 5000],
    ['Daniel Kim', 'Male', 38, 'Sales Director', 9000],
    ['Julia Wang', 'Female', 30, 'Product Manager', 7000],
    ['Andrew Taylor', 'Male', 31, 'UX Designer', 6000],
    ['Sarah Lee', 'Female', 24, 'Customer Service Representative', 4000],
    ['Peter Chen', 'Male', 27, 'Front-end Developer', 5500],
    ['Grace Lee', 'Female', 42, 'Accounting Manager', 8000],
    ['James Zhang', 'Male', 35, 'Business Analyst', 7000],
    ['Sophia Wang', 'Female', 29, 'Marketing Coordinator', 4500],
    ['William Liu', 'Male', 33, 'Back-end Developer', 6500],
    ['Olivia Chen', 'Female', 26, 'Graphic Designer', 5500],
    ['Edward Wu', 'Male', 39, 'IT Support Technician', 4500],
    ['Catherine Lee', 'Female', 31, 'Project Coordinator', 5500]
]

# Week 1: Variables, comments and calculations
# Week 5: User defined function, default arguments and multiple returns

# A function that calculate income tax deduction and superannuation deduction
# It accepts income, tax rate (optional) and Super rate (optional)
# It returns tax deduction and Super deduction
def calculate_tax_and_super_deduction(income, tax_rate=0.2, super_rate=0.1):
    income_tax_deduction = income * tax_rate
    superannuation_deduction = income * super_rate
    return income_tax_deduction, superannuation_deduction


# Week 3: append() function to add an element to the end of a list
# Week 3: extend() function to add multiple elements
# Week 4: For Loop

# A function that adds tax deduction and Super deduction to employee record
# It accepts a list of employee records. Each record consist of employee name, gender, age, job title and income
# It returns a list of extended employee records.
# Each record consist of employee name, gender, age, job title, income, tax deduction and Super deduction
def add_deductions_to_employees_information(employees):
    extended_employees_information = []
    for employee in employees:
        tax_deduction, super_deduction = calculate_tax_and_super_deduction(employee[4])
        employee.extend([tax_deduction, super_deduction])
        extended_employees_information.append(employee)
    return extended_employees_information


# Week 2: If and Else Statement
# Week 4: While Loops
# Week 7: Joining Strings
# External resource: isinstance() Function

# A while loop to capture each element in the nested list
# If statement and isinstance() function to test if 'each element is string datatype' is True
# Else statement will convert False (non-string) elements into stings
# Use .join() method to joining strings using the delimiter comma','
# to convert employees nested list into a .csv format, which is easier to import or edit for future use
outer_loop_iteration = 0
while outer_loop_iteration < len(employees):
    inner_loo_iteration = 0
    while inner_loo_iteration < len(employees[outer_loop_iteration]):
        field = employees[outer_loop_iteration][inner_loo_iteration]
        if isinstance(field, str):
            pass
        else:
            employees[outer_loop_iteration][inner_loo_iteration] = str(field)
        inner_loo_iteration += 1
    employee_record_separated_by_comma = ','.join(employees[outer_loop_iteration])
    print(employee_record_separated_by_comma)
    outer_loop_iteration += 1













