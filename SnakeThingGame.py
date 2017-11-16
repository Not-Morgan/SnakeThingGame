import pygame
import random 
import math

white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
blue  = (0,   0,   255)

display_height = 1000
display_width  = 1000

#change to speed up of slow down game
fps = 45

top_wall = 0
bottom_wall = 1000
left_wall = 0
right_wall = 1000

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Thing Game')
clock = pygame.time.Clock()
crashed = False

class snake_head:
	pos = [0, 0]
	direction = 0
	size = 0
	length = 0
	colour = (0, 0, 0)

	def __init__(self, size, color = green):
		self.size = size
		self.colour = color
		self.pos[0] = random.randint(left_wall, right_wall)
		self.pos[1] = random.randint(top_wall, bottom_wall)

	def move(self, distance):
		self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
		self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
		self.food_check()

	def food_check(self):
		if 1 == 2:
			print("panic")
			#what is this


#class snake_tail:


class food:
	pos = [0, 0]
	direction = 0
	size = 0
	colour = (255, 0, 0)
	
def draw_food:




def Draw():
	gameDisplay.fill(white)
	print(snake.pos)
	print(snake.size)
	pygame.draw.circle(gameDisplay, green, snake.pos, snake.size, 0)

	#draw things here

	pygame.display.update()
	clock.tick(fps)

def Logic():
	#move snakes, eat food etc
	snake.move(10)

def Take_Input():
	global crashed

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #close button is hit
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				Print("keys work")
				
snake = snake_head(20)

"""
class store:

def prompt_purchase(score, price)
	pygame.mouse.get_pos()
	if global score >= price and pygame.mouse.get_pressed()[0]:
		score += -price
		return "add a snake"
	else:
		return "Not enough cash"
		
		
		
		
"""

while not crashed:
	Draw()
	Logic()
	Take_Input()

pygame.quit()
