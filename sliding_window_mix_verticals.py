
import random_solver as subsolver

from utils import score
from collections import deque
import itertools

SIZE = 50

def solver(tags, horizontals, verticals, *args, **kwargs):
	old = subsolver.solver(tags, horizontals, verticals, *args, **kwargs)

	solution, window, remainder = old[0:1], old[1:SIZE], deque(old[SIZE:])
	hors = [s for s in window if len(s) == 1 for i in s]
	vers = [i for s in window if len(s) == 2 for i in s]

	def score_(slide):
		return score([solution[-1], slide], tags)

	while hors or vers:
		if hors:
			hscore, hindex, hvalue = max((score_(e), i, e) for i, e in enumerate(hors))
		else:
			hscore, hindex, hvalue = -1, None, None

		if vers:
			vscore, (vindex1, vindex2), vvalue = max(
				(score_([v1, v2]), (i1, i2), (v1, v2))
				for (i1, v1), (i2, v2)
				in itertools.combinations(enumerate(vers), r=2)
			)
		else:
			vscore, (vindex1, vindex2), vvalue = -1, (None, None), None

		# vscore, (vindex1, vindex2), vvalue = max((((i1, i2), [v1, v2]) for (i1, v1), (i2, v2) in itertools.combinations(enumerate(vers), repeat=2)), key=score_)
		if hscore > vscore:
			solution.append(hvalue)
			del hors[hindex]
		else:
			solution.append(vvalue)
			vindex1, vindex2 = sorted([vindex1, vindex2])
			del vers[vindex2]
			del vers[vindex1]
		try:
			next = remainder.popleft()
			if len(next) == 1: hors.append(next)
			else: vers.extend(next)
		except IndexError:
			pass

	return solution

