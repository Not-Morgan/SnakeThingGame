import pygame

white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
blue  = (0,   0,   255)

display_height = 1000
display_width  = 1000

#change to speed up of slow down game
fps = 45


pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Thing Game')
clock = pygame.time.Clock()
crashed = False

class snake:


class snake_tail:


class food:


def Draw():
	gameDisplay.fill(white)

	#draw things here

	pygame.display.update()
	clock.tick(fps)

def Logic():
	#move snakes, eat food etc

def Take_Input():
	global crashed

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #close button is hit
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ #key name
				

while not crashed:
	Draw()
	Logic()
	Take_Input()

pygame.quit()
