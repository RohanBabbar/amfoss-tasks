a = int(input())
answerlist=[]

i=int(0)
for i in range (0,a):
    i=i+1
    b = int(input())
    list1 = []
    c = list(map(int,input().strip().split()))[:b]
    l = len(c)
    c.sort()
    s = set(c)
    e = len(s)
    from collections import Counter
    x = 0
    d = Counter(c)
    if ((e == l) and (d[x]==0)):
        mama=(l+1)
    elif d[x]==0:
        mama=(l)
    else:
        mama=(l-d[x])
    answerlist.append(mama)
    
for x in answerlist:
    print(x)
    
    
    
    

