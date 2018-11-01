Algorithm Description
=====================
First, we rotate all the blocks in every possible orientation so that blocks can be stacked on top of themselves if necessary. We then sort this list of blocks by horizontal area, ignoring their heights. No block will ever be able to have a horizontal area greater than the block below it, so sorting the blocks before we start stacking them ensures that the largest blocks will be at the bottom of the tower. We continue this pattern, choosing the partially built tower with the maximum height to continue to build on.

Proof
-----
Filling in the table left to right, we are adding a new smaller block each time that we can use to form a new potentially tallest tower. We find the tallest such partial tower to try to add the next block to it, so that across all possible towers we will always be able to store the largest one currently buildable with the blocks up to that index.

Runtime
-------
For every block given to us as input, we need to rotate it for 6n operations; therefore, our DP table will be O(n) in terms of size. We then sort the list by area, which takes O(nlogn) time. For each element in the DP table, we have to look at all the elements to the left of it, which on average will be 6n/2=3n, for a runtime of O(n) per element. Therefore, our total runtime is O(n^2) across every entry of the table.

Alternate Algorithm
===================
Alternatively, we could have gone for a (non dynamically programmed) greedy algorithm that simply takes the tallest block and tries to stack it onto the next tallest blocks, or takes the block with the largest area and tries to stack it under blocks with the closest area. The issue with both of these greedy choices is that we might end up with a tower comprised of a few tall blocks or many short but fat blocks, where both towers might eschew "mixed" options. This is why we need a way to reference partially built towers to select for the best one.

Implementation
==============
We encoded our algorithm using a list of 3-tuples storing to store every possible rotation rotation of the blocks (so with an input of n blocks, we get 6n rotations). We sorted this list by area, so that the first element had the highest area. We used an array where each entry houses the maximum height of the tower we could build with blocks ranging from the first up to the index of the array's element, along with the index of the block we used here and the index of the block below it in the tower. So, every entry in our array stores the components to build the tallest possible tower with the blocks up to that index.

Testing the Code
----------------
Our code is compiled simply by moving to the directory in which the files are saved and typing "python blockstacking.py <infile.txt> <outfile.txt>", replacing <infile.txt> and <outfile.txt> with the appropriate file names. The only package imported is sys, which is built into Python.
