import grid
import heapq


class Astar:
	frontier = []#Discovered nodes that must be evaluated
	closedSet = {} #nodes already evaluated
	g_score = {}


	def __init__(self,start, goal):

		self.start = start
		self.goal = goal

		self.frontier.append(start)
		self.g_score[start] =0



	#manhattan heuristic
	def heuristic(self,a,b):
		x1,y1 =a
		x2, y2 =b
		return abs(x2-x1) + abs(y2-y1)

	def astar_search(self,graph, start, goal):
		pass
