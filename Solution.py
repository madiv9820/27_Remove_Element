from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer 'actual_Index' to keep track of the position
        # where the next element (not equal to 'val') will be placed.
        actual_Index = 0
        
        # Iterate over each element in the 'nums' array by index
        for index in range(len(nums)):
            # If the current element is not equal to 'val', move it to the 'actual_Index' position
            if nums[index] != val:
                nums[actual_Index] = nums[index]
                # Increment the 'actual_Index' to track the next available position
                actual_Index += 1
        
        # Return the new length of the array (all elements before 'actual_Index' do not contain 'val')
        return actual_Index

# Time Complexity:
# The loop iterates through each element of the list exactly once, so the time complexity is O(n), 
# where 'n' is the number of elements in 'nums'.

# Space Complexity:
# This approach modifies the list in place, so no additional space proportional to the input size is used.
# Hence, the space complexity is O(1) (constant space), since only a few extra variables are used.