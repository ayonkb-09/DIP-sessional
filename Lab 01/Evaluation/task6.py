subject = input("Enter subject name (Math/Physics/English): ").lower()
if subject == "math":
    marks = math_marks
elif subject == "physics":
    marks = physics_marks
elif subject == "english":
    marks = english_marks
else:
    print("Invalid subject name.")
    marks = None

if marks is not None:
    if 80 <= marks <= 100:
        grade = "A+"
    elif 70 <= marks <= 79:
        grade = "A"
    elif 60 <= marks <= 69:
        grade = "A-"
    elif 50 <= marks <= 59:
        grade = "B"
    else:
        grade = "F"
    print(f"Grade for {subject.title()}: {grade}")