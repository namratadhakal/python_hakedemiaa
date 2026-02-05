## basic financial calculator

monthly_income = float(input("Enter your monthly income: "))
monthly_expences =float(input("Enter your monthly expenses:"))
savings = monthly_income - monthly_expences
print(f"savings:{savings}")

# without typecasting:  " TypeError: unsupported operand type(s) for -: 'str' and 'str' "   is returned.


# 1. Why does Python delay type errors until runtime, unlike compiled languages?
#Ans: In compiled languages, compiler check the code before execution so catch errors early. But in python type errors is detected only when the line executes which results in delay type errors.

# 2. How could unvalidated user input compromise real-world systems?
# Ans: In the real world, unvalidated input can lead to errors, fraud or even security breaches. 
# For eg, if a user enter text instead of numbers, calculation could fail or give incorrect output.