# Task 1: Grades List
# Given list of grades, sort into descending order

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# First, sort them into ascending order
# Then, reverse that order

grades.sort() 
grades.reverse()
print(grades) 

# Task 2: Grade Average
# Find the average Grade and print

average_grade = sum(grades) / len(grades) 
print(average_grade) 