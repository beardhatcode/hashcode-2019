from utils import score
#from start import Image
import random
from collections import namedtuple



ImageH = namedtuple('ImageH', ['num', 'tags'])


def makeH(vertical: set()):
    l = list(vertical)
    random.shuffle(l)
    return [ImageH((l[k].num,l[k+1].num), l[k].tags | l[k+1].tags) for k in range(0,len(l),2)]

def conv( i ):
    if isinstance(i, tuple):
        return list(i)
    else:
        return [i]


def solver(images, horizontal: set(), vertical: set(), maxtag) -> [[int]]:


    groups = maxtag*[None]
    for i in range(maxtag):
        groups[i] = set()

    images = horizontal | set(makeH(vertical))

    for i in images:
        for t in i.tags:
            groups[t].add(i)

    # print(groups)

    used = set()
    slides = []
    for i in images:
        if i not in used:
            used.add(i)
            curTags = i.tags
            buddys = [groups[t] - used for t in curTags]
            used.remove(i)

            buddysS = {}
            for bl in buddys:
                for b in bl:
                    if b not in buddysS:
                        buddysS[b] = 1
                    else:
                        buddysS[b] += 1
            similars = [i for i, c in buddysS.items() if c > 1]
            if similars:
                slides.append(conv(i.num))
                slides.append(conv(similars[0].num))
                used.add(similars[0])
                used.add(i)

    return slides
