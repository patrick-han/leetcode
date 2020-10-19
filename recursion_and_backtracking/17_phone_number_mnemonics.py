# Test cases
testcase1 = "22"
testcase2 = "223"

# Mapping of numbers to letters
ht = {"2":["a","b","c"], 
"3":["d","e","f"],
"4":["g","h","i"],
"5":["j","k","l"],
"6":["m","n","o"],
"7":["p","q","r","s"],
"8":["t","u","v"],
"9":["w","x","y","z"]}

# Recursive
def letterCombinations(s):
    if len(s) == 1:
        return ht[s]
    first = letterCombinations(s[:-1])
    second = ht[s[-1]]
    new = []
    for i in first:
        for j in second:
            new.append(i + j)
    return new

out1 = letterCombinations(testcase1)
print(out1)
print(len(out1))

out2 = letterCombinations(testcase2)
print(out2)
print(len(out2))


# Recursive, with index pointer
def letterCombinations2(digits):
    def comb(partial, idx_ptr, digits, answers):
        if idx_ptr == len(digits):
            return answers.append(partial)
        letters_for_current = ht[digits[idx_ptr]]
        for letter in letters_for_current:
            partial_temp = partial + letter
            comb(partial_temp, idx_ptr + 1, digits, answers)

        return answers

    
    return comb("", 0, digits, [])

out1 = letterCombinations2(testcase1)
print(out1)
print(len(out1))

out2 = letterCombinations2(testcase2)
print(out2)
print(len(out2))