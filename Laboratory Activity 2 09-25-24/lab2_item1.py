number = int(input("Enter an integer: "))

str_num = str(number)

if str_num == str_num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")