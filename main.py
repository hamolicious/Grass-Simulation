import pygame
from time import time
from random import randint
from vector2d import Vec2d

from grass import Grass

#region pygame init
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 0

delta_time = 0
frame_start_time = 0
#endregion


def generate_grass(amount):
	dx = size[0] / amount
	grass = []

	for x in range(amount):
		g = Grass(x * dx, 600, 300 + randint(-100, 100), 6)
		grass.append(g)

	return grass


grass = generate_grass(200)
wind = (Vec2d(-100, size[1] * 0.6), 100)

take_screen_shots = True
frame_index = 0

key_lock = False
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	frame_start_time = time()
	screen.fill([200, 200, 250])

	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()
	key_press = pygame.key.get_pressed()

	if sum(key_press) == 0:
		key_lock = False

	wind[0].x += 50 * delta_time
	# pygame.draw.circle(screen, [51, 51, 51], wind[0].get(), 100, 2)

	if wind[0].x > size[0] + wind[1]:
		wind[0].x = -wind[1]
		take_screen_shots = False

	for g in grass:
		g.avoid([(mouse_pos, 50), wind])
		g.update(delta_time)
		g.display(screen)

	pygame.display.update()
	clock.tick(fps)
	delta_time = time() - frame_start_time
	pygame.display.set_caption(f'Framerate: {int(clock.get_fps())}')

	if take_screen_shots:
		pygame.image.save(screen, f'Frames/frame-{frame_index:05}.png')
		frame_index += 1
