def weighted_minimal_edit(string_a, string_b, insertion_cost, deletion_cost, substitution_cost):
    len_a, len_b = len(string_a), len(string_b)
    matrix = []
    backtrace = []
    for i in range(len_a + 1):
        matrix.append([])
        backtrace.append([])
        for j in range(len_b + 1):
            if i == 0 and j == 0:
                matrix[-1].append(0)
            elif j == 0:
                matrix[-1].append(i + deletion_cost[string_a[i - 1]])
            elif i == 0:
                matrix[-1].append(j + insertion_cost[string_b[j - 1]])
            else:
                deletion = matrix[i - 1][j] + deletion_cost[string_a[i - 1]]
                insertion = matrix[i][j - 1] + insertion_cost[string_b[j - 1]]
                substitution = matrix[i - 1][j - 1] + substitution_cost[(string_a[i - 1], string_b[j - 1])]
                best = min(deletion, insertion, substitution)
                if deletion == best:
                    backtrace[-1].append((i - 1, j))
                elif insertion == best:
                    backtrace[-1].append((i, j - 1))
                else:
                    backtrace[-1].append((i - 1, j - 1))
                matrix[-1].append(best)
    return matrix, backtrace


def unweighted_minimal_edit(string_a, string_b):
    insertion_cost = {chr(i): 1 for i in range(97, 123)}
    deletion_cost = {chr(i): 1 for i in range(97, 123)}
    substitution_cost = {}
    for i in range(97, 123):
        for j in range(97, 123):
            substitution_cost[(chr(i), chr(j))] = (0 if i == j else 2)
    return weighted_minimal_edit(string_a, string_b, insertion_cost, deletion_cost, substitution_cost)
