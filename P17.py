num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
