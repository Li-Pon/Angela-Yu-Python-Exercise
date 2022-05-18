student_heights = input("Input a list of student height ").split(",")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
number = 0
for i in student_heights:
    total += i
    number += 1

average = round(total/number)

print(f"Average height is {average}")
