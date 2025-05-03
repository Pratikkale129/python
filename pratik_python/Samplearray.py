cars = ['BMW','Buggati','Lamborghini','Dodge','Rolls Royace','Bentley']
print(cars)
print(cars[1])


import array as arr
array1 = arr.array('i',[3,6,9,4,1])
print(array1[:3])


import array as arr
array1 = arr.array('i',[3,6,9,4,1])
print("Before Changing Elements")
print(array1)
array1[2] = 2
print("\nAfter Changing Elements")
print(array1)


import array as arr
array1 = arr.array('i',[3,6,9,4,1])
print("Before Deleting Elements")
print(array1)
del array1[2]
print("\nAfter Deleting Elements")
print(array1)


import array as arr
array1 = arr.array('i',[3,6,9,4,3,4,3,8,1])
print(len(array1))


import array as arr
array1 = arr.array('i',[3,6,9,4,3,4,3,8,1])
# print(len(array1))
array2 = arr.array('i',[2,3,4,6,7])
add = array1 + array2
print(add)