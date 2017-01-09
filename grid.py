
BLOCK_DIST = 1
MAX_MOVE = (2**.5)* BLOCK_DIST
class Grid:

	grid = []
	edges = {}

	def __init__(self, arg):
		if str(arg) == "def":
			self.defaultArgs()
			self.goal_x, self.goal_y = (4,4)
			self.start_x, self.start_y = (1,1)
		else:
			x,y = self.init_grid()
			self.row = x
			self.col = y

			assert(x > 0 and y >0)
			for i in range(self.row):
				self.grid.append([])
				for j in range(self.col):
					self.grid[i].append('0')
			print (self.grid)

			self.goal_x, self.goal_y = self.set_goal()
			self.start_x, self.start_y = self.set_start()
			print("TESTING",self.grid[0])
	# For debugging
	def defaultArgs(self):
		self.row = 6
		self.col =6
		for i in range(self.row):
			self.grid.append([])
			for j in range(self.col):
				self.grid[i].append('0')
		print (self.grid)

		self.populate_grid(4, 4, 'G')
		self.populate_grid(1, 1, 'S')

	def init_grid(self):
		x = int(raw_input("Enter grid rows: "))
		y = int(raw_input("Enter grid cols: "))
		return x, y

	#Put adgacent values in dictionary

	# def neighbors(self,position_list):
	# 	edges = {}
	# 	x,y = position_list
	#
	# 	assert(x!= None and y!= None)
	# 	# -1 from y because self.grid[y] is 1 larger than y
	# 	if len(self.grid) > y+1: #Make sure that we haven't gone out of range
	# 		if len(self.grid[y]) >= x+1:
	# 			if (x and (y+1)) > 0:
	# 				print "x index", x-1
	# 				print "y index", y
	# 				edges['up'] = x, y+1
	#
	# 	if len(self.grid) >= y+1: #Make sure that we haven't gone out of range
	# 		if len(self.grid[y]) > x:
	# 			if (y and (x+1)) > 0:
	# 				print "y index", y-1
	# 				edges['right'] = x+1, y
	# 	if len(self.grid) >= y+1: #Make sure that we haven't gone out of range
	# 		if len(self.grid[y]) >= x+1:
	# 			if (y and (x-1)) >= 0:
	# 				print "y index", y-1
	# 				edges['left'] = x-1, y
	# 	if len(self.grid) >= y+1: #Make sure that we haven't gone out of range
	# 		if len(self.grid[y]) >= x+1:
	# 			if (x and (y-1)) >= 0:
	# 				print "y index", y-2
	# 				edges['down'] = x, y-1
	# #add diagnols
	# 	# if len(self.grid) > y-1: #Make sure that we haven't gone out of range
	# 	# 	if len(self.grid[y]) >= x:
	# 	# 		if ((y+1) and (x+1)) > 0:
	# 	# 			edges['NE'] =y+1,x+1
	# 	#
	# 	# if len(self.grid) > y-2: #Make sure that we haven't gone out of range
	# 	# 	if len(self.grid[y]) >= x-2:
	# 	# 		if ((y+1) and (x-1)) > 0:
	# 	# 			edges['NW'] =y+1,x-1
	# 	#
	# 	# if len(self.grid) > y-2: #Make sure that we haven't gone out of range
	# 	# 	if len(self.grid[y]) >= x-2:
	# 	# 		if ((y-1) and (x-1)) > 0:
	# 	# 			edges['SW'] =y-1,x-1
	# 	# if len(self.grid) > y-3: #Make sure that we haven't gone out of range
	# 	# 	if len(self.grid[y]) >= x:
	# 	# 		if ((y-1) and (x+1)) > 0:
	# 	# 			edges['SE'] =y-1,x+1
	#
	# 	#Dont allow blocks to be vertices
	# 	for key, val in edges.items():
	# 		if val == 'X':
	# 			del myDict[key]
	#
	# 	print("Edges dictonary: ", edges)
	# 	return edges
	def neighbors(self, position_list):

		x,y = position_list
		count=0
		assert(x!= None and y!= None)
		#up, right, down, left, NW, NE, SE, SW
		edges = [(x,y+1),(x+1, y), (x, y-1), (x-1, y), (x-1,y+1),(x+1,y+1),(x+1,y-1),(x-1,y-1)]
		for pos in edges:
			if pos[0] > position_list[0]:
				#pop that
				del pos
			elif pos[1] > position_list[1]:
				#pop that
				del pos
		print("Edges list: ", edges)		
		return edges



		# # -1 from y because self.grid[y] is 1 larger than y
		# if len(self.grid) > y+1: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x+1:
		# 		if (x and (y+1)) > 0:
		# 			print "x index", x-1
		# 			print "y index", y
		# 			edges['up'] = x, y+1
		#
		# if len(self.grid) >= y+1: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) > x:
		# 		if (y and (x+1)) > 0:
		# 			print "y index", y-1
		# 			edges['right'] = x+1, y
		# if len(self.grid) >= y+1: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x+1:
		# 		if (y and (x-1)) >= 0:
		# 			print "y index", y-1
		# 			edges['left'] = x-1, y
		# if len(self.grid) >= y+1: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x+1:
		# 		if (x and (y-1)) >= 0:
		# 			print "y index", y-2
		# 			edges['down'] = x, y-1
	#add diagnols
		# if len(self.grid) > y-1: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x:
		# 		if ((y+1) and (x+1)) > 0:
		# 			edges['NE'] =y+1,x+1
		#
		# if len(self.grid) > y-2: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x-2:
		# 		if ((y+1) and (x-1)) > 0:
		# 			edges['NW'] =y+1,x-1
		#
		# if len(self.grid) > y-2: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x-2:
		# 		if ((y-1) and (x-1)) > 0:
		# 			edges['SW'] =y-1,x-1
		# if len(self.grid) > y-3: #Make sure that we haven't gone out of range
		# 	if len(self.grid[y]) >= x:
		# 		if ((y-1) and (x+1)) > 0:
		# 			edges['SE'] =y-1,x+1

		#Dont allow blocks to be vertices
		# for key, val in edges.items():
		# 	if val == 'X':
		# 		del myDict[key]

		# print("Edges list: ", edges)
		# return edges


	def cost(self, cur_pos, next_pos):
		print "next_pos ", next_pos
		(x1, y1) = cur_pos
		(x2, y2) = next_pos
		#functionality for diagnals too.
		print "Cost going in: ", BLOCK_DIST *( ((x2 - x1)**2 + (y2 -y1)**2)**.5 )
		return BLOCK_DIST *( ((x2 - x1)**2 + (y2 -y1)**2)**.5 )

	def place_block(self):
		place_x = int(raw_input("Set x coordinate of block: "))
		place_y = int(raw_input("Set y coordinate of block: "))
		self.populate_grid(place_x, place_y, 'X')
		#call a function to make sure that it is possible to find the path
		return place_x, place_y

	# Put a 'C' in the current position of the algorithm on the grid.
	# Also represents any previous positions with a '.' by calling populate_grid()
	def set_cur_pos(self,cur_pos):
		x_pos, y_pos = cur_pos
		validPos = self.populate_grid(x_pos,y_pos, 'C')


	def set_goal(self):
		goal_x = int(raw_input("Set x coordinate of goal: "))
		goal_y = int(raw_input("Set y coordinate of goal: "))
		self.populate_grid(goal_x, goal_y, 'G')
		return goal_x, goal_y

	def get_goal(self):
		return self.goal_x, self.goal_y

	def set_start(self):
		start_x = int(raw_input("Set x coordinate of start: "))
		start_y = int(raw_input("Set y coordinate of start: "))
		self.populate_grid(start_x, start_y, 'S')
		return start_x, start_y

	def get_start(self):
		return self.start_x, self.start_y

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
		return position

	def draw_grid(self):
		print ("Here is the grid: \n")
		for colIndex in range(self.row):
			print(str(self.grid[colIndex]).strip('[').strip(']'))

	def populate_grid(self, pos_x,pos_y, character):
		try:
			if self.grid[pos_y][pos_x]!='0':
				print ("Will not go here")
				return False
			self.grid[pos_y][pos_x] = character

			self.calc_pos_grid(pos_x, pos_y)# single number for position

		except Exception as error:
			print ("The error: ", error)
			exit(0)

		return True

	#Places a dot on the grid to show the astar path
	def place_path(self, xylocation):
		x, y = xylocation
		if self.grid[y][x]=='X':
			return None
		if self.grid[y][x] == 'G':
			print("Found Goal!")
			return True
		else:
			self.grid[y][x] = '.'

		return False
