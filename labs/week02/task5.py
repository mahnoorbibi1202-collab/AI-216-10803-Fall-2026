# Applicant 1
age = 19
programming_score = 72
prerequisite_completed = True

print("Applicant 1")

if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Eligible")
else:
    print("Not Eligible")

if age < 18:
    print("Age requirement not met")
if programming_score < 60:
    print("Programming score requirement not met")
if not prerequisite_completed:
    print("Prerequisite course not completed")


# Applicant 2
age = 18
programming_score = 60
prerequisite_completed = True

print("\nApplicant 2")

if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Eligible")
else:
    print("Not Eligible")

if age < 18:
    print("Age requirement not met")
if programming_score < 60:
    print("Programming score requirement not met")
if not prerequisite_completed:
    print("Prerequisite course not completed")


# Applicant 3
age = 17
programming_score = 55
prerequisite_completed = False

print("\nApplicant 3")

if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Eligible")
else:
    print("Not Eligible")

if age < 18:
    print("Age requirement not met")
if programming_score < 60:
    print("Programming score requirement not met")
if not prerequisite_completed:
    print("Prerequisite course not completed")
