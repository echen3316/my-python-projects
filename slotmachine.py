#Slot Machine
#Init
import random
import time
slot_symbols = ["🌟", "🌙", "7","⚡"]

#Functions
#Main

quit = print("Bye player!")

#Introduction

print("Welcome to the slot machines where you can make it big!!")
while True:
    global credit
    credits = 300
    slots = input("Would you like to spin or no?: ")
    if slots == "yes":
        credits = credits - 50
        slot1 = random.choice(slot_symbols)
        slot2 = random.choice(slot_symbols)
        slot3 = random.choice(slot_symbols)
        print("Spinning....")
        time.sleep(1)
        print(slot1)
        time.sleep(1)
        print(slot2)
        time.sleep(1)
        print(slot3)

    if slots == "no":
        print(quit)
        break
    if slot1 == "7" and slot2 == "7" and slot3 == "7":
        credits = credits + 2000
        print("JACKPOT! You won 2000 credits!!!" +str (credits))
    elif slot1 == "🌟" and slot2 == "🌟" and slot3 == "🌟":
        credits = credits + 400
        print("Nice Match! You won 400 credits!" +str (credits))
    elif slot1 == "🌙" and slot2 == "🌙" and slot3 == "🌙":
        credits = credits + 400
        print("Nice Match! You won 400 credits!" +str (credits))
    elif slot1 == "⚡" and slot2 == "⚡" and slot3 == "⚡":
        credits = credits + 400
        print("Nice Match! You won 400 credits!" +str (credits))
    elif slot1 == "⚡" and slot2 =="⚡" or slot1 == "⚡" and slot3 == "⚡" or slot2 =="⚡" and slot3 == "⚡":
        credits = credits + 150
        print("2 in a row, you won 150 credits!" +str (credits))
    elif slot1 == "🌟" and slot2 =="🌟" or slot1 == "🌟" and slot3 == "🌟" or slot2 =="🌟" and slot3 == "🌟":
        credits = credits + 150
        print("2 in a row, you won 150 credits!" +str (credits))
    elif slot1 == "🌙" and slot2 =="🌙" or slot1 == "🌙" and slot3 == "🌙" or slot2 =="🌙" and slot3 == "🌙":
        credits = credits + 150
        print("2 in a row, you won 150 credits!" +str (credits))
    elif slot1 == "7" and slot2 =="7" or slot1 == "7" and slot3 == "7" or slot2 =="7" and slot3 == "7":
        credits = credits + 150
        print("2 in a row, you won 150 credits!" +str (credits))
    else:
        print("You won nothing" +str (credits))

