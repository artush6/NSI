def main(x: int) -> list:
    lst = [x for x in range(x) if x % 2 == 0]

    print(lst)


main(20)
