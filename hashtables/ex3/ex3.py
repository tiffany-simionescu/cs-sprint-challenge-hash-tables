def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    count = {}

    for item in arrays:
        for i in item:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

    for item in count.items():
        if item[1] == len(arrays):
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
