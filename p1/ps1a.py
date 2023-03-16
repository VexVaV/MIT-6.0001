

total_cost = 0
portion_down_payment = 0.25
current_savings = 0
r= 0.04

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

monthly_saving = (annual_salary / 12) * portion_saved
numbers_of_months = 0

while total_cost * portion_down_payment > current_savings:
    additional_saving = current_savings * r / 12
    current_savings = current_savings + additional_saving + monthly_saving
    numbers_of_months += 1
print("Number of months",numbers_of_months)