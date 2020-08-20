from array import *

a=array('i',[10,20,40,100])

print(a[2])

for i in a:
    print(i,end=' ')
print()
a.insert(1,200)

for i in a:
    print(i,end=' ')

print()
a.remove(a[0])

for i in a:
    print(i,end=' ')
