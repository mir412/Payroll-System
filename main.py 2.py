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
code = code.lower()  # Convert code input to lowercase to validate

# Initially set pay to 0
pay = 0

# Check value of code, and assign value of pay accordingly
# If code is not in cashier, clerk or manager, exit code
if code == "cashier":
    pay = 12.25
elif code == "clerk":
    pay = 18
elif code == "manager":
    pay = 25.75
else:
    print("Invalid Code")
    exit()

# Check if hours > 40, if yes calculate overworked hours else set it to 0
if hours > 40:
    normal_hours = 40
    over_worked_hours = hours - 40
else:
    normal_hours = hours
    over_worked_hours = 0

# Calculate normalpay, overpay, grosspay, taxes and netpay
normal_pay = normal_hours * pay
over_worked_pay = pay * 1.5 * over_worked_hours
gross_pay = normal_pay + over_worked_pay

federal_tax = 0
if gross_pay > 500:
    federal_tax = (gross_pay - 500) * 0.10

state_tax = gross_pay * 0.03
net_pay = gross_pay - (federal_tax + state_tax)

def start_date():
    return '01/14/2020'

def end_date():
    return '01/20/2020'

def pay_date():
    return '01/27/2020'

# Print detailed report
print("                 BoxMart Pay Stub")
print()
print(f"Employee Name: {name}")
print("Pay Period:  ", start_date(), 'to', end_date())
print()
print("%-35s%s%d hrs" % ("Normal Hours Worked:", "$ ", normal_hours))
print("%-35s%s%d hrs" % ("Overtime Hours Worked:", "$ ", over_worked_hours))
print("%-35s%s%0.2f/hr" % ("Hourly Wages:", "$ ", pay))
print()
print("%-35s%s%0.2f" % ("Normal Pay:", "$ ", normal_pay))
print("%-35s%s%0.2f" % ("Overtime Pay:", "$ ", over_worked_pay))
print("%-35s%s%0.2f" % ("Gross Pay:", "$ ", gross_pay))
print("%-35s%s%0.2f" % ("Federal Tax:", "$ ", federal_tax))
print("%-35s%s%0.2f" % ("State Tax:", "$ ", state_tax))
print("%-35s%s%0.2f" % ("Net Pay:", "$ ", net_pay))
print()
print("%-35s%s" % ("Box Mart, Inc.", pay_date()))
print("%s%-30s%s%0.2f" % ("Pay to: ", name, "$ ", net_pay)) 

# TODO complete print
