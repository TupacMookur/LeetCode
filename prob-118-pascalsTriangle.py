### PAIRWISE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
### ZIP      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from itertools import pairwise

y = [1,2,3]
z = [2,3,4,5,2,1]
x = list(pairwise(z))
print(x)
x = list(pairwise(y))
print(x)


### START


for a, b in zip(x,x[1:]):
    print(a,b)