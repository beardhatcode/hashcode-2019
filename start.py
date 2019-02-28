import logging
import os
import fileinput
import sys
from collections import namedtuple

# Debugging format.
DEBUG_FORMAT = '%(levelname)s:%(filename)s:%(funcName)s:%(asctime)s %(message)s\n'

Image = namedtuple('Image', ['num', 'tags'])


def score(slides, tags):
    s = 0
    for i in range(len(slides) - 1):
        tags1 = tags[slides[i]].tags[0] if len(slides[i]) == 1 else tags[slides[i]].tags[0] + tags[slides[i]].tags[1]
        tags2 = tags[slides[i + 1]].tags[0] if len(slides[i + 1]) == 1 else tags[slides[i + 1]].tags[0] + tags[slides[i + 1]].tags[1]
        s += min(len(tags1 | tags2), len(tags1 - tags2), len(tags2 - tags1))
    return s


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

        tags.append(Image(i, set(map(lambda t: encountered[t], taglist))))
        if orientation == 'H':
            horizontals.add(tags[-1])
        else:
            verticals.add(tags[-1])

    slides = []

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
