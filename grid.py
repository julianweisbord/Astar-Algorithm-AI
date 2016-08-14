
class Grid:

	grid = []

	def __init__(self):
		x,y = self.init_grid()
		self.row =x
		self.col = y
		assert(x > 0 and y >0)
		for i in range(self.row):
			self.grid.append([])
			for j in range(self.col):
				self.grid[i].append(0)
		print (self.grid)

		self.goal_x, self.goal_y = self.set_goal()
		self.start_x, self.start_y = self.set_start()
		print("TESTING",self.grid[0])

	def init_grid(self):
		x = int(raw_input("Enter grid rows: "))
		y = int(raw_input("Enter grid cols: "))
		return x, y

	def place_block(self):
		place_x = int(raw_input("Set x coordinate of block: "))
		place_y = int(raw_input("Set y coordinate of block: "))
		self.populate_grid(place_x, place_y, 1)
		return place_x, place_y

	def current_pos(self,x_pos, y_pos):
		self.populate_grid(x_pos,y_pos, 'C')

	def set_goal(self):
		goal_x = int(raw_input("Set x coordinate of goal: "))
		goal_y = int(raw_input("Set y coordinate of goal: "))
		self.populate_grid(goal_x, goal_y, 'G')
		return goal_x,goal_y

	def set_start(self):
		start_x = int(raw_input("Set x coordinate of start: "))
		start_y = int(raw_input("Set y coordinate of start: "))
		self.populate_grid(start_x, start_y, 'S')
		return start_x, start_y

	#Calculates the nth position from x and y coordinates
	def calc_pos_grid(self,x, y):
		assert(x <=self.row and y <= self.col)
		assert(x > 0 and y >0)
		print("self.row: ", self.row, " self.col:", self.col)
		position =1
		count_cols = 1
		count_rows =1
		while count_cols < y:
			position += self.col #increase position by length of each row
			count_cols+=1
		while count_rows < x:
			position+=1
			count_rows+=1
		print ("position is: ", position)


	def print_grid(self):
		print "Here is the grid: "
		for colIndex in range(self.row):
			print str(self.grid[colIndex]).strip('[').strip(']')

	def populate_grid(self, pos_x,pos_y, character):
		try:
			if self.grid[pos_y-1][pos_x-1]!=0:
				print ("cannot place a block here, exiting")
				exit(0)
			self.grid[pos_y-1][pos_x-1] = character

			self.calc_pos_grid(pos_x, pos_y)# single number for position
		except Exception as error:
			print ("error: ", error)
			exit(0)
