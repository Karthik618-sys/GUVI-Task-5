# Sample list containing integers and strings
sample_list = [10, "hello", 20, "world", 30, "Python"]

# Use a lambda function to check the type of each element and map the result to a list
result = list(map(lambda x: "Integer" if isinstance(x, int) else "String", sample_list))

# Print the list of type checks
print(result)
