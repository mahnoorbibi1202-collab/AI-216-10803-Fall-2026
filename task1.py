# Input: food_expense, transport_expense, other_expense, daily_budget
# Processing: Calculate total_expense, remaining_budget, and budget status
# Output: Print total_expense, remaining_budget, and status

# 1. Input Values (Directly stored as integers)
food_expense = 450
transport_expense = 200
other_expense = 150
daily_budget = 1000

# 2. Processing (Calculations)
total_expense = food_expense + transport_expense + other_expense
remaining_budget = daily_budget - total_expense

# 3. Decision Logic
if total_expense < daily_budget:
    status = "Within budget"
elif total_expense == daily_budget:
    status = "Exactly at budget"
else:
    status = "Over budget"

# 4. Output Display
print(f"Total expense: {total_expense}")
print(f"Remaining budget: {remaining_budget}")
print(f"Status: {status}")
