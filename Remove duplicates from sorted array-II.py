class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write_index = 0
        count = 1  # Initialize count for the first element

        for i in range(1, len(nums)):
            if nums[i] == nums[write_index]:
                count += 1
                if count <= 2:
                    write_index += 1
                    nums[write_index] = nums[i]
            else:
                count = 1  # Reset count for a new unique element
                write_index += 1
                nums[write_index] = nums[i]

        return write_index + 1

if __name__ == '__main__':
    solution = Solution()  # Create an instance of the Solution class
    nums = [1,1,1,2,2,3]
    expectedNums = [1,1,2,2,3]  # The expected array after removing duplicates

    k = solution.removeDuplicates(nums)  # Calls the removeDuplicates method on the instance

    # Verify the length
    assert k == len(expectedNums)
    
    # Verify the contents
    for i in range(k):
        assert nums[i] == expectedNums[i]

    print("All test cases passed.")
