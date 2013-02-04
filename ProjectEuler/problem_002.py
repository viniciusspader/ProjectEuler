# Initiate fibonacci list with the numbers out of the rule
fibonacci = [1, 2]

# Initiate the counter variables
new_fibonacci = 0
sum_even = 0

while new_fibonacci < 4000000:

    # Calculate the new fibonacci with the last two number on the sequence
    new_fibonacci = fibonacci[-1] + fibonacci[-2]

    # Append the new fibonacci number to the list
    fibonacci.append(new_fibonacci)

    # If the new number is even, sum it to the result
    if new_fibonacci % 2 == 0:
        sum_even += new_fibonacci
    else:
        pass

# I added 2 here because this number don't pass the loop, once it is already
# on the list
print sum_even + 2