def print_fibonacci_series(n):
  a, b = 0, 1
  print("Fibonacci Series:")
  for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
  print()

num_terms = 10
print_fibonacci_series(num_terms)