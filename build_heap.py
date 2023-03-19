import os

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        godown(data, i, swaps)
    return swaps

def godown(data, i, swaps):
    n = len(data)
    min_inde = i
    lhs = 2 * i + 1
    rhs = 2 * i + 2
    if lhs < n and data[lhs] < data[min_inde]:
        min_inde = lhs
    if rhs < n and data[rhs] < data[min_inde]:
        min_inde = rhs
    if min_inde != i:
        swaps.append((i, min_inde))
        data[i], data[min_inde] = data[min_inde], data[i]
        godown(data, min_inde, swaps)

def main():
    userinput = input()
    if "I" in userinput:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in userinput:
        f = input()
        loc = './tests/'
        floc = os.path.join(loc, f)
        with open(floc, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
   swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

#KristapsOzolins
