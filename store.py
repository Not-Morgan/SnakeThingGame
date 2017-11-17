# import Image

GameOn = True
purchase = False

score = 0
priceofsnake = 100
priceofsupersnake = 1000


while GameOn:
    if score > priceofsnake:
        GameOn = False
        print "Would you like to buy a snake?"
        purchase = raw_input ("> ")
        if purchase == "Y" or "Yes" or "Yea" or "Si" or "go" or "Aye" or "Sure":
            # Add a snake
        
    if score > priceofsupersnake:
        GameOn = False
        print "Would you like to buy a supersnake?"
        purchase = raw_input ("> ")
        if purchase == "Y" or "Yes" or "Yea" or "Si" or "go" or "Aye" or "Sure":
            # Add a supersnake




# import Image    
# image = Image.open('Test.jpg')
# image.show()
