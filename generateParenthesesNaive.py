import itertools

def generateParenthesis(N):
    results = []
    binary = [] # 0 represents '(' and 1 represent ')'

    # Initialize N pairs of 0s and 1s
    for i in range(N):
        binary.append(0)
        binary.append(1)

    # Generate all permuations of binary
    for b in set(itertools.permutations(binary, N*2)):
        balance = 0

        # Check if the parenthesis is valid
        for i in b:
            if i == 0:
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break

        # Convert binary into parenthesis
        if balance == 0:
            parenthesis = ''
            for i in b:
                if i == 0:
                    parenthesis += '('
                else:
                    parenthesis += ')'
            results.append(parenthesis)
            
    return results