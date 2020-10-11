alpha="abcdefghijklmnopqrstuvwxyz"
alpha=list(alpha)
value=input()
value=value.lower()
for i in range(len(value)): 
    if value[i]!=' ': 
         if value[i] in alpha: 
             alpha.remove(value[i])
if len(alpha)==0: 
    print('pangram')
else: 
    print('not pangram')
        
        
        
