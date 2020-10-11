def fib(n): 
    a,b=1,1
    for i in range(n+1):
         yield a
         a,b=b,a+b
for i in fib(5): 
    print(i)
        