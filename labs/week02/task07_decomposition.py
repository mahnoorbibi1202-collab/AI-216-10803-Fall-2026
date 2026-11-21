# Problem: Analyze student attendance.
# Inputs: Attendance percentages of students.
# Rules: 75% or above is eligible.
# Repetition: Check each student's attendance.
# Outputs: Eligible count, below requirement count and percentage.

# Attendance percentages
attendance = [82, 74.9, 75, 91, 60, 88, 70]

eligible = 0
below_requirement = 0

# Check each student's attendance
for percentage in attendance:
    if percentage >= 75:
        eligible = eligible + 1
    else:
        below_requirement = below_requirement + 1

# Calculate eligible percentage
total_students = len(attendance)
eligible_percentage = (eligible / total_students) * 100

# Print results
print("Eligible (>= 75%):", eligible)
print("Below requirement:", below_requirement)
print("Eligible percentage:", round(eligible_percentage, 2), "%")
