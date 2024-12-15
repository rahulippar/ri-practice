"""
Problem statement : You are provided with two integer arrays, nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n. These integers represent the count of elements in nums1 and nums2 respectively. Your task is to merge these two arrays into a single sorted array, while storing the result within nums1.
To make room for the merged result, nums1 has a size of m + n, where the first m elements represent the data to be merged, and the last n positions are filled with zeros, which should be ignored. nums2 contains n elements
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1, 2, 2, 3, 5, 6]
Explanation: You are merging [1, 2, 3] and [2, 5, 6] into nums1, producing [1, 2, 2, 3, 5, 6].
Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays are [1] and an empty array [], so the result is [1].
Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays are [] and [1], so the result is [1].

"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    #nums1 = [x for x in nums1 if x != 0]
    #nums2 = [x for x in nums2 if x != 0]
    pt1, pt2, p = m-1, n-1, m+n-1

    while pt1 >= 0 and pt2 >= 0:
        print( "pt1 ", pt1, " pt2 " , pt2 )
        if nums1[pt1] > nums2[pt2]:
            nums1[p] = nums1[pt1]
            pt1 -= 1
        else:
            nums1[p] = nums2[pt1]
            pt2 -= 1
        p -= 1
    
    while pt2 >= 0:
        nums1[p] = nums2[pt2]
        pt2 -= 1
