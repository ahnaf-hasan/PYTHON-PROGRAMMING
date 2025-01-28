#Let's Start
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test these
print(is_prime(17))  #  That's True
print(is_prime(99))  #  That's False
