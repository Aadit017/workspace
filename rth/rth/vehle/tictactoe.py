from keyboard import *
board=['1','2','3','4','5','6','7','8','9']
def display(board,a): 
    print('\n'*50)
    print(board[6]+"|"+board[7]+"|"+board[8])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[0]+"|"+board[1]+"|"+board[2])
    print('\n'*2)
    c=a
    inputt(board,c)
def inputt(board,a):
  
    turn_1,turn_2,turn=0,0,0
    ch='x'
    c=a
   
    if c==0:
    
            turn_1=int(input("players ones turn "))
         
            turn=turn_1-1
            ch='x'
       
    else:
  
            turn_2=int(input("players twos turn "))
           
            turn=turn_2-1
            ch='o'
    logic(board,turn,ch,c)
def logic(board,turn,ch,a):
    c=a
    winner=" "
    if ch=='x': 
        board[turn]='X'
    else:
        board[turn]='O'
    if board[0]==board[1]==board[2] or board[0]==board[3]==board[6] or board[0]==board[4]==board[8]:
        if board[0]=='X':
            winner="player one"
            replay(board,winner)
        else: 
            winner="player two"
            replay(board,winner)
        
    elif board[1]==board[4]==board[7]:
         if board[1]=='X':
            winner="player one"
            replay(board,winner)
         else: 
            winner="player two"
            replay(board,winner)
    elif board[2]==board[5]==board[8] or board[2]==board[4]==board[6]:
         if board[2]=='X':
            winner="player one"
            replay(board,winner)
         else: 
            winner="player two"
            replay(board,winner)
    elif board[3]==board[4]==board[5]:
         if board[3]=='X':
             winner="player one"
             replay(board,winner)
         else:
             winner="player two"
             replay(board,winner)
    elif board[6]==board[7]==board[8]:
         if board[6]=='X':
             winner="player one"
             replay(board,winner)
         else:
             winner="player two"
             replay(board,winner)
    else: 
        if c==0:
            display(board,1)
        else:
            display(board,0)
def replay(board,winner): 
    board_1=['1','2','3','4','5','6','7','8','9']
    print('\n'*100)
    print(board[6]+"|"+board[7]+"|"+board[8])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("winner is "+winner.upper())
    again=" "
    a=0
    while again not in (['Yes','No']):
        again=input("wanna play again :'Yes' or 'No'")
    if again=='Yes': 
        print("press enter to be sure")
        display(board_1,a)
    else: 
  
        print('ThankYou')
a=0
display(board,a  )
 # we have to write a code as to what happens when there is a tie 
 # when ever a person enters an argument which is invalid ... app. msg    
   
   