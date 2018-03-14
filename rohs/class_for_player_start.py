from folder_for_classes import *


class player_start(object):
	
	
	def __init__(self, hero):
		self.hero = hero
	
	
	def return_attr(self):
		"""willl return the attributes of 
		   the hero that the player chose"""
		

		try:
			
			exec('return ' + '(' + self.hero + '.health, ' + self.hero + '.imgfile, ' + self.hero + '.heroname)')
		
		except:
			
			return (30, 'somefile.png', 'Knight')
	
	
	