import pygame
import random 
import math
from store import *
white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
blue  = (0,   0,   255)


display_height = 500
display_width  = 600

#change to speed up of slow down game
fps = 30

top_wall = 0
bottom_wall = display_height
left_wall = 0
right_wall = display_width - 100

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Thing Game')
clock = pygame.time.Clock()
crashed = False

score = 100
score_increment = 5
#set a score variable


class snake_head:
	direction = 0
	length = 1000
	tails = []

	def __init__(self, size, color = green, speed_multiplier = 1):
		self.size = size
		self.colour = color
		self.speed_multiplier = speed_multiplier
		self.pos = [0, 0]
		self.pos[0] = random.randint(left_wall + 10, right_wall - 10)
		self.pos[1] = random.randint(top_wall +  10, bottom_wall - 10)

	def move(self, speed):
		distance = speed * self.speed_multiplier
		#move  a distance of distance
		self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
		self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
		
		#turn randomly
		self.direction += random.randint(-15, 15)
		self.direction % 360
		
		if self.pos[1] < top_wall or self.pos[1] > bottom_wall:
			self.direction += 180
			self.move(6)
		if self.pos[0] < left_wall or self.pos[0] > right_wall:
			self.direction += 180
			self.move(6)
			
		#create a new tail segment
		self.tails.append(snake_tail(self.pos, self.length))
		
		self.tail_check()
		self.food_check()


	def food_check(self):
		global foods
		global score
		for food_thing in foods:
			if (abs(food_thing.pos[0] - self.pos[0]) < 5 and abs(food_thing.pos[1] - self.pos[1]) < 5):
				score += score_increment
				foods.remove(food_thing)
				foods.append(food(5))
				print("test")
			
			
	
	def tail_check(self):
		for tail in self.tails:
			if tail.check_if_dead() == True:
				self.tails.remove(tail)
				


class snake_tail:
	def __init__(self, snake_head_pos, last_time):
		self.created_time = pygame.time.get_ticks()
		#self.pos = snake_head_pos
		self.pos = [0, 0]
		self.pos[0] += snake_head_pos[0]
		self.pos[1] += snake_head_pos[1]
		self.last_time = last_time
	
	def check_if_dead(self):
		if pygame.time.get_ticks() > self.created_time + self.last_time:
			return True
		

class food:
	def __init__(self, size, colour = red):
		self.pos = [0, 0]
		self.pos[0] = random.randint(left_wall + 10, right_wall - 10)
		self.pos[1] = random.randint(top_wall + 10, bottom_wall - 10)
		self.colour = colour
		self.size = size

def DrawBorders():

        pygame.draw.line(gameDisplay, black, (left_wall, top_wall), (right_wall + 100, top_wall), 5)
        pygame.draw.line(gameDisplay, black, (right_wall, top_wall), (right_wall, bottom_wall), 10)
        pygame.draw.line(gameDisplay, black, (right_wall + 100, bottom_wall), (left_wall, bottom_wall), 5)
        pygame.draw.line(gameDisplay, black, (left_wall, bottom_wall), (left_wall, top_wall), 5)
        pygame.draw.line(gameDisplay, black, (right_wall + 100, top_wall), (right_wall + 100, bottom_wall), 5)

def Draw():
	gameDisplay.fill(white)
	
	score_count(gameDisplay, score)
	side_bar(gameDisplay)
 
	for snake in snakes:
			pygame.draw.circle(gameDisplay, snake.colour, snake.pos, snake.size, 0)
			for tail in snake.tails:
				pygame.draw.circle(gameDisplay, snake.colour, tail.pos, snake.size, 0)
	
	for food in foods:
		pygame.draw.circle(gameDisplay, food.colour, food.pos, 5, 0)

	DrawBorders()

	pygame.display.update()
	clock.tick(fps)

def Logic():
	global score

	#move snakes, eat food etc
	for snake in snakes:
		snake.move(3)

		
	button = button_pressed()
	if button == "Snake":
		snakes.append(snake_head(5))
		score -= 20
	elif button == "Snake2":
		snakes.append(snake_head(7, blue))
		score -= 50
	elif button == "Snake3":
		snakes.append(snake_head(7, red, 1.5))
		score -= 100
	elif button == "Apple":
		foods.append(food(5))
		score -= 10

def Take_Input():
	global crashed

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #close button is hit
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				for snake in snakes:
					print(snake.pos)
				


snakes = [snake_head(5)]
foods = [food(5), food(5), food(5), food(5), food(5)]

while not crashed:
	Draw()
	Logic()
	Take_Input()

pygame.quit()
