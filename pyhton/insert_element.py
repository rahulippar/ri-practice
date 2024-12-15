"""
Problem : Given a sorted list of distinct integers and a target value, locate the position of the target in the list.
If the target is not present, identify the index where it should be inserted to preserve the order of the list. Return this index.
"""
def searchInsert(self, nums: List[int], target: int) -> int:
    for key, value in enumerate(nums):
        if target == value:
            return key
        elif value > target:
            nums.insert(key, target)
            return key
    else:
        nums.append(target) # if target is bigger than all elements then append it.
        return len(nums) - 1
