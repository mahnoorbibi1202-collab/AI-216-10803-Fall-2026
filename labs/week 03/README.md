# Week 03

## Task 1 - Function Design & Reuse
Task 2 — Part A: Observe Scope

1. Why are the two values different?

The values are different because the function has its own local variable. The global variable is 90, while the local variable is 70.

2. Which variable is local?

The variable "score = 70" inside the function is local.

3. Which variable is global?

The variable "score = 90" outside the function is global.

Task 2 — Part B: Refactor Hidden State

Testing:

- "is_qualified(0.90, 0.85)" → True
- "is_qualified(0.70, 0.85)" → False
- "is_qualified(0.85, 0.85)" → True

Reflection:

Explicit parameters make functions easier to reuse and test because they receive values directly. They do not depend on hidden global variables.

Task 3 — Create and Use Your Own Module

Purpose of Modules:

Modules help us organize code into separate files and reuse functions in other files.

Functions Created:

- "calculate_average(scores)"
- "is_passing(score, passing_score=50)"
- "count_above_threshold(scores, threshold)"

Main Guard:

The statement "if __name__ == "__main__":" runs the demo code only when the file is executed directly, not when it is imported into another file.
