scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.96, 0.79]
threshold = 0.85

meeting = 0
below = 0
total = 0

for score in scores:
    total += score

    if score >= threshold:
        meeting += 1
    else:
        below += 1

if len(scores) > 0:
    average = total / len(scores)
    percentage = (meeting / len(scores)) * 100

    print("Meeting target (>= 0.85):", meeting)
    print("Below target:", below)
    print("Average score:", format(average, ".2f"))
    print("Percentage meeting target:", format(percentage, ".2f") + "%")
else:
    print("No scores available")
