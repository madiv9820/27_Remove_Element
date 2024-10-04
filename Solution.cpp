#include <vector>
#include <iostream>
using namespace std;

class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            // 'actual_Index' keeps track of the position where the next valid element (i.e., not equal to 'val') will be placed.
            int actual_Index = 0;

            // Iterate through all elements in 'nums'
            for (int index = 0; index < nums.size(); ++index)
                // If the current element is not equal to 'val', move it to 'actual_Index' position
                if (nums[index] != val) 
                    nums[actual_Index++] = nums[index]; // Increment 'actual_Index' after placing the element

            // Return the new length of the array (number of elements not equal to 'val')
            return actual_Index;
        }
};

// Time Complexity:
// The loop runs through all elements of the input vector 'nums', making the time complexity O(n), where 'n' is the number of elements in 'nums'.

// Space Complexity:
// The algorithm modifies the vector in place and uses only a few extra variables (actual_Index), making the space complexity O(1), i.e., constant space.

int main() {
    vector<int> nums = {3,2,2,3}; int val = 3;
    Solution sol;

    int size = sol.removeElement(nums, val);
    for(auto start = nums.begin(); start != nums.begin() + size; ++start)
        cout << *start << " ";
    cout << endl;
}