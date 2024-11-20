def is_perfect_number(number):
    if number <= 0:
        return False
    return sum(divisor for divisor in range(1, number) if number % divisor == 0) == number

while True:
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        if is_perfect_number(num):
            print(f"{num}")
        else:
            print(f"{num}")
    except ValueError:
        print("Please enter a valid integer.")