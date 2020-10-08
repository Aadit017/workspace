def one(n): 
    return [str(x) for x in range(n)]
def two(n):
    return list(map(str,range(n)))
import time as t 
start_time=t.time()
result=one(1000000)
end_time=t.time()
elapsed_time=end_time - start_time
print(elapsed_time)

 