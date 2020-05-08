def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    sum = 0
    for i in range(length):

        if weights[i] not in cache:
            cache[weights[i]] = i
            if limit-weights[i] in cache:
                if cache[limit-weights[i]] >= cache[weights[i]]:
                    return (cache[limit-weights[i]], cache[weights[i]])
                else:
                    return (cache[weights[i]], cache[limit-weights[i]])

    return None
