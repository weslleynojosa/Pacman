"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  """
  "*** YOUR CODE HERE ***"
  node = (problem.getStartState(), [])
  if problem.isGoalState(node):
      return node
  edge = util.Stack()
  edge.push(node)
  visited = []
  while not edge.isEmpty():
      node, actions = edge.pop()
      visited.append(node)
      for successor, action, stepCost in problem.getSuccessors(node):
          if successor not in visited and edge:
              if problem.isGoalState(successor):
                  return actions + [action]
              edge.push((successor, actions + [action]))
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  nodeStart = (problem.getStartState(), [])
  edge = util.Queue()
  edge.push(nodeStart)
  visited = []
  while not edge.isEmpty():
      node, actions = edge.pop()
      visited.append(node)
      for successor, action, stepCost in problem.getSuccessors(node):
          if successor not in visited and edge:
              if problem.isGoalState(successor):
                  return actions + [action]
              edge.push((successor, actions + [action]))
              visited.append(successor)
  print 'fim'
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  node = (problem.getStartState(), ())
  if problem.isGoalState(node):
      return node
  edge = util.PriorityQueue()
  edge.push(node, 0)
  visited = []
  while not edge.isEmpty():
      node, actions = edge.pop()
      if problem.isGoalState(node):
          return actions
      visited.append(node)
      for successor, action, stepCost in problem.getSuccessors(node):
          if successor not in visited:
              setActions = actions + (action,)
              edge.push((successor, setActions), problem.getCostOfActions(setActions))
          visited.append(successor)

  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  node = (problem.getStartState(), ())
  edge = util.PriorityQueue()
  edge.push(node, heuristic(problem.getStartState(), problem))
  visited = []
  while not edge.isEmpty():
      node, actions = edge.pop()
      if problem.isGoalState(node):
          return actions
      visited.append(node)
      for successor, action, stepCost in problem.getSuccessors(node):
          if successor not in visited:
              setActions = actions + (action,)
              edge.push((successor, setActions), problem.getCostOfActions(setActions) + heuristic(successor, problem))
          visited.append(successor)

  util.raiseNotDefined()

    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


