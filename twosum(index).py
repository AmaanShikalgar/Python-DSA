def two_sum(arr,target):
    seen = {}

    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in seen:
            return [seen[needed],i]

        seen[arr[i]] = i

print(two_sum([2,7,11,15],9))