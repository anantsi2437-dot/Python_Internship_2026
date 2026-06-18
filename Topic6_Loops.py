# 1. Numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Odd numbers from 1 to 50
for i in range(1, 51, 2):
    print(i)

# 3. Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 4. Sum of first N natural numbers
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# 5. Pattern
for i in range(1, 6):
    print("*" * i)