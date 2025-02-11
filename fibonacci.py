#  Let's Start and generate Fibonacci sequence
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Input 
num_terms = int(input("Enter the number of terms: "))

# Fibonacci sequence
if num_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for num in fibonacci_sequence(num_terms):
        print(num)
