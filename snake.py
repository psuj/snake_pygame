import pygame, sys, os, time


pygame.init()

screen = pygame.display.set_mode((800, 800))
image1 = pygame.image.load("img1")
# width, height
snake_head_location = (0, 0)
current_move_direction = ""

screen.fill((100, 100, 100))
screen.blit(image1, (0, 0))

#pygame.display.flip()
#time.sleep(1)

def move_snake_head(direction):
	global snake_head_location
	screen.fill((100, 100, 100))
	#new_location = (5, 0)
	#print(snake_head_location[0])
	#print(snake_head_location[1])
	if direction == "right":
		new_location = (snake_head_location[0] + 5, snake_head_location[1])
		screen.blit(image1, (new_location[0], new_location[1]))
		snake_head_location = new_location
	elif direction == "left":
		new_location = (snake_head_location[0] -5, snake_head_location[1])
		screen.blit(image1, (new_location[0], new_location[1]))
		snake_head_location = new_location
	elif direction == "up":
		new_location = (snake_head_location[0], snake_head_location[1] - 5)
		screen.blit(image1, (new_location[0], new_location[1]))
		snake_head_location = new_location
	elif direction == "down":
		new_location = (snake_head_location[0], snake_head_location[1] + 5)
		screen.blit(image1, (new_location[0], new_location[1]))
		snake_head_location = new_location


	#pygame.display.flip()

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
			print(event)
	

while True:
	moving_direction = input(pygame.event.get())
	print(moving_direction)
	if moving_direction:
		current_move_direction = moving_direction
	move_snake_head(current_move_direction)
	pygame.display.flip()
	#time.sleep(0.5)
