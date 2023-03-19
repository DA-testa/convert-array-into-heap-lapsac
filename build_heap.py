#python3

def build_heap(data):
    swaps = []
    size = len(data)
    for i in range(size // 2, -1, -1):
        j = i
        while True:
            k = j * 2 + 1
            if k >= size:
                break
            if k + 1 < size and data[k + 1] < data[k]:
                k = k + 1
            if data[j] <= data[k]:
                break
            swaps.append((j,k))
            data[j], data[k] = data[k], data[j]
            j = k

    return swaps


def main():
    izvele = input()
    if "I" in izvele:
        n= int(input())
        data = list(map(int, input().split()))
    elif "F" in izvele:
        f = input()
        with open("tests/"+f,'r') as f:
                m = int(f.readline())
                data = list(map(int, f.readline().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
