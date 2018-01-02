#! /usr/bin/env python2.7
'''
branchNinePuzzle: This script solves 9 puzzle.
A 9 puzzle is a 3x3 version of a 15 puzzle.
Your puzzle should be represented as an nxn
nested list. The numbers should range from 1 - n ^ 2
n ^ 2 represents the empty space.
'''
import string, random, heapq, time, math


'''
Given a 2-d nested list, this method returns a version
that represents shuffling the puzzle.
Note that this will only shuffle with 100 moves
'''
def makePuzzle(l): # [[1,2,3][4,5,6][7,8,9]]
	state = solution(l)
	explored = set()
#	random.seed(3)
	for i in xrange(100):
                posMove = []
                for a in nextMove(state):
                        posMove.append(a)
                b = random.sample(posMove, 1)[0]
                if b not in explored:
                        state = b
                        explored.add(b)
        return state
                
'''
 Given a puzzle, it will generate all possible moves
 that can be done from the state.
 Note: this method returns tuples.
'''
def nextMove(l):
	a = [[y for y in x] for x in l]
	for r in xrange(len(l)):
		for c in xrange(len(l)):
			if a[r][c] == len(l) ** 2:
				i, j = r, c


	if i == 0 and j == 0:
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		yield tuple(tuple(s) for s in a)
	elif i == len(l) - 1 and j == len(l) - 1:
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		yield tuple(tuple(s) for s in a)
	elif i == 0 and j == len(l) - 1:
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		yield tuple(tuple(s) for s in a)
	elif j == 0 and i == len(l) - 1:
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		yield tuple(tuple(s) for s in a)
	elif i == 0:
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		yield tuple(tuple(s) for s in a)
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		a[i][j - 1], a[i][j] = a[i][j], a[i][j - 1]
		yield tuple(tuple(s) for s in a)
	elif i == len(l) - 1:
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		yield tuple(tuple(s) for s in a)
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		a[i][j - 1], a[i][j] = a[i][j], a[i][j - 1]
		yield tuple(tuple(s) for s in a)
	elif j == 0:
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		yield tuple(tuple(s) for s in a)
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		yield tuple(tuple(s) for s in a)
	elif j == len(l) - 1:
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		yield tuple(tuple(s) for s in a)
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		yield tuple(tuple(s) for s in a)
	else:
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		yield tuple(tuple(s) for s in a)
		a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		yield tuple(tuple(s) for s in a)
		a[i - 1][j], a[i][j] = a[i][j], a[i - 1][j]
		a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
		yield tuple(tuple(s) for s in a)



'''
Given a puzzle, this will find a solution to solving it.
This is not guaranteed to return a solution for certain
puzzles(especially, 5x5 or higher), but it will return
an optimal solution.
The output will be printed on the console. The first line is an index
that represents the move number. The next n lines represent the 
state of the nxn - 1 puzzle. 
'''
def shortestPath(start):
	i = 0
	start = start[:]
	heap = [(wrongs(tuple(tuple(s) for s in start)),0, tuple(tuple(s) for s in start), None)] #(value, weight, node, parent)
	heapq.heapify(heap)
	sol = solution(len(start))
	mins  = {heap[0][2]: heap[0][1]}
	moves = []
	while heap:
		node = heapq.heappop(heap) #(value, movesDone, board, parent)
		moves.append(node)
		#print node
		if node[2] == sol:
			#print '\n'
			path = [moves.pop()]
			while moves:
				a = moves.pop()
				if a[2] == path[-1][3] and a[1] == path[-1][1] - 1:
					path.append(a)
			for i in xrange(len(path)):
                                print '\n',i
				for a in path.pop()[2]:
                                        for b in a:
                                                print b,
                                        print
			return node

		for a in nextMove(node[2]):
			if a not in mins:
				mins[a] = node[1]
			elif mins[a] <= node[1]: continue

			heapq.heappush(heap, (wrongs(a) + node[1] + 1
				, node[1] + 1, a, node[2]))

'''
returns a nested TUPLE of size n x x that represents
a solved n x n - 1 puzzle
'''
def solution(n):
	return tuple([tuple([i + n * j + 1 for i in xrange(n)]) for j in xrange(n)])

'''
 Divides n and l and returns the quotient and remainder.
 It's used to find where a number should be on the board.
 In practice, n should be the index and l should be the length
 of the board
 Examples:
 ij(4, 2) returns (2, 0)
 ij(8, 3) returns (2, 2)
 ij(19, 7) returns (2, 5)
'''
def ij(n, l):
	return (n / l, n % l)

'''
Given a puzzle, this method returns the sum of the
Manhattan distance from the tile position to it's correct place
'''
def wrongs(l):
	wrong = 0
	space = len(l) ** 2
	for a in xrange(space):
		i,j = ij(a, len(l))
		if l[i][j] == space: continue
		wrong = wrong + int(math.fabs(ij(l[i][j] - 1, len(l))[0] - i)
		+ math.fabs(ij(l[i][j] - 1, len(l))[1] - j))
	return wrong


if __name__ == "__main__":
	l = [[3, 9, 7, 4],[1, 16, 2, 8],[ 5, 13, 10, 14],[6, 11, 12, 15]]
	# l = makePuzzle(3)
	print l

	solution(len(l))
	a = time.time()
	shortestPath(l)
	print time.time() - a
