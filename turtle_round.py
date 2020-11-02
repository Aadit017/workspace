import turtle  
  
tut = turtle.Screen() 
  
tut.bgcolor("green") 
  
tut.title("Turtle") 
my_pen = turtle.Turtle() 
  

my_pen.color("orange") 
tut = turtle.Screen()            
  
# forming front square face 
for i in range(70): 
    my_pen.forward(100) 
    my_pen.left(90) 
    for o in range(10): 
        my_pen.forward(10)
        my_pen.right(22)
  
