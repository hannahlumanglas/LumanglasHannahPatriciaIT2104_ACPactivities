str = input("Enter a string: ")
vowel_list = []

for char in str:
    if char in 'aeiouAEIOU' :
        vowel_list.append(char)

print(vowel_list)