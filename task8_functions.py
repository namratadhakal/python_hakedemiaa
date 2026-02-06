
def calculate_average(marks,n):  # function for ave_mark calculation
    return sum(marks) / n

# Function for determining grade based on average

def finding_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# ouptut function: 

def format_output(total, average, highest, lowest, grade):
    
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Grade: {grade}")

# Main program
def main():
    n = int(input("Enter number of subjects: "))
    marks = []

    for i in range(n):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = calculate_average(marks,n)
    highest = max(marks)
    lowest = min(marks)
    grade = finding_grade(average)

    format_output(total, average, highest, lowest, grade)

main()  ##calling main function


## 1. Why is returning values better than printing inside functions? 

# Ans : Printing value inside function only shows the output and cannot be used for further calculations. On the other hand, returned value can be reused in other parts of the program thats whay it is better than printing inside the functions.

