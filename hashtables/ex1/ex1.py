def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    indices = {}
    result = []

    for i in range(length):
        indices[weights[i]] = i

    for i in range(length):
        cur = weights[i]
        remainder = limit - cur

        if remainder in indices:
            result.append(i)

    if result:
        return sorted(result, reverse=True)
    
    return None
