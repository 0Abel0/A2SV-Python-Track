if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    unique_arr = []
    for num in set(arr):
        unique_arr.append(num)
    
    print(unique_arr[len(unique_arr) - 2])
