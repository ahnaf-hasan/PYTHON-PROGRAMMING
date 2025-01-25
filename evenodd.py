#Let's Start
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example

number = 9
print(f"{number} is {check_odd_even(number)}.")
