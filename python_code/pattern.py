import time 
start=time.time()
for i in range(5): 
	print('#'*(i+1))
# the most easy way to create a pattern program 
print('-----------')
lst=[6,5,4,3,2,1]
for i in lst: 
	print('#'*(i-1))
#017Devs
for i in range(5): 
	if i%2==0:
		print('#'*(i+1))
	else: 
		print('$'*(i+1))
for i in range(5): 
	print("[i]"*(2*i-1))
end=time.time()
print(end-start)