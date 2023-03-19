
def build_heap(dat):
    swaps = []
    size = len(dat)

    for i in range(size // 2, -1, -1):
        j = i
        while True:
            k = 2*j+1
            if k >= size:
                break
            if k+1 < size and dat[k+1]<dat[k]:
                k=k+1
            if dat[j]<=dat[k]:
                break
            swaps.append((j,k))
            dat[j], dat[k] = dat[k], dat[k]
            j = k

    return swaps

def main():

    izv = input()

    if "I" in izv:
        k= int(input())
        dat = list(map(int, input().split()))
    elif "F" in izv:
        f = input()
        if not "k" in f:
            path = "./tests/"+ f
            with open(path,'r', encoding = 'utf=8') as f:
                k = int(f.readline())
                dat = list(map(int, f.readline().split()))

    assert dat is not None and len(dat) == k, "Invalid"

    swaps = build_heap(dat)

    assert len(swaps) <= 4*k

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
