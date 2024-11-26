from Capybara import Capybara

capybaras = [
    Capybara("Biscoff", "M", 5),
    Capybara("Caramel", "F", 3),
    Capybara("Toffee", "M", 7),
]

try:
    InputNum = int(input("Enter the test case number: "))
    capybara = capybaras[InputNum- 1]
    print(f"Test Case {InputNum} : Name: {capybara.name}, "f"Gender: {capybara.gender}, Age: {capybara.age} years old")
except (ValueError, IndexError):
    print("Invalid test case number.")