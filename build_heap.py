# python3

import os


def build_heap(data):
    swaps = []
    # TODO: Create heap and heap sort
    # try to achieve O(n) and not O(n2)

    n = len(data)
    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps


def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)


def main():

    # TODO: add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file

    option = input("Enter input type: ")
    data = []

    if "F" in option:
        # input from file
        try:
            file_path = input("Input file path: ").strip()
            with open(f"tests/{file_path}", "r") as file:
                n = int(file.readline().strip())
                data = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    elif "I" in option:
        # input from keyboard
        try:
            n = int(input().strip())
            data = list(map(int, input().split()))
        except ValueError:
            print("Invalid input format.")
            return
    else:
        print("Invalid input type.")
        return

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
