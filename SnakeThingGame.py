import pygame
import random 
import math
import store

white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
blue  = (0,   0,   255)

display_height = 1000
display_width  = 1000

#change to speed up of slow down game
fps = 10

top_wall = 0
bottom_wall = 1000
left_wall = 0
right_wall = 1000

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Thing Game')
clock = pygame.time.Clock()
crashed = False

snake_heads = [snake_head(5)]
foods = []

class snake_head:
	pos = [0, 0]
	direction = 0
	size = 0
	length = 1
	colour = (0, 0, 0)
	tails = []

	def __init__(self, size, color = green):
		self.size = size
		self.colour = color
		self.pos[0] = random.randint(left_wall, right_wall)
		self.pos[1] = random.randint(top_wall, bottom_wall)

	def move(self, distance):
		self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
		self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
		
		self.direction += random.randint(-15, 15)
		self.direction % 360
		
		if self.pos[1] < top_wall or self.pos[1] > bottom_wall:
			self.direction += 180
		if self.pos[0] < left_wall or self.pos[0] > right_wall:
			self.direction += 180
			
		tails.append(snake_tail(self.pos, self.colour, self.size, length)
		
		self.food_check()

	def food_check(self):
		if 1 == 2:
			print("panic")
			#what is this
	
	def tail_check(self):
		for tail in tails:
			if tail.check_if_dead() = True:
				tails.remove(tail)
				


class snake_tail:
	pos = [0, 0]
	colour = (0, 0, 0)
	size = 0
	last_time = 0
	created_time = pygame.get_ticks()
	
	def __init__(self, snake_head_pos, colour, size, last_time):
		self.pos = snake_head_pos
		self.colour = colour
		self.size = size
		self.last_time = last_time
	
	def check_if_dead(self)
		if pygame.get_ticks() > created_time + last_time:
			return True
		

class food:
	pos = [0, 0]
	size = 6
	colour = red
	def __init__(self):
		self.pos[0] = random.randint(left_wall, right_wall)
		self.pos[1] = random.randint(top_wall, bottom_wall)
	
def draw_food(self, color = red):
	self.pos[0] = random.randint(left_wall, right_wall)
	self.pos[1] = random.randint(top_wall, bottom_wall)
	self. colour = color
	food.append(self.pos[0], self.pos[1])
	
	
	
	print food
	
	



def Draw():
	gameDisplay.fill(white)
	
	#pygame.draw.line(gameDisplay, black, (top_wall
	
	for snake in snake_heads:
			pygame.draw.circle(gameDisplay, green, snake.pos, snake.size, 0)
	
	#draw things here
	
	for food in foods:
		pygame.draw.circle(gameDisplay, food.colour, food.pos, 5, 0)

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
