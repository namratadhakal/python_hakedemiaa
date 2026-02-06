def student_details():  # student details function
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    return name, ID

def enter_marks():  # marks function
    n = int(input("Enter number of subjects: "))
    marks = []
    for i in range(n):
        while True:  
            mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break   
            else:
                print("Please enter marks between 0 and 100")
    return marks

def calculate_average(marks):  # avg calculation function
    return sum(marks) / len(marks)

def finding_grade(average):  # function for finding grade
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

def result_summary(name, ID, marks):  # result summary function
    if not name or not ID: 
        print("Please enter student details first!") 
        return
    if not marks:
        print("Please enter your marks first!!")
        return
    total = sum(marks)
    average = calculate_average(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = finding_grade(average)

    print("\n--- Result Summary ---")
    print(f"Name: {name}")
    print(f"ID: {ID}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Grade: {grade}")

def main():  # main program
    name = ""
    ID = ""
    marks = []

    while True:
        print("\n--- Student Utility System ---")
        print("1. Enter student details")
        print("2. Enter marks")
        print("3. View result summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name, ID = student_details()
        elif choice == "2":
            marks = enter_marks()
        elif choice == "3":
            result_summary(name, ID, marks)
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice!")

main()  # running main


#1. What changes would be required to convert this into a web application? 

#Ans:  To convert it into a web application, we need to create a user interface, handle input/output through browser and add web framework.