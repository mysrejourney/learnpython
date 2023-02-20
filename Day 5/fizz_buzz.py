for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print(f" {number} : Fizz Buzz")
  elif number % 3 == 0:
    print(f" {number} : Fizz")
  elif number % 5 == 0:
    print(f" {number} : Buzz")
