def max_subarray_sum(arr):
    max_so_far = curr_max = arr[0]
    for x in arr[1:]:
        curr_max = max(x, curr_max + x)
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

if __name__ == "__main__":
    print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # 6
