from employee import Developer, Designer, Manager

employees = [
    Developer("Sajad", 1200),
    Designer("Roya", 1000),
    Manager("Nastaran", 1500),
]

for employee in employees:
    employee.show_info()
    print("Work:", employee.work())
    print()
