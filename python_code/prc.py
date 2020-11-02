count=0
n=input()
n=list(n)
lst=[]
def func(i,n): 
    count=0
    for o in list(n):
        if o==i:
            count+=1
        else: 
            continue
    return count 
for i in n:
    count=func(i,n)
    if count%2==0:
        continue
    else: 
      lst.append(i)
m=set(lst)
m=list(m)
m.sort()
if len(m)!=0:
    p="".join(str(e) for e in m)
    print(p)
else: 
    print("Empty String")


    