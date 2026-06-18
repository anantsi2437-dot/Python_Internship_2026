# 1. Simple Interest
p = 1000
r = 5
t = 2

si = (p * r * t) / 100
print("Simple Interest =", si)

# 2. Reverse a Number
num = int(input("Enter number: "))
reverse = int(str(num)[::-1])

print("Reverse =", reverse)

# 3. Count Digits
num = input("Enter number: ")
print("Number of digits =", len(num))

# 4. Factorial
num = int(input("Enter number: "))

fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# 5. Square and Cube
num = int(input("Enter number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)