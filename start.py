import logging
import os
import fileinput
import sys
from collections import namedtuple

from random_solver import solver
from utils import score

# Main method
def main():
    logging.debug("Debug enabled! :)")

    # Meta-data input
    a = fileinput.input(sys.argv[1])
    num = int(a.readline().strip())
    horizontals = set()
    verticals = set()
    images = []

    encountered = {}
    j = 0
    for i in range(num):
        orientation, _, *taglist = a.readline().strip().split()
        for tag in taglist:
            if tag not in encountered:
                encountered[tag] = j
                j += 1

        images.append(frozenset(map(lambda t: encountered[t], taglist)))
        if orientation == 'H':
            horizontals.add(images[-1])
        else:
            verticals.add(images[-1])

    slides = solver(images, horizontals, verticals, j)

    print(score(slides, images), file=sys.stderr)
    print(len(slides))
    for s in slides:
        print(" ".join(map(str, s)))


# Entry point of the application.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <dataset>'.format(sys.argv[0]))
        sys.exit(1)

    # Execute the main function.
    main()
