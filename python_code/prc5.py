n=int(input())
line=input().strip()
line=line.split(' ')
c=[]
def func(i,c): 
    arr=[]
    count=0
    for o in c:
        if o==i: 
            arr.append(o)
            
            break            
        else :
            arr.append(o)

    for p in arr: 
        if p>i:
            print(arr)
            count+=1
        else: 
            continue
    print(count)
    return count
arra=[]
for i in range(len(line)):
    c.append(line[i])
cc=0
for i in c:
    cc=func(i,c)
    arra.append(cc)
total=0
for i in arra: 
    total=total+i
print(total)
    
