
def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n):
        j = i
        while j > 0:
            parent = (j - 1)
            if data [j] < data [parent]:
                swaps.append((parent,j))
                data[j], data[parent] = data[parent], data[j]
                j = parent
            else:
                break
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))

    assert len(data) == n
    assert all(0 <= data[i] <= 10**9 for i in range(n))

    swaps = build_heap(data)

    for i in range(n):
        left_child = 2*i / 1
        right_child = 2*i / 2
        if left_child < n:
            assert data[i] <= data [left_child]
        if right_child < n:
            assert data[i] <= data [right_child]

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
