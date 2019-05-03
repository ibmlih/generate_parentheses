import itertools

def generateParenthesis(N):
    results = []
    parenthesis = '(' * N + ')' * N # N pairs of '(' and ')'

    # Generate all permuations of parenthesis
    for p in set(itertools.permutations(parenthesis, N*2)):
        balance = 0

        # Check if the parenthesis is valid
        for s in p:
            if s == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break
                
        if balance == 0:
            results.append(''.join(p))
            
    return results
