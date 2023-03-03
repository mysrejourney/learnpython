def prime_check(num):
    count = 0
    for n in range(3, num):
        if num % n == 0:
            count += 1
    if count > 0:
        print(f"{num} : Its not a prime number")
    else:
        print(f"{num} : Its a prime number")
number = int(input("Enter the number: "))
prime_check(number)

