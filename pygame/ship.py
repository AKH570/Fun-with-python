import pygame
class Ship():
	def __init__(self,screen):
		self.screen = screen
		# Load the ship image and get its rect.
		self.img = pygame.image.load('E:/project-django/python_program/pygame/img/rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.img,self.rect)