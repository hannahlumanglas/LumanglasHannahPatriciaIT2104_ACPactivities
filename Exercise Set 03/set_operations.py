set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference_set1 = set1.difference(set2)
difference_set2= set2.difference(set1)

union_set1 = set1.union(set2)

symdiff_set1 = set1.symmetric_difference(set2)
symdiff_set2 = set2.symmetric_difference(set1)

intersection_set1 = set1.intersection(set2)
intersection_set2 = set1.intersection(set1)

print("Set Difference")
print("set1 - set2 :", difference_set1)
print("set2 - set1 :",difference_set2)

print("Union of Sets")
print("set1 | set2 :", union_set1)

print("Symmetric Difference")
print("set2 ^ set set1 :", symdiff_set1)
print("set1 ^ set set2 :", symdiff_set2)

print("Set Intersection")
print("set1 & set2 :", intersection_set1)
print("set1 & set2 :", intersection_set2)