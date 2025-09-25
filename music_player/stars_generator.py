import random


colors = '#ffffff, #ff0000, #00ff00, #0000ff, #ffff00, #ff00ff, #00ffff'.split(', ')
transparency = '66, 80, 99, b3, cc, e6, ff'.split(', ')
sizes = [(3, 3), (1, 2), (1, 3), (2, 2), (2, 3)]
X, Y = list(range(1440)), list(range(1024))
random.shuffle(X)
random.shuffle(Y)

result = {}

for i in range(1000):
    color = random.choice(colors)
    size = random.choice(sizes)
    transp = random.choice(transparency)
    x = f'{X[i]}px'
    y = f'{Y[i]}px'
    result[size] = result.get(size, list())
    result[size].append((x, y, 0, color + transp))


for key, value in result.items():
    width, height = key
    print(f'width: {width}px;', f'height: {height}px;')
    print('box-shadow: ')
    for x, y, undef, color in value:
        print(x, y, undef, color, end=', ')
    print()
