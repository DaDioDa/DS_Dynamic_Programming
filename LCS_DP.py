import sys

def LCS_DP(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m + 1) for _ in range(n + 1)]

    # 建立一個二維的 DP 表格
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # 從表格中回溯找到 LCS
    index = L[n][m]
    lcs = [""] * index

    i, j = n, m
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            index -= 1
            lcs[index] = X[i - 1]
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)





def LCS_DaC(X, Y, m, n):
    if m == 0 or n == 0:
        return ""
    elif X[m-1] == Y[n-1]:
        return LCS_DaC(X, Y, m-1, n-1) + X[m-1]
    else:
        left = LCS_DaC(X, Y, m, n-1)
        right = LCS_DaC(X, Y, m-1, n)
        if len(left) > len(right):
            return left
        else:
            return right

# 使用示例
sys.setrecursionlimit(10000)

X = "AGCAGAAGGTTTGAGGAATAGGTTAAATTGAGTGGTTTAATAACGGTATGTCTGGGATTAAAGTGTAGTATAGTGTGATTATCGGAGACGGTTTTAAGACACGAGTTCCCAAAATCAAGCGGGGTCATTACAACGGTTATTCCTGGTAGTTTAGGTGTACAATGTCCTGAAGAATATTTAAGAAAAAAGCACCCCTCATCGCCTAGAATTACCTACTACGGTCGACCATACCTTCGATTATCGCGGCCACTCTCGCATTAGTCGGCAGAGGTGGTTGTGTTGCGATAGCCCAGTATAATATTCTAAGGCGTTACCCTGATGAATATCCAACGGAATTGCTATAGGCCTTGAACGCTACACGGACGATACGAAATTATGTATGGACCGGGTCATCAAAAGGTTATACCCTTGTAGTTAACATGTAGCCCGGCCCTATTAGTACAGTAGTGCCTTGAATGGCATTCTCTTTATTAAGTTTTCTCTACAGCTAAACGATCAAGTGCACTTCCACAGAGCGCGGTGGAGATTCATTCACTCGGCAGCTCTGTAATAGGGACTAAAAAAGTGATGATAATCATGAGTGCCGCGTTATGGTGGTGTCGGAACAGAGCGGTCTTACGGCCAGTCGTATGCCTTCTCGAGTTCCGTCCAGTTAAGCGTGACAGTCCCAGTGTACCCACAAACCGTGATGGCTGTGCTTGGAGTCAATCGCAAGTAGGATGGTCTCCAGACACCGGGGCACCAGTTTTCACGCCGAAAGCATAAACGACGAGCAGATATGAAAGTGTTAGAACTGGACGTGCCGTTTCTCTGCGAAGAACACCTCGAGCTGTAGCGTTGTTGCGCTGCCTAGATGCAGTGTTGCTCATATCACATTTGCTTCAACGACTGCCGCCTTCGCTGTATCCCTAGACACTCAACAGTAAGCGCTTTTTGTAGGCAGGGGCACCCCCTATCAGTGACTGCGCCAAAACATCTTCGGATCCCCTTGTCCAATCAA"
Y = "ACTCATCGAATTCTTACATTTAAGACCCTAATATCACATCATTAGTGATTAATTGCCACTGCCAAAATTCTGTCCAGAAGCGTTTTAGTTCGCTCCACTAAAGTTGTTTAAAACGACTACCAAATCCGCATGTTAGGGGATTTCTTATTAATTCTTTTATCGTGAGGAACAGCGGATCTTAATGGATGGCCGCAGGTGGTATGGAAGCTAATAGCGCGGGTGAGAGGGTAATCAGCCGTGTTCACCTACACAACGCTAACGGGCGATTCTATAAGATTCCGCATTGCGTCTACTTATAAGATGTCTCAACGGTATCCGCAACTTGTGAAGTGCCTACTATCCTTAAACGCATATCTCGCCCAGTAGCTTCCCAATATGTGAGCATCAATTGTTGTCCGGGCCGAGATAGTCATGTGCTCACGGAACTTACTGTATGAGTAGTGATTTGAAAGAGTTGTCAGTTTGCTGGTTCAGGTAAAGGTTCCTCACGCTACCTCAAAGTAAGAGAGCGGTCGTGACATTATCCGTGATTTTCTCACTACTATTAGTACTCACGACTCGATTCTGCCGCAGCCATGTTTCGCCAGAATGCCAGTCAGCATTAAGGAGAGCTCAGGGCAGGTCAACTCGCATAGTGAGGGTTACATGTTCGTTGGGCTCTTCCGACACGAACCTCAGTTAGCCTACATCCTACCAGAGGTCTGTGCCCCGGTGGTGAGAAGTGCGGATTTCGTATTTGCAGCTCGTCAGTACTTTCAGAATCATGGCCTGCACGGCAAAATGACGCTTATAATGGACTTCGACATGGCAATAACGCCTCGTTTCTACGTCAGGAGGAGAATAGTATAAACATAACTGCTGTCGGCAGAAGCGCCAAAGGAGTCTCTGAATTCTTATTCCCGAATAACATCCGTCTCCGTGCGGGAAAATCACCGACGGCGTTTTATAGAAGCCTAGGGGAACAGATTGGTCTAATTAGCTTAAGAGAGTAAATTCTGGG"
#print("Longest Common Subsequence: ", LCS_DaC(X, Y, len(X), len(Y)))
print("Longest Common Subsequence: ", LCS_DP(X, Y))