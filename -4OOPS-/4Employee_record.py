emp1 = Employee('Edward', 'Snowden', 50000)
emp2 = Employee('Julian', 'Assange', 60000)
emp3 = Employee('Larry', 'Page', 85000)
print('Employee1 details =>')
print('Full Name : {}'.format(emp1.fullname()))
print('Actual salary : {}'.format(emp1.pay))
#employee1 raise is different from others
emp1.raise_amount = 1.20
emp1.raiseA()
print('Salary after raise: {}'.format(emp1.pay))
print('\n')
print('Employee2 details =>')
print('Full Name : {}'.format(emp2.fullname()))
print('Actual salary : {}'.format(emp2.pay))
emp2.raiseA()
print('Salary after raise : {}'.format(emp2.pay))
print('\n')
print('Employee3 details =>')
print('Full Name : {}'.format(emp3.fullname()))
print('Actual salary : {}'.format(emp3.pay))
emp3.raise_amount = 1.50
emp3.raiseA()
print('Salary after raise : {}'.format(emp3.pay))
print('\n')
print('Total number of employees registered : {}'.format(Employee.no_of_emps))
