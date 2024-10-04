# 27. Remove Element

__Type:__ Easy <br>
__Topics:__ Array, Two Pointers <br>
__Companies:__ Google, Microsoft, Amazon, Bloomberg, Meta, Apple, Adobe, Yahoo, Uber, Yandex, Accenture <br>
<hr>

### Question

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [__in-place__](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return _the number of elements in_ `nums` _which are not equal to_ `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`. 
<br><br>

__Custom Judge:__

The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be __accepted__.
<hr>

### Examples

__Example 1:__

__Input:__ nums = [3,2,2,3], val = 3 <br>
__Output:__ 2, nums = [2,2,_,_] <br>
__Explanation:__ Your function should return k = 2, with the first two elements of nums being 2. <br>
It does not matter what you leave beyond the returned k (hence they are underscores).

__Example 2:__

__Input:__ nums = [0,1,2,2,3,0,4,2], val = 2 <br>
__Output:__ 5, nums = [0,1,4,0,3,_,_,_] <br>
__Explanation:__ Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4. <br>
Note that the five elements can be returned in any order. <br>
It does not matter what you leave beyond the returned k (hence they are underscores).
<hr>

### Constraints:

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`
<hr>

### Hints
- The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to remove that element per-say, right?

- We can move all the occurrences of this element to the end of the array. Use two pointers!
![](https://assets.leetcode.com/uploads/2019/10/20/hint_remove_element.png)

- Yet another direction of thought is to consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.