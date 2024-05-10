import pygame
import sys
from life import Life
from ants import Ants
from loops import Loops
from wa_tor import Wator

pygame.init()

GRID = (90, 90, 90)
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800
CELL_SIZE = 10
FPS = 12

automata = ['Life-Like', 'Ants', 'Loops', 'Wa-Tor']
simulations = [Life(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE),
               Ants(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE),
               Loops(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE),
               Wator(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)]

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


clock = pygame.time.Clock()

automaton_index = 0
automaton = automata[automaton_index]
simulation = simulations[automaton_index]
rule = simulation.rule_list[simulation.rule_index]
state = 'INITIAL'


def build_caption():
    return automaton.upper() + '  -  ' + rule.upper() + '  -  ' + str(FPS) + ' FPS  -  ' + state


pygame.display.set_caption(build_caption())

# Simulation Loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():

        # quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if automaton == 'Ants':
                pos = pygame.mouse.get_pos()
                row = pos[1] // CELL_SIZE
                column = pos[0] // CELL_SIZE
                simulation.place_ant(row, column)
            elif automaton == 'Loops':
                pos = pygame.mouse.get_pos()
                row = pos[1] // CELL_SIZE
                column = pos[0] // CELL_SIZE
                simulation.place_loop(row, column)
            else:
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
                if FPS < 58:
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

            elif event.key == pygame.K_p:
                if simulation.is_running() == False:
                    if automaton_index < len(automata) - 1:
                        automaton_index += 1
                    else:
                        automaton_index = 0
                    automaton = automata[automaton_index]
                    simulation.clear()
                    simulation = simulations[automaton_index]
                    rule = simulation.rule_list[simulation.rule_index]
                    pygame.display.set_caption(build_caption())

            elif event.key == pygame.K_o:
                if simulation.is_running() == False:
                    if automaton_index > 0:
                        automaton_index -= 1
                    else:
                        automaton_index = len(automata) - 1
                    automaton = automata[automaton_index]
                    simulation.clear()
                    simulation = simulations[automaton_index]
                    rule = simulation.rule_list[simulation.rule_index]
                    pygame.display.set_caption(build_caption())

    # 2. Updating State
    simulation.update()

    # 3. Drawing
    window.fill(GRID)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
