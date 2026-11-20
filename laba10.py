def merge_intervals(intervals):
    if not intervals:
        return []

    arr = sorted(intervals)
    for start, end in arr:
        if start > end:
            raise ValueError
    result = [arr[0][:]]

    for start, end in arr[1:]:
        last = result[-1]

        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

        return result
print(merge_intervals([[1, 3], [2, 6], [8, 10]]))
print(merge_intervals([[1, 2], [2, 3]]))
print(merge_intervals([[1, 10], [2, 3]]))
print(merge_intervals([]))
