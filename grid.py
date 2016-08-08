
class Grid:

	grid = []

	def __init__(self):
		x,y = self.init_grid()
		self.x =x
		self.y = y
		assert(x > 0 and y >0)
		for i in range(x):
			self.grid.append([])
			for j in range(y):
				self.grid[i].append(0)
		print self.grid

		self.goal_x, self.goal_y = self.set_goal()
		self.start_x, self.start_y = self.set_start()


	def init_grid(self):
		x = int(raw_input("Enter grid rows: "))
		y = int(raw_input("Enter grid cols: "))
		return x, y

	def place_block(self):
		place_x = int(raw_input("Set x coordinate of block: ")) -1
		place_y = int(raw_input("Set y coordinate of block: ")) -1
		self.populate_grid(place_x, place_y, 1)
		return place_x, place_y

	def current_pos(self,x_pos, y_pos):
		self.populate_grid(x_pos,y_pos, 'C')
		
	def set_goal(self):
		goal_x = int(raw_input("Set x coordinate of goal: ")) -1
		goal_y = int(raw_input("Set y coordinate of goal: ")) -1
		self.populate_grid(goal_x, goal_y, 'G')
		return goal_x,goal_y

	def set_start(self):
		start_x = int(raw_input("Set x coordinate of start: ")) -1
		start_y = int(raw_input("Set y coordinate of start: ")) -1
		self.populate_grid(start_x, start_y, 'S')
		return start_x, start_y


	def print_grid(self):
		print "Here is the grid: "
		for colIndex in range(self.x):
			print str(self.grid[colIndex]).strip('[').strip(']')

	def populate_grid(self, pos_x,pos_y, character):
		try:
			if self.grid[pos_x][pos_y]!='0':
				print "cannot place a block here, exiting"	
				exit(0)	
			self.grid[pos_x][pos_y] = character

		except  Exception as error:
			print error
			exit(0)
