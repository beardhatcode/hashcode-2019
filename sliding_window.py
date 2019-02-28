
import random_solver as subsolver

from utils import score
from collections import deque

SIZE = 100

def solver(tags, horizontals, verticals, *args, **kwargs):
	old = subsolver.solver(tags, horizontals, verticals, *args, **kwargs)

	solution, window, remainder = old[0:1], old[1:SIZE], deque(old[SIZE:])

	def score_(tup):
		return score([solution[-1], tup[1]], tags)

	while window:
		index, value = max(enumerate(window), key=score_)
		solution.append(value)
		del window[index]
		try:
			window.append(remainder.popleft())
		except IndexError:
			pass

	return solution

