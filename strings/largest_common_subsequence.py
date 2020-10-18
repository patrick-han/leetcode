string1 = "AGGTAB"
string2 = "GXTXAYB"

# With slicing, recursive
def LCS(s1, s2):
    if (s1 == "" or s2 == ""):
        return 0
    if (s1[-1] == s2[-1]):
        return 1 + LCS(s1[:-1], s2[:-1])
    else:
        return max(LCS(s1, s2[:-1]), LCS(s1[:-1], s2))

print(LCS(string1, string2))


# DP, bottom up building a table
def LCS_DP(s1, s2):
    n = len(s2)
    m = len(s1)

    memo = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Starting at row = 1, col = 1 since we know the 0th columns and rows are 0 (base case of comparing with an empty string)
    for row in range(1,  n + 1):
        for col in range(1, m + 1):
            if (s1[col - 1] == s2[row - 1]): # Same last letter, 1 + LCS(s1 last removed, s2 last removed)
                memo[row][col] = 1 + memo[row - 1][col - 1]
            else: # Different last leters, compete by removing last letter of one or the other
                memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

    return memo[-1][-1]



print(LCS_DP(string1, string2))

string3 = "ADDSDLF"
string4 = "DSLF"

print(LCS_DP(string3, string4))
