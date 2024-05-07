import pygame, sys
from simulation import Simulation

pygame.init()

GRID = (90, 90, 90)
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800
CELL_SIZE = 10
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

rule = simulation.rule_list[simulation.rule_index]
state = 'INITIAL'

def build_caption():
	return rule.upper() + '  -  ' + str(FPS) + ' FPS  -  ' + state

pygame.display.set_caption(build_caption())

#Simulation Loop
while True:

	# 1. Event Handling
	for event in pygame.event.get():

		# quit event
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# click event
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			row = pos[1] // CELL_SIZE
			column = pos[0] // CELL_SIZE
			simulation.toggle_cell(row, column)

		# key press event
		if event.type == pygame.KEYDOWN:

			# return
			if event.key == pygame.K_RETURN:
				simulation.start()
				state = 'RUNNING'
				pygame.display.set_caption(build_caption())

			# space
			elif event.key == pygame.K_SPACE:
				simulation.stop()
				state = 'PAUSED'
				pygame.display.set_caption(build_caption())

			# f
			elif event.key == pygame.K_f:
				if FPS < 60:
					FPS += 2
					pygame.display.set_caption(build_caption())

			# s
			elif event.key == pygame.K_s:
				if FPS > 5:
					FPS -= 2
					pygame.display.set_caption(build_caption())

			# r
			elif event.key == pygame.K_r:
				simulation.create_random_state()

			# c
			elif event.key == pygame.K_c:
				simulation.clear()

			# esc
			elif event.key == pygame.K_q:
				pygame.quit()
				sys.exit()

			elif event.key == pygame.K_DOWN:
				simulation.rule_down()
				rule = simulation.rule_list[simulation.rule_index]
				pygame.display.set_caption(build_caption())

			elif event.key == pygame.K_UP:
				simulation.rule_up()
				rule = simulation.rule_list[simulation.rule_index]
				pygame.display.set_caption(build_caption())

	# 2. Updating State
	simulation.update()

	# 3. Drawing
	window.fill(GRID)
	simulation.draw(window)

	pygame.display.update()
	clock.tick(FPS)