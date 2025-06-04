#CREATE PROJECT
#Fortune Cookies
import time
import requests #Lines 4-6 were found by python forums of people wondering how to print out a picture from a URL
from PIL import Image
from io import BytesIO

fortune_cookies= ["fcookie1", "fcookie2","fcookie3","fcookie4","fcookie5","fcookie6","fcookie7"]
menu= ["pho noodles", "mongolian beef", "takoyaki", "kimpbob", "Udon", "Peking Duck Rice", "Sushimi"]
menu_pictures= ["https://www.oliveandmango.com/images/uploads/2021_12_26_beef_pho_noodle_soup_recipe_2.jpg","https://www.closetcooking.com/wp-content/uploads/2014/01/Mongolian-Beef-800-1117.jpg","https://i0.wp.com/www.angsarap.net/wp-content/uploads/2013/06/takoyaki.jpg?w=1080&ssl=1","https://www.maangchi.com/wp-content/uploads/2007/08/gimbap_blog-590x351.jpg","https://i0.wp.com/kennascooks.com/wp-content/uploads/2024/05/img_6828.jpg?w=1500&ssl=1","https://cookingwithcocktailrings.com/wp-content/uploads/2021/12/Faux-peking-duck-recipe-25-683x1024.jpg","https://www.threesixtyguides.com/wp-content/uploads/2015/12/sushimi-2.jpg"]
fortune= ["https://vaulted.com/wp-content/uploads/Money-Supply-Gold.jpg","https://images.squarespace-cdn.com/content/v1/52f17606e4b0c058f609ee0e/1410361734144-AZOS0O30MFTJXSRIJT8X/image-asset.jpeg?format=2500w","https://miro.medium.com/v2/resize:fit:1100/format:webp/1*m23Sw6LmSNJuyrbh-KGAcg.jpeg","https://www.spiritualquesters.org/wp-content/uploads/2021/11/miracle.jpg","https://image.marriage.com/advice/wp-content/uploads/2015/07/Tips-To-Improve-Your-Love-Life.jpg","https://miro.medium.com/v2/resize:fit:750/format:webp/1*fvZ7diCBdx2i6F8NieLR7A.jpeg","https://wallpapers.com/images/featured/jesus-aesthetic-obydv9rxpqmyz9a6.webp"]
def resturantexperience():
        print("You stumbled upon an intriguing looking resturant in Chinatown, with smells that make your stomach grumble...")
        print("You decide to enter the resturant...")
        time.sleep(2)
        print("----------------------------------Suprise Kang--------------------------------------")
        print("Welcome to Suprise Kang! Let me introduce you to our menu! I promise your day will be made with us here today!")
        time.sleep(1)
        print("There will be a special suprise in the end, be weary of that!")
        time.sleep(2)
        print("You get a menu filled with numbers ranging from 1 to 7 and instructions choose you to pick one")
        while True:
            choice = int(input("What suprise meal do you want? (Choose from 1 to 7 for a suprise dish or, if your not hungry, just say 0!"))
            print("Customer choice:", choice)
            if choice == 1:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[0])
                print(fortune_cookies[0])
                time.sleep(2)
                response = requests.get(menu_pictures[0]) #Every function printing url pictures of the python forum figuring
                img = Image.open(BytesIO(response.content))
                img.show()
                print("Here is your pho noodles")
                print("Our chefs recomend squeezing our lime and oyster sauce onto the bowl to have the most fulfilling bowl")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[0])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will earn multi-millions doing work you love in the coming years")
                elif opens.lower == "n":
                    print("You returned the fortune cookie")
            if choice == 2:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[1])
                print(fortune_cookies[1])
                time.sleep(2)
                response = requests.get(menu_pictures[1])
                img = Image.open(BytesIO(response.content))
                img.show()
                print("Here is your mongolian beef, along with a rice bowl to eat your food!")
                print("Eating them together is how you would properly eat this peppered delight")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower() == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[1])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will be humble and charitable with many appreciating your work")
                elif opens.lower == "n":
                    print("You returned the fortune cookie")
            if choice == 3:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[2])
                print(fortune_cookies[2])
                time.sleep(2)
                response = requests.get(menu_pictures[2])
                img = Image.open(BytesIO(response.content))
                img.show()
                print("This takoyaki has intriguing flakes that move when you eat, don't worry these are just fish flakes")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower() == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[2])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will be an inspiration to many, being selfless and improving the lives of many")
                elif opens.lower == "n":
                    print("You returned the fortune cookie")
            if choice == 4:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[3])
                print(fortune_cookies[3])
                time.sleep(2)
                response = requests.get(menu_pictures[3])
                img = Image.open(BytesIO(response.content))
                img.show()
                print("We recomend eating this kimpbob, mixing it together with pickled radish!")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower() == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[3])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will face a miracle, recovering from a future sickness unscaved and will learn a lot of wisdom")
                elif opens.lower() == "n":
                    print("You returned the fortune cookie")
            if choice == 5:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[4])
                print(fortune_cookies[4])
                time.sleep(2)
                response = requests.get(menu_pictures[4])
                img = Image.open(BytesIO(response.content))
                img.show()
                print("Here is your udon, our customers love to mix these noodles with green onions, and dip it in our seasme paste!")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[4])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will have a great family and love life!")
                elif opens.lower == "n":
                    print("You returned the fortune cookie")
            if choice == 6:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[5])
                print(fortune_cookies[5])
                time.sleep(2)
                response = requests.get(menu_pictures[5])
                img = Image.open(BytesIO(response.content))
                img.show()
                print("Oh this is my personal favorite! I recommend you eating this with rice or wrapping these with bao and cucumber, it'll blow your tastebuds!")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[5])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will abundant resources and have power over many industries")
                elif opens.lower == "n":
                    print("You returned the fortune cookie")
            if choice == 7:
                print("This is the food you ordered, give us a minute to prepare you our dish!")
                print(menu[6])
                print(fortune_cookies[6])
                time.sleep(2)
                response = requests.get(menu_pictures[6])
                img = Image.open(BytesIO(response.content))
                img.show()
                print("This is sushimi, you should dip these with soy sauce and wasabi!")
                time.sleep(1)
                opens = input("Would you like to see your fortune, y or n?")
                if opens.lower == "y":
                    print("opening cookie...")
                    time.sleep(2)
                    response = requests.get(fortune[6])
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    print("You will talk with your lord and savior frequently and closely!")
                elif opens.lower == "n":
                    print("You returned the fortune cookie")
            if choice == 0:
                print("Thanks for visiting!")
                break

resturantexperience()
