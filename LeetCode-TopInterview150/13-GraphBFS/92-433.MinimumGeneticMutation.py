"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene 
where one mutation is defined as one single character changed in the gene string.
For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. 
A gene must be in bank to make it a valid gene string.
Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene.
 If there is no such a mutation, return -1.
Note that the starting point is assumed to be valid, so it might not be included in the bank.
Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Constraints:
0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
from collections import deque
class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)             # use a set for O(1) lookups/removes
        if endGene not in bank_set:
            return -1
        
        genes = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        # If startGene is in bank_set, remove it to avoid revisiting it later
        if startGene in bank_set:
            bank_set.discard(startGene)

        while queue:
            current, steps = queue.popleft()

            if current == endGene:
                return steps

            for i in range(len(current)):
                for g in genes:
                    if current[i] == g:
                        continue
                    mutated = current[:i] + g + current[i+1:]
                    if mutated in bank_set:
                        bank_set.discard(mutated)            # prevent revisiting
                        queue.append((mutated, steps + 1))
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(sol.minMutation(startGene, endGene, bank))   # expected 2

    # the other testcase you mentioned:
    startGene = "AAAAACCC"
    endGene = "AACCCCCC"
    bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    print(sol.minMutation(startGene, endGene, bank))   # expected 3

#  Time       :-  O(N * L * 4) → N = bank size, L = gene length (8) 
#  Space      :-  O(N)                                          
