names = ['mark', 'henry', 'matthew', 'paul',
        'luke', 'robert', 'joseph', 'carl', 'michael']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

print d
