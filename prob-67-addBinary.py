


a = "111"     # 7
b = "100"     # 4

# convert to an integer
a = int(a, 2)
b = int(b, 2)

c = a + b

print(c)


# convert back to BINARY.... crop off "0b" from front
c = bin(c)[2:]


print(c)