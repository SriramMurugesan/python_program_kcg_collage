# maximum subarray of size k
# sliding window
# nums = [2,1,5,1,3,2]
# k=3
# window_sum=0
# max_sum=0
# for i in range(k):
#     window_sum+=nums[i]
# max_sum=window_sum
# for i in range(k,len(nums)):
#     window_sum=window_sum-nums[i-k]+nums[i]
#     max_sum=max(max_sum,window_sum)
# print(max_sum)
# heapq
# import heapq
# heap=[]
# heapq.heappush(heap,5)
# heapq.heappush(heap,2)
# heapq.heappush(heap,3)
# print(heap)
# smallest=heapq.heappop(heap)
# print(smallest)
# smallest=heapq.heappop(heap)
# print(smallest)
# print(heap)
# find kth largest element using heapq
# import heapq
# nums=[2,1,5,1,3,2]
# k=3
# heap=[]
# for i in nums:
#     heapq.heappush(heap,i)
#     if len(heap)>k:
#         heapq.heappop(heap)
# print(heap[0])
# top k frequent elements
import heapq
l=[1,2,3,3,3,1,2,4,5,2]
k=2
freq={}     #{1:2,2:3,3:3,4:1,5:1}
for i in l: #i=1
    freq[i]=freq.get(i,0)+1#freq[1]=freq.get(1,0)=>2+1
heap=[]
for key in freq:
    heapq.heappush(heap,(freq[key],key))#([((3,2),(3,3)])
    if len(heap)>k:
        heapq.heappop(heap)
res=[]
for i in range(len(heap)):
    res.append(heap[i][1])
        
print(res)

# sort characters by frequency
s="aababcdabd"






