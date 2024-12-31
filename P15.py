n=int(input('Enter Number:'))
for i in range(1, n+1):
    print("Multiplication Table for", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
