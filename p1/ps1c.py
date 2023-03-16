total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
r= 0.04
semi_annual_raise = .07
months = 36
min_rate = 0
max_rate = 10000
steps = 0
found = False

starting_salary = float(input("Enter your starting annual salary: "))
portion_saved = int((max_rate + min_rate) / 2)


while abs(min_rate - max_rate) > 1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12) * (portion_saved / 10000)
    current_savings = 0.0
    
    for i in range(1, months + 1):
        additional_saving = current_savings * r / 12
        current_savings += additional_saving + monthly_saved
        
        if abs(current_savings - portion_down_payment * total_cost) < 100:
            min_rate = max_rate
            found = True
            break
        elif current_savings > portion_down_payment * total_cost + 100:
            break
        
        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_saved = (annual_salary / 12) * (portion_saved / 10000)
    if current_savings < portion_down_payment * total_cost - 100:
        min_rate = portion_saved
    elif current_savings > portion_down_payment * total_cost - 100:
        max_rate = portion_saved
    
    portion_saved = int((max_rate + min_rate) / 2)
if found:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search", steps - 1)
else:
    print("Is is not possible to pay the down payment in three years")