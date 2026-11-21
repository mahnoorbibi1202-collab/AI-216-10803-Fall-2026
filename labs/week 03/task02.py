PART - A
score = 90

def show_score():
    score = 70
    print("Inside function:", score)

show_score()
print("Outside function:", score)


def is_qualified(score, threshold):
    return score >= threshold

print(is_qualified(0.90, 0.85))
print(is_qualified(0.80, 0.85))
print(is_qualified(0.85, 0.85))

PART_B
threshold = 0.85

def is_qualified(score, threshold):
    return score >= threshold

print(is_qualified(0.90, 0.85))
print(is_qualified(0.70, 0.85))
print(is_qualified(0.85, 0.85))
