# Academic Decision System


attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter total marks (out of 100): "))
if attendance < 75:
    print("Not eligible for exams due to low attendance.")
else:

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Eligible for exams.")
    print(f"Grade : {grade}")

# Scholarship Eligibility Checker

cgpa = float(input("Enter CGPA: "))
income = float(input("Enter annual family income: "))
attendance = float(input("Enter attendance percentage: "))


if cgpa >= 3.2 and income <= 30000 and attendance >= 80:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")
