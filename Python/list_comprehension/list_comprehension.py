# list comprehension = a way to  create a new list with less syntax
#                        can mimic certain lambda functions, easier to read
#                        list = [expression for item in iterable]
#                        list = [expression for item in iterable if conditional]
#                        list = [expression if/else for item in iterable]

students = [100,34,23,54,22,33,44,55,87]

passed_students = [student for student in students if student>35]
print(passed_students)

passed_students_appending = [student if student>35 else "FAILED" for student in students]
print(passed_students_appending)

square = [student**2 for student in students]
print(square)
