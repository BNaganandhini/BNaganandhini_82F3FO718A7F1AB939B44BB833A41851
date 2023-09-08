def factorial(n):
  if (n == 1 or n == 0):
    return 1
  else:
    return n * factorial(n - 1)


number = 6
result = factorial(number)
print("The factorial of", number, "is", factorial(number))
