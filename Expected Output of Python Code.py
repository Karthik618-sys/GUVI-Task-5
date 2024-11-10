data = [10, 501, 22, 37, 100, 999, 87, 351]  # Original list of numbers
# Filter the numbers to only include those greater than 4
result = filter(lambda x: x > 4, data)
# Convert the filter object to a list and print it
print(list(result))
