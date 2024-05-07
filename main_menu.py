import pygame 
import pygame_menu
import main

pygame.init()
surface = pygame.display.set_mode((1500, 800))

def start_simulation():
	main()

menu = pygame_menu.Menu('Menu', 1400, 700, theme='default')

menu.add.button('Run', start_simulation)