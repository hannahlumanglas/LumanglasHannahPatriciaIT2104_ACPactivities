char1, char2  = input("Enter two space-separated characters: ").split()

asciiVal1 = ord(char1)
asciiVal2 = ord(char2)

greater_char = max(char1,char2)

print("--------------------------------")
print("The character with greater value is: ", greater_char)
print("--------------------------------")

print("This part is optional to include.")
print("Showing ASCII Values: ")
print(f"{char1} : {asciiVal1}")
print(f"{char2} : {asciiVal2}")