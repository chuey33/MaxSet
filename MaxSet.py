# Colin Huey
# CS 325 Assignment #4 Question #1
# Citation: https://www.hackerrank.com/challenges/max-array-sum/problem

# -------------------------------------------- QUESTION 1 PART A--------------------------------------------------------

def max_independent_set(nums):
    """
    This function returns a subset of non-consecutive numbers in the form of a list that would have the maximum sum.
    :param nums: int
    :return: int
    """
    length = len(nums)
    result = [0] * length
    cache_memo = {}

    # Store results of each sub-problem
    for i in range(0, length):

        # While array has only 1 item
        while length == 1:
            if nums[i] < 0:
                nums[i] = 0
            return nums

        # Finds max sub-problem and stores
        if nums[i] + result[i - 2] > result[i - 1]:
            result[i] = nums[i] + result[i - 2]
            cache_memo[result[i]] = nums[i]

        else:
            result[i] = result[i - 1]

    # Finds optimal solution set, max sum of nums
    solution_set = []
    n = result[length - 1]

    while n > 0:
        # Store found sum in cache_memo
        solution_set.append(cache_memo[n])
        n = n - cache_memo[n]

    # Sort in descending order
    solution_set.reverse()
    return solution_set

# -------------------------------------------- QUESTION 1 PART B--------------------------------------------------------
# Time Complexity: O(n)
