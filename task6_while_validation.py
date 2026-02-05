#   Validation with while Loops


n = int(input("Enter number of subjects: "))

marks = []
for i in range(n):
    while True:  
        mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
        if 0 <= mark <= 100:
            marks.append(mark)
            break   
        else:
            print("Please enter marks btn 1 to 100")

print("\n--- Marks Analyzer ---")
print(f"Total Marks: {sum(marks)}")
print(f"Average Marks: {sum(marks)/n}")
print(f"Highest Marks: {max(marks)}")
print(f"Lowest Marks: {min(marks)}")


# 1. Why is validation better handled with while loops than for loops? 

# Ans: we use for loop if the number of iteration is fixed. But we don't know how many times the user is going to input invalid data.  So, validatiion is better handled with while loop as it keep asking untill the input data is entered.