def alignement(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    sc = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        sc[i][0] = -i

    for j in range(n + 1):
        sc[0][j] = -j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                sc[i][j] = max(
                    sc[i][j - 1] - 1,
                    sc[i - 1][j] - 1,
                    sc[i - 1][j - 1] + 1
                )
            else:
                sc[i][j] = max(
                    sc[i][j - 1] - 1,
                    sc[i - 1][j] - 1,
                    sc[i - 1][j - 1] - 1
                )

    return sc[m][n]


seq1 = "ACTACGAACTAG"
seq2 = "GACTAGACTAAGC"

result = alignement(seq1, seq2)

print(result)
