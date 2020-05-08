def intersection(arrays):

    cache = {}
    result = []
    for row in range(len(arrays)):
        for item in arrays[row]:
            if item not in cache:
                cache[item] = 1
            else:
                cache[item] += 1

    for element in cache:
        if cache[element] == len(arrays):
            result.append(element)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
