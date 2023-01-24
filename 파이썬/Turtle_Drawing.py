import turtle

myT = turtle.Turtle()
myT.shape("turtle")


myT.fillcolor('skyblue')
myT.begin_fill()
for i in range(0,4):
    myT.forward(300)
    myT.right(90)
myT.end_fill()
myT.left(180)

myT.fillcolor("greenyellow")
myT.begin_fill()
for i in range(0,2):
    myT.right(120)
    myT.forward(300)
myT.end_fill()    

myT.right(30)
myT.forward(150)
myT.right(90)
myT.forward(100)
myT.left(90)
myT.forward(75)

myT.fillcolor("orange")
myT.begin_fill()
myT.circle(10)
myT.end_fill()

myT.forward(75)
myT.penup()
myT.right(90)
myT.forward(100)
myT.right(90)
myT.forward(250)

myT.fillcolor('white')
myT.begin_fill()
for i in range(0,4):
    myT.right(90)
    myT.forward(80)
myT.end_fill()
myT.left(190)
myT.forward(50)


myT.write("Home",False,"left",("Arial",20,"normal"))

turtle.done()