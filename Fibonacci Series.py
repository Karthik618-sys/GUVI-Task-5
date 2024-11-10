from functools import reduce  # Import reduce function from functools module

# Lambda function to generate Fibonacci series
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Print the first 50 elements of the Fibonacci series
print(fibonacci_series(50))
