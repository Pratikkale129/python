#1. Change Tuple values
Ash = ("Pikachu","Bulbasaur","Squirtle")
y = list(Ash)
y[1] = "Charmendor"
Ash = tuple(y)
print(Ash)

#2. Add items
Ash = ("Pikachu","Bulbasaur","Squirtle")
y = list(Ash)
y.append("Gangar")
Ash = tuple(y)
print(Ash)

#3. Add tuple to a tuple
Ash = ("Pikachu","Bulbasaur","Squirtle")
y = ("Charmendor",)
Ash += y
print(Ash)

#4. Remove Items
Ash = ("Pikachu","Bulbasaur","Charmendor")
y = list(Ash)
y.remove("Bulbasaur")
Ash = tuple(y)
print(Ash)

#5. Delete Tuple
Pratik = ("Apple","Banana","Cherry")
del Pratik
print(Pratik)
