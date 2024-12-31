import math
def meananddeviation(z):
    s=0
    for i in l:
        s=s+i
    m=s/len(l)
    print('MEAN',m)
    d=0
    for i in l:
        d=d+math.sqrt(((i-m)**2/len(l)-1))
    print('Deviation:',d)

l=[12,34,8,18,44]
meananddeviation(l)
