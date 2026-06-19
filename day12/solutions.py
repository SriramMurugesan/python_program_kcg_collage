# # reverse string
# s = ["h","e","l","l","o"]
# left = 0
# right = len(s) - 1
# while left < right:
#     s[left], s[right] = s[right], s[left]
#     left += 1
#     right -= 1
# print(s)

# # two sum
# nums = [2,7,11,15]
# target = 9
# seen = {}
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in seen:
#         print([seen[diff], i])
#         break
#     seen[nums[i]] = i

# # valid palindrome
# s = "A man, a plan, a canal: Panama"
# filtered = [c.lower() for c in s if c.isalnum()]
# left = 0
# right = len(filtered) - 1
# is_palindrome = True
# while left < right:
#     if filtered[left] != filtered[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1
# print(is_palindrome)

# # merge sorted array
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# i = m - 1
# j = n - 1
# k = m + n - 1
# while j >= 0:
#     if i >= 0 and nums1[i] > nums2[j]:
#         nums1[k] = nums1[i]
#         i -= 1
#     else:
#         nums1[k] = nums2[j]
#         j -= 1
#     k -= 1
# print(nums1)

# # container with most water
# height = [1,8,6,2,5,4,8,3,7]
# left = 0
# right = len(height) - 1
# max_water = 0
# while left < right:
#     water = min(height[left], height[right]) * (right - left)
#     if water > max_water:
#         max_water = water
#     if height[left] < height[right]:
#         left += 1
#     else:
#         right -= 1
# print(max_water)

# # next permutation
# nums = [1,2,3]
# i = len(nums) - 2
# while i >= 0 and nums[i] >= nums[i + 1]:
#     i -= 1
# if i >= 0:
#     j = len(nums) - 1
#     while nums[j] <= nums[i]:
#         j -= 1
#     nums[i], nums[j] = nums[j], nums[i]
# nums[i + 1:] = reversed(nums[i + 1:])
# print(nums)

# # generate all permutations
def permute(nums):
    res = []
    def backtracking(path, options):
        if not options:
            res.append(path)
            return
        for i in range(len(options)):
            backtracking(path + [options[i]], options[:i] + options[i+1:])
    backtracking([], nums)
    return res
print(permute([1,2,3]))

# # remove duplicates from sorted array
# nums = [1,1,2]
# k = 1
# for i in range(1, len(nums)):
#     if nums[i] != nums[i-1]:
#         nums[k] = nums[i]
#         k += 1
# print(k, nums[:k])

# move zeroes
nums = [0,1,0,3,12]
insert_pos = 0
for num in nums:
    if num != 0:
        nums[insert_pos] = num
        insert_pos += 1
for i in range(insert_pos, len(nums)):
    nums[i] = 0
print(nums)

# # remove element
nums = [3,2,2,3]
val = 3
k = 0
for num in nums:
    if num != val:
        nums[k] = num
        k += 1
print(k, nums[:k])
