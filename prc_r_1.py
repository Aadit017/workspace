from random import shuffle 
def func(list):
    shuffle(list)
    return list
def inputt():
    
    guess=" "
    while guess not in['0','1','2']: 
        guess=input("please enter the value ")
    guess=int(guess)
    shuffled=[" ","0"," "]
    func(shuffled)
    if shuffled[guess]=="0":
        print(" yes it is correct ")
        print(shuffled)
        print(" wanna play again ")
 
        ans=input("type yes ")
        if ans=='yes': 
            normal()
    else: 
        print(" wrong ")
        inputt()    

def normal(): 
    print(" the org value of 0 in the list is [" ",0," "] ") 
    inputt()
print(" the org value of 0 in the list is [" ",0," "] ") 
inputt()