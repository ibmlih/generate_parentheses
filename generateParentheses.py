def generateParenthesis(N):
    results = []

    def backtrack(parenthesis, opening, closing):
        if len(parenthesis) == 2 * N:
            results.append(parenthesis)
            return

        if opening < N:
            backtrack(parenthesis + '(', opening + 1, closing) # generate opening bracket

        if closing < opening:
            backtrack(parenthesis + ')', opening, closing + 1) # generate closing bracket

    backtrack('', 0, 0)
    return results