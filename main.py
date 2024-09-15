# input statements
salary = float(input("Enter your salary: "))
numDependents = float(input("Enter the number of dependents: "))

# tax rates
stateTaxRate = 0.065 
federalTaxRate = 0.28
dependentDeductionRate = 0.025

# calculate state tax here
stateTax = round(salary * stateTaxRate, 2)
federalTax = round (salary * federalTaxRate, 2)
dependentDeduction = round (numDependents * dependentDeductionRate * salary, 2)
totalWithholding = round (stateTax + federalTax + dependentDeduction, 2)

#calculate take-home pay here
takeHomePay = salary - totalWithholding

# output statements
print('State Tax: $' + str(stateTax))
print('Federal Tax: $' + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))