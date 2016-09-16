# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


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
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    #print "Start:", problem.getStartState()
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # Declare your closed and open list
    closed = []
    open = util.Stack()
    # Current state = initial state
    current = [problem.getStartState(),'None', '1']
    # Create parent dictionary
    parentMap = {}
    #Start while loop
    while not problem.isGoalState(current[0]) and open:
        successors = problem.getSuccessors(current[0])

        for state, direction, cost in reversed(successors):
            #check if the state is in the closed list or is the current one
            flag = False
            #Check if the succesor state is in the closed list
            for closedState in closed:
                if cmp(closedState, state) == 0:
                    flag = True
            #Check if the successor state is not the current one.
            flag = flag or state == current[0]
            if not flag:
                #add the successor states to the open list
                open.push([state, direction, cost])
                # Add the new parent - state to the hashmap
                parentMap[state] = [current[0], current[1]]


        #Append visited state to the closed list
        closed.append(current[0])
        #Take the next state in the open list.
        current = open.pop()


    if problem.isGoalState(current[0]):
        path = []
        path.append(current[1])
        #you found the goal state, now iterate back up the tree to find all the parents.
        state = current
        while not cmp(parentMap.get(state[0])[0],problem.getStartState()) == 0:
            path.append(parentMap.get(state[0])[1])
            state = parentMap.get(state[0])
        path.reverse()
        return path
    else:
        return []

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    closed = []
    open = util.Queue()
    # Current state = initial state
    current = [problem.getStartState(), 'None', '1']
    # Create parent dictionary
    parentMap = {}
    # Start while loop
    while not problem.isGoalState(current[0]) and open:
        successors = problem.getSuccessors(current[0])
        # Append visited state to the closed list
        closed.append(current[0])
        for state, direction, cost in successors:
            # check if the state is in the closed list or is the current one
            flag = False
            # Check if the successor state is in the closed and open list
            for closedState in closed:
                if cmp(closedState, state) == 0:
                    flag = True
            for openState in open.list:
                if cmp(openState[0], state) == 0:
                    flag = True
            # Check if the successor state is not the current one.
            flag = flag or cmp(state,current[0]) == 0
            if not flag:
                # add the successor states to the open list
                open.push([state, direction, cost])
                # Add the new parent - state to the hashmap
                parentMap[state] = [current[0], current[1]]

        # Take the next state in the open list.
        current = open.pop()

    if problem.isGoalState(current[0]):
        path = []
        path.append(current[1])
        # you found the goal state, now iterate back up the tree to find all the parents.
        state = current
        while not cmp(parentMap.get(state[0])[0], problem.getStartState()) == 0:
            path.append(parentMap.get(state[0])[1])
            state = parentMap.get(state[0])
        path.reverse()
        return path
    else:
        return []
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "


    closed = []
    pQ = util.PriorityQueue()
    openList = []
    # Current state = initial state
    current = [problem.getStartState(), 'None', 0, 0]
    pQ.push(current, 0)
    openList.append(current[0])
    # Create parent dictionary
    parentMap = {}
    # minCost = float('inf')
    #https://algorithmicthoughts.wordpress.com/2012/12/15/artificial-intelligence-uniform-cost-searchucs/
    # Start while loop
    while not problem.isGoalState(current[0]) and pQ:
        #state, direction, cost, costParent = pQ.pop()
        current = pQ.pop()
        openList.remove(current[0])
        successors = problem.getSuccessors(current[0])
        # Append visited state to the closed list
        closed.append(current[0])
        for state, direction, costSucc in successors:
            flag = False
            #Check if the cost of the successor is greater than the minCost
            #If the cost is greater,dont expand it.
            # if costSucc > minCost
            #     flag = True
            # Check if the successor state is in the closed and open list
            for closedState in closed:
                if cmp(closedState, state) == 0:
                    flag = True
            for openState in openList:
                if cmp(openState, state) == 0:
                    flag = True
            # Check if the successor state is not the current one.
            flag = flag or cmp(state, current[0]) == 0
            if not flag:
                # add the successor states to the open list
                # Add the new parent - state to the hashmap
                node = [state, direction, current[2] + costSucc, current[2]]
                parentMap[state] = [current[0], current[1]]
                pQ.push(node, current[2] + costSucc)
                openList.append(state)


        # #update minCost
        # minCost = localMin
    if problem.isGoalState(current[0]):
        path = []
        path.append(current[1])
        # you found the goal state, now iterate back up the tree to find all the parents.
        state = current
        while not cmp(parentMap.get(state[0])[0], problem.getStartState()) == 0:
            path.append(parentMap.get(state[0])[1])
            state = parentMap.get(state[0])
        path.reverse()
        return path
    else:
        return []
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# AbbreviationsvvVVVVVVVVVVVVVVVVVVVVV
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
