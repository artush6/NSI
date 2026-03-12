import random

lst = sorted([random.randint(0, 2000) for _ in range(2000)])

# Exercice version


def rechercheDichoRec(lst, elt):
    if len(lst) == 0:
        return None

    mid = len(lst) // 2

    if lst[mid] == elt:
        return True
    elif elt < lst[mid]:
        return rechercheDichoRec(lst[:mid], elt)
    elif elt > lst[mid]:
        return rechercheDichoRec(lst[mid+1:], elt)


print(rechercheDichoRec([2, 5, 8, 12, 16, 23], 16))

# Improvised version with better debugging


def rechercheDichoRec_debug(lst, elt, depth=0):
    print("  " * depth + f"Searching in: {lst}")

    if len(lst) == 0:
        print("  " * depth + "Element not found")
        return False

    mid = len(lst) // 2
    print("  " * depth + f"Middle element: {lst[mid]}")

    if lst[mid] == elt:
        print("  " * depth + "Element found!")
        return True

    elif elt < lst[mid]:
        print("  " * depth + f"{elt} < {lst[mid]} → LEFT")
        return rechercheDichoRec_debug(lst[:mid], elt, depth + 1)

    else:
        print("  " * depth + f"{elt} > {lst[mid]} → RIGHT")
        return rechercheDichoRec_debug(lst[mid+1:], elt, depth + 1)


print("Result:", rechercheDichoRec_debug(lst, 20))
