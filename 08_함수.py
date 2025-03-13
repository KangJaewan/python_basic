a = [1,2,3]
print(id(a))
b = a
print(id(b))
c = [1,2,3]
print(id(c))
a[0] = 9
print(b)
print(c)
print(a is b)
print(a is c)
