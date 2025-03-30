import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	fps = 60
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT /2
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots, updateable, drawable)
	player = Player(x,y)
	field = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updateable.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				return
		pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.Surface.fill(screen, color=(0,0,0))
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		clock.tick(fps)
		dt = (clock.tick(fps))/1000


if __name__ == "__main__":
	main()
