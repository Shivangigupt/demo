def find_min_count(arr):
    freq = {}
    n = len(arr)

    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1

        else:
            freq[arr[i]] = 1

    listt1 = list(freq.values())
    return (len(arr) - max(listt1))


print(find_min_count([1,2,2,3])

