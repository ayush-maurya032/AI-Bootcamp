a = [1, 2]

b = a

print("Before:")
print("a =", a)
print("b =", b)

b.append(3)

print("\nAfter:")
print("a =", a)
print("b =", b)

print(id(a))
print(id(b))