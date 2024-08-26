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

name = input("Enter employee name:\n")
hours = int(input("Enter hours worked:\n"))
code = input("Enter position code:\n")

# TODO add calculations

print("            BoxMart Pay Stub")
print()
print(f"Employee Name: {name}")  

# TODO complete print