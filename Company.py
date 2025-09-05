from employee import Employee, SalaryEmployee, HourlyEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employee(self):
        print('Current Employee')
        for i in self.employees:
            print(i.fname, i.lname)

    def payemployess(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('-----------------------')
    

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Jack', 'DK', 50000)    
    my_company.add_employee(employee1)    

    employee2 = HourlyEmployee('Mac', 'Jaade', 25, 50)    
    my_company.add_employee(employee2)    

    # employee3 = Employee('Ibu', 'Ngo', 50000)    
    # my_company.add_employee(employee3)    

    my_company.display_employee()
    my_company.payemployess()

main()