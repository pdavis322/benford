from tkinter import Tk
from tkinter.filedialog import askopenfilename
from text2digits import text2digits
from string import digits
from collections import defaultdict
Tk().withdraw()
filename = askopenfilename()
print(f'File: {filename}')
with open(filename, 'r') as f:
    corpus = f.read()
    print('Removing numerals not in text form...')
    corpus = corpus.translate({ord(k): None for k in digits})
    mappings = defaultdict(int)
    print('Converting numbers in text form...')
    t2d = text2digits.Text2Digits(convert_ordinals=False)
    corpus = t2d.convert(corpus)
    letters = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for w in corpus.split(' '):
        if len(w) > 0 and w[0] in letters:
            mappings[int(w[0])] += 1
    total = sum(mappings.values())
    print(f'Total numerals: {total}')
    for m in sorted(mappings):
        print(f'{m}: {(mappings[m] / total):.3f} ({mappings[m]})')
    