from random import randint

# 1. Create a table with n rows and p columns filled with random integers between 0 and 100


def create_table(n, p):
    table = []
    for i in range(n):
        row = []
        for j in range(p):
            row.append(randint(0, 100))
        table.append(row)
    return table


# 2. Sum of a given row k
def sum_row(table, k):
    total = 0
    for value in table[k]:
        total += value
    return total


# 3. Sum of a given column k
def sum_column(table, k):
    total = 0
    for row in table:
        total += row[k]
    return total


# 4. Sum of the two main diagonals of a square table
def sum_diagonals(table):
    n = len(table)  # number of rows (and columns, since it's a square)

    diag1 = 0
    for i in range(n):
        diag1 += table[i][i]   # main diagonal

    diag2 = 0
    for i in range(n):
        diag2 += table[i][n - 1 - i]   # secondary diagonal

    return [diag1, diag2]


table = create_table(4, 4)   # square table 4x4
for row in table:
    print(row)

print("Sum of row 2:", sum_row(table, 2))
print("Sum of column 1:", sum_column(table, 1))
print("Sums of diagonals:", sum_diagonals(table))
