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
    print(blocks)
    base_blocks.append([int(d) for d in blocks])

print(base_blocks)
