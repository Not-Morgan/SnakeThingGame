import pygame
import time

def score_count(screen, count):
        black = (0,     0,      0)
        font = pygame.font.SysFont(None, 17)
        text = font.render("Coins: "+str(count), True, black)
        screen.blit(text,(520, 50))
        #prints the score at the top of side bar
        
def side_bar(screen):
        
        #displays the buttons

        dim_red = (200,0,0)
        dim_green = (0,200,0)
        
        red   = (255, 0,     0)
        green = (0,   255,   0)
        
        black = (0,0,0)
        
        

        
        button1_pos = [515, 100, 75, 50]
        button2_pos = [515, 200, 75, 50]
        button3_pos = [515, 300, 75, 50]
        button4_pos = [515, 400, 75, 50]
        
        font = pygame.font.SysFont(None, 17)
        
        text1 = font.render("Apple", True, black)
        price1 = font.render("10 coins", True, black)
 
        
        text2 = font.render("Snake", True, black)
        price2 = font.render("20 coins", True, black)

        text3 = font.render("Snake2", True, black)
        price3 = font.render("50 coins", True, black)

        text4 = font.render("Snake3", True, black)
        price4 = font.render("100 coins", True, black)
        
        
        
        mouse = pygame.mouse.get_pos()

        def display_buttons(button_pos, text, price, colour, dim_colour):
                if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]: #if mouse is inside the button
                        pygame.draw.rect(screen, colour,(button_pos[0],button_pos[1],button_pos[2],button_pos[3])) #change colour
                        screen.blit(text,(button_pos[0], button_pos[1])) #display text
                        screen.blit(price,(button_pos[0], button_pos[1] + 10))
                        
                       
                else:
                        pygame.draw.rect(screen, dim_colour,(button_pos[0],button_pos[1],button_pos[2],button_pos[3])) 
                        screen.blit(text,(button_pos[0], button_pos[1]))
                        screen.blit(price,(button_pos[0], button_pos[1] + 10))

        display_buttons(button1_pos, text1, price1, red,  dim_red)
        display_buttons(button2_pos, text2, price2, green, dim_green)
        display_buttons(button3_pos, text3, price3, green,  dim_green)
        display_buttons(button4_pos, text4, price4, red, dim_red)
        

				
				
def button_pressed(score, price1, price2, price3, price4):

        snake_price = 10
        apple_price = 10
        score_multiplier = 1.5

        button1_pos = [515, 100, 75, 50]
        button2_pos = [515, 200, 75, 50]
        button3_pos = [515, 300, 75, 50]
        button4_pos = [515, 400, 75, 50]

        mouse = pygame.mouse.get_pos()

        def buttonClicked(button_pos):
                if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]:
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        return True

        if buttonClicked(button1_pos) and score >= price1:
                return "Apple"
        if buttonClicked(button2_pos) and score >= price2:
                return "Snake1"
        if buttonClicked(button3_pos) and score >= price3:
                return "Snake2"
        if buttonClicked(button4_pos) and score >= price4:
                return "Snake3"
        else:
                return "None"        
                
