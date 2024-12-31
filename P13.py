def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Example usage
number = 5  # Change this number to compute a different factorial
result = factorial(number)
print("The factorial of", number, "is", result)
