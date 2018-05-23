import pygame, sys, os, time, random


pygame.init()
pygame.mixer.init()
pygame.font.init()

font_object = pygame.font.Font("/Library/Fonts/Comic Sans MS.ttf", 40)
game_over_text = font_object.render("GAME OVER", True, (255, 20, 20))
score_text = font_object.render("0", True, (20, 255, 20))


#print(font)
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
points = 0
game_running = 1

#object loads
snake_unit = pygame.image.load("img1")
snake_body_img = pygame.image.load("img2")
snake_food = pygame.image.load("img3")
sound1 = pygame.mixer.Sound("sound1.wav")

# width, height
snake_head_location = (0, 0)
previous_snake_head_location = (0, 0)
food_location = (999, 999)
current_move_direction = ""
food_spawned = 0
snake_body = list()
snake_body.append(snake_head_location)

screen.fill((100, 100, 100))
screen.blit(snake_unit, (0, 0))

def game_over_procedure():
	while True:
		#screen.fill((50, 50, 50))
		screen.blit(game_over_text, (380, 380))
		pygame.display.flip()
	#time.sleep(2)
	#a = input()


def check_if_move_is_possible(location):
	#for unit in snake_body:
	#print("checking for location " + str(location))
	for i in range(2, len(snake_body), 1):
		#print("comparing" + str(location) + " and " + str(snake_body[i]))
		#if location[0] >= unit[0] and location[0] <= unit[0] and location[1] >= unit[1] and location[1] <= unit[1]:
			#print("loc check")
		if location == snake_body[i]:
			#print("wykryto kolizje")
			return False
		#if 1:
		#	return True
		#else:
			#print("loc2")
		#	return True
	return True


def enlarge_snake(head_x, head_y):
	global snake_body
	global points
	global score_text
	#snake_head_location[0] = head_x
	#snake_head_location[1] = head_y
	#if len(snake_body) == 1:
	#new_body_unit = (snake_head_location[0] - 20, snake_head_location[1])
		#new_body_unit = (snake_body[len(snake_body)-1][0] - 20, snake_body[len(snake_body)-1][1])
		#new_body_unit = (snake_body[0][0] - 20, snake_body[0][1])
		#print(new_body_unit)
		#snake_body.append(new_body_unit)
	#elif len(snake_body) > 1:
	#new_body_unit = (snake_body[len(snake_body)-1][0], snake_body[len(snake_body)-1][1])
	new_body_unit = (999, 999)
	if len(snake_body) == 1:
		snake_body.append(new_body_unit)
	snake_body.append(new_body_unit)
	points += 1
	score_text = font_object.render(str(points), True, (20, 255, 20))
	#


	#else:
	#	print(snake_body[0])
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
				#print("food eaten")
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
	global snake_body
	#print("move snake head")
	#screen.fill((100, 100, 100))
	move_unit = 20
	wall_hit = 0
	new_location = (0, 0)
	#print(snake_head_location[0])
	#print(snake_head_location[1])
	if direction == "right":
		new_location = (snake_head_location[0] + move_unit, snake_head_location[1])
		if new_location[0] < width - 30:#and check_if_move_is_possible(new_location):
			#print(new_location)
			#screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
			snake_body[0] = snake_head_location
		else:
			#print("else")
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
			wall_hit = 1
	elif direction == "left":
		new_location = (snake_head_location[0] - move_unit, snake_head_location[1])
		if new_location[0] > -10:#and check_if_move_is_possible(new_location):
			#screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
			snake_body[0] = snake_head_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
			wall_hit = 1
	elif direction == "up":
		new_location = (snake_head_location[0], snake_head_location[1] - move_unit)
		if new_location[1] > -10:#and check_if_move_is_possible(new_location):
			#screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
			snake_body[0] = snake_head_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
			wall_hit = 1
	elif direction == "down":
		new_location = (snake_head_location[0], snake_head_location[1] + move_unit)
		if new_location[1] < height - 30:#and check_if_move_is_possible(new_location):
			#screen.blit(snake_unit, (new_location[0], new_location[1]))
			snake_head_location = new_location
			snake_body[0] = snake_head_location
		else:
			screen.blit(snake_unit, (snake_head_location[0], snake_head_location[1]))
			wall_hit = 1
		
		#print(len(snake_body))
	snake_body_to_show = list()
	snake_body_to_show.append(snake_head_location)
	#snake_body_to_show.append(snake_head_location)
		
		#if len(snake_body) > 1:
			#if len(snake_body) == 1:
			#	pass
			#print("show snake body")
	if not wall_hit:
		for i in range(1, len(snake_body), 1):
			snake_body_to_show.append(snake_body[i-1])
			#print("snake_body " + str(i) + "=" + str(snake_body_to_show[i]))
		#for i in range(1, len(snake_body), 1):
			#unit = (snake_body[i-1][0] - 10, snake_body[i-1][1])
			#snake_body_to_show.append(unit)

		#for i in range(0, len(snake_body), 1):
			#print("snake_body " + str(i) + "=" + str(snake_body_to_show[i]))

		for i in range(0, len(snake_body_to_show), 1):
			snake_body[i] = snake_body_to_show[i]
	#print("---")
	if check_if_move_is_possible(snake_body[0]):
	#print("\n")
		for i in range(1, len(snake_body), 1):
			screen.blit(snake_body_img, snake_body[i])

	#if check_if_move_is_possible(snake_body[0]):
		screen.blit(snake_unit, snake_body[0])

	else:
		print("game over")
		return "game over"
		#game_over_procedure()
		#		print(i)
		#print("snake_body " + i + "=" + snake_body[i])
	#		new_snake_body[i] = snake_body[i-1]
		#print("snake_body " + str(i) + "=" + str(snake_body[i]))

	#for i in range(0, len(snake_body), 1):
		#print("snake_body " + str(i) + "=" + str(snake_body[i]))
		#for i in range(1, len(snake_body)-1, 1):
		#	screen.blit(snake_body_img, new_snake_body[i])
	
	#snake_body = new_snake_body
	#pygame.display.flip()

def kb_input(events):
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
	moving_direction = kb_input(pygame.event.get())
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
	#if previous_location_counter % 2 == 0:
		#previous_snake_head_location = snake_head_location
	#move_snake_head(current_move_direction)
	#print(snake_body[0])
	#print(len(snake_body))
	#show_snake_body()
	#move_snake_head(current_move_direction)
	#show_snake_body()
	screen.blit(score_text, (750, 750))
	result = move_snake_head(current_move_direction)
	if result == "game over":
		screen.blit(game_over_text, (360, 360))
		game_running = 0
		pygame.display.flip()
		#game_running = 0
		#print("game over main")
		#pygame.quit()
		#while True:
			#screen.fill((50, 50, 50))
			#screen.blit(game_over_text, (380, 380))
			#pygame.display.flip()
		#time.sleep(2)
	#screen.blit(game_over_text, (100, 100))
	
	if game_running:
		pygame.display.flip()
	
#game_over_procedure()
	#time.sleep(1)
	#previous_location_counter += 1
