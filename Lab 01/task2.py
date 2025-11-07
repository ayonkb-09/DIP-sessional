list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)

totalsum = 0

for num in list1:
      totalsum += num

for num in list2:
      totalsum += num

for num in list3:
      totalsum += num

print("The sum of all three lists is:", totalsum)