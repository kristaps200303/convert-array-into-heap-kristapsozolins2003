#KO
import os #KO
 #KO
def build_heap(data): #KO
    swaps = [] #KO
    n = len(data) #KO
    for i in range(n // 2, -1, -1): #KO
        godown(data, i, swaps) #KO
    return swaps #KO
 #KO
def godown(data, i, swaps): #KO
    n = len(data) #KO
    min_inde = i #KO
    lhs = 2 * i + 1 #KO
    rhs = 2 * i + 2 #KO
    if lhs < n and data[lhs] < data[min_inde]: #KO
        min_inde = lhs #KO
    if rhs < n and data[rhs] < data[min_inde]: #KO
        min_inde = rhs #KO
    if min_inde != i: #KO
        swaps.append((i, min_inde)) #KO
        data[i], data[min_inde] = data[min_inde], data[i] #KO
        godown(data, min_inde, swaps) #KO
 #KO
def main(): #KO
    userinput = input().strip() #KO
    if "I" in userinput: #KO
        n = int(input().strip()) #KO
        data = list(map(int, input().strip().split())) #KO
        assert len(data) == n #KO
    elif "F" in userinput: #KO
        f = input().strip() #KO
        loc = './tests/' #KO
        floc = os.path.join(loc, f) #KO
        with open(floc, mode="r") as file: #KO
            n = int(file.readline().strip()) #KO
            data = list(map(int, file.readline().strip().split()) #KO
        assert len(data) == n #KO
    swaps = build_heap(data) #KO
    print(len(swaps)) #KO
    for i, j in swaps: #KO
        print(i, j) #KO
#KO
if __name__ == "__main__": #KO
    main() #KO
