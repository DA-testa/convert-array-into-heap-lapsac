[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10388327)
#  Problem: Convert array into heap
In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting
algorithm called HeapSort. It has guaranteed worst-case running time of 𝑂(𝑛 log 𝑛) as opposed to QuickSort’s
average running time of 𝑂(𝑛 log 𝑛). QuickSort is usually used in practice, because typically it is faster, but
HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your
computer.

# Problem description
## Task. 
The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the
way, did you know that algorithms based on Heaps are widely used for external sort, when you need
to sort huge files that don’t fit into memory of a computer?
Your task is to implement this first step and convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap using
only 𝑂(𝑛) swaps, as was described in the lectures. Note that you will need to use a min-heap instead
of a max-heap in this problem.
## Input Format. 
The first line of the input contains single integer 𝑛. The next line contains 𝑛 space-separated
integers 𝑎𝑖.
## Constraints. 
1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109. All 𝑎𝑖 are distinct.

## Output Format. 
The first line of the output should contain single integer 𝑚 — the total number of swaps.
𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain the swap operations used
to convert the array 𝑎 into a heap. Each swap is described by a pair of integers 𝑖, 𝑗 — the 0-based
indices of the elements to be swapped. After applying all the swaps in the specified order the array
must become a heap, that is, for each 𝑖 where 0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:
1. If 2𝑖 + 1 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+1.
2. If 2𝑖 + 2 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+2.
3. 
Note that all the elements of the input array are distinct. Note that any sequence of swaps that has
length at most 4𝑛 and after which your initial array becomes a correct heap will be graded as correct.

## Sample 
Input:
5

5 4 3 2 1

Output:
3
1 4
0 1
1 3

After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4.
2
After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4.

After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, which is
already a heap, because 𝑎0 = 1 < 2 = 𝑎1, 𝑎0 = 1 < 3 = 𝑎2, 𝑎1 = 2 < 5 = 𝑎3, 𝑎1 = 2 < 4 = 𝑎4.


## Sample
Input:
5

1 2 3 4 5

Output:
0

The input array is already a heap, because it is sorted in increasing order.
