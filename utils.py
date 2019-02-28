
def score(slides, tags):
    s = 0
    for i in range(len(slides) - 1):
        tags1 = tags[slides[i][0]].tags if len(slides[i]) == 1 else tags[slides[i][0]].tags + tags[slides[i][1]].tags
        tags2 = tags[slides[i + 1][0]].tags if len(slides[i + 1]) == 1 else tags[slides[i + 1][0]].tags + tags[slides[i + 1][1]].tags
        s += min(len(tags1 & tags2), len(tags1 - tags2), len(tags2 - tags1))
    return s
