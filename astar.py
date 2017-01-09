import grid
import heapq

# A* Algorithm:
#f(n) = g(n) + h(n) where g(n) represents the cost of a node n from the start,
# and h(n) represents the heuristic's estimated cost from the current node n
# to the goal

class Astar:
	frontier = []#Discovered nodes that must be evaluated, list of node lists
	cameFrom = {} #nodes already evaluated
	cost_so_far = {} #neighbor is key, cost is value, holds temperary gcost at nodes


	def __init__(self,start, goal):

		self.start = start
		self.goal = goal

		heapq.heapify(self.frontier)
		heapq.heappush(self.frontier, (0, start)) # Heapq can take tuples for priority (priority, task)
		self.cost_so_far[start] =0
		self.cameFrom[start] = None



	#Adjusted manhattan heuristic h(n)
	def heuristic(self,startArr,goalArr, current, neighborTup):
		print("In heuristic current, start, goal: ", current, startArr, goalArr)

		start_x,start_y =startArr
		goal_x, goal_y =goalArr
		cur_x, cur_y = current
		next_x, next_y = neighborTup

		manhattan = abs(goal_x - next_x) + abs(goal_y - next_y)
		#Adjusted for tie breakers, heuristic will favor straight line paths to goal
		#change in position
		dx1= next_x - goal_x
		dy1= next_y - goal_y
		dx2= start_x -goal_x
		dy2= start_y - goal_y
		cross = abs(dx1*dy2 - dy1*dx2)
		# print "cross: ", cross

		return (manhattan + cross*.0001)

	# Examines which neighbor has the lowest f(n) = g(n) + h(n)
	def astar_search(self,graph, start, goal):
		count = 0
		prev_cur = None
		while len(self.frontier) >0:
			#This chunk makes sure the algorithm doesn't try to go places outside the MAX_MOVE cost
			# if prev_cur != None and prev_cur[0] >=0 and prev_cur[1] >=0:
			# 	index=0
			# 	for node in self.frontier:
			# 		print "Node: ", node
			# 		# print "prev_cur ", prev_cur
			# 		if int(abs(node[1][0] - prev_cur[0])) >int(grid.MAX_MOVE): #if the zero position is not within move cost of prev_cur[0]
			# 			print "\n DELETEING ",self.frontier[index] ,"\n"
			# 			print "\n IMPORTANT ", abs(node[1][0] - prev_cur[0]), "\n"
			# 			print "node[1][0] ", node[1][0], " prev_cur[0] ", prev_cur[0]
			# 			del self.frontier[index] #delete that node
			# 		elif int(abs(node[1][1] - prev_cur[1])) >int(grid.MAX_MOVE): #if the first position is not with move cost of prev_cur[1]
			# 			print "\n DELETEING ",self.frontier[index] ,"\n"
			# 			print "\n IMPORTANT ", abs(node[1][1] - prev_cur[1]), "\n"
			# 			print "node[1][1] ", node[1][1], " prev_cur[1] ", prev_cur[1]
			# 			del self.frontier[index] #delete that node, it cannot be considered for movement
			# 		index+=1

			current = heapq.heappop(self.frontier)[1] #get lowest cost node
			prev_cur =current
			print "\n Current: ", current, "\n"
			count+=1

			foundGoal =graph.place_path(current)
			if foundGoal == True:
				break
			elif foundGoal == None:
				continue # test this

			for neighbor in graph.neighbors(current):
				print "Neighbor: ", neighbor
				print "Cost So Far Dict: ", self.cost_so_far
				gcost = self.cost_so_far[current] + graph.cost(current, neighbor) # neighbor is the tuple
				#if neighbor is not in self.cost_so_far, default value is near infinity
				if neighbor not in self.cost_so_far or gcost < self.cost_so_far[neighbor]: #neighbor might be in cost{} with a higher cost value
				#which means we will have to replace it with the new value
					self.cost_so_far[neighbor] = gcost #update neighbor gscore to be the smaller cost
					priority = gcost + self.heuristic(self.start, self.goal, current, neighbor) # set a node's priority in the open set.
					heapq.heappush(self.frontier,(priority,neighbor))
					print "Frontier: ", self.frontier
					self.cameFrom[neighbor] = current
		return count-1

		# def astar_search(self,graph, start, goal):
		# 	count = 0
		# 	prev_cur = None
		# 	while len(self.frontier) >0:
		# 		#This chunk makes sure the algorithm doesn't try to go places outside the MAX_MOVE cost
		# 		# if prev_cur != None and prev_cur[0] >=0 and prev_cur[1] >=0:
		# 		# 	index=0
		# 		# 	for node in self.frontier:
		# 		# 		print "Node: ", node
		# 		# 		# print "prev_cur ", prev_cur
		# 		# 		if int(abs(node[1][0] - prev_cur[0])) >int(grid.MAX_MOVE): #if the zero position is not within move cost of prev_cur[0]
		# 		# 			print "\n DELETEING ",self.frontier[index] ,"\n"
		# 		# 			print "\n IMPORTANT ", abs(node[1][0] - prev_cur[0]), "\n"
		# 		# 			print "node[1][0] ", node[1][0], " prev_cur[0] ", prev_cur[0]
		# 		# 			del self.frontier[index] #delete that node
		# 		# 		elif int(abs(node[1][1] - prev_cur[1])) >int(grid.MAX_MOVE): #if the first position is not with move cost of prev_cur[1]
		# 		# 			print "\n DELETEING ",self.frontier[index] ,"\n"
		# 		# 			print "\n IMPORTANT ", abs(node[1][1] - prev_cur[1]), "\n"
		# 		# 			print "node[1][1] ", node[1][1], " prev_cur[1] ", prev_cur[1]
		# 		# 			del self.frontier[index] #delete that node, it cannot be considered for movement
		# 		# 		index+=1
		#
		# 		current = heapq.heappop(self.frontier)[1] #get lowest cost node
		# 		prev_cur =current
		# 		print "\n Current: ", current, "\n"
		# 		count+=1
		#
		# 		foundGoal =graph.place_path(current)
		# 		if foundGoal == True:
		# 			break
		# 		elif foundGoal == None:
		# 			continue # test this
		#
		# 		for neighbor in graph.neighbors(current).iteritems():
		# 			print "Neighbor: ", neighbor
		# 			print "Cost So Far Dict: ", self.cost_so_far
		# 			gcost = self.cost_so_far[current] + graph.cost(current, neighbor[1]) # neighbor[1] is the tuple, problem line!
		# 			#if neighbor is not in self.cost_so_far, default value is near infinity
		# 			if neighbor not in self.cost_so_far or gcost < self.cost_so_far[neighbor]: #neighbor might be in cost{} with a higher cost value
		# 			#which means we will have to replace it with the new value
		# 				self.cost_so_far[neighbor[1]] = gcost #update neighbor gscore to be the smaller cost
		# 				priority = gcost + self.heuristic(self.start, self.goal, current, neighbor[1]) # set a node's priority in the open set.
		# 				heapq.heappush(self.frontier,(priority,neighbor[1]))
		# 				print "Frontier: ", self.frontier
		# 				self.cameFrom[neighbor] = current
		# 	return count-1
