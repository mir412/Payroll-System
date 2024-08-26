'''
Assignment 1 - Boxmart Payroll

This script will on input of an employee name, number of hours worked, and a position code, compute and
print a pay stub and a pay check for the employee.  Rules for computation are as follows:

1. Hourly rate is determined by a position code where a cashier is paid $ 12.25/hr, clerk is paid $ 
   18.00/hr, and manager is paid $ 25.75/hour.
2. If the position code is not one of above, then print "Invalid code", and exit()
3. For everyone except for managers, the hours over 40 in a week are considered to be overtime hours 
   (note normal hours of non-manager's can be at most 40).
4. Normal pay is normal hours times hourly rate.
5. Overtime pay is overtime hours times hourly rate times 1 1/2.
6. Gross pay is the sum of normal pay and overtime pay.
7. Federal tax is 10% of gross pay in excess of 500.
8. State tax is 3% of gross pay.
9. Net pay is gross pay less federal tax and less state tax.
10. Use start_date and end_date functions from the pay_period module to get the pay period dates. See module pay_period.py.
11. Use the pay_date function from the pay_period module to get the date of the check. See module pay_period.py.

Created on Feb 20, 2020

@author: PUT YOUR NAME HERE
'''
name=input("Enter Employee name: \n")
hrs=int(input("Hours worked:\n"))
positionCode=input("Enter position code:\n").lower()
cashierPay,clerkPay,managerPay=12.25,18.00,35.75
if positionCode=='cashier' or positionCode=='manager' or positionCode=='clerk':
    print('          Boxmart Pay Stub')
    print()
    print('Enter name: {}'.format(name))
    print('Pay period:    01/144/2020 to 01/20/2020\n')
    print("Normal Hours worked: ".ljust(30),'{} hrs'.format(hrs))
    overTime=hrs-40
    print("Overtime Hours Worked: ".ljust(30),'{} hrs'.format(overTime))
    if positionCode=='cashier':
        pay=cashierPay
    if positionCode=='clerk':
        pay==clerkPay
    if positionCode=='manager':
        pay==managerPay
    print("Hourly Wage: ".ljust(25),'$ {}/hr'.format(pay))
    print()
    normalPay=40*pay
    print("Normal pay: ".ljust(25),'$ {:.2f}'.format(normalPay))
    overTimerate=pay*1.5*overTime
    print("Overtime Pay: ".ljust(25),'$ {}'.format(round(overTimerate,2)))
    grossPay=normalPay*overTimerate
    print('Gross pay: '.ljust(25),'$ {:.2f}'.format((grossPay)))
    if grossPay>500:
        federalTax=(grossPay-500)*10/100
        print('Federal tax: '.ljust(25),'${:.2f}'.format((federalTax)))
    stateTax=grossPay*3/100
    print('State tax: '.ljust(25),'$ {:.2f}'.format((stateTax)))
    netPay=grossPay-federalTax-stateTax
    print('Net Pay: '.ljust(25),'${:.2f}'.format((netPay)))
          
        
