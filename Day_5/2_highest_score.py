student_score = input("Input a list of student ").split(",")

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

highest_score = 0

for i in student_score:
    if i > highest_score:
        highest_score = i

print(f"Higest score is {highest_score}")
