#Evan Chen
#9/30/2024
#Picnic!
#Init
import turtle
alison=turtle.Turtle()
marianne=turtle.Turtle()
evan = turtle.Turtle()
import random
turtle.colormode(255)

#This was coded by Alison 
def tree(color,x,y):
    alison.penup()
    alison.goto(x,y)
    alison.pendown()
    alison.color("#964B00")
    alison.begin_fill()
    for i in range(4):
        alison.forward(60)
        alison.left(90)
    alison.end_fill()
    alison.right(90)
    alison.backward(60)
    alison.left(90)
    alison.color(color)
    alison.begin_fill()
    alison.forward(70)
    length=40
    for i in range(4):
        alison.forward(length)
        alison.left(125)
        alison.forward(60)
        alison.right(120)
        length=length-5
    alison.left(200)
    length=20
    for i in range(4):
        alison.forward(60)
        alison.left(125)
        alison.forward(length)
        alison.right(120)
        length=length+5
    alison.left(120)
    alison.forward(60)
    alison.end_fill()

#This was coded by Alison
#This is all the trees together
#They each have a color and coordinates
def trees():
    tree("#097969",-500,75)
    tree("#AFE1AF",-400,75)
    tree("#355E3B",-300,75)
    tree("#097969",-200,75)
    tree("#AFE1AF",-100,75)
    tree("#355E3B",0,75)
    tree("#097969",100,75)
    tree("#AFE1AF",200,75)
    tree("#355E3B",300,75)
    tree("#097969",400,75)
    tree("#AFE1AF",500,75)

#This was coded by Alison
#This created the blue sky in the backround
def sky():
    alison.penup()
    alison.goto(600,100)
    alison.pendown()
    alison.color("#87CEEB")
    alison.begin_fill()
    alison.left(90)
    alison.forward(400)
    alison.left(90)
    alison.forward(2000)
    alison.left(90)
    alison.forward(400)
    alison.left(90)
    alison.forward(2000)
    alison.end_fill()

#This was coded by Alison
#This creates the sun in the corner
def sun():
    alison.penup()
    alison.goto(400,350)
    alison.right(90)
    alison.color("#FFFF00")
    alison.begin_fill()
    alison.circle(50)
    alison.end_fill()
    
#This was coded by Alison
#This creates a single cloud
def cloud():
    alison.color("#FFFFFF")
    alison.begin_fill()
    alison.circle(25,90)
    alison.left(90)
    alison.forward(100)
    alison.left(90)
    alison.circle(25,90)
    alison.right(90)
    alison.circle(25,180)
    alison.end_fill()

#This was coded by Alison
#This makes multiple clouds throughout the sky
def clouds():
    alison.penup()
    alison.right(90)
    alison.forward(800)
    alison.pendown()
    for i in range(3):
        cloud()
        alison.left(90)
        alison.penup()
        alison.forward(300)
        alison.left(180)
        alison.pendown()
#Functions
def rectangle():#creates the grasses figure/ marianne
#code
    for i in range(2):
        marianne.forward(500)
        marianne.right(90)
    marianne.forward(1000)
    marianne.right(90)
    marianne.forward(500)
        
    

def grass_floor():      # draws the base(grass) for the image #marianne
#code:
#color=string
    marianne.penup()
    marianne.goto(0,100)  # goes to the location that the first tree will be in
    marianne.pendown()
    marianne.color("#31a833")  # color of the grass
    marianne.begin_fill()
    rectangle()
    marianne.end_fill()

def square():   # draws the base figure of the blanket #marianne
#code:
    for i in range(4):
        marianne.forward(350)
        marianne.left(90)

def stripe(x,y): #draws one stipe horozontal and vertical
#x=integer
#y=integer
#color=string
#code:
    marianne.color("#ffcccc")
    marianne.penup()
    marianne.goto(x,y) 
    marianne.pendown()
    marianne.right(90)
    marianne.begin_fill()
    marianne.forward(350)
    marianne.right(90)
    marianne.forward(20)
    marianne.right(90)
    marianne.forward(350)
    marianne.right(90)
    marianne.end_fill()
