def func(word): 
    lst=list(word)
    for i in range(len(lst)): 
        if i%2==0:
            lst[i]=lst[i].upper()
        else: 
            lst[i]=lst[i]
    return lst
print(func('word'))