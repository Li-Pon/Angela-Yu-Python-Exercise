student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grade = {}

for key in student_score:
    if student_score[key] >= 91:
        student_grade[key] = "Outstranding"
    elif student_score[key] >= 81:
        student_grade[key] = "Exceeds Expectation"
    elif student_score[key] >= 71:
        student_grade[key] = "Acceptable"
    elif student_score[key] <= 70:
        student_grade[key] = "Fail"


print(student_grade)
