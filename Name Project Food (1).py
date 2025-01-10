print("Welcome to Yummy Food Generator")
print("Answer these questions to see what food you will get")
ans = input("meat (m) or vegetable (v) ?")
if ans == "m":
    ans = input("Steak (stk) or Chicken (chk) ?")
    if ans == "stk":
        ans = input("Fries (f) or rice (r) ?")
        if ans == "f":
            print("You want Steak Frites")
        else:
            print("You want Mongolian Beef Bowl")
    if ans == "chk":
        ans = input("Oil (o) or buns (b) ?")
        if ans == "o":
            print("You want Fried Chicken")
        else:
            print("You want Chicken Sandwich")

if ans == "v":
    ans = input("Tomato (Tom) or Beans (Be) ?")
    if ans == "Tom":
        ans = input("Egg (eg) or cheese (ch) ?")
        if ans == "eg":
            print("You want Tomato Stir-Fry")
        else:
            print("You want Caprese Salad")
    if ans == "Be":
        ans = input("Tortilla (tl) or Toast (to) ?")
        if ans == "tl":
            print("You want Taco")
        else:
            print("You want Beans n Toast")
