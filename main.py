from ctm.full import Full
from ctm.Constants import *
import pygame

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("CTM maker")

running = True

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	window.fill((60,60,60,255))
	pygame.display.flip()

pygame.quit()