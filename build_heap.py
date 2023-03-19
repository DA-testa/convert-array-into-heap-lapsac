def build_heap(data):
    swaps = []
    size = len(data)

    for i in range(size // 2, -1, -1):
        j = i
        while True:
            k = 2*j+1
            if k >= size:
                break
            if k+1 < size and data[k+1]<data[k]:
                k=k+1
            if data[j]<=data[k]:
                break
            swaps.append((j,k))
            data[j], data[k] = data[k], data[k]
            j = k

    return swaps

def main():

    izv = input()

    if "I" in izv:
        k= int(input())
        data = list(map(int, input().split()))
    elif "F" in izv:
        f = input()
        if not "k" in f:
            path = "./tests/"+ f
            with open(path,'r', encoding = 'utf=8') as f:
                k = int(f.readline())
                data = list(map(int, f.readline().split()))

    assert data is not None and len(data) == k, "Invalid"

    swaps = build_heap(data)

    assert len(swaps) <= 4*k

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
