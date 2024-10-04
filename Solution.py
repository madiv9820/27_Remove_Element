from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Create a temporary array that includes all elements of nums except those equal to 'val'
        # This is done using list comprehension.
        temp_Array = [x for x in nums if x != val]
        
        # Copy elements from temp_Array back into the original nums array
        # to reflect the changes in place for the part of the list that matters.
        for index in range(len(temp_Array)):
            nums[index] = temp_Array[index]
        
        # Return the new length of the list after removing the elements.
        # The length of the new list is simply the length of temp_Array.
        return len(temp_Array)

# Time Complexity:
# The list comprehension [x for x in nums if x != val] iterates over 'nums', which takes O(n) time.
# Copying the elements from temp_Array back into nums also takes O(n) time.
# Therefore, the overall time complexity is O(n), where n is the number of elements in the input list 'nums'.

# Space Complexity:
# We are using an additional list temp_Array to store the filtered values, which takes O(n) space.
# Thus, the space complexity is O(n), where n is the number of elements in 'nums'.