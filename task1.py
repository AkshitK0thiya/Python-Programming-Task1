print("List :")
my_list = [1, 2, 3, 4]
print("Original List:", my_list)
my_list.append(5)
print("After Adding 5:", my_list)
my_list.remove(2)
print("After Removing 2:", my_list)
my_list[2] = 10
print("After Modifying Element at Index 2:", my_list)
print()


print("Tuple :")
my_tuple = (1, 2, 3, 4)
print("Original Tuple:", my_tuple)
new_tuple = my_tuple + (5,)
print("After Adding 5:", new_tuple)
temp_list = list(my_tuple)
temp_list.remove(2)
new_tuple = tuple(temp_list)
print("After Removing 2:", new_tuple)
temp_list[2] = 10
new_tuple = tuple(temp_list)
print("After Modifying Element at Index 2:", new_tuple)
print()


print("Set :")
my_set = {1, 2, 3, 4}
print("Original Set:", my_set)
my_set.add(5)
print("After Adding 5:", my_set)
my_set.remove(2)
print("After Removing 2:", my_set)
my_set.remove(3)
my_set.add(10)
print("After Modifying 3 to 10:", my_set)
print()


print("Dictionary :")
my_dict = {'Ravi': 1, 'Akshit': 2, 'Kishan': 3}
print("Original Dictionary:", my_dict)
my_dict['Aelish'] = 4
print("After Adding {'Aelish': 4}:", my_dict)
del my_dict['Ravi']
print("After Removing Key 'Ravi':", my_dict)


