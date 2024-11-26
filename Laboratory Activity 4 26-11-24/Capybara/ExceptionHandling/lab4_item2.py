try:
    size = int(input("Enter the size of the array: "))
    print("Enter the elements of the array:")
    arr = [float(input()) for _ in range(size)]
    IntputNum = int(input("Enter the index of the element to print: "))
    print(f"Element at index {IntputNum}: {arr[IntputNum]:.2f}")
except IndexError:
    print(f"Index { IntputNum} is invalid.")