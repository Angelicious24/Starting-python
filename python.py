
fruits = [ "apple", "banana", "grape", "cherry"]
    
for fruit in fruits:
    if fruit == "grape":
      break
    print(fruit)
    
print()
for fruit in fruits:
    if fruit == "grape":
        continue
    print(fruit)
    
print()
for fruit in fruits:
    if fruit == "grape":
        pass
    print(fruit)


