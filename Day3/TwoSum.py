def twoSum(nums,target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in hash_table:
            hash_table[nums[i]] = i
            print(hash_table)
        else:
            return [hash_table[complement], i]
       
            
nums = [2,17,11,7,15]
target = 9
print(twoSum(nums,target))