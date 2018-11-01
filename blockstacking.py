#Joe Brennan and James Marshall
#Block Stacking
from typing import Tuple
import sys

#infilePath = sys.argv[0]
#outfilePath = sys.argv[1]

infile = open("blocks100.in", "r")
#outfile = open("outfile.txt", "w")
numBlocks = infile.readline()

base_blocks = []

for i in range(int(numBlocks)):
    line = infile.readline()
    blocks = line.rstrip()
    blocks = blocks.split(" ")
    base_blocks.append([int(d) for d in blocks])

blocks = []

#add all 3 possible orientations for each block to the list of blocks
for block in base_blocks:
    blocks.append(block)
    blocks.append([block[2],block[1],block[0]])
    blocks.append([block[0],block[2],block[1]])

blocks.sort(key=lambda x: x[0]*x[1], reverse = 1)

print(blocks)

dp_table = [Tuple[int,int,int] for block in blocks] #The tuples are (maxheight, index, previousblockindex)
dp_table[0] = (blocks[0][2], 0, -1) #create the first block in the dp table
for i in range(1, len(dp_table)):
    sublist = dp_table[:i]

    sublist = filter(lambda x: (((blocks[x[1]][0] > blocks[i][0]) and (blocks[x[1]][1] > blocks[i][1])) 
    			or ((blocks[x[1]][0] > blocks[i][1]) and (blocks[x[1]][1] > blocks[i][0]))), sublist)

    if len(sublist) == 0:
    	#if a block is the bottom block in a stack, its previous block index is -1
    	dp_table[i] = (blocks[i][2], i, -1)
    else:
		prevBlock = max(sublist, key=lambda x: x[0])
		newHeight = blocks[i][2] + prevBlock[0]
		dp_table[i] = (newHeight, i, prevBlock[1])

print(dp_table)

#get the entry from the dp table with the highest total height
maxHeightEntry = max(dp_table, key=lambda x: x[0]) 
totalHeight = maxHeightEntry[0]
solutionBlockList = [] #list of blocks used in optimal solution
solutionBlockList.append(maxHeightEntry)
currIndex = maxHeightEntry[1]

#work backwards through the dp table until we find the bottom block of
#the optimal solution
while(dp_table[currIndex][2] != -1):
	solutionBlockList.append(dp_table[dp_table[currIndex][2]])
	currIndex = dp_table[currIndex][2]

print("The tallest tower has " + str(len(solutionBlockList)) + " blocks and a height of " + str(totalHeight))

outfile.write(str(totalHeight))
