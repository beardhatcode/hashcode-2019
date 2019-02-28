import random
from collections import deque

SIZE = 50

def solver(tags, horizontal, vertical, _num_tags):
    slides = list(map(lambda x: [x.num], list(horizontal)))

    vertical = [v.num for v in vertical]
    vertical.sort(key=lambda i: len(tags[i]))
    window, vertical = vertical[:SIZE], deque(vertical[SIZE:])

    while window:
        ia, a, ib, b = max(
            ((ia, a, ib, b) for ia, a in enumerate(window) for ib, b in enumerate(window)),
            key=lambda t4: len(tags[t4[1]].tags | tags[t4[3]].tags)
        )
        ia, ib = sorted([ia, ib])
        del window[ib]
        del window[ia]
        slides.append([a, b])
        try:
            window.append(vertical.popleft())
            window.append(vertical.popleft())
        except IndexError:
            pass

    random.shuffle(slides)
    return slides
