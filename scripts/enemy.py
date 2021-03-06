import sys
import pygame
import random
from pygame.locals import *

initial_pos_list = [[[(50 ,465), (300 ,315)]]]

class Enemy(pygame.sprite.Sprite):
	def __init__(self, character, level, number):
		"""
		arg:
			character: player number (0 for korea fish)
			level: which level's enemy (start from 0)
			number: which enemy of this level (start from 0)
		"""
		#todo: change character image to the right character (current: black)
		super(Enemy, self).__init__()
		self.surf = pygame.Surface((60, 90))
		self.surf.fill((255,0,0))
		#self.rect = self.surf.get_rect()
		self.rect = self.surf.get_rect(topleft = initial_pos_list[character][level][number])
		self.character = character
		self.level = level
		self.number = number
		self.b_move_right = True
		self.behavior = 1

	def is_out_of_range(self, move_x, floor):
		if self.rect.left + move_x < floor.left:
			return True
		elif self.rect.right + move_x > floor.right:
			return True

		return False

	def get_floor(self, floor_list):
		floor_target = Rect(0,0,0,0)
		diff_min = 100000
		for ifloor in floor_list:			
			self.rect.centery
			if ifloor.left <= self.rect.centerx and ifloor.right >= self.rect.centerx:
				diff = ifloor.top - self.rect.bottom
				if diff >= 0 and diff_min > diff:
					diff_min = diff
					floor_target = ifloor

		return floor_target

	def update(self, floor_list, player_rect):
		"""
		This function will be called in the main loop. Update enemy's behavior.

		arg:
			floor_list: a list of all floor's rect in this stage
			player_rect: player's current rect
		"""
		#todo : enemy AI (move)
		floor = self.get_floor(floor_list)
		player_x = player_rect.centerx
		player_y = player_rect.centery
		move_step = 1  
		if self.behavior == 0:       # random move
			local = random.randint(floor.left, floor.right)
			if local > self.rect.centerx:
				self.rect.move_ip(+move_step, 0)
			elif local < self.rect.centerx:
				self.rect.move_ip(-move_step, 0)

		elif self.behavior == 1:      # the rightest to the leftest			
			if self.b_move_right:
				if self.is_out_of_range(move_step, floor):
					self.b_move_right = False					
				else:
					self.rect.move_ip(move_step, 0)
			else:
				if self.is_out_of_range(-move_step, floor):
					self.b_move_right = True					
				else:
					self.rect.move_ip(-move_step, 0)
		elif self.behavior == 2:     # close to player
			if self.rect.centerx < player_x:
				if not self.is_out_of_range(move_step,floor):
					self.rect.move_ip(move_step, 0)
			else:
				if not self.is_out_of_range(-move_step,floor):
					self.rect.move_ip(-move_step, 0)

	def get_surf(self):
		return self.surf

	def get_rect(self):
		return self.rect