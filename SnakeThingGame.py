import pygame
import random 
import math
from store import *
import time

white = (255, 255, 255)
black = (0,   0,     0)
red   = (255, 0,     0)
green = (0,   255,   0)
dim_green = (0,	200,	0)
blue  = (0,   0,   255)

cool_colour = (178,34,34) #for the secret snake

pygame.init()
sound = pygame.mixer.Sound("sounds/apple.ogg")
background_sound = pygame.mixer.Sound("sounds/background.ogg")
button_click = pygame.mixer.Sound("sounds/button.ogg")

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

	def __init__(self, size, color = green, max_length = 1000, length_change = 50, speed_multiplier = 1):
		self.tails = []
		
		self.size = size
		self.colour = [color[0], color[1], color[2]]
		self.speed_multiplier = speed_multiplier
		self.max_length = max_length
		self.length_change = length_change
		
		self.pos = [0, 0]
		self.pos[0] = random.randint(left_wall + 10, right_wall - 10)
		self.pos[1] = random.randint(top_wall +  10, bottom_wall - 10)
	
	#does all the stuff for each tick
	def update(self, speed):
	
		if self.length < self.max_length:
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
			
	#uses trigonometric math to move in trigonomaly
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
				sound.play(0,0,0)
				foods.remove(food_thing)
				if not random.randint(1, 5) == 1:
					foods.append(food(5))
				self.length += self.length_change
			
			
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
		snakes.append(snake_head(8, blue, 1500))
		score -= 50
	elif button == "Snake3":
		snakes.append(snake_head(8, cool_colour, 1500, 37, 1.5))
		score -= 100
	elif button == "Snake4":
		snakes.append(snake_head(4, (255, 165, 0), 1500, 25, 2))
	elif button == "Apple":
		foods.append(food(5))
		score -= 10

	if not button == "None":
		button_click.play(0,0,0)

def Take_Input():
	global crashed
	global score

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #close button is hit
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_m:
				score += 20
			if event.key == pygame.K_v:
				print("---")
				for snake in snakes:
					print(snake.colour)
					print(snake.length)
			if event.key == pygame.K_b:
				for i in range(200):
					foods.append(food(5))
				score = 0
			if event.key == pygame.K_n:
				print("---")
				print(len(foods))
				print(len(snakes))


snakes = [snake_head(6)]
foods = [food(5), food(5), food(5), food(5), food(5)]

def game_intro():
	intro = False
	while not intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
                                      
		button_pos = [250, 225, 100, 50]
		mouse = pygame.mouse.get_pos()
		text = pygame.font.SysFont(None, 17).render("Click to Start", True, black)
		title = pygame.font.SysFont(None, 50).render("Snake Thing Game", True, black)
		subtitle = pygame.font.SysFont(None, 35).render("A game about snake farming!", True, black)
		instructions = pygame.font.SysFont(None, 20).render("Buy stuff on the right and watch your snakes eat apples", True, black)
		names = pygame.font.SysFont(None, 20).render("Proudly created by Mason and Josh", True, black)

		center_text(gameDisplay, title, 300, 100)
		center_text(gameDisplay, subtitle, 300, 300)
		center_text(gameDisplay, instructions, 300, 400)
		center_text(gameDisplay, names, 300, 170)
		

        
		if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]: #if mouse is inside the button
			pygame.draw.rect(gameDisplay, green,(button_pos[0],button_pos[1],button_pos[2],button_pos[3])) #change colour
			center_text(gameDisplay, text, 300, button_pos[1] + 17)
			if pygame.mouse.get_pressed()[0] == True:
				intro = True
				button_click.play(0,0,0)
                         
                       
		else:
			pygame.draw.rect(gameDisplay, dim_green,(button_pos[0],button_pos[1],button_pos[2],button_pos[3])) #otherwise use the regular colour
			center_text(gameDisplay, text, 300, button_pos[1] + 17)


			
		pygame.display.update()
		clock.tick(fps)

background_sound.set_volume(1.0)                                    
background_sound.play (-1,0,0)
game_intro()
background_sound.set_volume(0.4) 
while not crashed:
	Draw()
	Logic()
	Take_Input()

pygame.quit()
