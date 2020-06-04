'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''


# O(n^2) Solution
# def twoSum(arr,t):
#     for x in range(0,len(arr)-1):
#         for y in range(1,len(arr)):
#             if arr[x] + arr[y] == t:
#                 return x,y

# O(n) Solution
def twoSum(arr,t):
    for x in range(0,len(arr)):
        if arr[x] < t:
            y = t - arr[x]
            if y in arr:
                return arr.index(y),x
                break

print(twoSum([2, 7, 11, 15,16],31))