from text2digits import text2digits
from string import digits
from collections import defaultdict
with open('kjv.txt', 'r') as f:
    corpus = f.read()
    corpus = corpus.translate({ord(k): None for k in digits})
    mappings = defaultdict(int)
    t2d = text2digits.Text2Digits(convert_ordinals=False)
    corpus = t2d.convert(corpus)
    letters = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for w in corpus.split(' '):
        if len(w) > 0 and w[0] in letters:
            mappings[int(w[0])] += 1
    print(mappings)
    