def search(nums, target) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums, target))