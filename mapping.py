TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

def looping_map(tiles):
    for x in range(0,len(tiles)):
        if tiles[x] == '||':
            print('\n')
        else:
            print(tiles[x], end="")

looping_map(TILES)