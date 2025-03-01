# Let's Start
def print_star_grid(rows, cols):
    for row in range(rows):
        for col in range(cols):
            print('*', end=' ')
        print()

# Define these
rows = 3
cols = 5

# print it
print_star_grid(rows, cols)
