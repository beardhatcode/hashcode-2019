from utils import score
import random

def solver(tags, horizontal, vertical):
    slides = list(map(lambda x: [x.num], list(horizontal)))
    vertical = list(vertical)
    for i in range(0, len(vertical), 2):
        slides.append([vertical[i].num, vertical[i + 1].num])
    random.shuffle(slides)
    return slides