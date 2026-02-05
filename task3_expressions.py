# Student Performance Score Calculator

# for input
assignment_score = float(input("Enter assignment score (out of 100): "))
lab_score = float(input("Enter lab score (out of 100): "))
exam_score = float(input("Enter exam score (out of 100): "))

#  weights: 20% assignments, 30% labs, 50% exams)
final_score = (assignment_score * 0.3) + (lab_score * 0.2) + (exam_score * 0.5)

print("\n-- Student Performance Report --")
print(f"Assignment Score: {assignment_score}")
print(f"Lab Score: {lab_score}")
print(f"Exam Score: {exam_score}")
print(f"Final Weighted Score: {final_score}")


# 1. Why is operator precedence critical in scientific or financial software? 

# Ans :operator precedence is critical in scientific or financial software as it determines the accuracy of calculations and maintains the financial integrity.

#2. 2. How could floating-point precision errors affect real-world applications? 

# Ans: Computers cannot store decimal nos and tiny errors happens in calculations and over the time small errors can add up giving the wrong results in the real world systems.
