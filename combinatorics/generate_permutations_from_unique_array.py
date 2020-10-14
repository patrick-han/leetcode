# 46. Given a collection of distinct integers, return all possible permutations.
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums: # For each new number to add
            new_perms = [] # Generate permutations with that number...
            for perm in perms: # ...by adding to the existing permutations
                for i in range(len(perm) + 1): # Insert n in each possible position of each existing permutation to generate the new ones
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        
        return perms
                    

solver = Solution()
testcase = [1,2,3]
solution = solver.permute(testcase)
print(solution)