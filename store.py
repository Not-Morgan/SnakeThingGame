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
        font = pygame.font.SysFont(None, 17)
        text1 = font.render("Snake", True, black)
        price1 = font.render("10 coins", True, black)
        button2_pos = [515, 200, 75, 50]
        text2 = font.render("Apple", True, black)

        
        mouse = pygame.mouse.get_pos()
        
        if button1_pos[0] + button1_pos[2] > mouse[0] > button1_pos[0] and button1_pos[1] + button1_pos[3] > mouse[1] > button1_pos[1]: #if mouse is inside the button
                pygame.draw.rect(screen, green,(button1_pos[0],button1_pos[1],button1_pos[2],button1_pos[3])) #change colour
                screen.blit(text1,(button1_pos[0], button1_pos[1])) #display text
                screen.blit(price1,(button1_pos[0], button1_pos[1] + 10))
                        
                       
        else:
                pygame.draw.rect(screen, dim_green,(button1_pos[0],button1_pos[1],button1_pos[2],button1_pos[3])) 
                screen.blit(text1,(button1_pos[0] + 10, button1_pos[1] + 10))


        if button2_pos[0] + button2_pos[2] > mouse[0] > button2_pos[0] and button2_pos[1] + button2_pos[3] > mouse[1] > button2_pos[1]: #if mouse is inside the button
                pygame.draw.rect(screen, red,(button2_pos[0],button2_pos[1],button2_pos[2],button2_pos[3])) #change colour
                screen.blit(text2,(button2_pos[0] + button2_pos[2]/4, button2_pos[1] + button2_pos[3]/3)) #display text
                        
        else:
                pygame.draw.rect(screen, dim_red,(button2_pos[0],button2_pos[1],button2_pos[2],button2_pos[3]))
                screen.blit(text2,(button2_pos[0] + button2_pos[2]/4, button2_pos[1] + button2_pos[3]/3))

				
				
def button_pressed():

        snake_price = 10
        apple_price = 10
        score_multiplier = 1.5

        button1_pos = [515, 100, 75, 50]
        button2_pos = [515, 200, 75, 50]
        button3_pos = [515, 300, 75, 50]
        button4_pos = [515, 300, 75, 50]

        mouse = pygame.mouse.get_pos()

        def buttonClicked(button_pos):
                if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]:
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        return True

        if buttonClicked(button1_pos):
                return "Snake"
        if buttonClicked(button2_pos):
                return "Apple"
        if buttonClicked(button3_pos):
                return "Snake2"
        if buttonClicked(button4_pos):
                return "Snake3"
        else:
                return "None"
        
                
                







