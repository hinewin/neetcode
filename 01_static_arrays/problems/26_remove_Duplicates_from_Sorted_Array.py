from typing import List

'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)
        nums.clear()
        nums.extend(new_list)        
        return len(nums), nums
                    
                    
class Solution2: 
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = set(nums)
        nums.sort()
        return len(nums), nums

class Solution3:
    """
    We have 2 pointers, 1(`l`) to check the current index and another(`r`) to compare each value in the array.
    We start the first pointer at index 1 because index 0 will never need to change.
    Because it's a sorted aray, we can check if `r` value already exist in `l` index.
    If `r` exists, `r` = `l`.
    Else `r` = `r`
    Then we want to increase l after each loop. `l+1` to move on to the next `l` index.
    We don't need to increase `r` since we're already doing that in the loop
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            print (nums)
        return l, nums[:l]
            

# Test Case #1
# nums_1 = [0,0,1,1,2,-2,3]
# nums_2 = [0,0,1,1,2,-2,3]
nums_3 = [0,0,1,1,2,-2,3,4,2,2,2,2]



# solution = Solution()
# print (f"Solution #1: {solution.removeDuplicates(nums_1)}")

# solution_two = Solution2()
# print (f"Solution #2: {solution_two.removeDuplicates(nums_2)}")

solution_three = Solution3()
print (f"Solution #3: {solution_three.removeDuplicates(nums_3)}")