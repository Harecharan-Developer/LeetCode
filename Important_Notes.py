print(print())
print("----------------------------------------------------------------")
print(print(1))
print("----------------------------------------------------------------")
print(print("Hello, world!"))
print("----------------------------------------------------------------")
print(print(True))

#print returns None object in c however, it returns the successful no of elements printed  in console
x="".join(reversed("Hello, world!"))
print(x)
x=(list(reversed([1,2,3])))
print(x)

# if u dont include the list(reversed) or .join(reversed) it will return a object of type reverse