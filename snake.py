import pygame, sys, os, time, random


pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
snake_unit = pygame.image.load("img1")
snake_food = pygame.image.load("img2")
# width, height
snake_head_location = (0, 0)
current_move_direction = ""
food_spawned = 0

screen.fill((100, 100, 100))
screen.blit(snake_unit, (0, 0))

#pygame.display.flip()
#time.sleep(1)
def draw_board():
	screen.fill((100, 100, 100))
	pygame.display.flip()


def spawn_snake_food():
	food_location = (random.randrange(0, 780, 10), random.randrange(0, 780, 10))
	#print(food_location)
	screen.blit(snake_food, food_location)
	return food_location


def move_snake_head(direction):
	global snake_head_location
	#screen.fill((100, 100, 100))
	move_unit = 10
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
	for event in events:
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
	screen.fill((100, 100, 100))
	moving_direction = input(pygame.event.get())
	#print(moving_direction)
	#if not food_spawned:
	if not food_spawned:
		food_location = spawn_snake_food()
		food_spawned = 1
	else:
		screen.blit(snake_food, food_location)
	if moving_direction:
		current_move_direction = moving_direction
		#spawn_snake_food()
	move_snake_head(current_move_direction)
	pygame.display.flip()
	#time.sleep(0.5)
