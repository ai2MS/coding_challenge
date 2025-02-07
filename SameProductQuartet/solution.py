class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_dict={}
        tuple_count = 0
        sorted_nums = sorted(nums)
        len_nums = len(nums)
        for a_n in range(len_nums):
            for b_n in range(a_n+1, len_nums):
                a = sorted_nums[a_n]
                b = sorted_nums[b_n]
                if a == b: 
                    continue
                else:
                    p = a * b
                    if p in temp_dict:
                        tuple_count += 8 * (int(len(temp_dict[p])/2))
                        temp_dict[p].update([a,b])
                    else:
                        temp_dict[p] = set([a,b])

        return tuple_count
    
    
    def tupleSameProduct_ref(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        nums_count = len(nums)
        seq_numbers = list(range(nums_count))
        same_product_count = 0
        for pair_1_a in seq_numbers:
            for pair_1_b in seq_numbers[pair_1_a+1:]:
                for pair_2_a in seq_numbers[pair_1_a+1:pair_1_b]:
                    for pair_2_b in seq_numbers[pair_2_a+1:]:
                        if pair_2_b == pair_1_b:
                            continue
                        pair_1_product = sorted_nums[pair_1_a] * sorted_nums[pair_1_b]
                        pair_2_product = sorted_nums[pair_2_a] * sorted_nums[pair_2_b]
                        if pair_1_product ==  pair_2_product:
                            same_product_count += 1
                            #print(pair_1_product, pair_1_a, pair_1_b, pair_2_a, pair_2_b)
                            break
                        elif pair_1_product < pair_2_product:
                            break


        return (same_product_count*8)

def test():
    """
    >>> spq = Solution()
    >>> spq.tupleSameProduct((1,2,4,5,10))
    16
    >>> spq.tupleSameProduct((2,3,4,6))
    8
    >>> spq.tupleSameProduct((2,3,4,6,8,12))
    40
    >>> spq.tupleSameProduct((8,448,264,525,435,486,378,308,144,75,196,110,231,120,39,288,50,616,140,261,272,783,225,552,598,30,128,570,322,77,340,19,72,224,294,390,276,87,238,180,80,33,68,210,725,243,696,198,208,46,21,58,360,170,190,510,375,551,348,396,377,69,84,300,572,468,160,24,34,667,29,64,253,115,690,100,870,754,102,1,11,312,609,161,493,450,342,133,588,48,152,10,42,273,440,728,65,98,5,23,250,242,38,182,26,648,99,357,400,275,187,483,414,323,408,105,230,520,750,4,500,32,286,418,189,638,528,234,315,96,352,812,232,40,3,130,184,17,15,324,240,392,7,174,270,416,513,25,203,221,399,475,9,54,476,442,406,840,12,504,114,675,624,621,56,405,125,119,136,506,702,364,70,60,228,20,85,575,135,117,78,171,156,55,299,462,116,780,52,432,165,88,325,338,391,546,522,209,176,108))
    251424
    >>> spq.tupleSameProduct((69,252,95,725,112,345,390,221,405,27,58,100,392,156,147,377,32,288,350,17,230,609,29,357,66,728,140,462,190,621,51,7,475,105,255,81,391,120,690,250,308,261,68,464,28,540,116,18,192,16,468,189,532,60,56,420,207,425,630,126,40,432,2,153,84,272,870,210,552,200,228,161,285,648,322,320,132,87,459,70,336,64,184,44,338,15,196,90,117,20,14,45,266,270,374,204,133,416,165,99,780,102,551,195,34,506,182,160,513,48,114,175,72,560,494,364,22,299,225,180,460,171,104,580,476,598,4,437,150,152,76,340,650,50,145,672,522,378,75,396,12,325,375,406,21,1,170,702,10,306,348,304,224,575,418,342,696,368,24,500,483,231,203,78,399,253,26,644,174,19,54,9,486,128,567,57,720,450,8,297,162,52,96,125,588,35,456,240,30,440,260,130,594,525,91,840,154,25,330,264))
    293728
    """
    

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import random
    import time

    # setting up the test run
    no_of_rounds = 40
    inputs = []
    for i in range(no_of_rounds):
        inputs.append(set([random.randint(1,10000) for _ in range(random.randint(1,1000))]))

    spq = Solution()

    solutions = []
    solutions_ref = []

    start_time = time.time()
    for i in range(no_of_rounds):
        solutions.append(spq.tupleSameProduct(inputs[i]))
    end_time = time.time()
    print(f"Solution took: {end_time - start_time} seconds.")    

    start_time = time.time()
    for i in range(no_of_rounds):
        solutions.append(spq.tupleSameProduct_ref(inputs[i]))
    end_time = time.time()
    print(f"Reference Solution took: {end_time - start_time} seconds.")    

    assert solutions == solutions_ref