import pygame
import random 
import math
from store import *
import time

white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
blue  = (0,   0,   255)

cool_colour = (178,34,34) #for the secret snake


display_height = 500
display_width  = 600

#change to speed up of slow down game
fps = 60

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
	length = 500 #how long tail objects last before disappearing

	def __init__(self, size, color = green, speed_multiplier = 1):
		self.tails = []
		
		self.size = size
		self.colour = [color[0], color[1], color[2]]
		self.speed_multiplier = speed_multiplier
		
		self.pos = [0, 0]
		self.pos[0] = random.randint(left_wall + 10, right_wall - 10)
		self.pos[1] = random.randint(top_wall +  10, bottom_wall - 10)
	
	#does all the stuff for each tick
	def update(self, speed):
	
		if self.length < 1000:
			#increase speed if it's a fast snake
			distance = speed * self.speed_multiplier
			self.move(distance)
		
			#create a new tail segment
			self.tails.append(snake_tail(self.pos, self.length))
		
			self.tail_check()
			self.food_check()
			
			return "not dead"
		else:
			for c in range(len(self.colour)):
				self.colour[c] += 5
				if self.colour[c] > 255:
					self.colour[c] = 255
			if self.colour[0] + self.colour[1] + self.colour[2] == 765:
				return "dead"
			
	#uses trigonomentric math to move in trigonomaly
	def move(self, distance):
		
		#move  a distance of distance
		self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
		self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
		
		#turn randomly
		self.direction += random.randint(-15, 15)
		self.direction % 360
		
		#bounce off walls
		if self.pos[1] < top_wall or self.pos[1] > bottom_wall:
			self.direction += 180
			
			self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
			self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
		if self.pos[0] < left_wall or self.pos[0] > right_wall:
			self.direction += 180
			
			self.pos[0] += int(distance * math.sin(math.radians(self.direction)))
			self.pos[1] += int(distance * math.cos(math.radians(self.direction)))
			
		

	#checks if near food then moves it and adds score
	def food_check(self):
		global foods
		global score
		
		#checks if it's near any food
		for food_thing in foods:
			if (abs(food_thing.pos[0] - self.pos[0]) < self.size * 1.5 and abs(food_thing.pos[1] - self.pos[1]) < self.size * 1.5):
				score += score_increment
				foods.remove(food_thing)
				foods.append(food(5))
				self.length += 50
			
			
	#checks if tails are dead and removes them
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
	
	#draws the stuff from the store file
	score_count(gameDisplay, score)
	side_bar(gameDisplay, score)
 
	for snake in snakes: #draw each sake
			pygame.draw.circle(gameDisplay, snake.colour, snake.pos, snake.size, 0)
			for tail in snake.tails: #draw tail for snake
				pygame.draw.circle(gameDisplay, snake.colour, tail.pos, snake.size - 1, 0)
	
	for food in foods:
		pygame.draw.circle(gameDisplay, food.colour, food.pos, 5, 0)

	DrawBorders()

	pygame.display.update()
	clock.tick(fps)

def Logic():
	global score

	#move snakes, eat food etc
	for snake in snakes:
		if snake.update(3) == "dead":
			snakes.remove(snake)

	#checks if buttons are pressed and takes the appropriate action
	button = button_pressed(score, 10, 20, 50, 100)
	if button == "Snake":
		snakes.append(snake_head(6))
		score -= 20
	elif button == "Snake2":
		snakes.append(snake_head(8, blue))
		score -= 50
	elif button == "Snake3":
		snakes.append(snake_head(8, cool_colour, 1.5))
		score -= 100
	elif button == "Snake4":
		snakes.append(snake_head(4, (255, 165, 0), 2))
	elif button == "Apple":
		foods.append(food(5))
		score -= 10

def Take_Input():
	global crashed
	global score

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #close button is hit
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				score += 20
			if event.key == pygame.K_v:
				print("---")
				for snake in snakes:
					print(snake.colour)
					print(snake.length)
				


snakes = [snake_head(6)]
foods = [food(5), food(5), food(5), food(5), food(5)]

def game_intro():
	intro = False
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

	gameDisplay.fill(white)

	pygame.display.update()
	clock.tick(fps)



game_intro()

while not crashed:
	Draw()
	Logic()
	Take_Input()

pygame.quit()
