import math

print("Hello! I am your Earned Value Management Buddy.")

# How much is completed so far
percent_complete = int(input("Please enter the completion percentage of the project (do not include the '%'): "))

# How many days have passed
days_into_project = int(input("Please enter how many days into the project you are: "))

# How many days will the project last total
planned_project_length = int(input("How many days the project will last: "))

# Budget at Completion (BAC) or Budgeted Cost 

budget_at_completion = int(input("Please enter the budget at completion: "))

# Actual Cost (AC)
actual_cost = int(input("Please provide the actual cost of the project up to now: "))

# Custom rounding function
def custom_round(value):
    if value % 1 == 0.5:
        return float(math.ceil(value))
    else:
        return float(round(value, 2))

# Planned Value (PV)
# PV = (Planned % Complete) X (BAC)
planned_percent_complete = round((days_into_project / planned_project_length) * 100,0)

planned_value = custom_round((planned_percent_complete * budget_at_completion) / 100)

pv_formatted = '${:,.2f}'.format(planned_value)
print(f"Planned value: {pv_formatted}")

# Earned Value (EV)
# EV = (% Complete) X (BAC)
earned_value = custom_round(budget_at_completion * (percent_complete / 100))

ev_formatted = '${:,.2f}'.format(earned_value)
print(f"Earned value: {ev_formatted}")

# Schedule Variance (SV)
# SV = EV - PV
schedule_variance = custom_round(earned_value - planned_value)

sv_formatted = '${:,.2f}'.format(schedule_variance)

if schedule_variance < 0:
    print(f"Project is behind schedule with a SV of {sv_formatted}")
elif schedule_variance > 0:
    print(f"Project is ahead of schedule with a SV of {sv_formatted}")
else:
    print(f"Project is on schedule with a SV of {sv_formatted}")

# Schedule Performance Index (SPI)
# SPI = EV/PV
schedule_performance_index = round(earned_value / planned_value,3)

if schedule_performance_index < 1:
    print(f"Project is behind schedule with a SPI of {schedule_performance_index}")
elif schedule_performance_index > 1:
    print(f"Project is ahead of schedule with a SPI of {schedule_performance_index}")
else:
    print(f"Project is on schedule with a SPI of {schedule_performance_index}")

# Cost Variance (CV)
# CV = EV – AC
cost_variance = custom_round(earned_value - actual_cost)

cv_formatted = '${:,.2f}'.format(cost_variance)

if cost_variance < 0:
    print(f"Project is over budget with a CV of {cv_formatted}")
elif cost_variance > 0:
    print(f"Project is under budget with a CV of {cv_formatted}")
else:
    print(f"Project is on budget with a CV of {cv_formatted}")

# Cost Performance Index (CPI)
# CPI = EV/AC
cost_performance_index = round(earned_value / actual_cost,3)

if cost_performance_index < 1:
    print(f"Project is over budget with a CPI of {cost_performance_index}")
elif cost_performance_index > 1:
    print(f"Project is under budget with a CPI of {cost_performance_index}")
else:
    print(f"Project is on budget with a CPI of {cost_performance_index}")

# Estimated Cost at Completion 
# EAC = BAC / CPI
est_cost_at_completion = custom_round(budget_at_completion / cost_performance_index)

eac_formatted = '${:,.2f}'.format(est_cost_at_completion)

if est_cost_at_completion > budget_at_completion:
    print(f"This EAC of {eac_formatted} is the average you need to plan to correct by or prepare to incur the cost of. This is because it is greater than the BAC (Budget at Completion)")
else:
    print(f"EAC is {eac_formatted}")

# Variance at Completion (VAC)
# VAC = BAC - EAC
variance_at_completion = custom_round(budget_at_completion - est_cost_at_completion)

vac_formatted = '${:,.2f}'.format(variance_at_completion)
print(f"The VAC is {vac_formatted}")
