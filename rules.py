
# rules for conway's game of life
def conways(cell_value, live_neighbors):
	if cell_value == 1:
		if live_neighbors > 3 or live_neighbors < 2:
			return 0 
		else:
			return 1
	else:
		if live_neighbors == 3:
			return 1
		else:
			return 0

def day_and_night(cell_value,live_neighbors):
	if cell_value == 1:
		if live_neighbors < 3 or live_neighbors == 5:
			return 0 
		else:
			return 1
	else:
		if live_neighbors == 3 or live_neighbors >= 6:
			return 1
		else:
			return 0