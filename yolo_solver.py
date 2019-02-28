from utils import score
import random

def solver(images, horizontal, vertical, maxtag):
    groups=maxtag*[None]
    for i in range(maxtag):
        groups[i] = set()
    
    for i in images:
        if i.orientation:
            for t in i.tags:
                groups[t].add(i)
    
    #print(groups)

    used = set()
    slides  = []
    for i in images:
        if i not in used and i.orientation:
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
            similarsH = [i for i,c in buddysS.items() if c > 1 and i.orientation == "H"]
            similarsV = [i for i,c in buddysS.items() if c > 1 and i.orientation == "V"]
            if i.orientation == "H":
                if len(similarsV) >= 2:
                    slides.append([i.num])
                    slides.append([similarsV[0].num,similarsV[1].num])
                    used.add(similarsV[0])
                    used.add(similarsV[1])
                    used.add(i)
                elif similarsH:
                    slides.append([i.num])
                    slides.append([similarsH[0].num])
                    used.add(similarsH[0])
                    used.add(i)
            else: # V
                if len(similarsV) >= 2 or similarsH:
                    for _ in range(30):
                        j = random.choice(images)
                        if j.orientation == 'V' and j not in used:
                            similarsV2 = [i for i in similarsV if i.num != j.num]
                            similarsH2 = [i for i in similarsH if i.num != j.num]
                            if len(similarsV2) >= 2:
                                slides.append([i.num, j.num])
                                slides.append([similarsV2[0].num,similarsV2[1].num])
                                used.add(similarsV2[0])
                                used.add(similarsV2[1])
                                used.add(i)
                                used.add(j)
                            elif similarsH2:
                                slides.append([i.num])
                                slides.append([similarsH2[0].num])
                                used.add(similarsH2[0])
                                used.add(i)
                            break

                

    return slides
            