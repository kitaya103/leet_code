class Solution(object):
    def findMaxAverage(self, nums, k):
        length = len(nums)
        maximum = -sys.maxsize
        
        if length < k:
            return maximum / k
        
        left, right = 0, k - 1
        sum = 0
        
        for i in range(right + 1):
            sum += nums[i]
        
        maximum = max(maximum, sum)
        
        while right + 1 < length:
            sum -= nums[left]
            left += 1
            right += 1
            sum += nums[right]
            maximum = max(maximum, sum)
        
        return maximum / k