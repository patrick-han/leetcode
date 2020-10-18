




# Normal recursive calls, O(2^N), 2 branches per call
def decode(s):
    def dec(s, ptr_idx):
        if (ptr_idx >= len(s)): # If the pointer moves past the entire string, we're done
            return 1

        curr_sum = 0
        if ((int(s[ptr_idx:ptr_idx + 2]) <= 26) and ((ptr_idx + 2) <= len(s))): # Increment pointer by 2
            curr_sum += dec(s, ptr_idx + 2)
        curr_sum += dec(s, ptr_idx + 1) # Increment pointer by 1

        return curr_sum
    return dec(s, 0)

testcase1 = "223" # Should output 3
testcase2 = "273" # Should output 1
testcase3 = "33" # Should output 1

print(decode(testcase1))
print(decode(testcase2))
print(decode(testcase3))




# With memoization, O(N), since the # of sub problems is the number of positions ptr_idx can be in, i.e. length of the string N
def decodeMemo(s):
    ht = {} # Memoization table
    def dec(s, ptr_idx):
        if (ptr_idx >= len(s)): # BASE CASE: If the pointer moves past the entire string, we're done
            return 1

        if (ptr_idx not in ht): # If we haven't cached the answer yet

            curr_sum = 0
            if ((int(s[ptr_idx:ptr_idx + 2]) <= 26) and ((ptr_idx + 2) <= len(s))): # Increment pointer by 2
                curr_sum += dec(s, ptr_idx + 2)
            curr_sum += dec(s, ptr_idx + 1) # Increment pointer by 1

            ht[ptr_idx] = curr_sum # Memoize the answer
        
        return ht[ptr_idx]
    return dec(s, 0)

print(decodeMemo(testcase1))
print(decodeMemo(testcase2))
print(decodeMemo(testcase3))