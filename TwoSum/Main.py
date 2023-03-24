def twoSum(nums, target)-> list[int]:
    list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                list.append(i)
                list.append(j)
            else:
                continue
    return list

lst = twoSum([3,2,4], 6)
print(lst)