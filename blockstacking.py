#Joe Brennan and James Marshall
#Block Stacking
from typing import Tuple
import sys

#infilePath = sys.argv[0]
#outfilePath = sys.argv[1]

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

dp_table = [Tuple[int,int,int] for block in blocks] #The tuples are (maxheight, index, previousblockindex)
dp_table[0] = (blocks[0][2], 0, 0)
for i in range(1, len(dp_table) - 1):
    sublist = dp_table[:i]
    sublist = filter((lambda x: ((blocks[x[1]][0] < blocks[i][0]) and (blocks[x[1]][1] < blocks[i][1])) 
    			or ((blocks[x[1]][0] < blocks[i][1]) and (blocks[x[1]][1] < blocks[i][0]))), sublist)

    if len(sublist) == 0:
    	dp_table[i] = (blocks[i][2], i, -1)
    else:
		prevBlock = max(sublist, key=lambda x: x[0])
		print("prevBlock = " + str(prevBlock))
		newHeight = blocks[i][2] + prevBlock[0]
		dp_table[i] = (newHeight, i, prevBlock[1])

print(dp_table)

maxHeightEntry = max(dp_table, key=lambda x: x[0])
totalHeight = maxHeightEntry[0]
solutionBlockList = []
solutionBlockList.append(maxHeightEntry)
currIndex = maxHeightEntry[1]
while(dp_table[currIndex][2] != -1):
	solutionBlockList.append(dp_table[dp_table[currIndex][2]])
	currIndex = dp_table[currIndex][2]

print("The tallest tower has " + str(len(solutionBlockList)) + " blocks and a height of " + str(totalHeight))

