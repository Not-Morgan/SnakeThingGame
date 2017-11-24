import pygame
import webbrowser

def score_count(screen, count):
        black = (0,     0,      0)
        font = pygame.font.SysFont(None, 17)
        text = font.render("Coins: "+str(count), True, black)
        screen.blit(text,(520, 50))
        #prints the score at the top of side bar
        
def side_bar(screen, score): #displays only buttons, credits and the you've won screen
        
        #define colours of the buttons

        dim_red = (200,0,0)
        dim_green = (0,200,0)
        dim_blue = (136,206,250)
        
        red   = (255, 0,     0)
        green = (0,   255,   0)
        blue = (0,191,255)
        
        black = (0,0,0)
        
        
        #define all the button positions
        
        button1_pos = [515, 100, 75, 50]
        button2_pos = [515, 200, 75, 50]
        button3_pos = [515, 300, 75, 50]
        button4_pos = [515, 400, 75, 50]
        
        font = pygame.font.SysFont(None, 17)

        mouse = pygame.mouse.get_pos()
        
        #define all the text displayed in the buttons        
        text1 = font.render("Apple", True, black)
        price1 = font.render("10 coins", True, black)
 
        
        text2 = font.render("Snake", True, black)
        price2 = font.render("20 coins", True, black)

        text3 = font.render("Super Snake", True, black)
        price3 = font.render("50 coins", True, black)

        text4 = font.render("Hyper Snake", True, black)
        price4 = font.render("100 coins", True, black)

        screen.blit(font.render("Mason, Josh ®", True, black),(510, 480))

        def display_buttons(button_pos, text, price, colour, dim_colour):
                if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]: #if mouse is inside the button
                        pygame.draw.rect(screen, colour,(button_pos[0],button_pos[1],button_pos[2],button_pos[3])) #change colour
                        screen.blit(text,(button_pos[0], button_pos[1])) #display product
                        screen.blit(price,(button_pos[0], button_pos[1] + 10)) #display price
                         
                       
                else:
                        pygame.draw.rect(screen, dim_colour,(button_pos[0],button_pos[1],button_pos[2],button_pos[3])) #otherwise use the regular colour
                        screen.blit(text,(button_pos[0], button_pos[1])) #display product
                        screen.blit(price,(button_pos[0], button_pos[1] + 10)) #display price

        #display all the buttons

        display_buttons(button1_pos, text1, price1, red,  dim_red)
        display_buttons(button2_pos, text2, price2, green, dim_green)
        display_buttons(button3_pos, text3, price3, blue,  dim_blue)
        display_buttons(button4_pos, text4, price4, red, dim_red)
        screen.blit(font.render("Mason, Josh", True, black),(510, 480))

        #displays credits and the "you have won screen"

        if score >= 100000:
                font = pygame.font.SysFont(None, 17)
                screen.blit(font.render("You have won, Congratulations!", True, black),(10,10))

				
				
def button_pressed(score, price1, price2, price3, price4):

        snake_price = 10
        apple_price = 10

        button1_pos = [515, 100, 75, 50]
        button2_pos = [515, 200, 75, 50]
        button3_pos = [515, 300, 75, 50]
        button4_pos = [515, 400, 75, 50]
        buttoncredits_pos = [510, 480, 80, 20] #secret button for the credits, shhhh its a secret
        buttoncheat_pos = [515, 0, 75, 30]

        mouse = pygame.mouse.get_pos()

        def buttonClicked(button_pos):
                if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]: #if the mouse is in the boundaries of the button
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN: #and the mouse is clicked
                                        return True
                

        if buttonClicked(button1_pos) and score >= price1:
                return "Apple"
        if buttonClicked(button2_pos) and score >= price2:
                return "Snake"
        if buttonClicked(button3_pos) and score >= price3:
                return "Snake2"
        if buttonClicked(button4_pos) and score >= price4:
                return "Snake3"
        if buttonClicked(buttoncheat_pos):
                return "Snake4"
        if buttonClicked(buttoncredits_pos):
                webbrowser.open("https://github.com/Not-Morgan/SnakeThingGame")
        
        else:
                return "None"
        
                
