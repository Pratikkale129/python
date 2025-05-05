'''
#Python Arrays
# list of similar datatype elements

list1 = ['Amit','Neha','Rupam','Rani','Kajal','Piyush']
print(list1)
print(list1[3:])



import array as arr
# define Array Elements variable
array1 = arr.array('i',[3,8,1,4,7])

print(array1[2:4])



import array as arr
# define Array Elements variable
array1 = arr.array('i',[3,8,1,4,7])
print('Before Changing')
print(array1)
# Change the element value 1 of 9
array1[2] = 9
print('\nAfter changing')
print(array1)




import array as arr
#Delete Elements from an Array
array1 = arr.array('i',[3,8,1,4,7])
print('Before deleting element')
print(array1)

del array1[2]
print('After Delete array element')
print(array1)'''


# find length of array
import array as arr
#Delete Elements from an Array
array1 = arr.array('i',[3,8,1,4,7,9,5,4])
print(len(array1))



# Join two array lists
import array as arr
#Delete Elements from an Array
array1 = arr.array('i',[3,8,1,4,7])
array2 = arr.array('i',[5,2,8,1,6])
add = array1 + array2
print(add)