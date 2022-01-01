def print_mappings(name, mappings):
    total = sum(mappings.values())
    print(f'{name} total: {total}')
    for m in sorted(mappings):
        print(f'{m}: {(mappings[m] / total):.3f}')

shakespeare = {4: 177, 1: 2295, 2: 842, 9: 58, 5: 158, 3: 425, 6: 63, 8: 37, 7: 70}
kjv = {1: 2619, 2: 937, 4: 378, 7: 436, 8: 50, 9: 46, 6: 169, 3: 515, 5: 349}
print_mappings("KJV", kjv)