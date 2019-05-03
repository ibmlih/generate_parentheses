def generateParenthesis(N):
    results = []

    def backtrack(parentheses, opening, closing):
        if len(parentheses) == 2 * N:
            results.append(parentheses)
            return

        if opening < N:
            backtrack(parentheses+'(', opening + 1, closing)

        if closing < opening:
            backtrack(parentheses+')', opening, closing + 1)

    backtrack('', 0, 0)
    return results