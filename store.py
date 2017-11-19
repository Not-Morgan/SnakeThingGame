import pygame

def score_count(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: "+str(count), True, black)
        gameDisplay.blit(text,(0,0))

def side_bar(score):

        dim_red = (200,0,0)
        dim_green = (0,200,0)
        
        button1_pos = [550, 100, 100, 50]
        mouse = pygame.mouse.get_pos()
        if button1_pos[0] + button1_pos[2] > mouse[0] > button1_pos[0] and button1_pos[1] + button1_pos[3] > mouse[1] > button1_pos[1]:
                pygame.draw.rect(gameDisplay, bright_green,(button1_pos[0],button1_pos[1],button1_pos[2],button1_pos[3]))
        """else:
                pygame.draw.rect(gameDisplay, green,(button1_pos[1],button1_pos[2],button1_pos[3],button1_pos[4]))"""