def stripeup(x,y): #draws stripes vertically #marianne
#color=string
#code:
    marianne.color("#ff6666")
    marianne.penup()
    marianne.goto(x,y)
    marianne.pendown()
    marianne.right(90)
    marianne.begin_fill()
    marianne.forward(20)
    marianne.right(90)
    marianne.forward(350)
    marianne.right(90)
    marianne.forward(20)
    marianne.right(90)
    marianne.end_fill()

def manystripes(): #draws many stripes horozontal and vertical #marianne
#(x,y)= location
#x=integer
#y=integer
#code:
    stripe(-170,50)
    stripe(-170,0)
    stripe(-170,-50)
    stripe(-170,-100)
    stripe(-170,-150)
    stripe(-170,-200)
    stripe(-170,-250)
    stripeup(-150,50)
    stripeup(-110,50)
    stripeup(-70,50)
    stripeup(-30,50)
    stripeup(10,50)
    stripeup(50,50)
    stripeup(90,50)
    stripeup(130,50)
    

def picnic_blanket():   # draws a complete picnic blanket
#color=string
    marianne.goto(180,-300)
    marianne.color("#ffffcc")
    marianne.begin_fill()
    square()
    marianne.end_fill()
    marianne.goto(-170,50)
    manystripes()

def basket():  #draws a picnic basket #evan
    evan.penup()
    evan.goto(-150,-150)
    evan.pendown()
    evan.color("burlywood")
    evan.begin_fill()
    evan.forward(100)
    evan.left(65)
    evan.forward(60)
    evan.left(115)
    evan.forward(150)
    evan.left(115)
    evan.forward(60)
    evan.end_fill()
    evan.left(155)
    evan.forward(55)
    evan.width(10)
    evan.color("tan")
    evan.right(90)
    evan.forward(90)
    evan.right(180)
    evan.forward(10)
    evan.width(4)
    evan.right(90)
    for i in range(2):
     evan.forward(50)
     evan.left(90)
     evan.forward(70)
     evan.left(90)
    evan.right(90)
    evan.penup()
    evan.forward(50)
    evan.pendown()
    
def drinks(color1, color2):    #draws random beverages #evan
    evan.color(color1)
    evan.begin_fill()
    evan.forward(20)
    evan.left(90)
    evan.forward(60)  
    evan.circle(10,180)
    evan.forward(60)
    evan.end_fill()
    evan.color(color2)
    evan.width(15)
    evan.penup()
    evan.left(180)
    evan.forward(35)
    evan.right(90)
    evan.forward(5)
    evan.pendown()
    evan.forward(10)
    evan.penup()
    evan.left(90)
    evan.forward(40)
    evan.left(90)
    evan.forward(4)
    evan.pendown()
    evan.width(10)
    evan.forward(1)
    evan.penup()
    evan.left(90)
    evan.forward(75)
    evan.left(90)
    evan.forward(20)
    
def bottle(): #color randomizer for drink #evan
    drinks((random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
def water(): #Makes 3 copies of drink #evan
 for i in range(3): 
   bottle()
   

def food(): #makes a slice of bread #evan
    evan.width(3)
    evan.penup()
    evan.pendown()
    evan.pencolor("brown")
    evan.fillcolor("navajowhite")
    evan.begin_fill()
    evan.forward(60)
    evan.left(90)
    evan.forward(60)
    evan.right(90)
    evan.forward(10)
    evan.left(90)
    evan.circle(40,180)
    evan.left(90)
    evan.forward(10)
    evan.right(90)
    evan.forward(60)
    evan.end_fill()

def bread():#makes 2 different bread slices #evan
    food()
    evan.right(180)
    evan.forward(30)
    evan.right(90)
    evan.penup()
    evan.forward(10)
    evan.pendown()
    food()
def food_water():#combines the food and drinks #evan
    water()
    bread()
def picnicfood(): #Adds the basket with all the food/drinks #evan
    basket()
    food_water()
    
#The entire picnic together #Evan
def picnic():
    marianne.speed(1000)
    grass_floor()
    picnic_blanket()
    alison.speed(1000)
    sky()
    trees()
    sun()
    clouds()
    picnicfood()

#Main
picnic()

