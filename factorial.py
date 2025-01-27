#Let's Start
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# For Example
value = 7
print(f"Factorial of {value} is {factorial(value)}")
