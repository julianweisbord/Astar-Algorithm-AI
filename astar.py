import grid
import heapq

# A* Algorithm:
#f(n) = g(n) + h(n) where g(n) represents the cost of a node n from the start,
# and h(n) represents the heuristic's estimated cost from the current node n
# to the goal

class Astar:
	frontier = []#Discovered nodes that must be evaluated, list of node lists
	closedSet = {} #nodes already evaluated
	cost = {} #vertex is key, cost is value


	def __init__(self,start, goal):

		self.start = start
		self.goal = goal

		heapq.heapify(self.frontier)
		heapq.push(self.frontier, (0, start)) # Heapq can take tuples for priority (priority, task)
		self.cost[start] =0
		self.cost[start] = None



	#Adjusted manhattan heuristic
	def heuristic(self,startArr,goalArr, current):
		print(current)

		start_x,start_y =startArr
		goal_x, goal_y =goalArr
		cur_x,cur_y = current

		manhattan = abs(goal_x - start_x) + abs(goal_y - start_y)
		#Adjusted for tie breakers, heuristic will favor straight line paths to goal
		#change in position
		dx1= goal_x - cur_x
		dy1= goal_y -cur_y
		dx2= goal_x - start_x
		dy2= goal_y -start_y
		cross = abs(dx1*dy2 - dy1*dx2)

		return (manhattan + cross*.0001)

	# Examines which vertex has the lowest f(n) = g(n) + h(n)
	def astar_search(self,graph, start, goal):
		current = heapq.heappop(self.frontier)[1]
		print("Should be start val: ", current)

		while self.frontier.len() >0:

			foundGoal =graph.place_path(current)
			if foundGoal == True:
				break

			for vertex in graph.neighbors(current):
				gcost = self.cost[current] + graph.cost(current, vertex)
				#if vertex is not in self.cost, default value is near infinity
				if gcost < self.cost.get(vertex, 1000000): # if current gscore + movement cost < vertex gscore:
					cost[vertex] = gcost
					priority = gcost + self.heuristic(start, goal, current)
