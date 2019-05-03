import itertools

def generateParenthesis(N):
    results = []

    def backtrack(string, left, right):
        if len(string) == 2 * N:
            results.append(string)
            return
        if left < N:
            backtrack(string+'(', left+1, right)
        if right < left:
            backtrack(string+')', left, right+1)

    backtrack('', 0, 0)
    return results


# print(generateParenthesis(3))
for s in itertools.combinations([0,0,1,1], 2):
    print(s)
