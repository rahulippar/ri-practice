"""
Problem : Given an array of integers nums and a target integer target, find and return the indices of two distinct numbers in the array whose sum equals the target.
Assume there is always one unique solution, and the same element cannot be used twice to achieve the sum.
You can provide the indices in any order.

Example 1:
Input: nums = [8, 9, 12, 16], target = 16
Output: [0, 1]
Explanation: Indices 0 and 1 correspond to values 8 and 9, and their sum equals 16

Example 2:
Input: nums = [4, 3, 5], target = 7
Output: [1, 2]
Explanation: Indices 1 and 2 correspond to values 3 and 5, which add up to 7.
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    print("nums", nums)
    print("target", target)
    output = []
    for index1, element1 in enumerate(nums):
        for index2, element2 in enumerate(nums):
            if (index1 != index2) and (element1 + element2) == target:
                output.append(index1)
                output.append(index2)
                print("output", output)
                return output
    return output
