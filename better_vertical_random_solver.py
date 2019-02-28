import random

def solver(tags, horizontal, vertical, _num_tags):
    slides = list(map(lambda x: [x.num], list(horizontal)))
    vertical = [v.num for v in vertical]
    vertical.sort(key=lambda i: len(tags[i]))

    while vertical:
        a = vertical[-1]
        j, b = max(enumerate(vertical), key=lambda t: len(tags[t[1]].tags - tags[a].tags))
        del vertical[j]
        del vertical[-1]
        slides.append([a, b])

    random.shuffle(slides)
    return slides
