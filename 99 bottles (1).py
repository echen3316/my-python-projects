#99 Bottles

#Initialize

#Procedures
def bottles():
    milk = 99
    milk >= 1
    for i in range (99):
        print(str(milk) + "bottles of milk on the wall, ")
        print(str(milk) + "bottles of milk ")
        print("Take one down and pass it around, ")
        milk = milk - 1 #decreaase milk by 1
        if milk >=1:
            print(str(milk) + "bottles of beer on the wall ")


#Main
bottles()
