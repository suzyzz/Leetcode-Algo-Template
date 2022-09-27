# 使用条件 
# • 排序数组 (30-40%是二分) 
# • 当面试官要求你找一个比 O(n) 更小的时间复杂度算法的时候(99%) 
# • 找到数组中的一个分割位置，使得左半部分满足某个条件，右半部分不满足(100%) 
# • 找到一个最大/最小的值使得某个条件被满足(90%) 

# 复杂度 
# • 时间复杂度：O(logn) 
# • 空间复杂度：O(1)

from turtle import end_fill


def binary_search(self, nums, target):
    # corner case 处理
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    # 用 start + 1 < end 而不是 start < end 是为了避免死循环
    # 在 first position of target 的情况下不会出现死循环，在 last position 会出现死循环
    while start + 1 < end:
        mid = (start + end) // 2
        # >, =, < 的逻辑分开写，然后再看 = 的情况是否能合并到其他分支

        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid

        # 因为上面的循环推出条件是 start + 1 < end，因此这里循环结束的时候， start 和 end 的关系是相邻关系
        # 所以需要再单独判断 start 和 end 这两个数组谁是答案，如果找 first 就先看start，否则先看end
        if nums[start] == target:
            return start

        if nums[end] == target:
            return end
    return -1






    
def binary_search(self, nums, target):
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
            
    return -1