import pygame
import time
import random
import math

pygame.init()

display_width = 400
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bisque = (255,228,196)
green = (0,128,0)
navy = (0,0,128)
yellow = (255,255,0)
orange = (255,165,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project')
clock = pygame.time.Clock()


def man(x_changed,ang):
	angle = ang
	arm = 50
	#right arm
	rastart = [200-x_changed,130]
	raend = [200-x_changed+int(arm*math.cos((math.pi*angle)/180)),130+int(arm*math.sin((math.pi*angle)/180))]
	print("change in arm & leg", angle)
#	raend = [230-x_changed,130]


	#left arm
	lastart = [200-x_changed,130]
	laend = [200-x_changed-int(arm*math.cos((math.pi*angle)/180)),130-int(arm*math.sin((math.pi*angle)/180))]

	#right leg
	rlstart = [200-x_changed,210]
	rlend = [200-x_changed+int(arm*math.cos((math.pi*angle)/180)),210+int(arm*math.sin((math.pi*angle)/180))]

	#left leg
	llstart = [200-x_changed,210]
	llend = [200-x_changed-int(arm*math.cos((math.pi*angle)/180)),210-int(arm*math.sin((math.pi*angle)/180))]

	pygame.draw.circle(gameDisplay,bisque,[200-x_changed,80],30)
	pygame.draw.arc(gameDisplay,red,[190-x_changed,80,20,20],math.pi,2*math.pi,3)
	pygame.draw.circle(gameDisplay,green,[190-x_changed,70],3)
	pygame.draw.circle(gameDisplay,green,[210-x_changed,70],3)
	pygame.draw.line(gameDisplay,navy,[200-x_changed,110],[200-x_changed,210],3)
	pygame.draw.line(gameDisplay,orange,rastart,raend,3)#right arm
	pygame.draw.line(gameDisplay,orange,lastart,laend,3)#left arm
	pygame.draw.line(gameDisplay,yellow,rlstart,rlend,3)#right leg
	pygame.draw.line(gameDisplay,yellow,llstart,llend,3)#left leg

	pygame.display.update()


def gameLoop():
	for i in range(100000): pass
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	started = True
	gameExit = False
	isPaused = False
	x_changed = 0
	xx = 0
	fps = 10
	ang = 45
	while not gameExit:
		gameDisplay.fill(white)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					if not isPaused: isPaused = True
					else: isPaused = False
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		if isPaused: continue
		test = random.randrange(0,100)
		if test%2 == 0: xx = 5
		else: xx = -5
		print("change in position ",xx)
		ang = x_changed+xx#abs(xx)
		x_changed += xx
		man(x_changed,ang)
		clock.tick(fps)
		
gameLoop()
pygame.quit() #Anti init
quit()