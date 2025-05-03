# Accessing Array Elements
import array as arr    
a = arr.array('i', [2, 4, 5, 6])    
print("First element is:", a[0])    
print("Second element is:", a[1])   
print("Third element is:", a[2])  
print("Forth element is:", a[3])  
print("last element is:", a[-1])    
print("Second last element is:", a[-2])    
print("Third last element is:", a[-3])    
print("Forth last element is:", a[-4])    
print(a[0], a[1], a[2], a[3], a[-1],a[-2],a[-3],a[-4])  


# Change or Add Elements
Numbers = arr.array('i', [12,7,2,4,5,6])
Numbers[0] = 11
print(Numbers)

Numbers[1:3] = arr.array('i',[10,8,3])
print(Numbers)


# Delete Array Element
Numbers = arr.array('i', [12,7,2,4,5,6])
del Numbers[3]
print(Numbers)


