def func(n): 
    for i in range(n): 
        yield i**2
res=1
for i in func(5): 
    res=i
# guess the output 
print(res)
