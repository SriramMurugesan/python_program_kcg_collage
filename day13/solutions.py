# # combinations
# def combine(n, k):
#     res = []
#     def backtracking(start, path):
#         if len(path) == k:
#             res.append(path)
#             return
#         for i in range(start, n + 1):
#             backtracking(i + 1, path + [i])
#     backtracking(1, [])
#     return res
# print(combine(4, 2))

# # generate all subsets
# def subsets(nums):
#     res = []
#     def backtracking(i, path):
#         if i == len(nums):
#             res.append(path)
#             return
#         backtracking(i+1, path+[nums[i]])
#         backtracking(i+1, path)
#     backtracking(0, [])
#     return res
# print(subsets([1,2]))

# # combination sum
# def combinationSum(candidates, target):
#     res = []
#     def backtracking(i, path, total):
#         if total == target:
#             res.append(path)
#             return
#         if i >= len(candidates) or total > target:
#             return
#         backtracking(i, path + [candidates[i]], total + candidates[i])
#         backtracking(i + 1, path, total)
#     backtracking(0, [], 0)
#     return res
# print(combinationSum([2,3,6,7], 7))

# # permutations ii
# def permuteUnique(nums):
#     nums.sort()
#     res = []
#     def backtracking(path, options):
#         if not options:
#             res.append(path)
#             return
#         for i in range(len(options)):
#             if i > 0 and options[i] == options[i-1]:
#                 continue
#             backtracking(path + [options[i]], options[:i] + options[i+1:])
#     backtracking([], nums)
#     return res
# print(permuteUnique([1,1,2]))

# # subsets ii
# def subsetsWithDup(nums):
#     nums.sort()
#     res = []
#     def backtracking(i, path):
#         if i == len(nums):
#             res.append(path)
#             return
#         backtracking(i+1, path+[nums[i]])
#         while i+1 < len(nums) and nums[i] == nums[i+1]:
#             i += 1
#         backtracking(i+1, path)
#     backtracking(0, [])
#     return res
# print(subsetsWithDup([1,2,2]))

# # top k elements (kth largest)
# import heapq
# nums = [3,2,1,5,6,4]
# k = 2
# heap = []
# for i in nums:
#     heapq.heappush(heap, i)
#     if len(heap) > k:
#         heapq.heappop(heap)
# print(heap[0])

# # top k frequent elements
# import heapq
# nums = [1,1,1,2,2,3]
# k = 2
# freq = {}
# for i in nums:
#     freq[i] = freq.get(i, 0) + 1
# heap = []
# for key in freq:
#     heapq.heappush(heap, (freq[key], key))
#     if len(heap) > k:
#         heapq.heappop(heap)
# res = []
# for i in range(len(heap)):
#     res.append(heap[i][1])
# print(res)

# # sort characters by frequency
# import heapq
# s = "tree"
# freq = {}
# for i in s:
#     freq[i] = freq.get(i, 0) + 1
# heap = []
# for key in freq:
#     heapq.heappush(heap, (-freq[key], key))
# res = ""
# while heap:
#     count, char = heapq.heappop(heap)
#     res += (-count) * char
# print(res)

# # k closest points to origin
# import heapq
# points = [[1,3],[-2,2]]
# k = 1
# heap = []
# for x, y in points:
#     dist = x**2 + y**2
#     heapq.heappush(heap, (-dist, x, y))
#     if len(heap) > k:
#         heapq.heappop(heap)
# res = []
# for dist, x, y in heap:
#     res.append([x, y])
# print(res)

# # find k pairs with smallest sums
# import heapq
# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3
# heap = []
# for i in range(min(k, len(nums1))):
#     heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
# res = []
# while heap and len(res) < k:
#     sm, i, j = heapq.heappop(heap)
#     res.append([nums1[i], nums2[j]])
#     if j + 1 < len(nums2):
#         heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
# print(res)

# # merge k sorted lists
# # assuming arrays for simplicity
# lists = [[1,4,5],[1,3,4],[2,6]]
# import heapq
# heap = []
# for i in range(len(lists)):
#     if lists[i]:
#         heapq.heappush(heap, (lists[i][0], i, 0))
# res = []
# while heap:
#     val, list_idx, element_idx = heapq.heappop(heap)
#     res.append(val)
#     if element_idx + 1 < len(lists[list_idx]):
#         heapq.heappush(heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
# print(res)

# # top k frequent words
# import heapq
# words = ["i","love","leetcode","i","love","coding"]
# k = 2
# freq = {}
# for w in words:
#     freq[w] = freq.get(w, 0) + 1
# class Word:
#     def __init__(self, count, word):
#         self.count = count
#         self.word = word
#     def __lt__(self, other):
#         if self.count == other.count:
#             return self.word > other.word
#         return self.count < other.count
# heap = []
# for word in freq:
#     heapq.heappush(heap, Word(freq[word], word))
#     if len(heap) > k:
#         heapq.heappop(heap)
# res = []
# while heap:
#     res.append(heapq.heappop(heap).word)
# res.reverse()
# print(res)

# # median from data stream
# import heapq
# small = [] # max heap
# large = [] # min heap
# def addNum(num):
#     heapq.heappush(small, -num)
#     if small and large and (-small[0]) > large[0]:
#         val = -heapq.heappop(small)
#         heapq.heappush(large, val)
#     if len(small) > len(large) + 1:
#         val = -heapq.heappop(small)
#         heapq.heappush(large, val)
#     if len(large) > len(small) + 1:
#         val = heapq.heappop(large)
#         heapq.heappush(small, -val)
# def findMedian():
#     if len(small) > len(large):
#         return -small[0]
#     if len(large) > len(small):
#         return large[0]
#     return (-small[0] + large[0]) / 2.0
# addNum(1)
# addNum(2)
# print(findMedian())
# addNum(3)
# print(findMedian())
