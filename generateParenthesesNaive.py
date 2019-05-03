import itertools

def generateParenthesis(N):
    results = []
    parentheses = '(' * N + ')' * N # N pairs of '(' and ')'

    # Generate all permuations of parentheses
    for p in set(itertools.permutations(parentheses, N*2)):
        balance = 0

        # Check if the parenthesis is valid
        for i in p:
            if i == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break
                
        if balance == 0:
            results.append(''.join(p))
            
    return results
