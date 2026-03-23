import time


def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n - 2)


def fibonacci_BU(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


n = 40

# --- Recursive timing ---
start = time.perf_counter()
res_rec = fibonacci_rec(n)
end = time.perf_counter()

print("Recursive result:", res_rec)
print("Recursive time:", end - start, "seconds")


# --- DP timing ---
start = time.perf_counter()
res_dp = fibonacci_BU(n)
end = time.perf_counter()

print("DP result:", res_dp)
print("DP time:", end - start, "seconds")
