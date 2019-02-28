from utils import score
import random

def solver(images, horizontal, vertical, maxtag):
    groups=maxtag*[None]
    for i in range(maxtag):
        groups[i] = set()
    
    for i in images:
        if i.orientation == "H":
            for t in i.tags:
                groups[t].add(i)
    
    #print(groups)

    used = set()
    slides  = []
    for i in images:
        if i not in used and i.orientation == "H":
            used.add(i)
            curTags = i.tags
            buddys = [groups[t] - used for t in curTags]
            
            buddysS = {}
            for bl in buddys:
                for b in bl:
                    if b not in buddysS:
                        buddysS[b] = 1
                    else:
                        buddysS[b] += 1
            similars = [i for i,c in buddysS.items() if c > 0]
            if len(similars) > 0:
                slides.append([i.num])
                slides.append([similars[0].num])
                used.add(similars[0])
            else:
                used.remove(i)

    return slides
            