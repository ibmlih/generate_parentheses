import itertools

def generateParenthesis(N):
    results = []
    binary = [] # 0 represents ( and 1 represent )

    for i in range(N):
        binary.append(0)
        binary.append(1)

    for t in set(itertools.permutations(binary, N*2)):
        balance = 0

        # Check if the parenthesis is valid
        for i in t:
            if i == 0:
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break

        # Convert binary into parenthesis
        if balance == 0:
            parenthesis = ''
            for i in t:
                if i == 0:
                    parenthesis += '('
                else:
                    parenthesis += ')'
            results.append(parenthesis)
            
    return results