from ctm.full import Full
from ctm.Constants import *
import pygame

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("CTM maker")

running = True

class Scene:
	def __init__(self, surface):
		self.surface = surface
		self.surface.fill((60,60,60,255))

	def draw(self):
		self.surface.fill((60,60,60,255))

	def update(self):
		self.draw()

scene = Scene(window)

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	scene.update()
	pygame.display.flip()

pygame.quit()