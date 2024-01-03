student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
for x in student_heights:
    total_height += x
print(total_height)
num_student = 0
for x in student_heights:
    num_student += 1
print(num_student)
average_height = round(total_height / num_student)
print(f"The Average height of the class is {average_height}")
