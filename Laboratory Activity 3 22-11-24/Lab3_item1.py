def roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = roman.upper()
    total = 0
    prev_value = 0
    repeat_count = 0
    
    for char in reversed(roman):
        value = roman_values.get(char, 0)
        if value == 0:
            return "Invalid Roman numeral!"
        
        if value == prev_value:
            repeat_count += 1
            if repeat_count > 2:
                return "Invalid Roman numeral!"
        else:
            repeat_count = 0
        
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

roman_input = input("Enter a Roman numeral: ")
result = roman_to_integer(roman_input)
print(f"The integer value of '{roman_input.upper()}' is: {result}")