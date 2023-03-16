

total_cost = 0
portion_down_payment = 0.25
current_savings = 0
r= 0.04
semi_annual_raise = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

numbers_of_months = 0

while total_cost * portion_down_payment > current_savings:
    monthly_saving = (annual_salary / 12) * portion_saved
    additional_saving = current_savings * r / 12
    current_savings = current_savings + additional_saving + monthly_saving
    numbers_of_months += 1
    if numbers_of_months % 6 == 0:
        annual_salary = annual_salary + annual_salary * semi_annual_raise
print("Number of months",numbers_of_months)