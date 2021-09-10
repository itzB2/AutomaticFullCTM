from ctm.full import Full
from ctm.Constants import *
import pygame

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("CTM maker")

running = True

class Button:
	def __init__(self, pos):
		self.pos = pos
		self.hasImage = False
		self.nS = pygame.image.load("assets/imageSelect.png")
		self.nSRect = self.nS.get_rect()
		self.nSRect.topleft = pos
		self.S = pygame.image.load("assets/imageSelected.png")
		self.SRect = self.S.get_rect()
		self.SRect.topleft = pos
		self.image = ""

	def draw(self, surface):
		if self.hasImage:
			surface.blit(self.S, self.SRect)
		else:
			surface.blit(self.nS, self.nSRect)


class TextButton:
	def __init__(self, text, pos):
		self.pos = pos
		self.text = text

	def draw(self, surface):
		pass

class Scene:
	def __init__(self, surface):
		self.surface = surface
		self.surface.fill((60,60,60,255))
		self.sceneID = 1
		self.flags = {}
		self.pushFlags = {}
		self.font = pygame.font.Font("assets/font.ttf", 35)

	def draw(self):
		self.surface.fill((60,60,60,255))
		if self.sceneID == 1:
			self.flags = {
						  "clearSelectedImage": "",
						  "fullSelectedImage": "",
						  "objects": {}
						 }

			self.flags["objects"]["clearSelectedButton"] = Button((50, 50))
			self.flags["objects"]["fullSelectedButton"] = Button((350, 50))

			for obj in self.flags["objects"]:
				self.flags["objects"][obj].draw(self.surface)

			self.pushFlags["1"] = self.flags
		elif self.sceneID == 2:
			pass

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