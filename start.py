import logging
import os
import fileinput
import sys
from collections import namedtuple

from empty import solver

# Debugging format.
DEBUG_FORMAT = '%(levelname)s:%(filename)s:%(funcName)s:%(asctime)s %(message)s\n'

Image = namedtuple('Image', ['num', 'tags'])

# Main method
def main():
    logging.debug("Debug enabled! :)")

    # Meta-data input
    a = fileinput.input(sys.argv[1])
    num = int(a.readline().strip())
    horizontals = set()
    verticals = set()
    tags = []

    encountered = {}
    j = 0
    for i in range(num):
        orientation, _, *taglist = a.readline().strip().split()
        for tag in taglist:
            if tag not in encountered:
                encountered[tag] = j
                j += 1

        tags.append(Image(i, frozenset(map(lambda t: encountered[t], taglist))))
        if orientation == 'H':
            horizontals.add(tags[-1])
        else:
            verticals.add(tags[-1])

    slides = solver(tags, horizontals, verticals)

    print(len(slides))
    for s in slides:
        print(" ".join(s))


# Entry point of the application.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <dataset>'.format(sys.argv[0]))
        sys.exit(1)

    # Execute the main function.
    main()
