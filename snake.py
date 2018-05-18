import pygame, sys, os, time, random


pygame.init()
pygame.mixer.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))

#object loads
snake_unit = pygame.image.load("img1")
snake_body_img = pygame.image.load("img2")
snake_food = pygame.image.load("img3")
sound1 = pygame.mixer.Sound("sound1.wav")

# width, height
snake_head_location = (0, 0)
food_location = (999, 999)
current_move_direction = ""
food_spawned = 0
snake_body = list()

screen.fill((100, 100, 100))
screen.blit(snake_unit, (0, 0))

def show_snake_body():
	#global snake_body
	#new_snake_body = list()
	if len(snake_body) > 0:
		'''if move_direction == "right":
			for unit in snake_body:
				new_unit = (unit[0] + 20, unit[1])
				new_snake_body.append(new_unit)



		#snake_body[0] = snake_head_location
		for unit in new_snake_body:
			screen.blit(snake_body_img, unit)
		pygame.display.flip()
		
		#print(len(snake_body))
		#snake_body[0] = snake_head_location
		#for i in range(1, len(snake_body), 1):
		#	snake_body[i] = snake_body[i-1] 
		#snake_body[0] = snake_head_location

		#for unit in snake_body:
			#screen.blit(snake_body_img, unit)
		#pygame.display.flip()
	'''
		snake_body[0] = snake_head_location
		screen.blit(snake_body_img, snake_body[0])

def enlarge_snake(head_x, head_y):
	global snake_body
	#snake_head_location[0] = head_x
	#snake_head_location[1] = head_y
	if len(snake_body) == 0:
		new_body_unit = (head_x - 20, head_y)
		snake_body.append(new_body_unit)
	#else:
		print(snake_body[0])
		#snake_body[len(snake_body)-1]
	
	#for unit in snake_body:
		#screen.blit(snake_unit, unit)
		#pygame.display.flip()





def food_eaten_check():
	global food_spawned
	head_x = snake_head_location[0]
	head_y = snake_head_location[1]
	food_x = food_location[0]
	food_y = food_location[1]

	for x in range(head_x, head_x + 21, 1):
		for y in range(head_y, head_y + 21, 1):
			if x == food_x and y == food_y:
				print("food eaten")
				food_spawned = 0
				sound1.play()
				enlarge_snake(head_x, head_y)
				break


def spawn_snake_food():
	global food_location
	food_location = (random.randrange(0, 780, 20), random.randrange(0, 780, 20))
	#print(food_location)
	screen.blit(snake_food, food_location)
	return food_location


def move_snake_head(direction):
	global snake_head_location
	#print("move snake head")
	#screen.fill((100, 100, 100))
	move_unit = 20
	#new_location = (5, 0)
	#print(snake_head_location[0])
	#print(snake_head_location[1])
	if direction == "right":
		new_location = (snake_head_location[0] + move_unit, snake_head_location[1])
		if new_location[0] < width - 30:
			#print(new_location)
			screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
	elif direction == "left":
		new_location = (snake_head_location[0] - move_unit, snake_head_location[1])
		if new_location[0] > -10:
			screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
	elif direction == "up":
		new_location = (snake_head_location[0], snake_head_location[1] - move_unit)
		if new_location[1] > -10:
			screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
	elif direction == "down":
		new_location = (snake_head_location[0], snake_head_location[1] + move_unit)
		if new_location[1] < height - 30:
			screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))


	pygame.display.flip()

def input(events):
	#print("input")
	for event in events:
		#print(event)
		if event.type == pygame.QUIT:
			sys.exit(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				move_snake_head("right")
				return "right"
			elif event.key == pygame.K_a:
				move_snake_head("left")
				return "left"
			elif event.key == pygame.K_w:
				move_snake_head("up")
				return "up"
			elif event.key == pygame.K_s:
				move_snake_head("down")
				return "down"
			#print(event)
	

while True:
	#draw_board()
	#screen.fill((100, 100, 100))
	#food_eaten_check()
	#show_snake_body(current_move_direction)
	food_eaten_check()
	moving_direction = input(pygame.event.get())
	#print(moving_direction)
	#if not food_spawned:
	screen.fill((100, 100, 100))
	if not food_spawned:
		food_location = spawn_snake_food()
		food_spawned = 1
	else:
		screen.blit(snake_food, food_location)
	if moving_direction:
		current_move_direction = moving_direction
		#spawn_snake_food()
	#screen.fill((100, 100, 100))
	move_snake_head(current_move_direction)
	show_snake_body()
	#show_snake_body()
	#move_snake_head(current_move_direction)
	pygame.display.flip()
	#time.sleep(0.3)
