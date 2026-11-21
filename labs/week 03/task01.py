# Student assessment scores
scores = [78, 85, 92, 67, 88]


# Calculate average of scores
def calculate_average(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)


# Find highest score
def find_highest(scores):
    if len(scores) == 0:
        return None
    return max(scores)


# Count scores above or equal to threshold
def count_above_threshold(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count


# Classify average score
def classify_average(average):
    if average is None:
        return "No valid data"
    elif average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# Call functions and display results
average = calculate_average(scores)
highest = find_highest(scores)
count = count_above_threshold(scores, 80)
result = classify_average(average)

print("Student Scores:", scores)
print("Average Score:", average)
print("Highest Score:", highest)
print("Scores above or equal to 80:", count)
print("Performance:", result)
