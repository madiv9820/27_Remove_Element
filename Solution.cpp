#include <vector>
#include <iostream>
using namespace std;

class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            // Create a temporary vector to store elements from 'nums'
            // that are not equal to 'val'
            vector<int> temp_Vector;
            
            // Iterate over all elements in 'nums'
            // Add elements that are not equal to 'val' to 'temp_Vector'
            for (const int& x : nums)
                if (x != val) 
                    temp_Vector.emplace_back(x);
            
            // Copy the elements from 'temp_Vector' back into 'nums'
            // This modifies 'nums' in place for the required part of the array
            for (int index = 0; index < temp_Vector.size(); ++index)
                nums[index] = temp_Vector[index];
            
            // Return the new size of 'nums', which is the size of 'temp_Vector'
            return temp_Vector.size();
        }
};

// Time Complexity:
// The first loop iterates through the 'nums' array, and for each element not equal to 'val', it adds it to 'temp_Vector', taking O(n) time.
// The second loop copies elements from 'temp_Vector' back into 'nums', which also takes O(n) time.
// Thus, the overall time complexity is O(n), where 'n' is the number of elements in 'nums'.

// Space Complexity:
// We are using an extra vector 'temp_Vector' to store the filtered elements, which takes O(n) additional space.
// Therefore, the space complexity is O(n), where 'n' is the size of the input vector 'nums'.


int main() {
    vector<int> nums = {3,2,2,3}; int val = 3;
    Solution sol;

    int size = sol.removeElement(nums, val);
    for(auto start = nums.begin(); start != nums.begin() + size; ++start)
        cout << *start << " ";
    cout << endl;
}