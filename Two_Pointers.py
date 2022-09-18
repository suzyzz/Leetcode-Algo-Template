# 双指针 Two Pointers 
# 使用条件 
#    • 滑动窗口 (90%) 
#    • 时间复杂度要求 O(n) (80%是双指针) 
#    • 要求原地操作，只可以使用交换，不能使用额外空间 (80%) 
#    • 有子数组 subarray /子字符串 substring 的关键词 (50%) 
#    • 有回文 Palindrome 关键词(50%)
# 复杂度 
# 	• 时间复杂度：O(n) 
# 			￮ 时间复杂度与最内层循环主体的执行次数有关 
# 			￮ 与有多少重循环无关 
# 	• 空间复杂度：O(1) 
# 			￮ 只需要分配两个指针的额外内存    

# 相向双指针(patition in quicksort)
def patition(self, A, start, end):
    if start >= end:
        return
    left, right = start, end
    # key point 1: pivot is the value, not the index
    pivot = A[(start + end) // 2]
    # key point 2: every time you compare left & right, it should be left <= right not left < right

    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


# 背向双指针
left = position
right = position + 1
while left >= 0 and right < len(s):
    if left and right 可以停下来了:
        break
    left -= 1
    right += 1

# 同向双指针
j = 0 or j = 1
for i in range(n):
    # 不满足则循环到满足搭配为止
    while j < n and i 到 j 之间不满足条件：
        j += 1
    if i 到 j 之间满足条件:
        处理 i 到 j 这段区间

# 数据流问题 （Data Stream Problem) - 链表重点
slow, fast = head, head.next
while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

return slow



 # 合并双指针
 def merge(list1, list2):
    new_list = []
    i, j = 0, 0
    # 合并的过程只能操作 i, j 的移动，不要去用 list1.pop(0) 之类的操作 因为 pop(0) 是 O(n) 的时间复杂度
    while i < len(list1) and len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
        # 合并剩下的数到 new_list 里 不要用 new_list.extend(list1[i:]) 之类的方法 因为 list1[i:] 会产生额外空间耗费
    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    while j < len(list2):
        new_list.append(list2[j])
        j += 1
    return new_list


# 排序算法 Sorting
# 使用条件
# 复杂度 
#     • 时间复杂度： 
#         ￮ 快速排序(期望复杂度) ： O(nlogn) 
#         ￮ 归并排序(最坏复杂度) ： O(nlogn) 
#     • 空间复杂度： 
#         ￮ 快速排序 ： O(1) 
#         ￮ 归并排序 ： O(n)  

# quick sort
class Solution:
    def sortIntegers(self, A):
        self.quickSort(A, 0, len(A) -  1)
    
    def quickSort(self, A, start, end):
        # 如果是一个数就不用排了
        if start >= end:
            return
        left, right = start, end
        # key point 1: pivot is the value, not the index
        pivot = A[(start + end) // 2]
        # key point 2: every time you compare left & right, it should be left <= right not left < right， 
        # 为了让结果必须交叉 再执行一次 left += 1 或者 right -=， 不然就会有 left = right and start - left 重复， right - end 重复
        while left <= right:
            while left <= right and A[left] < pivot: #尽量让中间值均分， 极端情况 1，1，1，1，1， 如果是<= 这里第一个while就会直接走到最末
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

# merge sort       
class Solution:
    def sortIntegers(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        # 处理左半区间
        self.merge_sort(A, start, (start + end) // 2, temp)
        # 处理右半区间
        self.merge_sort(A, (start + end) // 2 + 1, end, temp)
        # 合并排序数组
        self.merge(A, start, end, temp)
    
    def merge(self, A, start, end, temp):
        middle = (start + end) // 2
        left_index = start
        right_index = middle + 1
        index = start
        while left_index <= middle and right_index <= end:
            if A[left_index] < A[right_index]:
                temp[index] = A[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = A[right_index]
                index += 1
                right_index += 1
        while left_index <= middle:
            temp[index] = A[left_index]
            index += 1
            left_index += 1
        while right_index <= end:
            temp[index] = A[right_index]
            index += 1
            right_index += 1
        for i in range(start, end + 1):
            A[i] = temp[i]

        
