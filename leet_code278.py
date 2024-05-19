# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n # 左右边界
        while left + 1 < right:
            mid = left + (right - left) // 2
            # 判断mid是否为正确版本，如果是的话，那么说明错误版本在mid的右边，反之则在左边
            if isBadVersion(mid): 
                right = mid # 向[left，mid]查找错误版本
            else: 
                left = mid # 向[mid，right]查找错误版本
        # 最后判断下left是否是错误版本
        if isBadVersion(left): 
            return left
        return right