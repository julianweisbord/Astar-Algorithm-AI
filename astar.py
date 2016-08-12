import grid
import heapq

Class Astar:
	closedSet = [] #nodes already evaluated
	openSet = [] #Discovered nodes that must be evaluated
	g_score = {}
	
	def __init__(start, goal):
		self.start = start
		self.goal = goal
		
		self.openSet.append(start)
		self.g_score[start] =0