import sys
import pygame
from game_settings import Settings
from ship import Ship

def run_game():
	#Initialize game and create a screen object.
	pygame.init()
	py_settings = Settings()
	screen = pygame.display.set_mode((py_settings.screen_width,py_settings.screen_height)) # to create a display window called 
												 #screen, on which we’ll draw all of the game’s graphical elements
	pygame.display.set_caption('fun game')
	# bg_color = (230,230,230)
	# Make a ship
	ships = Ship(screen)
	while True:
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():#Any keyboard or mouse event will cause the for loop to run
			if event.type == pygame.QUIT:
				sys.exit()
		# background color
		screen.fill(py_settings.bg_color)

		ship.blitme()
		# Make the most recently drawn screen visible.
		pygame.display.flip() #tells Pygame to make the most 
								#recently drawn screen visible
run_game() 