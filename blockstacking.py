#Joe Brennan and James Marshall
#Block Stacking


infile = open("blocks10.in", "r")
#outfile = open("outfile.txt", "w")
numBlocks = infile.readline()

base_blocks = []

for i in range(int(numBlocks)):
    line = infile.readline()
    blocks = line.rstrip()
    blocks = blocks.split(" ")
    base_blocks.append([int(d) for d in blocks])

blocks = []

for block in base_blocks:
    blocks.append(block)
    blocks.append([block[2],block[1],block[0]])
    blocks.append([block[0],block[2],block[1]])

blocks.sort(key=lambda x: x[0]*x[1], reverse = 1)

dp_table = [[] for block in blocks]
dp_table[0] = blocks[0][2]
for i in range(1, len(dp_table) - 1):
    sublist = [dp_table[:i-1]]
    if blocks[i][0] > blocks[i+1][0] and
    dp_table[i] = dp_table[i-1] + newblockheight
