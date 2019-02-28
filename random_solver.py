import random


def solver(_images, horizontal, vertical, _num_tags):
    slides = list(map(lambda x: [x.num], list(horizontal)))
    vertical = list(vertical)
    for i in range(0, len(vertical), 2):
        slides.append([vertical[i].num, vertical[i + 1].num])
    random.shuffle(slides)
    return slides
