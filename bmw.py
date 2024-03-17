L = []
x = range(1,20)
for y in x:
    L.append(y)
print(L)
m = []    
for z in L:
    n = str(z)
    m.append(n)
print(m)

d = str("1") 
count = 0 
for e in m:
    if d in e:
        count+=1
        
print(count)