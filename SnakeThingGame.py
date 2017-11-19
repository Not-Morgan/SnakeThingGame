import pygame
import random 
import math
#import store #commented out until josh fixes

white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
blue  = (0,   0,   255)

display_height = 500
display_width  = 500

#change to speed up of slow down game
fps = 10

top_wall = 0
bottom_wall = display_height
left_wall = 0
right_wall = display_width

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Thing Game')
clock = pygame.time.Clock()
crashed = False


class snake_head:
	direction = 0
	length = 1000
	tails = []

	def __init__(self, size, color = green):
		self.size = size
		self.colour = color
		self.pos = [0, 0]
		self.pos[0] = random.randint(left_wall, right_wall)
		self.pos[1] = random.randint(top_wall, bottom_wall)

	def move(self, distance):
		#move  a distance of distance
		self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
		self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
		
		#turn randomly
		self.direction += random.randint(-15, 15)
		self.direction % 360
		
		if self.pos[1] < top_wall or self.pos[1] > bottom_wall:
			self.direction += 180
		if self.pos[0] < left_wall or self.pos[0] > right_wall:
			self.direction += 180
			
		#create a new tail segment
		self.tails.append(snake_tail(self.pos, self.length))
		
		self.tail_check()
		self.food_check()


	def food_check(self):
		if 1 == 2:
			print("panic")
			#draw a new food
	
	def tail_check(self):
		for tail in self.tails:
			if tail.check_if_dead() == True:
				self.tails.remove(tail)
				


class snake_tail:
	def __init__(self, snake_head_pos, last_time):
		self.created_time = pygame.time.get_ticks()
		self.pos = snake_head_pos
		self.last_time = last_time
	
	def check_if_dead(self):
		if pygame.time.get_ticks() > self.created_time + self.last_time:
			print("test")
			return True
		

class food:
	def __init__(self, size, colour = red):
		self.pos = [0, 0]
		self.pos[0] = random.randint(left_wall, right_wall)
		self.pos[1] = random.randint(top_wall, bottom_wall)
		self.colour = colour
		self.size = size


def Draw():
	gameDisplay.fill(white)
	
	pygame.draw.line(gameDisplay, black, (left_wall, top_wall), (right_wall, top_wall), 1)
	pygame.draw.line(gameDisplay, black, (right_wall, top_wall), (right_wall, bottom_wall), 1)
	pygame.draw.line(gameDisplay, black, (right_wall, bottom_wall), (left_wall, bottom_wall), 1)
	pygame.draw.line(gameDisplay, black, (left_wall, bottom_wall), (left_wall, top_wall), 1)
	
	for snake in snakes:
			pygame.draw.circle(gameDisplay, green, snake.pos, snake.size, 0)
			for tail in snake.tails:
				pygame.draw.circle(gameDisplay, blue, tail.pos, snake.size, 0)
	
	for food in foods:
		pygame.draw.circle(gameDisplay, food.colour, food.pos, 5, 0)

	pygame.display.update()
	clock.tick(fps)

def Logic():
	#move snakes, eat food etc
	for snake in snakes:
		snake.move(5)
	

def Take_Input():
	global crashed

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #close button is hit
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print("---")
				print(snakes[0].pos)
				print("---")
				for tail in snakes[0].tails:
					print(tail.pos)
				


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

snakes = [snake_head(5)]
foods = [food(5)]

while not crashed:
	Draw()
	Logic()
	Take_Input()

pygame.quit()
