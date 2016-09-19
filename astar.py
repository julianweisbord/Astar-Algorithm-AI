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



	#Adjusted manhattan heuristic
	def heuristic(self,startArr,goalArr, current):
		print("In heuristic currentL ", current)

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

	# Examines which neighbor has the lowest f(n) = g(n) + h(n)
	def astar_search(self,graph, start, goal):
		count = 0
		while len(self.frontier) >0:
			current = heapq.heappop(self.frontier)[1] #get lowest cost node
			print("Current: ", current)
			count+=1

			foundGoal =graph.place_path(current)
			if foundGoal == True:
				break
			elif foundGoal == None:
				continue # test this

			for neighbor in graph.neighbors(current).iteritems():
				gcost = self.cost_so_far[current] + graph.cost(current, neighbor[1]) # neighbors[1] is the tuple
				#if neighbor is not in self.cost_so_far, default value is near infinity
				if neighbor not in self.cost_so_far or gcost < self.cost_so_far[neighbor]: #neighbor might be in cost{} with a higher cost value
				#which means we will have to replace it with the new value
					self.cost_so_far[neighbor] = gcost #update neighbor gscore to be the smaller cost
					priority = gcost + self.heuristic(self.start, self.goal, current) # set a node's priority in the open set.
					heapq.heappush(self.frontier,(priority,neighbor))
					self.cameFrom[neighbor] = current
		return count
