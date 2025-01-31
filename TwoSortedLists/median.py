class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """



    def findMedianSortedArrays_ref(self, nums1, nums2):
        nums = nums1[:]
        nums.extend(nums2)
        nums.sort()
        ln = len(nums)
        if ln % 2:
            # if odd members
            midx = int((ln - 1) / 2)
            return nums[midx]
        else:
            # if even members, use average of two middle members
            midx = int(ln / 2)
            return (float(nums[midx] + nums[midx-1])/2)
        
if __name__ == "__main__":
    import random
    import time

    # setting up the test run
    no_of_rounds = 10000
    sol = Solution()
    list1 = []
    list2 = []
    ## generating no_of_rounds pairs of random lists
    for i in range(0, no_of_rounds):
        # Generate two lists with random number of elements, each element is a random number
        l1 = [random.randint(-999999, 999999) for _ in range(random.randint(0, min(i+1, 1000)))]
        l2 = [random.randint(-999999, 999999) for _ in range(random.randint(0, min(i+1, 1000)))]
        list1.append(sorted(l1) if len(l1) + len(l2) > 0 else [1])
        list2.append(sorted(l2))

    solutions1 = []
    solutions2 = []
  
    # evaluate run time of the given solution
    start_time = time.time()
    for i in range(0, no_of_rounds):
        solutions1.append(sol.findMedianSortedArrays(list1[i], list2[i]))
    end_time = time.time()
    print(f"findMedianSortedArrays, Time taken: {end_time - start_time} seconds")

    # evaluate run time of the reference solution
    start_time = time.time()
    for i in range(0, no_of_rounds):
        solutions2.append(sol.findMedianSortedArrays_ref(list1[i], list2[i]))
    end_time = time.time()
    print(f"findMedianSortedArrays_ref, Time taken: {end_time - start_time} seconds")

    # making sure the solutions are correct
    assert solutions1 == solutions2
