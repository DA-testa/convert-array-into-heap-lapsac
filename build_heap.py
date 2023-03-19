
def build_heap(data):
    swaps = []
    size = len(data)

    for i in range(size // 2, -1, -1):
        j = i
        while True:
            k = 2 * j + 1
            if k >= size:
                break
            if k + 1 < size and data[k + 1] < data[k]:
                k = k + 1
            if data[j] <= data[k]:
                break
            swaps.append((j,k))
            data[j], data[k] = data[k], data[k]
            j = k

    return swaps

def main():

    izvele = input()

    if "I" in izvele:
        m= int(input())
        data = list(map(int, input().split()))
    elif "F" in izvele:
        fails = input()
        if "a" not in fails:
            dirrect = "./tests/" + fails
            with open(dirrect, 'r', encoding = 'utf=8') as f:
                m = int(f.readline())
                data = list(map(int, f.readline().split()))

    assert data is not None and len(data) == m

    swaps = build_heap(data)

    assert len(swaps) <= 4*m

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
