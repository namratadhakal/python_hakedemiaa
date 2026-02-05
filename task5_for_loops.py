  
## Marks Analyzer 

n=int(input("Enter the total no of subjects:"))
marks=[]
for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / n
highest = max(marks)
lowest = min(marks)

print("\n--Marks Analyzer")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")