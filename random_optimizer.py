
import random_solver as subsolver

from utils import score
import random

def solver(tags, horizontals, verticals, *args, **kwargs):
	solution = subsolver.solver(tags, horizontals, verticals, *args, **kwargs)

	if len(solution) < 5: return solution

	for _ in range(100000):
		a = random.randint(1, len(solution) - 3)
		b = random.randint(1, len(solution) - 3)
		sa1 = score(solution[a - 1:a + 2], tags)
		sb1 = score(solution[b - 1:b + 2], tags)
		sa2 = score([solution[a - 1], solution[b], solution[a + 1]], tags)
		sb2 = score([solution[b - 1], solution[a], solution[b + 1]], tags)
		if sa2 + sb2 > sa1 + sb1:
			solution[a], solution[b] = solution[b], solution[a]

	return solution

