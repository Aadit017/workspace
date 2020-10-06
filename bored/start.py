# basic salary 
sal=int(input(" enter your salary annual income please "))
if sal>1000 and sal <2001: 
    sal=sal*0.5+sal
elif sal>2001 and sal<5001:
     sal=sal*2.5+sal 
else: 
    sal=sal*10+sal 
print('you total salary is ',sal)