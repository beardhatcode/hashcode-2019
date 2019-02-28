
def score(slides, tags):
    s = 0
    for i in range(len(slides) - 1):
        tags1 = tags[slides[i]].tags[0] if len(slides[i]) == 1 else tags[slides[i]].tags[0] + tags[slides[i]].tags[1]
        tags2 = tags[slides[i + 1]].tags[0] if len(slides[i + 1]) == 1 else tags[slides[i + 1]].tags[0] + tags[slides[i + 1]].tags[1]
        s += min(len(tags1 | tags2), len(tags1 - tags2), len(tags2 - tags1))
    return s
