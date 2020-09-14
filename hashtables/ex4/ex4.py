import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []

    pos_nums = {}
    neg_nums = {}

    for num in a:
        if num > 0:
            pos_nums[num] = num
        if num < 0:
            neg_nums[num] = num

    for num in neg_nums.items():
        if abs(num[0]) in pos_nums:
            result.append(abs(num[0]))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
