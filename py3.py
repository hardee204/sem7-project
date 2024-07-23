list1 = ["bvm","adit","mbit","gcet"]
print(list1)
print(list1[2])
print(list1[1:3])
print(list1[:2])
print(list1[-3])
print(len(list1))
print("After update index 2 element")
list1[2] = "bbit"
print(list1)
list1.insert(4,"mbit")
print(list1)
list2 = ["baps","ms_mistry","knowledge","jjis"]
list1.extend(list2)
print(list1)
for x in range(len(list2)):
    print(list1[x])
list1.sort()
print(list1)
list1.pop()
list3 = list2.copy()
print(list3)